# Research Thread 4 — US Regulation Primary Texts

**Agent:** general-purpose subagent | **Run:** 2026-09-29 | **Items covered:** 2, 15/22, 19, 20, 21, 23, 24, 25 (per `research/Research_Plan.md`)

## Prompt given

> You are researching for a fictitious-company business assignment requiring a Governance/Compliance section under US jurisdiction (satellite-fleet vulnerability-prioritisation AI platform, B2B/B2G). Use WebSearch/WebFetch and prefer PRIMARY sources (the actual government/standards documents), not secondary summaries.
>
> Research items 2, 15, 19, 20, 21, 22, 23, 24, 25 from the project's research/Research_Plan.md:
>
> 2. Confirm primary-source content: does EU NIS2 list space as a critical sector? What does the proposed EU Space Act say about cybersecurity rules (status as of now)? What does US Space Policy Directive-5 (SPD-5) actually say? (Note: this is background for "why is the sector ripe now" even though the jurisdiction chosen is US — EU NIS2 is comparative context only.)
> 15/22. ITAR (22 CFR 120-130) and EAR (Category 9, spacecraft) — find the actual primary-source scope: does it genuinely restrict sharing spacecraft technical data / satellite telemetry with foreign persons? Pull the specific regulatory citation.
> 19. NIST AI Risk Management Framework (AI RMF 1.0) — pull the four core functions (Govern, Map, Measure, Manage) with their actual sub-definitions from the primary NIST document, so they can be mapped to: human-in-the-loop uplink approval, escalation/stop rules, hallucination/reliability safeguards, monitoring/audits.
> 20. NIST IR 8270 (Introduction to Cybersecurity for Commercial Satellite Operations) and NIST IR 8401 (ground segment) — pull 2-3 specific control items or recommendations from each that are directly relevant to vulnerability/patch management, not just cite the document title.
> 21. SPD-5 — pull the actual cybersecurity principles it states (primary text, e.g. via federalregister.gov or the National Space Council archive), not just a news summary.
> 23. CCPA/CPRA — does it plausibly apply to subscriber-terminal location/identity data collected in a satellite communications context? Pull the statutory definition of "personal information" and check the fit.
> 24. For escalation thresholds and audit-trail standards, find one analogous standard (e.g. SOC 2 audit logging requirements, or NIST SP 800-53 audit control family) that could inform a concrete design.
> 25. As a fallback/comparison only: briefly confirm what India's DPDP Act 2023, IN-SPACe authorisation regime, and CERT-In's 6-hour incident reporting rule actually require (primary sources: meity.gov.in, cert-in.org.in, in-space.gov.in).
>
> Return a clean markdown section, one subsection per item, each with: the actual primary-source finding (quote or precise paraphrase) and the source URL. Flag anything you could only find secondary-source confirmation for. Do not write files — return markdown in your final message.

## Approach followed

Attempted direct fetch of each primary government/standards document (eCFR, Federal Register, NIST CSRC PDFs, cve.org-equivalent statutory sites, meity.gov.in, in-space.gov.in, cert-in.org.in) before falling back to any secondary source. Several PDFs (NIST IR 8270/8401, SPD-5's Federal Register PDF, CERT-In's directive PDF) would not render as clean text through the fetch tool — in those cases the agent used NIST's own HTML resource-center mirror or an archived White House memorandum page where available, and explicitly flagged every instance where only secondary-source confirmation was possible, rather than presenting a paraphrase as a verbatim primary quote.

## Sources visited

- https://eur-lex.europa.eu/eli/dir/2022/2555/oj/eng
- https://technical-barriers-trade.ec.europa.eu/en/notification/text/EU1214_EN_DRAFTTEXT1_abfaf4957f3929ce88ba3565d2d7f76f.pdf
- https://defence-industry-space.ec.europa.eu/eu-space-act_en
- https://www.ecfr.gov/current/title-22/chapter-I/subchapter-M/part-120/subpart-C/section-120.33
- https://www.ecfr.gov/current/title-22/chapter-I/subchapter-M/part-120/subpart-C/section-120.63
- https://www.federalregister.gov/documents/2013/05/24/2013-11986/export-administration-regulations-ear-control-of-spacecraft-systems-and-related-items-the-president
- https://www.federalregister.gov/documents/2017/01/10/2016-31755/revisions-to-the-export-administration-regulations-ear-control-of-spacecraft-systems-and-related
- https://www.federalregister.gov/documents/2024/10/23/2024-23932/export-administration-regulations-removal-of-license-requirements-for-certain-spacecraft-and-related
- https://airc.nist.gov/airmf-resources/airmf/5-sec-core/
- https://doi.org/10.6028/NIST.AI.100-1
- https://nvlpubs.nist.gov/nistpubs/ir/2023/NIST.IR.8270.pdf
- https://www.nist.gov/news-events/news/2023/07/introduction-cybersecurity-commercial-satellite-operations-nist-ir-8270
- https://industrialcyber.co/nist/new-nist-ir-8270-document-addresses-cybersecurity-risk-management-for-commercial-satellite-space/
- https://nvlpubs.nist.gov/nistpubs/ir/2022/NIST.IR.8401.pdf
- https://www.federalregister.gov/documents/2020/09/10/2020-20150/cybersecurity-space-systems-principles-space-policy-directive-5-of-september-4-2020
- https://irp.fas.org/offdocs/nspm/spd-5-fs.pdf
- https://trumpwhitehouse.archives.gov/presidential-actions/memorandum-space-policy-directive-5-cybersecurity-principles-space-systems
- https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1798.140
- https://csf.tools/reference/nist-sp-800-53/r5/au/
- https://www.meity.gov.in/static/uploads/2024/06/2bf1f0e9f04e6fb4f8fef35e82c42aa5.pdf
- https://www.inspace.gov.in/sys_attachment.do?sys_id=5d532e37877102503b0f0d060cbb35cf
- https://www.lexology.com/library/detail.aspx?g=5eae7307-664d-484e-8a58-f50bc24bb4d2
- https://trilegal.com/news-insights/how-to-comply-with-cert-ins-new-six-hour-time-frame-to-report-cyber-incidents/

## Full output

# Governance/Compliance Research — Primary-Source Findings

## Item 2 — NIS2 (space as critical sector), EU Space Act status, SPD-5 (background/comparative)

**NIS2 (Directive (EU) 2022/2555):** Annex I ("Sectors of high criticality") lists 11 sectors, and **space is included as sector 11** (alongside energy, transport, banking, financial market infrastructure, health, drinking water, wastewater, digital infrastructure, ICT service management B2B, and public administration). Coverage specifically reaches operators of ground-based infrastructure that supports the provision of space-based services (not the space segment itself, which is largely carved out under Art. 2(8) where covered by sector-specific EU law).
Source (primary): [Directive (EU) 2022/2555, EUR-Lex](https://eur-lex.europa.eu/eli/dir/2022/2555/oj/eng) — I confirmed the sector-list content via secondary summaries cross-checked against the EUR-Lex link; I was not able to pull the verbatim Annex I text in this session, so **flag: sector inclusion is secondary-confirmed, not verbatim-quoted**.

**EU Space Act (proposed):** Commission proposal **COM(2025) 335 final**, presented 25 June 2025 — "Regulation of the European Parliament and of the Council on the safety, resilience and sustainability of space activities in the Union." Dedicates **Articles 75–95 to cybersecurity and operational resilience**, including Article 88's mandatory threat-led penetration testing regime (pre-launch and at least every 3 years thereafter) and provisions establishing minimum standards for encryption, incident detection, and supply-chain security. It is designed as *lex specialis* relative to NIS2 for space operators that qualify as essential/important entities (avoiding duplicative requirements). **Status as of Sept 2026:** still in the legislative process — Parliament rapporteur draft and a Council Presidency compromise text (March 2026) show material divergence on cybersecurity requirements, market access, and third-country operator treatment; Commission did not envisage entry into force before 2030.
Source (primary): [COM(2025) 335 final full text PDF](https://technical-barriers-trade.ec.europa.eu/en/notification/text/EU1214_EN_DRAFTTEXT1_abfaf4957f3929ce88ba3565d2d7f76f.pdf); [EC Defence Industry & Space page](https://defence-industry-space.ec.europa.eu/eu-space-act_en). Status/timeline details are **secondary-sourced** (Hogan Lovells, Hannes Snellman, White & Case trackers) — I did not verify the March 2026 Council compromise text directly.

**SPD-5:** see Item 21 below (same content, cited there in full).

---

## Item 15/22 — ITAR (22 CFR 120–130) and EAR Category 9

**ITAR scope — does it restrict sharing spacecraft technical data with foreign persons? Yes.**

- **22 CFR 120.33** ("Technical data") — primary regulatory text: technical data means information "required for the design, development, production, manufacture, assembly, operation, repair, testing, maintenance, or modification of defense articles," including blueprints, drawings, photographs, plans, instructions or documentation, classified information relating to USML/600-series items, information covered by an invention secrecy order, and certain related software. Excludes general scientific/mathematical/engineering principles taught in schools.
Source: [eCFR 22 CFR 120.33](https://www.ecfr.gov/current/title-22/chapter-I/subchapter-M/part-120/subpart-C/section-120.33)

- **22 CFR 120.16** ("Foreign person") — a foreign person is "any natural person who is not a lawful permanent resident as defined by 8 U.S.C. 1101(a)(20) or who is not a protected individual as defined by 8 U.S.C. 1324b(a)(3)," and includes any foreign corporation, business association, partnership, trust, society, or entity not incorporated/organized to do business in the US, plus foreign governments and their agencies.
Source: [eCFR 22 CFR 120.16 / 120.63](https://www.ecfr.gov/current/title-22/chapter-I/subchapter-M/part-120/subpart-C/section-120.63)

- **Deemed export rule**: any release of technical data to a foreign person **inside the United States** is legally deemed to be an export to every country of which that person is a citizen/permanent resident — i.e., sharing spacecraft telemetry/technical data with a non-US-person employee or partner, even domestically, can trigger ITAR licensing obligations. (Secondary-confirmed summary of 22 CFR 120.50/126 "deemed export" doctrine; I did not pull the exact current CFR export-definition subsection text.)

**EAR Category 9 (dual-use, spacecraft):** Following the Export Control Reform Initiative, most commercial communications/remote-sensing satellites, planetary rovers/probes, and in-space habitats were moved off the USML into **ECCN 9A515** (Commerce Control List, Category 9) — the "500-series" ECCNs (9A515/9B515/9D515/9E515). ECCN 9A515.a explicitly covers "commercial communications satellites, remote sensing satellites, planetary rovers, planetary and interplanetary probes, and in-space habitats" not separately controlled under 9A004 or USML Category XV(a). Recent Federal Register rules (Oct 2024) removed license requirements for AUS/CAN/UK for items under 9A515.a.1–.4/.g and 9E515.f — meaning EAR **still requires a license for exports to most other foreign destinations/persons**, confirming that satellite telemetry/technical data sharing is genuinely restricted, just under the lighter dual-use regime rather than ITAR for these reclassified items.
Sources (primary, Federal Register): [2013 EAR spacecraft control rule](https://www.federalregister.gov/documents/2013/05/24/2013-11986/export-administration-regulations-ear-control-of-spacecraft-systems-and-related-items-the-president); [2017 revisions](https://www.federalregister.gov/documents/2017/01/10/2016-31755/revisions-to-the-export-administration-regulations-ear-control-of-spacecraft-systems-and-related); [2024 AUS/CAN/UK removal rule](https://www.federalregister.gov/documents/2024/10/23/2024-23932/export-administration-regulations-removal-of-license-requirements-for-certain-spacecraft-and-related).

**Bottom line for the report:** ITAR/EAR do genuinely and specifically restrict transferring spacecraft technical data and (by extension) operational telemetry to foreign persons — this is directly relevant to a B2G/B2B satellite-vulnerability platform that would need to gate foreign-national employee/contractor access to customer telemetry and vulnerability data.

---

## Item 19 — NIST AI RMF 1.0 (AI 100-1) — Four Core Functions

Primary source: NIST AI 100-1, *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*, https://doi.org/10.6028/NIST.AI.100-1 (official companion resource site: [airc.nist.gov](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/)). I could not get clean text out of the raw NIST PDF (binary/encoding issues in the fetch), so the function-level definitions below are pulled from NIST's own official AI RMF resource center (airc.nist.gov, a NIST-run site mirroring the framework), which I treat as primary; **flag: verbatim PDF quoting was not possible this session, so exact paragraph wording should be double-checked against the PDF before final citation.**

- **GOVERN** — "cultivates and implements a culture of risk management" across the organization; cross-cutting, spans the whole AI lifecycle. Categories include: Govern 1 (policies/processes for map/measure/manage are established), Govern 2 (accountability structures, clear roles/responsibilities), Govern 4 (organizational culture prioritizes critical thinking/safety-first mindset), Govern 6 (policies address third-party/supply-chain AI risk).
  → **Maps to:** human-in-the-loop uplink approval (accountability structures / clear roles, Govern 2), escalation/stop-rule policy (Govern 1/4).

- **MAP** — "establishes the context to frame risks related to an AI system," identifying purpose, deployment setting, and risk tolerances; enables "negative risk prevention." Categories include: Map 1 (context established), Map 2 (system categorized by task/method/knowledge limits), Map 4 (risks/benefits mapped across all components incl. third-party).
  → **Maps to:** defining scope/context for what the AI is and isn't authorized to do (e.g., recommend vs. execute uplink commands).

- **MEASURE** — "employs quantitative, qualitative, or mixed-method tools... to analyze, assess, benchmark, and monitor AI risk," feeding Manage. Categories include: Measure 1 (methods/metrics selected), Measure 2 (evaluated for trustworthy characteristics), Measure 3 (mechanisms track risks over time incl. emergent risks), Measure 4 (feedback on measurement efficacy).
  → **Maps to:** hallucination/reliability safeguards and ongoing monitoring/audits — this is the direct home for reliability metrics and drift/degradation tracking.

- **MANAGE** — "entails allocating risk resources to mapped and measured risks on a regular basis," and developing response plans to decrease likelihood of failures/negative impacts. Categories include: Manage 1 (risks prioritized/responded to based on assessment), Manage 3 (third-party risk managed/monitored), Manage 4 (risk treatment, response, recovery, communication plans documented and monitored).
  → **Maps to:** escalation/stop rules and incident response workflow (Manage 1/4).

Source: [NIST AI RMF Core, airc.nist.gov](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/); [NIST AI 100-1 DOI landing page](https://doi.org/10.6028/NIST.AI.100-1).

---

## Item 20 — NIST IR 8270 and NIST IR 8401 (control items relevant to vulnerability/patch management)

**Flag up front: I could not extract clean text from either PDF directly (both returned as corrupted/binary through the fetch tool). The items below are secondary-sourced (industry summaries, NIST news pages, and a third-party technical breakdown), cross-referenced against the NIST CSF subcategory codes each document is known to use. Recommend independently opening the PDFs to pull exact quoted language before final report submission.**

**NIST IR 8270** — *Introduction to Cybersecurity for Commercial Satellite Operations* (2023), applies NIST CSF to commercial space. Relevant items:
1. Vulnerability management: "A vulnerability management plan is developed and implemented" (maps to CSF PR.IP-12 / CSF 2.0 ID.RA-01 "asset vulnerabilities are identified, validated, and recorded") — IR 8270 frames the first task as identifying and documenting asset vulnerabilities as part of an organizational cybersecurity program.
2. Patchability as a design consideration: the report specifically flags that satellite software "can often be patched or modified from the ground" and treats ground-updatability as a key cybersecurity design/operations consideration (distinct from hardware, which cannot be serviced post-launch).
3. Supply chain / threat intel: recommends organizations understand suppliers' security/privacy policies and engage ISACs for shared threat intelligence relevant to emerging vulnerabilities.
Source: [NIST IR 8270 final PDF](https://nvlpubs.nist.gov/nistpubs/ir/2023/NIST.IR.8270.pdf) (title/existence primary; content above is secondary-sourced via [NIST news release](https://www.nist.gov/news-events/news/2023/07/introduction-cybersecurity-commercial-satellite-operations-nist-ir-8270), [Industrial Cyber summary](https://industrialcyber.co/nist/new-nist-ir-8270-document-addresses-cybersecurity-risk-management-for-commercial-satellite-space/)).

**NIST IR 8401** — *Satellite Ground Segment: Applying the Cybersecurity Framework to Assure Satellite Command and Control* (2022), structured around CSF's five functions (Identify/Protect/Detect/Respond/Recover), 23 categories, 108 subcategories, explicitly built to "address the goals of SPD-5." Relevant items:
1. Access control (PR.AC): access to physical/logical ground-segment assets (antenna fields, operation centers) "limited to authorized users, processes, and devices," with encryption/authentication required for command-and-control data in transit.
2. Environment separation (PR.DS): development/testing environments kept separate from production systems, to prevent untested software/patches reaching operational satellite command-and-control systems — directly relevant to patch-management gating before uplink.
3. Continuous monitoring (DE.CM) and supply-chain risk management: ongoing surveillance for ground-segment anomalies, plus supplier/third-party audits to prevent vulnerabilities entering via the supply chain.
Source: [NIST IR 8401 final PDF](https://nvlpubs.nist.gov/nistpubs/ir/2022/NIST.IR.8401.pdf) (title/structure primary; specific control content secondary-sourced via a third-party technical breakdown — **weakest sourcing in this report, verify directly**).

---

## Item 21 — SPD-5 cybersecurity principles (primary text)

Space Policy Directive-5, signed 4 Sept 2020, "the Nation's first comprehensive cybersecurity policy for space systems." Section 4 lays out the operative principles. Per the memorandum text:

- Space systems and supporting infrastructure should be developed using "risk-based, cybersecurity-informed engineering," with cybersecurity integrated into design **before launch**, since most satellites cannot be physically serviced once on orbit.
- Owners/operators should protect against unauthorized access by "physical means or electronic spoofing," and should use "authentication or encryption measures designed to remain secure against existing and anticipated threats" for command-and-control links.
- Reduce vulnerabilities in space vehicles' receiver systems, including protection against jamming and spoofing.
- Ground systems should adopt NIST Cybersecurity Framework practices — patching, network segregation, antivirus/malware protection, and insider-threat training.
- Supply-chain risk management: tracking of products and services, verification of suppliers, and detection of counterfeit/tampered components.
- Information sharing: collaboration through Information Sharing and Analysis Centers (ISACs) for threat intelligence.
- Applies broadly to "space systems," defined to include ground systems, sensor networks, and space vehicles that provide space-based services — covering both government and commercial systems.

Source (primary): [Federal Register, "Cybersecurity Principles for Space Systems" (SPD-5), 85 FR 56155, Sept. 10, 2020](https://www.federalregister.gov/documents/2020/09/10/2020-20150/cybersecurity-space-systems-principles-space-policy-directive-5-of-september-4-2020); [full-text PDF](https://irp.fas.org/offdocs/nspm/spd-5-fs.pdf); [official White House memorandum archive](https://trumpwhitehouse.archives.gov/presidential-actions/memorandum-space-policy-directive-5-cybersecurity-principles-space-systems). **Note:** the bullet list above is a close paraphrase reconstructed from the archived White House memorandum page (fetched successfully) rather than a verbatim block quote from the Federal Register PDF (which the fetch tool could not render as text) — recommend a direct verbatim pull of Section 4 before final citation in the report.

---

## Item 23 — CCPA/CPRA: does it plausibly cover subscriber-terminal location/identity data?

**Yes — strong fit.** Cal. Civ. Code § 1798.140(v) defines "personal information" as: "information that identifies, relates to, describes, is reasonably capable of being associated with, or could reasonably be linked, directly or indirectly, with a particular consumer or household." Enumerated categories include:
- Identifiers: "real name, alias, postal address, unique personal identifier, online identifier, Internet Protocol address, email address, account name..."
- "Precise geolocation" — separately defined as location data accurate to within a **1,850-foot radius** (a "sensitive personal information" sub-category with extra rights under CPRA).
- Device data capable of connecting to the internet directly or indirectly.
- Commercial/behavioral records and inferences drawn about a consumer.

A satellite communications subscriber terminal that reports its location, account identity, and usage/telemetry data to the platform is very plausibly "personal information" (and the location data plausibly "sensitive personal information" if precision is within the statutory radius), assuming subscribers include California consumers/households (as opposed to purely B2G/military terminals, which may fall outside CCPA's "consumer" scope). Deidentified, aggregated, and publicly available data are excluded.
Source (primary): [Cal. Civ. Code § 1798.140, California Legislative Information](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1798.140).

---

## Item 24 — Escalation thresholds / audit-trail standard analogue

**NIST SP 800-53 Rev. 5, Audit and Accountability (AU) family** is the most directly usable analogue:
- **AU-2 (Event Logging):** organization decides which event types must be logged and why (the design-time policy question — e.g., every uplink command, every AI-recommended escalation, every human override).
- **AU-3 (Content of Audit Records):** records must capture event type, timestamp, location, source, outcome, and identity of the user/subject associated with the event — a ready-made schema for an audit-trail log entry.
- **AU-6 (Audit Record Review, Analysis, and Reporting):** requires periodic review of audit records; organization-defined frequency, though common baselines (e.g., FedRAMP Moderate/High) require **at least weekly** review, with higher-risk sources (privileged accounts, remote access) reviewed daily or near-real-time — a defensible basis for setting the platform's escalation/review cadence.
Source: [NIST SP 800-53 Rev. 5, AU family, CSF Tools mirror of NIST content](https://csf.tools/reference/nist-sp-800-53/r5/au/) — **secondary mirror of primary control text; NIST's own SP 800-53 PDF (csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) is the primary source and should be cited directly in the final report rather than csf.tools.**

**SOC 2 (Trust Services Criteria, AICPA) analogue:** Criterion **CC7.2** (system monitoring — real-time detection of anomalies/security events) and **CC7.3** (evaluation of detected events — requires a defined alert threshold, e.g., a named quantitative trigger, a named owner responsible for review, and a retained record that review occurred). Typical minimum log retention cited in practice: 12 months, often 15 months for Type II audit window coverage.
Source: secondary (industry compliance summaries); **primary source is the AICPA Trust Services Criteria document itself (not freely hosted in full text) — flag as not independently verified against AICPA's primary text this session.**

---

## Item 25 — India fallback/comparison (DPDP Act 2023, IN-SPACe, CERT-In)

**Digital Personal Data Protection Act, 2023 (Act No. 22 of 2023):**
- Section 2(t): "Personal Data" means "any data about an individual who is identifiable by or in relation to such data."
- Section 2(j): "Data Fiduciary" = person who alone or with others determines the purpose and means of processing personal data.
- Section 2(k): "Data Principal" = the individual to whom the personal data relates.
- Processing personal data requires the Data Principal's consent for a lawful purpose, subject to enumerated "legitimate uses" exemptions (Section 7) such as voluntary provision of data or State functions (benefits, licenses, permits).
Source (primary): [Digital Personal Data Protection Act, 2023 — full PDF, meity.gov.in](https://www.meity.gov.in/static/uploads/2024/06/2bf1f0e9f04e6fb4f8fef35e82c42aa5.pdf).

**IN-SPACe authorisation regime:** Under the "Norms, Guidelines and Procedures for Implementation of Indian Space Policy-2023 in respect of Authorization of Space Activities" (NGP), **any entity undertaking space activities within or from Indian territory must obtain authorization from IN-SPACe**; only Indian entities (govt or non-govt) are directly eligible — non-Indian entities must apply through an Indian subsidiary, joint venture, or other recognized collaboration. Requirements include registering space objects in India's national registry, debris-mitigation compliance, and mandatory third-party liability insurance.
Source (primary): [IN-SPACe NGP document, in-space.gov.in](https://www.inspace.gov.in/sys_attachment.do?sys_id=5d532e37877102503b0f0d060cbb35cf).

**CERT-In 6-hour reporting rule:** Issued 28 April 2022 under **Section 70B(6) of the Information Technology Act, 2000** ("Cyber Security Directions"), effective 27 June 2022 (MSME compliance extended to 25 Sept 2022). Requires "service providers, intermediaries, data centres, body corporates and Government organisations" to **mandatorily report cyber incidents to CERT-In within 6 hours of noticing the incident or being notified of it**; if full details aren't yet available, partial information may be submitted within the 6-hour window with supplementary details provided later.
Source (primary PDF exists at cert-in.org.in but returned corrupted/unreadable in this session's fetch — **flag: confirmed only via secondary legal-analysis sources** ([Lexology](https://www.lexology.com/library/detail.aspx?g=5eae7307-664d-484e-8a58-f50bc24bb4d2), [Trilegal](https://trilegal.com/news-insights/how-to-comply-with-cert-ins-new-six-hour-time-frame-to-report-cyber-incidents/)); recommend re-attempting a direct fetch of the CERT-In direction PDF, or citing the Gazette notification, before final submission.

---

## Summary of sourcing-confidence flags (things to independently re-verify before the report is finalized)
1. **NIS2 Annex I** — sector list is well-corroborated across many secondary sources but I did not pull verbatim Annex I text from EUR-Lex.
2. **EU Space Act status/timeline** (March 2026 Council compromise) — secondary-sourced only.
3. **NIST AI RMF 1.0** — function definitions pulled from NIST's own airc.nist.gov resource site (primary), but I could not get verbatim text out of the official AI 100-1 PDF itself.
4. **NIST IR 8270 / IR 8401 control content** — weakest sourcing in this batch; PDFs would not render as text through the fetch tool, so specific control bullets are secondary-sourced against known CSF subcategory codes. Titles, authors, publication dates, and structural scope (5 functions / 23 categories / 108 subcategories for IR 8401) are confirmed primary/NIST-stated facts.
5. **ITAR "deemed export" mechanics** — secondary-confirmed summary of the doctrine; the core definitions (120.33, 120.16) are directly cited from eCFR.
6. **SOC 2 Trust Services Criteria** — AICPA's own primary document was not accessed; summarized via compliance-industry secondary sources.
7. **CERT-In 6-hour direction** — PDF fetch failed; confirmed via secondary Indian legal-analysis sources (Lexology, Trilegal), not cert-in.org.in directly.
