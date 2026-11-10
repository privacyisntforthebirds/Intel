# Official source registry

The machine-readable registry is [feeds.json](feeds.json). It records the source owner, coverage, interface type, status, verification dates, evidence page, and any feed IDs. Only verified RSS or Atom endpoints are enabled for automatic collection.

Last reviewed: 2026-11-10.

## Status definitions

- **Verified** — an official RSS or Atom interface and its endpoint were confirmed. Only these sources may be enabled in the collector.
- **Manual-only** — an official, current web index was confirmed, but no suitable general feed or documented public API was verified. Review the page manually.
- **Pending** — the current stable public interface could not be confirmed. No feed or API endpoint is configured.

Status reflects interface verification, not the accuracy or significance of any publication. A source entry is not a warning or incident assessment.

## Verified feeds

| Source | Collected interface | Official evidence page | Verified |
|---|---|---|---|
| CISA | [All cybersecurity advisories](https://www.cisa.gov/cybersecurity-advisories/all.xml) and [CISA news](https://www.cisa.gov/news.xml) | [CISA advisories](https://www.cisa.gov/news-events/cybersecurity-advisories) | 2026-11-10 |
| FBI | [National press releases Atom](https://www.fbi.gov/feeds/national-press-releases/atom.xml) | [FBI feed directory](https://www.fbi.gov/feeds/national-press-releases) | 2026-11-10 |
| City of Grove City | [All News Flash RSS](https://www.grovecityohio.gov/RSSFeed.aspx?CID=All-newsflash.xml&ModID=1) | [Grove City RSS directory](https://www.grovecityohio.gov/rss.aspx) | 2026-11-10 |

Grove City's RSS directory describes available feed types and includes a News Flash feed. The collector uses the directory's “All” News Flash link. It does not subscribe to Alert Center or other feed categories.

The CISA endpoints returned RSS through a PowerShell probe, but Python urllib received HTTP 403 from both in this environment. GitHub Actions reachability is unverified because no workflow run was available during this review.

## Manual-only pages

| Source | Official index | Verification date | Why manual-only |
|---|---|---|---|
| ODNI | [Newsroom](https://www.odni.gov/newsroom/) | 2026-11-10 | Current dated newsroom listings were visible; no official RSS or documented public API was confirmed. |
| U.S. Department of Energy | [Newsroom](https://www.energy.gov/newsroom) | 2026-11-10 | Department-wide releases and updates are listed. RSS pages found were for narrower DOE offices, so they are not treated as a department-wide feed. |
| Ohio EMA | [News](https://ema.ohio.gov/media-publications/news/news) | 2026-11-10 | Official current news index; no RSS or documented public API was confirmed. |
| Ohio Department of Public Safety | [News and events](https://publicsafety.ohio.gov/news-and-events) | 2026-11-10 | Official current index; no RSS or documented public API was confirmed. |
| PUCO | [All News](https://puco.ohio.gov/news) | 2026-11-10 | Official news index. Newsletter and email subscriptions are available, but no public RSS feed or API was confirmed. |
| Franklin County, Ohio | [County News](https://www.franklincountyohio.gov/County-Government/County-News) | 2026-11-10 | The county index links multiple agency press rooms; no single county-wide feed or documented API was confirmed. |
| City of Columbus | [News articles](https://www.columbus.gov/News-articles) | 2026-11-10 | Official current news index; no RSS or documented public API was confirmed. |

These pages are not fetched by the collector. Any future automated feed must be linked from an official publisher page or documented by the publisher and checked before being added.

## Pending

| Source | Official starting page | Last reviewed | Reason |
|---|---|---|---|
| FEMA | [FEMA.gov](https://www.fema.gov/) | 2026-11-10 | A stable current news feed or documented public interface could not be confirmed in this review. No endpoint is configured. |

## Collection boundaries

- The collector reads only enabled entries in feeds.json.
- A feed failure is a collection gap, not evidence of an incident.
- Records remain source publications with assessment status not assessed and evidence grade not assigned.
- The repository does not automatically classify threats, infer imminence, or send public alerts.
- Collection is limited to public official pages and feeds; no credentials, private endpoints, or non-public sources are used.

## Other source candidates

The following initial reference sources have not been checked for a stable collection interface in this milestone. They are not configured in feeds.json: NSA, DHS, FERC, DoD, Ohio Homeland Security, Ohio Department of Health, Ohio DNR, NATO, the European Union, the UK National Cyber Security Centre, and Europol. Verify each official interface before adding it.

Preserve the exact publication title, issuing body, source URL, publication or update time, access date, and relevant excerpt when reviewing a source. Prefer the original official publication over a repost.
