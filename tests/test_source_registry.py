import copy
import json
import unittest
from pathlib import Path

from scripts.validate_source_registry import validate_registry


ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "sources" / "feeds.json"


class SourceRegistryValidationTests(unittest.TestCase):
    def setUp(self):
        self.registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))

    def test_checked_in_registry_is_valid(self):
        validate_registry(self.registry)

    def test_requested_agencies_are_present(self):
        required = {
            "odni",
            "doe",
            "fema",
            "ohio_ema",
            "ohio_dps",
            "puco",
            "franklin_county",
            "columbus",
            "grove_city",
        }
        registered = {source["id"] for source in self.registry["sources"]}
        self.assertTrue(required.issubset(registered))

    def test_duplicate_source_ids_are_rejected(self):
        invalid = copy.deepcopy(self.registry)
        invalid["sources"].append(copy.deepcopy(invalid["sources"][0]))
        with self.assertRaisesRegex(ValueError, "duplicate source id"):
            validate_registry(invalid)

    def test_manual_only_sources_cannot_be_added_to_collection(self):
        invalid = copy.deepcopy(self.registry)
        feed = copy.deepcopy(invalid["feeds"][0])
        feed.update({"id": "ohio_ema_unverified", "source_id": "ohio_ema"})
        invalid["feeds"].append(feed)
        with self.assertRaisesRegex(ValueError, "cannot use a source that is not verified"):
            validate_registry(invalid)

    def test_feed_urls_must_use_https(self):
        invalid = copy.deepcopy(self.registry)
        invalid["feeds"][0]["url"] = "http://example.gov/feed.xml"
        with self.assertRaisesRegex(ValueError, "url must be an official HTTPS .gov URL"):
            validate_registry(invalid)

    def test_feed_urls_must_use_an_official_domain(self):
        invalid = copy.deepcopy(self.registry)
        invalid["feeds"][0]["url"] = "https://example.com/feed.xml"
        with self.assertRaisesRegex(ValueError, "url must be an official HTTPS .gov URL"):
            validate_registry(invalid)

    def test_verification_dates_must_be_iso_dates(self):
        invalid = copy.deepcopy(self.registry)
        invalid["feeds"][0]["verified_on"] = "November 10, 2026"
        with self.assertRaisesRegex(ValueError, "verified_on must be an ISO date"):
            validate_registry(invalid)

    def test_feed_ids_must_match_source_metadata(self):
        invalid = copy.deepcopy(self.registry)
        invalid["feeds"][0]["id"] = "renamed_without_source_update"
        with self.assertRaisesRegex(ValueError, "feed_ids do not match feeds"):
            validate_registry(invalid)

    def test_pending_sources_cannot_claim_a_verification_date(self):
        invalid = copy.deepcopy(self.registry)
        invalid["sources"][4]["verified_on"] = "2026-11-10"
        with self.assertRaisesRegex(ValueError, "verified_on must be null while pending"):
            validate_registry(invalid)


if __name__ == "__main__":
    unittest.main()
