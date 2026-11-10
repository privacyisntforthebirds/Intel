import unittest
from scripts.correlate_evidence import build_candidates, parse_timestamp, similarity, tokens


def record(identifier, publisher, title, published_at, url=None, summary=""):
    return {
        "id": identifier,
        "publisher": publisher,
        "title": title,
        "published_at": published_at,
        "url": url or f"https://{publisher.lower().replace(' ', '')}.example/{identifier}",
        "summary": summary,
    }


class CorrelationTests(unittest.TestCase):
    def test_related_cross_publisher_items_are_review_candidates(self):
        items = [
            record("a1", "Agency One", "Water utility reports cyber incident affecting customer billing",
                   "2026-11-10T10:00:00Z"),
            record("b2", "Agency Two", "Cyber incident affects water utility customer billing systems",
                   "2026-11-11T04:00:00Z"),
        ]
        candidates = build_candidates(items)
        self.assertEqual(len(candidates), 1)
        self.assertEqual(candidates[0]["review_status"], "needs_human_review")
        self.assertEqual(candidates[0]["relationship"], "possible_related_publications")
        self.assertIn("do not establish a shared event.", candidates[0]["limitations"][0])

    def test_same_publisher_is_not_cross_source_corroboration(self):
        items = [
            record("a1", "Agency One", "Water utility cyber incident billing systems",
                   "2026-11-10T10:00:00Z"),
            record("a2", "Agency One", "Water utility cyber incident billing systems",
                   "2026-11-10T11:00:00Z"),
        ]
        self.assertEqual(build_candidates(items), [])

    def test_outside_time_window_is_excluded(self):
        items = [
            record("a1", "Agency One", "Water utility cyber incident customer billing",
                   "2026-11-01T10:00:00Z"),
            record("b2", "Agency Two", "Water utility cyber incident customer billing",
                   "2026-11-10T10:00:00Z"),
        ]
        self.assertEqual(build_candidates(items), [])

    def test_missing_publication_date_is_excluded(self):
        items = [
            record("a1", "Agency One", "Water utility cyber incident customer billing", None),
            record("b2", "Agency Two", "Water utility cyber incident customer billing",
                   "2026-11-10T10:00:00Z"),
        ]
        self.assertEqual(build_candidates(items), [])

    def test_identical_canonical_url_is_not_a_second_source(self):
        items = [
            record("a1", "Agency One", "Water utility cyber incident customer billing",
                   "2026-11-10T10:00:00Z", "https://example.gov/advisory#section"),
            record("b2", "Agency Two", "Water utility cyber incident customer billing",
                   "2026-11-10T11:00:00Z", "https://example.gov/advisory"),
        ]
        self.assertEqual(build_candidates(items), [])

    def test_similarity_is_jaccard(self):
        self.assertAlmostEqual(similarity({"water", "utility"}, {"water", "power"}), 1 / 3)

    def test_date_parser_normalizes_utc(self):
        parsed = parse_timestamp("2026-11-10T10:00:00-05:00")
        self.assertEqual(parsed.isoformat(), "2026-11-10T15:00:00+00:00")


if __name__ == "__main__":
    unittest.main()
