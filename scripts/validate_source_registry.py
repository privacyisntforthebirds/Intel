#!/usr/bin/env python3
"""Validate the public-source registry before collection."""
from __future__ import annotations

import json
import re
from datetime import date
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "sources" / "feeds.json"
SOURCE_STATUSES = {"verified", "manual_only", "pending"}
SOURCE_INTERFACES = {
    "verified": {"rss", "rss_or_atom"},
    "manual_only": {"web_index"},
    "pending": {"unverified"},
}
FEED_FORMATS = {"rss", "atom", "rss_or_atom"}
ID_PATTERN = re.compile(r"^[a-z0-9_]+$")


def _is_https_url(value: object) -> bool:
    if not isinstance(value, str):
        return False
    try:
        parsed = urlsplit(value)
        return (
            parsed.scheme == "https"
            and bool(parsed.hostname)
            and parsed.username is None
            and parsed.password is None
        )
    except ValueError:
        return False


def _is_official_https_url(value: object) -> bool:
    if not _is_https_url(value):
        return False
    host = urlsplit(value).hostname
    return bool(host and (host == "gov" or host.endswith(".gov")))


def _is_iso_date(value: object, *, nullable: bool = False) -> bool:
    if value is None:
        return nullable
    if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        return False
    try:
        date.fromisoformat(value)
        return True
    except ValueError:
        return False


def validate_registry(registry: object) -> None:
    """Raise ValueError when registry metadata or feed references are invalid."""
    errors: list[str] = []
    if not isinstance(registry, dict):
        raise ValueError("Registry root must be an object")
    if registry.get("schema_version") != 2:
        errors.append("schema_version must be 2")

    sources = registry.get("sources")
    feeds = registry.get("feeds")
    if not isinstance(sources, list):
        errors.append("sources must be a list")
        sources = []
    if not isinstance(feeds, list):
        errors.append("feeds must be a list")
        feeds = []

    source_by_id: dict[str, dict] = {}
    for index, source in enumerate(sources):
        label = f"sources[{index}]"
        if not isinstance(source, dict):
            errors.append(f"{label} must be an object")
            continue
        source_id = source.get("id")
        if not isinstance(source_id, str) or not ID_PATTERN.fullmatch(source_id):
            errors.append(f"{label}.id must contain lowercase letters, digits, or underscores")
            continue
        if source_id in source_by_id:
            errors.append(f"duplicate source id: {source_id}")
        source_by_id[source_id] = source
        for key in ("publisher", "title", "scope", "verification_note"):
            if not isinstance(source.get(key), str) or not source[key].strip():
                errors.append(f"{label}.{key} must be a non-empty string")
        if source.get("status") not in SOURCE_STATUSES:
            errors.append(f"{label}.status must be one of {sorted(SOURCE_STATUSES)}")
        status = source.get("status")
        if source.get("interface") not in SOURCE_INTERFACES.get(status, set()):
            errors.append(f"{label}.interface is inconsistent with its status")
        if not _is_official_https_url(source.get("official_page")):
            errors.append(f"{label}.official_page must be an official HTTPS .gov URL")
        if not _is_iso_date(source.get("last_reviewed")):
            errors.append(f"{label}.last_reviewed must be an ISO date")
        if status == "pending":
            if not _is_iso_date(source.get("verified_on"), nullable=True) or source.get("verified_on") is not None:
                errors.append(f"{label}.verified_on must be null while pending")
        elif not _is_iso_date(source.get("verified_on")):
            errors.append(f"{label}.verified_on must be an ISO date")
        feed_ids = source.get("feed_ids")
        if not isinstance(feed_ids, list) or any(not isinstance(feed_id, str) for feed_id in feed_ids):
            errors.append(f"{label}.feed_ids must be a list of strings")
        elif len(feed_ids) != len(set(feed_ids)):
            errors.append(f"{label}.feed_ids must not contain duplicates")
        elif status != "verified" and feed_ids:
            errors.append(f"{label} with status {status} cannot reference automated feeds")
        elif status == "verified" and not feed_ids:
            errors.append(f"{label} with status verified must reference at least one feed")

    feed_by_id: dict[str, dict] = {}
    feed_ids_by_source: dict[str, set[str]] = {}
    for index, feed in enumerate(feeds):
        label = f"feeds[{index}]"
        if not isinstance(feed, dict):
            errors.append(f"{label} must be an object")
            continue
        feed_id = feed.get("id")
        if not isinstance(feed_id, str) or not ID_PATTERN.fullmatch(feed_id):
            errors.append(f"{label}.id must contain lowercase letters, digits, or underscores")
            continue
        if feed_id in feed_by_id:
            errors.append(f"duplicate feed id: {feed_id}")
        feed_by_id[feed_id] = feed
        for key in ("publisher", "title", "scope"):
            if not isinstance(feed.get(key), str) or not feed[key].strip():
                errors.append(f"{label}.{key} must be a non-empty string")
        if not _is_official_https_url(feed.get("url")):
            errors.append(f"{label}.url must be an official HTTPS .gov URL")
        if not _is_official_https_url(feed.get("official_directory")):
            errors.append(f"{label}.official_directory must be an official HTTPS .gov URL")
        if feed.get("format") not in FEED_FORMATS:
            errors.append(f"{label}.format must be one of {sorted(FEED_FORMATS)}")
        if not _is_iso_date(feed.get("verified_on")):
            errors.append(f"{label}.verified_on must be an ISO date")
        if not isinstance(feed.get("enabled"), bool):
            errors.append(f"{label}.enabled must be a boolean")
        source_id = feed.get("source_id")
        source = source_by_id.get(source_id) if isinstance(source_id, str) else None
        if source is None:
            errors.append(f"{label}.source_id must reference a registered source")
            continue
        if source.get("status") != "verified":
            errors.append(f"{label} cannot use a source that is not verified")
        if not feed.get("enabled"):
            errors.append(f"{label} must be enabled only after feed verification")
        feed_ids_by_source.setdefault(source_id, set()).add(feed_id)

    for source_id, source in source_by_id.items():
        declared = source.get("feed_ids")
        expected = {feed_id for feed_id in declared if isinstance(feed_id, str)} if isinstance(declared, list) else set()
        actual = feed_ids_by_source.get(source_id, set())
        if expected != actual:
            errors.append(
                f"sources entry {source_id} feed_ids do not match feeds (expected {sorted(expected)}, got {sorted(actual)})"
            )
    for feed_id in feed_by_id:
        if feed_id not in {
            declared
            for source in source_by_id.values()
            for declared in source.get("feed_ids", [])
            if isinstance(declared, str)
        }:
            errors.append(f"feed {feed_id} is not declared by its source")

    if errors:
        raise ValueError("Invalid source registry:\n- " + "\n- ".join(errors))


def main() -> int:
    try:
        registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
        validate_registry(registry)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"Source registry validation failed: {exc}")
        return 1
    print(f"Source registry valid: {len(registry['sources'])} sources, {len(registry['feeds'])} feeds")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
