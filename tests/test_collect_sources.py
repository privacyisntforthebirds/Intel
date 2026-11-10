import io
import unittest
from unittest.mock import patch

from scripts.collect_sources import entry_link, fetch_feed, parse_date


class FeedParserTests(unittest.TestCase):
    def test_parse_rfc822_date(self):
        self.assertEqual(
            parse_date("Tue, 10 Nov 2026 12:00:00 GMT"),
            "2026-11-10T12:00:00+00:00",
        )

    def test_parse_iso_date(self):
        self.assertEqual(
            parse_date("2026-11-10T07:00:00-05:00"),
            "2026-11-10T12:00:00+00:00",
        )

    def test_invalid_date_is_null(self):
        self.assertIsNone(parse_date("not-a-date"))

    def test_atom_alternate_link(self):
        import xml.etree.ElementTree as ET
        entry = ET.fromstring(
            '<entry xmlns="http://www.w3.org/2005/Atom">'
            '<link rel="self" href="https://example.gov/self"/>'
            '<link rel="alternate" href="https://example.gov/story"/>'
            '</entry>'
        )
        self.assertEqual(entry_link(entry), "https://example.gov/story")

    @patch("scripts.collect_sources.urllib.request.urlopen")
    def test_rss_entry_is_recorded_without_threat_classification(self, mocked_open):
        payload = (
            b'<rss><channel><item><title>Advisory title</title>'
            b'<link>https://www.cisa.gov/example</link>'
            b'<pubDate>Tue, 10 Nov 2026 12:00:00 GMT</pubDate>'
            b'<description>Public notice</description></item></channel></rss>'
        )
        response = io.BytesIO(payload)
        response.__enter__ = lambda self=response: self
        response.__exit__ = lambda *args: False
        mocked_open.return_value = response

        records = fetch_feed({
            "id": "test_feed",
            "publisher": "Test Agency",
            "title": "Test feed",
            "url": "https://example.gov/feed.xml",
        })

        self.assertEqual(len(records), 1)
        self.assertEqual(records[0]["title"], "Advisory title")
        self.assertEqual(records[0]["record_type"], "source_publication")
        self.assertEqual(records[0]["assessment_status"], "not_assessed")
        self.assertEqual(records[0]["evidence_grade"], "not_assigned")

    @patch("scripts.collect_sources.MAX_FEED_BYTES", 10)
    @patch("scripts.collect_sources.urllib.request.urlopen")
    def test_oversized_feed_is_rejected_before_parsing(self, mocked_open):
        response = io.BytesIO(b"x" * 11)
        response.__enter__ = lambda self=response: self
        response.__exit__ = lambda *args: False
        mocked_open.return_value = response

        with self.assertRaisesRegex(ValueError, "safety limit"):
            fetch_feed({
                "id": "test_feed",
                "publisher": "Test Agency",
                "title": "Test feed",
                "url": "https://example.gov/feed.xml",
            })


if __name__ == "__main__":
    unittest.main()
