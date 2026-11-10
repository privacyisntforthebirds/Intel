# Automated public-source collection pipeline

## Current implementation

A GitHub Actions workflow runs daily at 16:15 UTC and can also be started manually from the Actions tab. GitHub cron uses UTC and does not adjust for daylight saving time.

The collector retrieves these verified official public feeds:

- CISA cybersecurity advisories: https://www.cisa.gov/cybersecurity-advisories/all.xml
- CISA news: https://www.cisa.gov/news.xml
- FBI national press releases Atom: https://www.fbi.gov/feeds/national-press-releases/atom.xml
- Grove City News Flash: https://www.grovecityohio.gov/RSSFeed.aspx?CID=All-newsflash.xml&ModID=1

The FBI feed directory lists RSS 1.0, RSS 2.0, and Atom formats. Grove City's official RSS directory lists its News Flash feeds; this project uses only the All News Flash feed.

The machine-readable registry, including source metadata, interface status, and verification dates, is sources/feeds.json. The registry validator runs in the collector, unit tests, and GitHub Actions before collection.

Other agency pages in the registry are manual-only or pending; see [the source registry](../sources/SOURCE_REGISTRY.md). They are not fetched automatically.

The Python collector is scripts/collect_sources.py. Daily machine-readable snapshots are written to data/collection/YYYY-MM-DD.json.

## Record semantics

Each entry is stored as a source publication, not as a confirmed incident. The collector does not infer severity, intent, imminence, threat-actor attribution, or civilian risk. Assessment status remains not_assessed and evidence grade remains not_assigned until a human review adds an evidence-led assessment.

Publication timestamps are retained separately from collection timestamps. Missing or malformed dates remain null; event dates are never invented.

## Correlation review queue

The optional script scripts/correlate_evidence.py compares publications in one snapshot and writes possible cross-publisher matches for human review:

    python scripts/correlate_evidence.py data/collection/YYYY-MM-DD.json

It uses a 72-hour publication-time window and a conservative text-similarity threshold. It does not merge records, confirm a shared incident, establish independent corroboration, or assign a threat level. See [Evidence correlation](EVIDENCE_CORRELATION.md) for the matching rule and limitations.

## Reliability and safeguards

- HTTPS requests only, with a bounded timeout and 10 MB response limit.
- XML is parsed as data; feed text is never executed.
- Maximum 25 entries are retained per feed per run.
- Each feed reports success or failure independently.
- A run fails only when every enabled feed fails.
- No credentials, private endpoints, or non-public sources are collected.
- The workflow has repository-content write permission only and commits collection snapshots.
- A feed failure is a collection gap, not evidence of an incident.
- A new publication is not automatically an alert to the public.
- Correlation candidates remain explicitly marked for human review.

## Operating limitations

This is an initial collection MVP, not a comprehensive all-agency monitor. The registry distinguishes verified feed endpoints, manual-only pages, and sources pending interface verification. Manual-only pages are not polled. Feed endpoints should be periodically checked for redirects, format changes, and publisher changes.

## Next engineering stages

1. Verify a stable FEMA public interface before adding any endpoint.
2. Add schema validation and automated tests for collected publication records.
3. Add deduplication across feed IDs and persistent item history.
4. Add human-reviewed triage fields and a change log; never auto-publish a threat level.
5. Add failure visibility and a status summary for stale or unavailable feeds.
