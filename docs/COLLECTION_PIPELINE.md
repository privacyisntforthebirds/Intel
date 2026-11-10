# Automated public-source collection pipeline

## Current implementation

A GitHub Actions workflow runs daily at 16:15 UTC and can also be started manually from the Actions tab. This is approximately 11:15 a.m. Eastern Standard Time or 12:15 p.m. Eastern Daylight Time. GitHub cron uses UTC and does not adjust for daylight saving time.

The collector retrieves these official public feeds:

- CISA cybersecurity advisories: https://www.cisa.gov/cybersecurity-advisories/all.xml
- CISA news: https://www.cisa.gov/news.xml
- FBI national press releases: https://www.fbi.gov/feeds/national-press-releases/rss.xml

The FBI feed is listed in the Bureau's official feed directory: https://www.fbi.gov/feeds/national-press-releases

Feed definitions are stored in sources/feeds.json. The Python collector is scripts/collect_sources.py. Daily machine-readable snapshots are written to data/collection/YYYY-MM-DD.json.

## Record semantics

Each entry is stored as a source publication, not as a confirmed incident. The collector does not infer severity, intent, imminence, threat-actor attribution, or civilian risk. Assessment status remains not_assessed and evidence grade remains not_assigned until a human review adds an evidence-led assessment.

Publication timestamps are retained separately from collection timestamps. Missing or malformed dates remain null; event dates are never invented.

## Reliability and safeguards

- HTTPS requests only, with a bounded timeout and 5 MB response limit.
- XML is parsed as data; feed text is never executed.
- Maximum 25 entries are retained per feed per run.
- Each feed reports success or failure independently.
- A run fails only when every enabled feed fails.
- No credentials, private endpoints, personal data, or non-public sources are collected.
- The workflow has repository-content write permission only and commits collection snapshots.
- A feed failure is a collection gap, not evidence of an incident.
- A new publication is not automatically an alert to the public.

## Operating limitations

This is an initial collection MVP, not a comprehensive all-agency monitor. ODNI, DoD, DOE, FERC, FEMA, Ohio EMA, Ohio DPS, PUCO, Franklin County, Columbus, and Grove City are research targets in the source registry, but should not be added to automated collection until their official feeds or stable public interfaces are verified. Feed endpoints must be checked periodically for redirects, format changes, and publisher changes.

## Next engineering stages

1. Verify and add official Ohio and federal source feeds individually.
2. Add schema validation and automated tests using saved sample RSS and Atom documents.
3. Add deduplication across feed IDs and persistent item history.
4. Add human-reviewed triage fields and a change log; never auto-publish a threat level.
5. Add failure visibility and a status summary for stale or unavailable feeds.
