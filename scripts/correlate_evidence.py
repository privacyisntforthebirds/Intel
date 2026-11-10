#!/usr/bin/env python3
"""Suggest cross-publisher publication pairs for human evidence review.

This tool does not confirm incidents, merge evidence, assign credibility, or
calculate threat levels. Similarity is a review queue heuristic only.
"""
from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import urldefrag, urlsplit, urlunsplit

ROOT = Path(__file__).resolve().parents[1]
STOPWORDS = {
    "about", "after", "against", "agency", "alert", "and", "are", "at",
    "breaking", "by", "for", "from", "has", "have", "in", "into", "is",
    "its", "latest", "new", "of", "on", "or", "press", "release", "said",
    "security", "the", "their", "to", "update", "updates", "us", "was",
    "with",
}
WINDOW = timedelta(hours=72)
MIN_SIMILARITY = 0.45


def parse_timestamp(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except (TypeError, ValueError):
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def tokens(record: dict) -> set[str]:
    text = " ".join((record.get("title") or "", record.get("summary") or "")).lower()
    words = set(re.findall(r"[a-z0-9]{3,}", text))
    return words - STOPWORDS


def similarity(left: set[str], right: set[str]) -> float:
    if not left or not right:
        return 0.0
    return len(left & right) / len(left | right)


def canonical_url(value: str) -> str:
    parts = urlsplit(value.strip())
    return urlunsplit((parts.scheme.lower(), parts.netloc.lower(), parts.path.rstrip("/"), parts.query, ""))


def build_candidates(items: list[dict]) -> list[dict]:
    prepared = []
    for item in items:
        published = parse_timestamp(item.get("published_at"))
        terms = tokens(item)
        if item.get("id") and published and terms and item.get("url"):
            prepared.append((item, published, terms))

    candidates = []
    for index, (left, left_date, left_terms) in enumerate(prepared):
        for right, right_date, right_terms in prepared[index + 1:]:
            if left.get("publisher") == right.get("publisher"):
                continue
            if canonical_url(left["url"]) == canonical_url(right["url"]):
                continue
            delta = abs(left_date - right_date)
            if delta > WINDOW:
                continue
            score = similarity(left_terms, right_terms)
            if score < MIN_SIMILARITY:
                continue
            candidates.append({
                "candidate_id": "|".join(sorted((left["id"], right["id"]))),
                "review_status": "needs_human_review",
                "relationship": "possible_related_publications",
                "similarity_heuristic": round(score, 3),
                "publication_time_delta_hours": round(delta.total_seconds() / 3600, 2),
                "items": [
                    {
                        "id": item["id"],
                        "publisher": item.get("publisher"),
                        "title": item.get("title"),
                        "url": item.get("url"),
                        "published_at": item.get("published_at"),
                    }
                    for item in (left, right)
                ],
                "limitations": [
                    "Text similarity and publication timing do not establish a shared event.",
                    "Independent corroboration and source provenance require human review.",
                    "This candidate is not a threat assessment or incident confirmation.",
                ],
            })
    return sorted(
        candidates,
        key=lambda row: (-row["similarity_heuristic"], row["publication_time_delta_hours"], row["candidate_id"]),
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("snapshot", type=Path, help="Daily collection JSON snapshot")
    parser.add_argument("--output", type=Path, help="Output JSON path; defaults beside snapshot")
    args = parser.parse_args()

    snapshot = json.loads(args.snapshot.read_text(encoding="utf-8"))
    candidates = build_candidates(snapshot.get("items", []))
    output = {
        "schema_version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "input_snapshot": str(args.snapshot),
        "method": "cross-publisher title/summary token Jaccard similarity within 72 hours",
        "threshold": MIN_SIMILARITY,
        "candidate_count": len(candidates),
        "review_required": True,
        "candidates": candidates,
        "disclaimer": "Candidates are leads for human review only; they do not confirm incidents, corroboration, attribution, severity, or imminence.",
    }
    destination = args.output or args.snapshot.with_name(args.snapshot.stem + ".correlation.json")
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {len(candidates)} human-review candidates to {destination}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
