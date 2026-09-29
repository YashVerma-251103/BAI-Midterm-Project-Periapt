# Research Thread 6 — Binding US Cyber Requirements on Commercial Satellite Operators

**Agent:** general-purpose subagent (Sonnet) | **Run:** 2026-09-29 | **Items covered:** 30 (new, added after the original 29-item plan; see `research/Research_Findings.md` item 30)

## Prompt given

> Research question (for a university business-strategy report, date today: 2026-09-29): Does any BINDING (legally enforceable, not voluntary guidance) US requirement exist that obliges COMMERCIAL satellite operators to perform cybersecurity vulnerability management — i.e., identify, prioritise, and remediate/patch vulnerabilities — across ground segment, links, or spacecraft? We already know SPD-5 (85 FR 56155) states "principles" and NIST IR 8270 / IR 8401 are voluntary guidance. We need to know whether anything with legal teeth exists beyond those.
>
> Check at least these candidate sources, using WebSearch/WebFetch, and prefer primary sources (eCFR, Federal Register, FCC orders, DFARS text, agency sites) over blogs:
> 1. FCC: satellite licensing conditions (47 CFR Part 25), any cybersecurity certification/requirements in FCC space orders (e.g., the 2024–2026 "Space Modernization" / Part 100 proceedings, any cyber risk-management plan certification requirement for licensees, Cyber Trust Mark is irrelevant unless it touches satellite).
> 2. DoD contracting: DFARS 252.204-7012, CMMC (32 CFR Part 170, 48 CFR rule) — do these apply to commercial satellite operators selling to DoD (e.g., Space Force Commercial Augmentation Space Reserve, SDA contracts)? What do they require re: flaw remediation (NIST SP 800-171 3.14.1)?
> 3. NOAA commercial remote sensing licensing (15 CFR Part 960) — any cybersecurity/data protection conditions?
> 4. FAA/DOT launch licensing (14 CFR Part 450) — any cyber requirement?
> 5. CIRCIA (Cyber Incident Reporting for Critical Infrastructure Act) final rule status as of 2026 and whether space operators are covered entities — note it's reporting, not vuln management.
> 6. Any proposed/enacted legislation: e.g., "Satellite Cybersecurity Act", space designated as critical infrastructure sector (status as of 2026), Executive Orders on space cyber.
> 7. FedRAMP / FISMA if operators host federal data.
>
> For each: state (a) binding or not, (b) who it applies to (all commercial operators vs only government contractors vs only licensees), (c) what exactly it requires — does it require vuln identification/prioritisation/remediation or just something weaker (reporting, a plan, certification), (d) status/date, (e) primary-source URL. Quote exact regulatory text where you can. Mark anything you could not confirm from a primary source as UNVERIFIED. Do not guess or fill gaps from memory — explicitly say "not found" where applicable.
>
> End with a 5-line bottom line: is the claim "US commercial satellite operators are legally bound to manage vulnerabilities" TRUE, PARTIALLY TRUE (for which subset), or FALSE?
>
> Return the full findings as your final message (markdown). Do not edit any project files.

## Approach followed

Pulled primary texts directly: the eCFR versioner API (as of 2026-09-01), the Federal Register API and full text, the circulated FCC Report and Order (FCC-CIRC2607-02), congress.gov bill text, the NIST SP 800-171r2 PDF, and CISA pages. Full-text keyword searches ("cyber", "vulnerab", "encrypt", "jamming") were run over the FCC R&O/FNPRM and NPRM texts. Where only law-firm or trade-press sources were available, the output says so and marks the claim UNVERIFIED. Triggered by the user's challenge that "companies are legally bound to do the security" (session of 2026-09-29).

## Sources visited

- https://www.ecfr.gov/current/title-47/part-25/section-25.271
- https://docs.fcc.gov/public/attachments/DOC-422740A1.pdf
- https://www.federalregister.gov/documents/2025/12/05/2025-22019/space-modernization-for-the-21st-century
- https://www.globalpolicywatch.com/2026/07/fcc-approves-massive-modernization-of-satellite-licensing-regime/
- https://www.federalregister.gov/documents/2025/12/15/2025-22830/protecting-the-nations-communications-systems-from-cybersecurity-threats
- https://www.ecfr.gov/current/title-48/section-252.204-7012
- https://www.ecfr.gov/current/title-32/part-170
- https://www.federalregister.gov/documents/2025/09/10/2025-17359/defense-federal-acquisition-regulation-supplement-assessing-contractor-implementation-of
- https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-171r2.pdf
- https://www.washingtontechnology.com/contracts/2026/09/cmmcs-phase-2-suspension-locked-binding-regulation/415883/
- https://federalnewsnetwork.com/cybersecurity/2026/07/pentagon-suspends-cmmc-phase-two-requirements-launches-review-of-program/
- https://defensescoop.com/2026/01/27/space-force-commercial-reserve-companies-casr-plans-2026/
- https://www.ecfr.gov/current/title-15/part-960
- https://www.ecfr.gov/current/title-14/part-450
- https://www.federalregister.gov/documents/2024/04/04/2024-06526/cyber-incident-reporting-for-critical-infrastructure-act-circia-reporting-requirements
- https://www.cisa.gov/topics/cyber-threats-and-advisories/information-sharing/cyber-incident-reporting-critical-infrastructure-act-2022-circia
- https://federalnewsnetwork.com/cybersecurity/2026/07/circia-other-big-cyber-rules-expected-to-get-finalized-this-fall/
- https://www.cisa.gov/topics/critical-infrastructure-security-and-resilience/critical-infrastructure-sectors
- https://www.congress.gov/119/bills/s3404/BILLS-119s3404is.htm
- https://www.mayerbrown.com/en/insights/publications/2025/12/securing-the-final-frontier-cybersecurity-risk-regulation-and-compliance-trends-in-space-and-satellite-operations
- https://www.fedramp.gov/2026/scope/

## Full output

# Binding US cyber requirements on commercial satellite operators: vulnerability management (as of 2026-09-29)

Method: I pulled primary sources directly. These were the eCFR versioner API (as of 2026-09-01), the Federal Register API and full text, the FCC circulated Report and Order text (FCC-CIRC2607-02), congress.gov bill text, NIST SP 800-171r2 PDF, and CISA pages. Where only law-firm or trade press was available I say so. Nothing below comes from memory.

## Headline

No binding US rule requires commercial satellite operators, as a class, to identify, prioritise and remediate/patch vulnerabilities in the ground segment, links or spacecraft. The strongest binding hooks are:
- (a) a one-sentence FCC licence duty to secure facilities and satellite commands "against unauthorized access and use";
- (b) NOAA licence conditions for Tier 2/3 remote-sensing systems (encryption plus access-prevention);
- (c) contract-only DFARS 252.204-7012 / CMMC, which do require flaw remediation, but only on contractor systems that handle CUI or covered defence information, and only for firms with DoD contracts.

---

## 1. FCC (47 CFR Part 25, and the Part 100 "Space Modernization" proceeding)

| Item | Finding |
|---|---|
| (a) Binding? | Yes, but the requirement is weak. It is a licence rule. |
| (b) Applies to | All FCC licensees, including space station and earth station operators (the rule text says "The licensee of a facility licensed under this part"). |
| (c) Requires | Only a general "secure against unauthorized access" duty. It has no vulnerability identification, prioritisation, patching, plan or certification requirement. |
| (d) Status | 47 CFR 25.271(d) is in force in the eCFR text as of 2026-09-01. The Part 100 rewrite was adopted 22 Jul 2026, but the effective date is not yet set (see below). |
| (e) URLs | https://www.ecfr.gov/current/title-47/part-25/section-25.271 ; https://docs.fcc.gov/public/attachments/DOC-422740A1.pdf ; https://www.federalregister.gov/documents/2025/12/05/2025-22019/space-modernization-for-the-21st-century |

Exact text of 47 CFR 25.271(d):
> "The licensee shall ensure that the licensed facilities are properly secured against unauthorized access or use whenever an operator is not present at the transmitter. For space station operations, this includes securing satellite commands against unauthorized access and use."

25.271(c)(2) also conditions remote-controlled earth stations on "appropriate security measures to prevent unauthorized entry or operations". That is physical/operational security, not vulnerability management.

Part 100 / Space Modernization:
- The NPRM was published at 90 FR 56338 on 2025-12-05. The Report and Order and FNPRM (SB Docket 25-306) were adopted 2026-07-22.
- In the circulated R&O text, the old 25.271(d) is carried over verbatim as proposed 47 CFR 100.202(d) "Unauthorized access": "Licensees shall ensure that the licensed facilities are properly secured against unauthorized access or use. For space station operations, this includes securing satellite commands against unauthorized access and use."
- I searched the R&O and FNPRM text (about 1.1 MB) and the NPRM full text (about 700 KB) for "cyber", "vulnerab", "encrypt" and "jamming". Result: zero hits for "cyber". There is no cyber risk-management plan, certification or vulnerability requirement in either document.
- Effective date: the Space Bureau will issue a public notice announcing it (per Global Policy Watch, secondary: https://www.globalpolicywatch.com/2026/07/fcc-approves-massive-modernization-of-satellite-licensing-regime/).
- UNVERIFIED: I used the circulated text (FCC-CIRC2607-02). The final released, adopted text could differ.
- Related but not satellite-specific: the FCC rescinded its Jan 2025 CALEA cybersecurity Declaratory Ruling and NPRM for telecom carriers (89 FR notice, 2025-12-15, https://www.federalregister.gov/documents/2025/12/15/2025-22830/protecting-the-nations-communications-systems-from-cybersecurity-threats). That ruling never targeted satellites and is now withdrawn.

## 2. DoD contracting: DFARS 252.204-7012, CMMC (32 CFR 170), DFARS 252.204-7021

| Item | Finding |
|---|---|
| (a) Binding? | Yes, but only as a contract condition. There is no general legal duty. |
| (b) Applies to | Only firms whose DoD contract or subcontract includes the clause, and only for "covered contractor information systems" that process, store or transmit Covered Defense Information (CDI/CUI). It is not tied to being a satellite operator. |
| (c) Requires | Yes, this is the closest thing to real vulnerability management. NIST SP 800-171 3.14.1 requires flaw remediation, but scoped to CUI-handling information systems. It does not cover spacecraft or RF links as such, unless they are in the CUI system boundary. |
| (d) Status | DFARS 7012 (MAY 2024 version) is in force. The CMMC 32 CFR 170 rule and the 48 CFR CMMC rule (90 FR 43560, published 2025-09-10, effective 2025-11-10) are in force. Phase 1 (self-assessments) is live. |
| (e) URLs | https://www.ecfr.gov/current/title-48/section-252.204-7012 ; https://www.ecfr.gov/current/title-32/part-170 ; https://www.federalregister.gov/documents/2025/09/10/2025-17359/defense-federal-acquisition-regulation-supplement-assessing-contractor-implementation-of ; https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-171r2.pdf |

DFARS 252.204-7012(b)(2)(i), exact text:
> "the covered contractor information system shall be subject to the security requirements in National Institute of Standards and Technology (NIST) Special Publication (SP) 800-171 ... in effect at the time the solicitation is issued or as authorized by the Contracting Officer."

The clause defines "Covered contractor information system" as "an unclassified information system that is owned, or operated by or for, a contractor and that processes, stores, or transmits covered defense information." It also requires that a cyber incident be reported "within 72 hours of discovery".

NIST SP 800-171 Rev 2, 3.14.1, verified in the PDF:
> "Identify, report, and correct system flaws in a timely manner."

The discussion says:
> "Organizations identify systems that are affected by announced software and firmware flaws including potential vulnerabilities resulting from those flaws and report this information to designated personnel ... Security-relevant updates include patches, service packs, hot fixes, and anti-virus signatures."

Note that "timely" is left to the organisation to define. Nothing requires risk-based prioritisation (for example, by exploitability). NIST does not define the timeframe.

32 CFR 170.3(a): the rule applies to "All DoD contract and subcontract awardees that will process, store, or transmit information, in performance of the DoD contract, that meets the standards for FCI or CUI on contractor information systems". 170.3(c) extends this to commercial items, except COTS-only.

3.14.1 shows up in the CMMC tables as SI.L1-b.1.xii at Level 1 (32 CFR 170.15 table). Level 2 requires all of 800-171 R2 to be "MET" (170.16), and Level 2 (C3PAO) is 170.17. The 170.16 self-assessment requires a MET result for all 800-171 requirements, as I read the text (170.16(a)(1)).

Phase status:
- Secondary sources report that DoD suspended CMMC Phase 2 (the third-party-assessment requirement) on 2026-07-13.
- A 2026-09-03 class deviation reportedly told contracting officers to strip third-party-assessment requirements from contracts. Sources: Washington Technology https://www.washingtontechnology.com/contracts/2026/09/cmmcs-phase-2-suspension-locked-binding-regulation/415883/ and Federal News Network https://federalnewsnetwork.com/cybersecurity/2026/07/pentagon-suspends-cmmc-phase-two-requirements-launches-review-of-program/.
- Self-attestation to the NIST standards still applies.
- UNVERIFIED from a primary source: I did not retrieve the actual class deviation text.

Gaps:
- Not found: any Space Force or SDA solicitation or contract text. That includes the Commercial Augmentation Space Reserve (CASR) documents.
- A search on CASR turned up only the framework, which names "cybersecurity" as an element and a planned surveillance plan (secondary: https://defensescoop.com/2026/01/27/space-force-commercial-reserve-companies-casr-plans-2026/). No binding text was found. Whether a given contract carries 7012 is UNVERIFIED.
- Also pending, from search results only: the FAR CUI rule (proposed, 91 FR 37550, 2026-06-23, Rev 3 baseline, comments closed 2026-07-23). Not final. It would extend the NIST 800-171 approach to all federal civilian contractors that handle CUI. UNVERIFIED beyond secondary summaries.

## 3. NOAA commercial remote sensing (15 CFR Part 960)

| Item | Finding |
|---|---|
| (a) Binding? | Yes. These are licence conditions. |
| (b) Applies to | Only NOAA-licensed private remote-sensing space systems, and only those classified Tier 2 or Tier 3 (not Tier 1). §960.9 covers Tier 2 and §960.10 covers Tier 3. Both also carry the §960.8 "all tiers" conditions. |
| (c) Requires | Encryption and access-prevention measures tied to limited-operations directives. Not vulnerability identification or remediation. |
| (d) Status | In force per the eCFR as of 2026-09-01. Source: 85 FR 30806, 20 May 2020. |
| (e) URL | https://www.ecfr.gov/current/title-15/part-960 |

§960.9(a)(1) (Tier 2), exact text:
> "The ability to implement National Institute of Standards and Technology-approved encryption, in accordance with the manufacturer's security policy, wherein the key length is at least 256 bits, for communications to and from the on-orbit components of the system related to tracking, telemetry, and control and for transmissions throughout the system of the data specified in the limited-operations directive; and (ii) Implementing measures, consistent with industry best practice for entities of similar size and business operations, that prevent unauthorized access to the system and identify any unauthorized access in the event of a limited-operations directive."

Tier 3 has the same wording (§960.10(a)(1)(i)(A)/(B)).

The application appendix has an affirmation that "there will be, at all times, measures in place to ensure positive control of any spacecraft in the system that have propulsion... Such measures include encryption of telemetry, command, and control communications or alternative measures consistent with industry best practice." I did not confirm the exact appendix letter.

This is the most specific binding text I found touching TT&C links. It is still about encryption and unauthorized-access prevention, with no reference to patching or vulnerabilities.

## 4. FAA / DOT launch licensing (14 CFR Part 450)

| Item | Finding |
|---|---|
| (a) Binding? | Yes, but there is no cyber requirement. |
| (b) Applies to | Launch/reentry licence applicants, and payload review. |
| (c) Requires | Nothing on vulnerability management. A search of Part 450 found no "cyber", "patch" or "information security" text. The only related item is a disclosure: §450.43(i)(1)(x) requires an applicant to identify "Any encryption associated with data storage on the payload and transmissions to or from the payload". "Vulnerability" hits in Part 450 refer to debris/people vulnerability. |
| (d) Status | In force. |
| (e) URL | https://www.ecfr.gov/current/title-14/part-450 |

## 5. CIRCIA (reporting only, not vulnerability management)

| Item | Finding |
|---|---|
| (a) Binding? | The statute is enacted (2022). The implementing rule is NOT yet final. |
| (b) Applies to | Statute: critical infrastructure entities. Proposed rule text explicitly lists satellite operators. |
| (c) Requires | Reporting of covered cyber incidents (72 hours) and ransom payments (24 hours). Nothing about vulnerability management. |
| (d) Status | The NPRM was published 2024-04-04 at 89 FR 23644. CISA missed the Oct 2025 statutory deadline. CISA's page says only "CISA continues to work on the final rule" with no date. Trade press citing the Unified Agenda gives a target of September 2026. I searched the Federal Register through 2026-09-29 for "CIRCIA" and found no final rule. |
| (e) URLs | https://www.federalregister.gov/documents/2024/04/04/2024-06526/cyber-incident-reporting-for-critical-infrastructure-act-circia-reporting-requirements ; https://www.cisa.gov/topics/cyber-threats-and-advisories/information-sharing/cyber-incident-reporting-critical-infrastructure-act-2022-circia ; https://federalnewsnetwork.com/cybersecurity/2026/07/circia-other-big-cyber-rules-expected-to-get-finalized-this-fall/ |

The NPRM's proposed covered-entity criterion, exact text:
> "The entity provides communications services by wire or radio communications, as defined in 47 U.S.C. 153(40), 153(59), to the public, businesses, or government, as well as one-way services and two-way services, including but not limited to: ... (iii) Satellite operators; ..."

So satellite operators would probably be covered through the Communications sector under the proposal, but the final rule could change that. It would be reporting only.

## 6. Legislation, executive orders, critical-infrastructure designation

Space is not one of the 16 CISA-listed critical infrastructure sectors. The list (chemical through water) has no space sector, per https://www.cisa.gov/topics/critical-infrastructure-security-and-resilience/critical-infrastructure-sectors.

| Item | Binding? | Details |
|---|---|---|
| Satellite Cybersecurity Act of 2025, S. 3404 (Peters/Cornyn) | No. It is not enacted. | Introduced 2025-12-09. Press says it advanced through Senate Commerce (Peters release, not primary; I could not retrieve the bill's action page as congress.gov blocked it). Text (https://www.congress.gov/119/bills/s3404/BILLS-119s3404is.htm): a GAO study; a Commerce clearinghouse of "voluntary cybersecurity recommendations"; a strategy. §6 (Rules of construction): "Nothing in this Act shall be construed to— (1) designate commercial satellite systems or other space assets as a critical infrastructure sector; or (2) infringe upon or alter the authorities of the agencies..." Even if enacted it imposes no duties on operators. |
| Space Infrastructure Act, H.R. 1154 | No. | Introduced 2025-02-10. It would add a space systems sector to the critical infrastructure list. Only committee-referral status was found (secondary sources). Not enacted. |
| EO 14144 (90 FR 6755, 17 Jan 2025) §3(e), as amended by EO 14306 (90 FR 24723, 11 Jun 2025) | Binds federal agencies, not commercial operators directly. | Text: "agencies shall take steps to continually verify that Federal space systems have the requisite cybersecurity capabilities..." and directs USGS/NOAA/NASA to recommend FAR civil space contract requirements: "a risk-based, tiered approach for all new civil space systems... designed to apply at minimum to the civil space systems' on-orbit segments and link segments," covering command encryption/authentication, anomaly detection and recovery, and "secure software and hardware development practices, consistent with the NIST SSDF". Nothing on patching or vulnerability management is in that section. EO 14306's amendment text does not strike this space subsection (it strikes other subsections and redesignates 3(c)-(e) as 3(a)-(c)); I read that as the space provision surviving. Not confirmed by a consolidated text. Status: no FAR final rule on civil space cyber was found. The only FAR items surfaced were the Revolutionary FAR Overhaul and the CUI proposed rule, and I did not check whether either includes the space language. If it is ever added, it would bind civil-space contractors only. |
| Mayer Brown, Dec 2025 (secondary) | n/a | Concludes there is no single unified cyber regulator for US space and that obligations arise via contracts and other triggers: https://www.mayerbrown.com/en/insights/publications/2025/12/securing-the-final-frontier-cybersecurity-risk-regulation-and-compliance-trends-in-space-and-satellite-operations. It does not mention FCC 25.271. |

## 7. FedRAMP / FISMA

| Item | Finding |
|---|---|
| (a) Binding? | Yes, but only when the operator sells cloud services or otherwise runs systems that hold federal data. |
| (b) Applies to | Cloud service offerings that "create, collect, process, store, or maintain Federal information on behalf of a Federal agency" (fedramp.gov scope text, https://www.fedramp.gov/2026/scope/). Agencies "must" use FedRAMP-certified services where in scope. Contractors running systems on behalf of agencies fall under FISMA via the agency, per the general FISMA framework. I did not retrieve the statute text (44 U.S.C. 3554), so this is UNVERIFIED as a primary quote. |
| (c) Requires | Authorisation against NIST 800-53 baselines with continuous monitoring. Flaw remediation (SI-2) is part of those baselines, and the 800-171 mapping table lists SI-2 "Flaw Remediation". Whether the FedRAMP baseline text itself requires timed vulnerability remediation was not confirmed. The scope page does not address it. |
| (d) Status | In force. |
| (e) URLs | https://www.fedramp.gov/2026/scope/ ; https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-171r2.pdf (SI-2 mapping) |

Applicability to satellite ground-station-as-a-service or on-orbit assets was not found. It would only matter for an operator that hosts federal data as a cloud provider.

---

## Bottom line

1. The claim "US commercial satellite operators are legally bound to manage vulnerabilities" is FALSE as a general statement. It is PARTIALLY TRUE only for narrow subsets, and the binding text is weaker than vulnerability management (a one-line unauthorised-access duty, an encryption condition).
2. All FCC licensees have a binding but generic duty (47 CFR 25.271(d), carried into proposed 100.202(d)) to secure facilities and satellite commands against unauthorised access. It contains no identify/prioritise/patch obligation, and the July 2026 R&O adds no cyber text ("cyber" appears 0 times in the R&O and the NPRM).
3. NOAA-licensed Tier 2/3 remote sensing operators must implement 256-bit NIST-approved encryption on TT&C links and access-prevention measures (15 CFR 960.9 and 960.10). Encryption is not vulnerability management.
4. The only binding flaw-remediation duty ("Identify, report, and correct system flaws in a timely manner", NIST SP 800-171 3.14.1) reaches operators only through DoD contracts (DFARS 252.204-7012, CMMC Phase 1 self-assessment in force; Phase 2 third-party audits reportedly suspended in 2026), and only for systems handling CUI/CDI, not the spacecraft or links as such. Contract-specific applicability for Space Force or SDA deals is UNVERIFIED, and CIRCIA (reporting only, final rule not yet published), space-as-critical-infrastructure and S. 3404 (voluntary, unenacted) are not vulnerability-management mandates. SPD-5 and NIST IR 8270 / IR 8401 remain voluntary, consistent with your framing.
5. For the report, suggested wording: "no general federal mandate; obligations arise only through licensing conditions (FCC, NOAA) that address access control and encryption, and through DoD contract flow-downs that address CUI-handling systems." I recommend avoiding any claim that operators are "required to patch" or "required to manage vulnerabilities".
