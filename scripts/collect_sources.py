#!/usr/bin/env python3
"""Collect official public RSS/Atom entries without automated threat classification."""
from __future__ import annotations

import json
import sys
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from hashlib import sha256
from pathlib import Path

if __package__:
    from .validate_source_registry import validate_registry
else:
    from validate_source_registry import validate_registry

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "sources" / "feeds.json"
OUTPUT_DIR = ROOT / "data" / "collection"
USER_AGENT = "PublicThreatIntelligenceObservatory/1.0 (+https://github.com/privacyisntforthebirds/Intel)"
MAX_ENTRIES_PER_FEED = 25
TIMEOUT_SECONDS = 25
MAX_FEED_BYTES = 10_000_000


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1].lower()


def child_text(element: ET.Element, *names: str) -> str:
    wanted = {name.lower() for name in names}
    for child in element.iter():
        if local_name(child.tag) in wanted and child.text:
            value = child.text.strip()
            if value:
                return value
    return ""


def entry_link(element: ET.Element) -> str:
    for child in element:
        if local_name(child.tag) == "link":
            href = child.attrib.get("href", "").strip()
            rel = child.attrib.get("rel", "alternate").lower()
            if href and rel in ("alternate", ""):
                return href
            if child.text and child.text.strip():
                return child.text.strip()
    return ""


def parse_date(value: str) -> str | None:
    if not value:
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=timezone.utc)
        return parsed.astimezone(timezone.utc).isoformat()
    except ValueError:
        pass
    try:
        parsed = parsedate_to_datetime(value)
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=timezone.utc)
        return parsed.astimezone(timezone.utc).isoformat()
    except (TypeError, ValueError, OverflowError):
        return None


def fetch_feed(feed: dict) -> list[dict]:
    request = urllib.request.Request(
        feed["url"],
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "application/atom+xml, application/rss+xml, application/xml, text/xml",
        },
    )
    with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
        raw = response.read(MAX_FEED_BYTES + 1)
        if len(raw) > MAX_FEED_BYTES:
            raise ValueError("Feed exceeded 10 MB safety limit")
    root = ET.fromstring(raw)
    entries = [
        node for node in root.iter()
        if local_name(node.tag) in ("item", "entry")
    ]
    records = []
    for entry in entries[:MAX_ENTRIES_PER_FEED]:
        title = child_text(entry, "title")
        link = entry_link(entry)
        if not title or not link:
            continue
        published_raw = child_text(entry, "published", "pubdate", "date", "updated")
        published = parse_date(published_raw)
        summary = " ".join(child_text(entry, "summary", "description", "encoded", "content").split())[:1200]
        stable = link or f'{feed["id"]}:{title}:{published_raw}'
        records.append({
            "id": sha256(stable.encode("utf-8")).hexdigest()[:20],
            "publisher": feed["publisher"],
            "feed_id": feed["id"],
            "feed_title": feed["title"],
            "title": " ".join(title.split())[:500],
            "url": link,
            "published_at": published,
            "published_at_raw": published_raw or None,
            "summary": summary,
            "record_type": "source_publication",
            "assessment_status": "not_assessed",
            "evidence_grade": "not_assigned",
        })
    return records


def main() -> int:
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    validate_registry(registry)
    collected_at = datetime.now(timezone.utc)
    output = {
        "schema_version": 1,
        "collection_date_utc": collected_at.date().isoformat(),
        "collected_at": collected_at.isoformat(),
        "method": "official RSS/Atom retrieval; no automated threat classification",
        "feeds": [],
        "items": [],
    }
    failures = 0
    for feed in registry.get("feeds", []):
        if not feed.get("enabled", False):
            continue
        status = {"feed_id": feed["id"], "publisher": feed["publisher"], "url": feed["url"]}
        try:
            items = fetch_feed(feed)
            output["items"].extend(items)
            status.update({"status": "ok", "items_collected": len(items)})
        except (urllib.error.URLError, TimeoutError, ET.ParseError, ValueError, KeyError) as exc:
            failures += 1
            status.update({"status": "error", "error": str(exc)[:500]})
        output["feeds"].append(status)
        time.sleep(0.5)

    unique = {item["id"]: item for item in output["items"]}
    output["items"] = sorted(
        unique.values(),
        key=lambda item: (item.get("published_at") or "", item["publisher"], item["title"]),
        reverse=True,
    )
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    destination = OUTPUT_DIR / f'{collected_at.date().isoformat()}.json'
    destination.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f'Wrote {len(output["items"])} records to {destination.relative_to(ROOT)}')
    for status in output["feeds"]:
        print(json.dumps(status, ensure_ascii=False))
    if failures == len(output["feeds"]) and failures:
        print("All configured feeds failed; failing this run.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
