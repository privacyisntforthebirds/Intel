# Public Threat Intelligence Observatory — Monitoring Update
## 2026-11-14

**Assessment:** Localized disruption risk is supported by verified incidents. This pass identified a major nationwide transportation-service disruption on November 13 that was not captured in the November 13 report. No public evidence reviewed establishes an imminent nationwide attack or a coordinated hostile campaign.

## Executive summary

1. **FAA nationwide ground stop — material new finding.** On November 13, the FAA stopped departures at U.S. airports after communications and radar-data instability affected multiple Air Route Traffic Control Centers. The ground stop was lifted at 8:15 p.m. Eastern. The event caused major travel disruption. The technical root cause remains under investigation; officials said they had no indication of a cyberattack.
2. **Microsoft 365 outage — recovery status updated.** Microsoft said on November 14 that it had restored service to remaining impacted customers and regions. AP reported Microsoft's statement. Reuters had reported earlier on November 14 that consumer services were recovered while enterprise recovery was still being monitored. Microsoft's full post-incident report remains pending.
3. **Existing grid baseline unchanged.** DOE's Wagner Unit 4 order remains effective through November 17, 2026. No extension or replacement order was verified in this pass.
4. **No other material new public warning or incident verified** in the ODNI, CISA/FBI/NSA, DoD, DOE/FERC, White House, allied-government, or Ohio/local source checks. Several source pages were dynamic, inaccessible, or did not expose complete current records; this is not proof that no other events occurred.

## 1. FAA nationwide ground stop — confirmed transportation-system disruption

- **Event date:** Friday, November 13, 2026.
- **Event time:** Transportation Secretary Sean Duffy said instability began at approximately 3:36 p.m. Eastern.
- **Publication date:** FAA and DOT statements published November 13, 2026.
- **Confirming authorities:** Federal Aviation Administration (FAA); U.S. Department of Transportation (DOT). DHS Secretary Markwayne Mullin also briefed reporters.
- **Affected geography / sector:** Nationwide U.S. airports and airspace; commercial passenger aviation and air cargo.
- **Classification:** Actual infrastructure/service disruption; not a confirmed hostile incident.

The FAA's preliminary statement says it issued a nationwide ground stop for all U.S. airports after communication issues affected multiple Air Route Traffic Control Centers. DOT described intermittent telecommunications outages that affected the stability of communications and radar systems used by air traffic control.

In the DOT account, Duffy said radar and communications became unstable at centers and TRACONs around the country. He reported more than 3,500 aircraft were airborne at the time and that controllers used established procedures to bring aircraft safely to the ground. Duffy said the airspace reopened at 8:15 p.m. Eastern. Reopening did not immediately restore normal airline schedules.

Duffy attributed the problem to overloaded legacy switches and routers handling data inconsistently; he said newer IP switches that had been installed did not fail. This is an official preliminary explanation, not a final engineering root-cause report. The FAA's own statement explicitly said the information was preliminary and that technicians were investigating.

The Associated Press reported at least 827 diversions and substantial delays and cancellations, with recovery expected to take time as aircraft and crews were repositioned. These are secondary-source operational figures, not a final FAA accounting.

### Civilian implications

The incident interrupted nationwide air departures and affected passengers, airline operations, and cargo movements. It demonstrates that a failure in shared communications and surveillance infrastructure can cause broad civilian disruption even without a hostile act. No report reviewed here indicates aircraft were lost; officials said aircraft already airborne were brought down safely.

### Attribution, uncertainty, and counterevidence

DHS Secretary Mullin said officials saw no indication of a cyberattack and described the problem as apparently mechanical. Duffy said the FAA's new SMART/AI forecasting tool was disconnected from the equipment that failed and was not involved. These statements weigh against a cyberattack or AI-system failure as the cause, but the public investigation was not complete. The specific failed component, why it overloaded, and whether configuration or contractor factors contributed remain unknown.

**Confidence:** High that the nationwide ground stop and communications/radar instability occurred; moderate on the precise technical cause pending a final investigation.

**Primary sources:**
- FAA preliminary statement: https://www.faa.gov/newsroom/faa-statement-nationwide-ground-stop
- DOT statement and Secretary Duffy's briefing remarks: https://www.transportation.gov/briefing-room/icymi-us-transportation-secretary-sean-p-duffy-announces-lifting-nationwide-ground
- AP incident reporting and operational context: https://apnews.com/article/f81b0904331dafad6133f291e5f531a8

## 2. Microsoft 365 outage — recovery update

- **Event began:** November 12, 2026; tracked by Microsoft as Exchange Online incident EX1550543 and broader Microsoft 365 incident MO1550821.
- **Publication / status update:** November 14, 2026.
- **Confirming source:** Microsoft service-health statements, as reported by AP and Reuters and reproduced in an institutional IT service notice.
- **Affected geography / sectors:** Global cloud productivity and communications services; businesses, government agencies, healthcare, courts, airlines, and other organizations using affected services.
- **Classification:** Actual cloud-service availability incident; no hostile activity indicated by Microsoft.

On November 14, Microsoft said it had completed efforts to address the underlying issue and restored service to remaining impacted customers and regions. AP quoted the company's statement. Reuters reported earlier on November 14 that consumer products were fully recovered while Microsoft 365 enterprise services were still in sustained but incomplete recovery and the email backlog was being monitored. An institutional IT service notice also reproduced a Microsoft service-health entry marked "Service has been restored."

Microsoft said the incident was not related to cyber activity or AI/agents and described it as an issue introduced during an earlier network-capacity upgrade that surfaced after a subsequent network change. The full post-incident report and final defense-in-depth actions remain pending.

**Assessment:** The outage is now treated as a resolved service incident based on Microsoft's November 14 statement, but the promised post-incident report has not yet been reviewed. No evidence reviewed links it to the FAA ground stop; officials and Microsoft treated the events as separate.

**Sources:**
- Microsoft public service status: https://status.cloud.microsoft/
- AP report quoting Microsoft's November 14 restoration statement: https://apnews.com/article/ca395c0f1e51af784b6d70afb6554f6a
- Reuters report on staged recovery: https://www.reuters.com/technology/microsoft-says-consumer-products-services-recovered-still-monitoring-enterprise-2026-11-14/
- Institutional IT service notice reproducing Microsoft service-health updates: https://thersac.icts.thers.ac.jp/hc/en-us/articles/64262985209881-November-13-2026-Microsoft-365-Outage-MO1550821-Restored

## 3. Existing items reviewed; no material change verified

- **PJM / Wagner Unit 4:** DOE's August 19 order remains effective August 20 through November 17, 2026. No new extension or replacement order was located. This is an existing grid-reliability action, not evidence of an imminent blackout. https://stage.energy.gov/articles/energy-secretary-acts-protect-mid-atlantic-grid
- **Water-sector PLC incidents:** FBI/EPA's July 30 report of incidents in at least seven states remains a significant prior confirmed finding; no new victim geography or incident update was verified in this pass. https://www.fbi.gov/investigate/cyber/alerts/2026/malicious-cyber-actors-targeting-water-and-wastewater-sector-internet--facing-programmable-logic-controllers-causing-operational-disruptions
- **Iran-affiliated PLC activity:** No new public update materially changing the April advisory / July update baseline was verified.
- **ODNI / intelligence community:** The 2026 Annual Threat Assessment remains the current strategic baseline; no new relevant testimony or declassified reporting was verified in this pass.
- **CISA / FBI / NSA:** FBI's 2026 alert index was reviewed. It lists several previously issued advisories, including January Kimsuky QR-code phishing, February ATM jackpotting, March Russian intelligence messaging-account targeting, April GRU router exploitation, and the July industrial-control advisories. These are not new November 14 incidents and were not treated as new alerts.
- **DoD readiness:** No new relevant public installation-resilience directive was verified.
- **DOE / FERC:** No new relevant order or material change verified beyond the existing Wagner order.
- **White House / continuity:** The current Presidential Actions listing showed no new relevant continuity-of-government action or emergency declaration in the reviewed entries.
- **Allied governments:** No new allied-government threat warning with a direct, verified implication for U.S. civilian infrastructure was identified.
- **Ohio / central Ohio:** No new official infrastructure disruption or protective action materially changing the local assessment was verified. The FAA event was nationwide, not a Columbus-specific incident.

## 4. Calibrated assessment

### Localized disruption risk — supported

There are verified examples of actual disruption to water-sector operations, Puerto Rico's electric grid, and now nationwide U.S. aviation communications. The FAA event was broad in geographic scope but time-limited and attributed provisionally to a technical/legacy-system failure rather than hostile activity.

### Broader coordinated disruption risk — persistent strategic concern, not established as an active campaign

Previously documented state-linked cyber activity against U.S. infrastructure remains serious. The FAA incident and Microsoft outage do not establish a common actor or coordinated campaign. No public evidence reviewed links them.

### Evidence of imminent danger — not established

No verified public evidence reviewed establishes an imminent nationwide attack or emergency with a specific timeframe. The FAA event was a serious completed disruption, not evidence of an impending attack.

## 5. Collection limitations

- FAA's statement is explicitly preliminary; the technical investigation and final root-cause report remain outstanding.
- Microsoft's public status page is JavaScript-rendered and did not expose the complete event timeline through the accessible text interface. Restoration details were cross-checked against AP, Reuters, and an institutional IT notice reproducing Microsoft service-health updates.
- Some CISA and Ohio state/local pages did not expose complete current records. No conclusion of safety is drawn from inaccessible sources.
- This assessment uses public information only and does not imply access to classified intelligence.

## Change log

- 2026-11-14 — Added the November 13 FAA nationwide ground stop as a newly identified material transportation-system disruption; updated Microsoft 365 incident status to reflect Microsoft's November 14 restoration statement; retained uncertainty about final technical root causes.
