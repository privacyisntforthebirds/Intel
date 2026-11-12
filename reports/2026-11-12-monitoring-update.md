# Monitoring update and baseline corrections — 2026-11-12

## Run conclusion
No new or materially changed threat development published since the 2026-11-11 monitoring pass was verified in the accessible public sources reviewed. This is not a finding that no incidents occurred. CISA's main advisory and alert index pages returned HTTP 403 during this pass; CISA GovDelivery bulletins, FBI public advisories, NSA releases, DOE records, and other official records were used where available.

## Important historical items missing from the prior evidence baseline
These are **backfills**, not newly occurring events and not evidence of a new escalation on November 12. They materially improve the record of previously documented hostile activity.

### 1. Iran-affiliated actors disrupted U.S. industrial control systems
- **Event timing:** Specific victim event dates are not disclosed; the joint advisory described the campaign as active by April 7, 2026.
- **Publication:** Original joint advisory April 7, 2026 (AA26-097A); updated July 22, 2026.
- **Confirming agencies:** FBI, CISA, NSA, EPA, DOE, and U.S. Cyber Command Cyber National Mission Force.
- **What is established:** The agencies reported Iran-affiliated APT exploitation of internet-facing PLCs and disruptions across U.S. critical-infrastructure sectors. The advisory describes malicious project-file interactions and manipulation of HMI/SCADA displays, with operational disruption and financial loss.
- **Affected sectors:** Water and wastewater, energy, and government services/facilities, including local municipalities. The July 22 update expanded observed PLC manufacturer targeting beyond Rockwell Automation/Allen-Bradley to include Schneider Electric and Siemens, with possible other manufacturers.
- **Classification:** Confirmed hostile cyber activity and actual OT/PLC disruptions; the advisory also provides a continuing warning and mitigations.
- **Civilian implications:** Depending on the system and process affected, loss of monitoring/control can disrupt essential services. Public material does not identify all victims, locations, incident dates, or duration.
- **Confidence:** High that the multi-agency advisory documents the activity; moderate on the full scale and geographic distribution because victim details are not public.
- **Sources:** [Original AA26-097A joint advisory (PDF)](https://media.defense.gov/2026/Apr/07/2003907538/-1/-1/0/AA26-097A-IRANIAN-AFFILIATED-CYBER-ACTORS-EXPLOIT-PROGRAMMABLE-LOGIC-CONTROLLERS-ACROSS-US-CRITICAL-INFRASTRUCTURE_508C.PDF); [CISA July 22 update](https://content.govdelivery.com/accounts/USDHSCISA/bulletins/4219689); [FBI alert](https://www.fbi.gov/investigate/cyber/alerts/2026/iranian-affiliated-cyber-actors-exploit-programmable-logic-controllers-across-us-critical-infrastructure-update).

### 2. Water and wastewater PLC incidents reported in at least seven states
- **Event timing:** FBI said utilities had reported incidents since July 27, 2026.
- **Publication:** FBI/EPA public service announcement July 30, 2026; CISA sector bulletin July 30, 2026.
- **Confirming agencies:** FBI and EPA; CISA separately reported a significant increase in targeting of water-sector PLCs.
- **What is established:** Utilities in at least seven states reported incidents involving internet-facing Rockwell Automation/Allen-Bradley MicroLogix 1100 and 1400 PLCs. FBI reported loss of monitoring/control, loss of pressure, and flooding; at least one organization reported PLC project-file/ladder-logic discrepancies. CISA reported boil-water notices and sustained manual operations.
- **Affected geography/sectors:** At least seven U.S. states; water and wastewater utilities. The agencies did not identify the states or all affected utilities in the public notices.
- **Classification:** Actual malicious cyber incidents with documented operational degradation; actor attribution was not provided in the FBI/EPA notice. Do not merge this activity with the Iran-attributed campaign absent evidence linking them.
- **Civilian implications:** Potential interruption of water operations, pressure loss, flooding, boil-water advisories, and temporary manual operation. The notices do not establish a nationwide water-system outage.
- **Confidence:** High for the agency-reported incident count threshold and operational effects; limited regarding exact locations, victim count beyond the stated threshold, duration, and actor identity.
- **Sources:** [FBI/EPA July 30 PSA](https://www.fbi.gov/investigate/cyber/alerts/2026/malicious-cyber-actors-targeting-water-and-wastewater-sector-internet--facing-programmable-logic-controllers-causing-operational-disruptions); [CISA July 30 sector bulletin](https://content.govdelivery.com/accounts/USDHSCISA/bulletins/422e63c).

### 3. Active reconnaissance and capability development against Siemens S7 PLCs
- **Event timing:** Reconnaissance and capability-development activity was ongoing by August 19, 2026; exact first-observed date is not stated in the public release.
- **Publication:** August 19, 2026.
- **Confirming agencies:** NSA, CISA, FBI, DOE, and EPA.
- **What is established:** The agencies described targeted reconnaissance and capability development against U.S.-based Siemens S7 PLC installations, including AI-generated exploitation scripts disguised as monitoring tools.
- **Affected sectors:** Critical manufacturing, energy, water and wastewater, chemical, food and agriculture, and commercial facilities.
- **Classification:** Active threat warning, reconnaissance, and capability development. The public release does not establish successful exploitation or resulting service outages from this specific Siemens activity.
- **Civilian implications:** Successful exploitation of inadequately protected controllers could disrupt industrial processes, create safety hazards, damage equipment, or affect connected services. These are potential impacts, not confirmed consequences of this particular activity.
- **Confidence:** High that the agencies issued the warning and described the observed activity; lower regarding actor identity and the extent of any successful access, which are not specified in the public summary.
- **Sources:** [NSA August 19 release](https://www.nsa.gov/Press-Room/Press-Releases-Statements/Press-Release-View/Article/4578318/nsa-and-others-release-report-on-active-threats-of-programmable-logic-controlle/); [CISA advisory AA26-231A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-231a).

### 4. North Korean theft from Binance
- **Event time:** On or about October 29, 2026; Binance's incident report places the unauthorized wallet activity on October 29 UTC.
- **Publication:** FBI attribution October 31, 2026; Binance preliminary incident report November 3, 2026.
- **Confirming sources:** FBI attributed the theft to North Korea's TraderTraitor activity. Binance independently confirmed a serious security incident and reported approximately US$6.34 billion in digital assets impacted.
- **What is established:** FBI reported theft of more than US$6 billion in virtual assets from Binance. Binance reported unauthorized access to an internal wallet transaction-signing service and temporary suspension of withdrawals during containment. Binance said approximately US$2.85 billion had been frozen or intercepted and that 98% of affected token assets had been replenished by its November 3 update; Binance stated it would absorb the financial impact. Those recovery figures are company-reported and were not independently audited in this monitoring pass.
- **Affected geography/sectors:** Global cryptocurrency exchange and digital-asset ecosystem; not evidence of compromise of U.S. banks, payment-card networks, or traditional financial-market clearing systems.
- **Classification:** Actual cyber theft and service disruption, with FBI state attribution.
- **Civilian implications:** Direct effects primarily concern exchange users and digital-asset counterparties; possible broader effects include temporary exchange-service disruption, asset-market volatility, and laundering activity. The public evidence does not establish disruption to core U.S. financial infrastructure.
- **Confidence:** High that FBI publicly attributed the theft and Binance confirmed the incident; company-reported recovery/replenishment amounts remain subject to its ongoing investigation and independent review.
- **Sources:** [FBI October 31 alert](https://www.fbi.gov/investigate/cyber/alerts/2026/north-korea-responsible-for-6-billion-binance-attack); [Binance November 3 incident report](https://www.binance.com/en/square/post/384336744180903).

## No new change since the previous run
- No newly published, verified ODNI threat assessment or intelligence-community testimony affecting the infrastructure-risk judgment was located.
- DOE's November 6 PREPA orders remain in effect November 8, 2026–February 5, 2027; no subsequent change was verified in this pass.
- The August 26 bulk-power-system emergency declaration remains an existing policy action; no new implementing rule or equipment-specific determination was verified in this pass.
- No new official Ohio or central Ohio emergency/infrastructure notice materially changing the assessment was verified in accessible records.
- No new public continuity-of-government action or relevant DoD installation-resilience directive was verified.

## Calibrated assessment
- **Localized disruption risk: supported.** The FBI/EPA and CISA water-sector notices document incidents and operational degradation at utilities in at least seven states. The Iran-attributed PLC advisory documents disruptions across several U.S. critical-infrastructure sectors. Puerto Rico's grid emergency remains a separate, documented regional reliability concern.
- **Broader coordinated disruption risk: persistent concern, not established as an active nationwide campaign.** The public record documents multiple threat actors and campaigns affecting operational technology, but does not establish that these incidents form one coordinated nationwide operation.
- **Evidence of imminent danger: not established.** No verified public source reviewed in this run identifies a specific imminent nationwide attack with a stated timeframe.

## Ohio relevance and limitations
The public FBI/EPA water notice does not name the seven or more states. The Iran-affiliated advisory names sectors, including local municipalities, but does not identify specific victim locations. No evidence in the reviewed material links the cited incidents specifically to Ohio. This does not prove Ohio systems were unaffected.
CISA's main advisory and alert index pages returned HTTP 403 during this run. Official CISA GovDelivery bulletins, FBI notices, NSA releases, DOE records, and the original joint advisory PDF were accessible and used where available. Missing or inaccessible source records are not treated as evidence of safety.

## Run-to-run conclusion
No new material development after the November 11 report was verified. This report corrects a material baseline coverage gap by backfilling three critical-infrastructure cyber advisories/incidents and one major virtual-asset theft that predated the prior reports. These corrections change the completeness of the evidence ledger, not the event chronology; they do not constitute a November 12 escalation.