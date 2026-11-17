# Research and assessment methodology

## 1. Collection priorities
Prioritize original government notices, agency advisories, court or regulatory filings, official incident statements, technical reports, and directly attributable statements. Use reputable journalism for corroboration and context, not as a substitute for primary records where those exist.

## 2. Required time fields
Record event time (when the event occurred), publication time, update time, and collection time separately. Never present a publication date as an event date. If the event date is unknown, record it as unknown; do not substitute the leak-site listing date or the date a researcher observed a claim.

## 3. Evidence grading
- **A — Primary and direct:** official record, original advisory, filing, data release, or direct technical artifact.
- **B — Strong corroboration:** multiple independent, reputable sources with clear sourcing.
- **C — Credible but incomplete:** one reliable secondary report or a primary source with material gaps.
- **D — Unverified:** unattributed, anonymous, social-media-only, or otherwise not independently confirmed.
Evidence grade is not the same as confidence in an analytic judgment. A high-confidence assessment that a threat actor made a claim is not a high-confidence assessment that the claimed breach occurred.

## 4. Analytic confidence
- **High:** multiple strong, independent lines of evidence; few material alternatives.
- **Moderate:** evidence supports the judgment, but gaps or plausible alternatives remain.
- **Low:** limited, indirect, conflicting, or unverified evidence.
Explain the basis and identify what evidence would raise or lower confidence. Do not use numerical probabilities without a defensible method and denominator.

## 5. Threat taxonomy
Keep observed incident, threat activity, capability, warning, exercise, and preparedness action distinct. A capability statement is not evidence an attack occurred; an exercise is not an incident; generic preparedness messaging does not establish imminence.

## 6. Corroboration and contradiction
Seek independent confirmation. Record credible contradictory evidence and competing explanations. Do not count syndicated copies of one report as independent sources.

## 7. Impact and likelihood
Assess likelihood and impact separately. Describe the time horizon and affected geography or sector. A severe but low-likelihood scenario must not be described as imminent.

## 8. Operational security and privacy
Use public, lawfully accessible information only. Do not seek classified material, private accounts, leaked credentials, personal identifying information, or unauthorized access. Do not publish exploitable details that materially increase risk to critical systems. Redact personal data and sensitive infrastructure details where appropriate.

## 9. Update discipline
Change an assessment only when evidence changes. Maintain a dated change log, link source versions where possible, and explain why the judgment changed. Correct errors visibly rather than silently rewriting history.

## 10. Financial-sector incident separation
For banks, credit unions, payment networks, processors, ACH, Fedwire, FedNow, Zelle, core-banking providers, identity/authentication services, and critical third parties, classify each development as one of:
- confirmed compromise;
- credible but unconfirmed allegation;
- outage with confirmed non-cyber cause;
- outage with unknown cause;
- vulnerability or advisory;
- routine maintenance or test.

Keep cyber compromise separate from operational disruption. For every outage, record the affected service, event start/end (or state when unknown), geography, customer impact, official cause statement, shared dependencies, and recovery status. Distinguish bank websites/apps and third-party integrations from the underlying payment rails. A bank-interface outage does not establish a Fedwire, ACH, FedNow, Zelle, Visa, or Mastercard network outage.

For extortion or leak-site allegations:
- Treat each named organization as a separate claim.
- Treat each alleged data category as a separate claim.
- Record the date the claim was observed separately from the unknown or known intrusion date.
- State whether the data category is mapped to a specific organization or only asserted in aggregate.
- Seek non-sensitive samples, cryptographic hashes, victim/vendor confirmation, regulator disclosures, notification letters, court filings, and credible forensic reporting.
- Do not download, redistribute, or expose stolen data, credentials, payment data, malware, or personal information. Do not visit or interact with criminal infrastructure.
- Never infer that card numbers, CVVs, passwords, balances, account access, or funds are exposed unless evidence specifically supports that category.
- Treat a threat-actor listing as evidence of a claim, not proof of a breach. Do not infer a shared supplier or common intrusion from coincident claims without evidence.

Use official Federal Reserve Financial Services status information and operator statements where available. If historical status archives are unavailable, say so; do not elevate third-party-only outage records to confirmed incidents without primary corroboration. Public FS-ISAC newsroom material may be used; member-only intelligence is not treated as public evidence.

## 11. Minimum report structure
1. Key judgment and confidence.
2. What changed and relevant dates.
3. Evidence supporting the judgment.
4. Contradictory evidence and alternative explanations.
5. Unknowns and collection gaps.
6. Geographic/sector impact.
7. Indicators that would change the assessment.
8. Proportionate civilian implications.
9. Primary-source links.
