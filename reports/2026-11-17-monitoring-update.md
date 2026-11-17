# Public Threat Watch — 2026-11-17

## Key judgment

The financial-sector expansion produced three distinct findings that must not be conflated:

1. **n0n extortion allegation:** On November 16, threat-intelligence firm Hackmanac relayed a claim that n0n had stolen customer and marketing data associated with JPMorgan Chase, Visa, and Mastercard. This is a credible report that the allegation was made, not proof that any of the three organizations was breached. The claimed data volume is unquantified, the alleged intrusion date is unknown, and the data categories are not mapped to individual companies.
2. **Visa third-party incident:** Visa told Cybernews that an incident involved a third-party service provider in the Asia-Pacific region. Visa said its own systems were not involved or impacted and that there was no indication payment data such as card numbers had been affected. The provider was not named, and Visa did not publicly attribute the incident to n0n.
3. **JPMorgan transaction outage:** JPMorgan confirmed that a software bug in on-premise hardware slowed some transactions on November 16. The bank said there was no evidence the issue was cyber-related. It reported normal processing again Monday evening, and on November 17 said services were back to normal. The outage is separate from the extortion allegation unless evidence later establishes a connection.

No verified evidence reviewed today establishes compromise of card authorization networks, Fedwire, FedNow, ACH, or the Zelle network itself. The Federal Reserve's official service-status page was accessible, but its embedded live-status content was not exposed to this review; a third-party status monitor reported Fedwire Funds up at 12:03 UTC on November 17. That secondary signal is not an official all-clear, so current Federal Reserve rail status remains incompletely verified.

**Overall national-security assessment:** localized and sector-specific disruption risk; persistent broader cyber concern; no evidence of imminent nationwide danger.

## 1. n0n allegation involving JPMorgan Chase, Visa, and Mastercard

### What is claimed

Hackmanac's November 16 public alert says n0n claims to have stolen sensitive customer and marketing data associated with three named organizations and threatens publication unless a settlement is reached. Cybernews reported that n0n's leak-site listing showed Visa and JPMorgan Chase and described a 48-hour countdown. Hackmanac's alert also names Mastercard. SOCRadar's public tracker separately records JPMorgan Chase and Mastercard as n0n claims with status **Claimed**, not as independently confirmed compromises.

The claim's observation/publication date is November 16, 2026. **The date of any alleged intrusion is unknown.** Neither the Hackmanac alert nor the public reporting provides a verified compromise window or a quantified dataset.

SOCRadar's public n0n profile, updated November 17, describes the group as a data-exfiltration and destructive-extortion operation that surfaced in September 2026 and appears financially motivated. Its victim counts are based on group listings; this actor-level background does not establish the truth of the current three-company claim or attribute it to a state.

### Organization-by-organization status

| Organization | What is publicly supported | What remains unverified |
|---|---|---|
| JPMorgan Chase | n0n's claim was relayed by Hackmanac and a leak-site listing was reported by Cybernews. JPMorgan separately confirmed a software-related transaction delay on November 16. | No public confirmation of data theft, no verified sample or hash, no disclosed dataset, no confirmed connection between the outage and the extortion claim, and no evidence of customer-account takeover or funds theft. |
| Visa | n0n's claim was relayed by Hackmanac. Visa's spokesperson told Cybernews that an incident involved a third-party service provider in Asia-Pacific, but Visa's systems were not involved or impacted and there was no indication card numbers were affected. | The vendor is unnamed. Visa has not publicly confirmed n0n attribution or the specific customer/marketing datasets in the allegation. The third-party incident may be related, but the public evidence does not establish that link. |
| Mastercard | Hackmanac's November 16 alert names Mastercard; SOCRadar's tracker also records a claim with status Claimed. | No Mastercard confirmation located in reviewed public sources; no independently verifiable sample, hash, victim/vendor confirmation, regulator notice, notification letter, or forensic report located. |

The public evidence does **not** justify describing any of these three organizations as a confirmed n0n breach victim. A leak-site listing or threat-intelligence repost establishes that a claim was made; it does not establish successful access, exfiltration, authenticity, or the origin of the data.

### Data-category claims — kept separate

Hackmanac's post lists the following categories at an aggregate level. It does not provide a reliable company-by-company mapping, so none should be assigned to JPMorgan, Visa, or Mastercard individually without further evidence.

| Claimed category | Evidence status | Material unknowns |
|---|---|---|
| Cardholder profiles | Unverified actor claim | Fields included, number of records, issuer/network mapping, authenticity, and whether any sensitive payment credentials are present |
| Personal contact details | Unverified actor claim | Exact fields, affected people, record count, source system, and authenticity |
| Premium travel and dining reservations | Unverified actor claim | Booking provider, affected travelers, dates, reservation fields, and whether the records are genuine |
| Banking associations | Unverified actor claim | Meaning of the term, whether it identifies an issuer relationship or something else, and which company or source holds the records |
| Marketing-campaign engagement records | Unverified actor claim | Campaign owner, regions, number of records, data fields, and whether the claimed “millions of interactions” are unique people, events, or records |

No publicly verifiable samples or cryptographic hashes were located. No stolen records were downloaded, opened, or redistributed. No criminal infrastructure was visited or contacted.

**Payment-data distinction:** Visa specifically said there was no indication card numbers were affected. The public claim does not establish exposure of PANs, CVVs, expiration dates, PINs, payment tokens, online-banking passwords, account balances, ACH details, wire instructions, or customer funds. Those categories must not be described as compromised.

### Confidence and implications

- **High confidence:** Hackmanac publicly relayed the allegation on November 16; Cybernews reported a Visa/JPMorgan leak-site listing; public threat-intelligence trackers recorded claims.
- **Moderate confidence:** Visa acknowledged a third-party-provider incident in Asia-Pacific through a spokesperson quoted by Cybernews.
- **Low confidence / unverified:** The alleged theft itself, n0n's attribution for the Visa third-party event, the authenticity and provenance of the alleged data, the number of affected people, and the company-specific data mapping.

If the contact or reservation data were genuine, plausible consumer consequences could include targeted phishing or social engineering. The current evidence does not support a blanket conclusion that cards, passwords, balances, or funds are exposed, and it does not support a general card-replacement recommendation.

## 2. JPMorgan Chase transaction-processing disruption

- **Event date:** November 16, 2026. The bank described the issue as occurring Monday; exact start and end times were not disclosed in the public statements reviewed.
- **Publication:** JPMorgan's statement was reported by Reuters and AP on November 16. Business Insider reported the bank's restoration update on November 17. The JPMorgan Form 8-K located in EDGAR on November 17 concerned a CFO succession and was not a cybersecurity incident disclosure; that filing does not resolve the separate extortion allegation.
- **Affected service:** JPMorgan transaction processing and some customer-facing online banking functions.
- **Cause stated by the bank:** A temporary software bug in on-premise hardware systems. JPMorgan said there was no evidence the issue was cyber-related.
- **Customer impact:** Some transactions took longer than usual; customers reported difficulty accessing online banking. JPMorgan said customers retained access to their accounts and funds.
- **Spillover:** Other institutions could experience delays when they were a party to a transaction involving JPMorgan. U.S. Bank said its own systems were not directly affected but some inter-institution Zelle transfers could be delayed.
- **Resolution:** JPMorgan said transactions were processing normally again Monday evening; on November 17, it said services were back to normal.

Early Warning Services, Zelle's operator, said the Zelle network was fully operational and that issues at participating financial institutions could delay some customers' payments. This is evidence of institution-level processing effects, not a Zelle network outage.

The reports do not establish a Fedwire, FedNow, ACH, Visa, or Mastercard network outage. The Federal Reserve Financial Services live status page showed Account Services, FedACH, FedNow, Fedwire Funds, Fedwire Securities, National Settlement, and listed access services in normal operation at the time checked on November 17.

**Classification:** Actual operational disruption with a bank-stated software cause; resolved. It is not a confirmed cyber incident. The separate n0n data-theft allegation remains unverified and has not been linked to this outage.

## 3. Visa Fall 2026 Biannual Threats Report

Visa published its Fall 2026 Biannual Threats Report on November 17. Its observation period is January through June 2026, so these are retrospective company telemetry findings, not incidents that began today.

Visa Payment Ecosystem Risk and Control reported:
- Third-party-agent incidents increased 62% compared with the preceding six-month period.
- Those providers were linked to approximately 56% of compromised payment credentials identified during the reporting period.
- Visa reported a more than 1,200% increase in recovered payment credentials from data breaches.
- Payment-account enumeration volume increased 35% year over year, while Visa said its Risk Operations Center blocked 200% more enumeration transactions and fraud losses associated with enumerated credentials fell 21.4% year over year.

These figures are Visa's own monitoring and measurement. They support the importance of third-party concentration and credential exposure as payment-sector risks, but they do not validate the n0n allegation or establish that the three named companies share a compromised supplier. The report also describes network-level defenses as reducing the impact of some observed threats.

## 4. Federal payment-system status and other operational checks

The Federal Reserve Financial Services official service-status page was checked, but its embedded live-status data was not readable through the available public page view. StatusGator reported Fedwire Funds as up at 12:03 UTC on November 17, but this is a third-party status signal rather than a Federal Reserve incident statement. I did not locate a primary Federal Reserve notice confirming a current outage or a full all-services status. Historical third-party outage entries were not elevated to confirmed incidents because a retained underlying Federal Reserve notice was not verified. Current rail status is therefore incompletely verified; absence of a primary incident notice is not an all-clear.

No additional newly confirmed bank, credit-union, processor, card-network, core-banking, or identity-provider incident was established from the public sources reviewed today. Public FS-ISAC member intelligence is not available through this public-source review; only public FS-ISAC material is in scope.

## 5. Other monitored national-security and infrastructure categories

- **ODNI / intelligence community:** No new public assessment or testimony verified that materially changes the previous baseline.
- **CISA / FBI / NSA:** No new November 17 advisory or confirmed critical-infrastructure incident verified in the accessible official records reviewed. Earlier water-sector PLC and Iran-affiliated PLC findings remain in the baseline.
- **DoD:** No new relevant public installation-resilience directive verified.
- **DOE / FERC:** DOE's published Wagner Unit 4 order has a stated end date of November 17; no extension or replacement was visible in the DOE order registry at the time checked. The J.H. Campbell MISO order remains listed through February 12, 2027. These are reliability policy actions, not current outage reports.
- **White House / continuity:** No new relevant emergency declaration or continuity action verified.
- **NATO / EU / UK:** No new public development verified that materially changes U.S. civilian-infrastructure risk.
- **Ohio / central Ohio:** No new official disruption or protective action materially changing the local assessment was verified in the accessible records reviewed.
- **Upcoming hearing:** The House Homeland Security Committee's November 18 worldwide-threats hearing remains scheduled; no new testimony was available at the time of this report.

## 6. Calibrated assessment

### Localized and sector-specific disruption risk — supported

The JPMorgan event was a real but resolved bank-service disruption. Visa has acknowledged a third-party-provider incident, while explicitly saying its own systems and payment data such as card numbers were not indicated as affected. The n0n allegations warrant continued verification but are not confirmed breaches.

### Broader coordinated disruption risk — persistent concern, not established by this run

Third-party dependencies and payment-data exposure are genuine sector-wide resilience concerns. The public evidence does not link the Visa provider incident, the JPMorgan software bug, the Mastercard allegation, or recent non-financial technology outages into one coordinated campaign.

### Evidence of imminent danger — not established

No verified public evidence reviewed today establishes an imminent nationwide financial-system attack or payment-rail failure with a specific timeframe. The current Federal Reserve service-status data was not independently readable in this pass; no primary rail outage notice was verified.

## 7. Collection limitations and next verification points

- The public-source review did not access classified information, private FS-ISAC member channels, criminal infrastructure, or stolen data.
- No samples, hashes, victim notifications, or independent forensic report substantiating the three-company n0n allegation were located.
- Visa's third-party provider was not named; the exact event date, data categories, and connection—if any—to n0n remain unknown.
- Mastercard and JPMorgan have not publicly substantiated the specific n0n data-theft claim in the sources reviewed. JPMorgan's denial of a cyber cause applies to its transaction-processing outage; it does not by itself resolve the separate data-theft allegation.
- The Federal Reserve's live status page is a point-in-time view, not a complete public historical incident archive.
- Some CISA and state/local pages did not expose complete current records. This is a collection limitation, not evidence that no other incidents occurred.

Next checks: any named Visa provider disclosure; company statements or regulatory notices from JPMorgan and Mastercard; independently verifiable non-sensitive evidence of the claimed data categories; n0n deadline outcome as reported by reputable public sources; and any official post-incident report for the JPMorgan outage.

## Primary and corroborating sources

1. [Hackmanac alert as reproduced by a public report, November 16](https://twitter.com/H4ckmanac/status/2122275583019172078)
2. [Cybernews: Visa and JPMorgan n0n claims; Visa spokesperson response](https://cybernews.com/security/visa-jpmorgan-data-breach/)
3. [SOCRadar — JPMorgan claim record](https://socradar.io/free-tools/ransomware-intelligence/victims/jpmorgan-chase-co-n0n-f760b681)
4. [SOCRadar — Mastercard claim record](https://socradar.io/free-tools/ransomware-intelligence/victims/mastercard-n0n-6592c874)
5. [SOCRadar — public n0n threat-actor profile, updated November 17](https://socradar.io/blog/dark-web-profile-n0n-ransomware/)
6. [Reuters — JPMorgan transaction issue, November 16](https://www.investing.com/news/stock-market-news/downdetector-reports-outages-major-us-banks-5030747)
7. [Associated Press — bank and Zelle service impacts, November 16](https://apnews.com/article/bank-outage-chase-wells-fargo-truist-50fee2693c22f597fa6ca51a97ef2cda)
8. [Business Insider — JPMorgan restoration update, November 17](https://www.businessinsider.com/chase-other-major-banks-hit-by-online-outages-2026-11)
9. [JPMorgan November 17 Form 8-K — CFO succession, not a cyber disclosure](https://www.sec.gov/Archives/edgar/data/19617/000001961726000407/jpm-20261117.htm)
10. [Early Warning Services newsroom](https://www.earlywarning.com/newsroom)
11. [Visa Fall 2026 Biannual Threats Report announcement, November 17](https://investor.visa.com/news/news-details/2026/Visa-Report-AI-Enabled-Fraud-and-Third-Party-Attacks-Are-Scaling-Worldwide/default.aspx)
12. [Visa Fall 2026 Biannual Threats Report PDF](https://corporate.visa.com/content/dam/VCOM/corporate/visa-perspectives/newsroom/documents/visa-fall-biannual-threats-report-2026.pdf)
13. [Federal Reserve Financial Services official service-status page](https://www.frbservices.org/service-status/)
14. [StatusGator Fedwire Funds status — secondary status signal only](https://statusgator.com/services/federal-reserve/fedwire-funds)
15. [DOE 2026 emergency-order registry](https://www.energy.gov/ceser/2026-doe-202c-orders)
16. [House Homeland Security November 18 hearing](https://homeland.house.gov/hearing/worldwide-threats-to-the-homeland-25-years-after-9-11/)
