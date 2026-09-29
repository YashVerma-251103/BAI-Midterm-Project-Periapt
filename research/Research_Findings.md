# Research Findings

Compiled from 5 parallel research threads run 2026-09-29 against `research/Research_Plan.md`, plus a 6th follow-up thread (item 30). Organized by rubric marker (`brief/Instructions.md` §A). Each finding is tagged **[primary]**/**[secondary]** for source type and, where the researching agent flagged it, a confidence note. Gaps are stated explicitly, never guessed.

---

## A.0 Company Overview

**Item 1 — Satellite count & market growth [primary: SIA report]**
**14,266 operational satellites** in orbit end of 2025 (SIA 29th Annual State of the Satellite Industry Report). 296 commercial launches deployed 4,434 satellites in 2025 — 65% more than 2024. Global space economy $429B (+3%); commercial satellite industry $303B (+4% YoY). Satellite broadband subscribers +62% to >10M.
→ **Correction:** supersedes the "~16,000–17,000 satellites" figure used in `topic/Topic_Brainstorm_Report.md` §13 — use 14,266 (SIA, end-2025) going forward.
No clean LEO CAGR published by SIA itself; third-party market-research aggregators show 11.9%–24.7% CAGR estimates (2025–2030/2034) — wide variance, cite as directional only if used.
Source: [SIA 29th Annual Report](https://sia.org/affordability-productivity-drive-historic-satellite-industry-growth-satellite-industry-association-releases-29th-annual-state-of-the-satellite-industry-report/)

**Item 2 — Regulatory pressure trend [secondary-confirmed]**
NIS2 (Directive (EU) 2022/2555) Annex I lists **space as sector 11** of 11 high-criticality sectors — covers ground infrastructure supporting space services, not the space segment itself (carved out under Art. 2(8)). The proposed **EU Space Act** (COM(2025) 335 final, 25 June 2025) dedicates Articles 75–95 to cybersecurity/operational resilience, including mandatory threat-led penetration testing (Art. 88, pre-launch + every 3 years). Still mid-legislative-process as of Sept 2026; Commission does not expect entry into force before 2030. Useful as comparative "regulatory direction of travel" context even though US is the chosen jurisdiction.
Sources: [Directive (EU) 2022/2555](https://eur-lex.europa.eu/eli/dir/2022/2555/oj/eng) · [COM(2025) 335 final](https://technical-barriers-trade.ec.europa.eu/en/notification/text/EU1214_EN_DRAFTTEXT1_abfaf4957f3929ce88ba3565d2d7f76f.pdf)

**Item 3 — Company name/mission/vision:** out of scope for research — creative decision, still open.

---

## A.1 Agentic AI & Value Proposition

**Item 4 — Cost of a patch-related failure [primary: Viasat 10-K]**
**No dollar figure exists for the Viasat KA-SAT (Feb 2022) attack.** Viasat's own 10-K states the incident had **no material impact** on financials — this is Viasat's actual disclosed position, not an omission. Do not assert a specific KA-SAT recovery cost. Usable instead: the attack disabled remote monitoring on ~5,800 Enercon wind turbines (11GW) for weeks, and ~30,000 modems were replaced — scale-of-disruption evidence, not cost evidence.
Smallsat replacement cost range (secondary, industry figures): commercial 3U CubeSats ~$500K build + $200–250K launch; GEO satellites ~$300M for contrast. Usable range for "what a bricked satellite is worth": **~$0.5–1M+ per constellation-class smallsat**.
Sources: [Viasat KA-SAT overview](https://www.viasat.com/perspectives/corporate/2022/ka-sat-network-cyber-attack-overview/) · [Viasat 10-K, SEC EDGAR](https://www.sec.gov/Archives/edgar/data/797721/000095017022010881/vsat-20220331.htm) · [NanoAvionics cost breakdown](https://nanoavionics.com/blog/how-much-do-cubesats-and-smallsats-cost/)

**Item 5 — Consulting/analyst cost baseline [secondary, gap: no space-sector premium found]**
No space-sector-specific rate found despite targeted search. General cybersecurity consultant baseline: US salary avg $115K–$159K/yr; US contractor avg $143/hr; UK day rate median £675/day. **State explicitly as a general-industry extrapolation, not a space-sector-sourced number.**
Sources: [Indeed](https://www.indeed.com/career/cybersecurity-consultant/salaries) · [contractrates.fyi](https://www.contractrates.fyi/CyberSecurity-Consultant/hourly-rates)

**Item 6 — Operational pipeline analogue [primary: NIST IR 8270 crosswalk + ESA OBSM]**
The claimed 8-step loop (ingest→map→score→validate→schedule→uplink→monitor→rollback) is a **real but composite synthesis**, not one documented process. NIST IR 8270 crosswalks CSF subcategories `ID.RA-1`/`ID.RA-2`/`PR.IP-12` to SP 800-53 controls (RA-3, RA-5, SI-2 "Flaw Remediation") covering ingest/map/score/patch. ESA's On-Board Software Maintenance (OBSM) concept — real, used on Cluster and GOCE missions — covers validate (dual-facility: SdeVF emulator + SimVF full-spacecraft simulator) → delta-patch generation → uplink → continuous configuration-state tracking.
**Honest gap: no documented automated rollback step anywhere in these sources** — real practice relies on configuration tracking (so a prior state *could* be reconstructed) and human judgment, not automated rollback. State this as an acknowledged limitation, not a solved problem.
Sources: [NIST IR 8270 PDF](https://nvlpubs.nist.gov/nistpubs/ir/2023/NIST.IR.8270.pdf) · [ESA Bulletin 91 — Cluster OBSM](https://www.esa.int/esapub/bulletin/bullet91/b91deni.htm) · [GOCE OBSM (ResearchGate)](https://www.researchgate.net/publication/258389277_On-Board_Software_Maintenance_for_GOCE_ESA's_Gravity_Mission)

---

## A.2 Moat & Defensibility

**Item 7 — Public data sufficiency for JEPA cold-start [primary: dataset papers]**
**Verdict: public data de-risks the architecture choice; it does not remove the need for design-partner data.** ESA-ADB: ~17.5 years telemetry, 3 ESA missions, 844 annotated events. OPS-SAT-AD: 2,123 short univariate fragments, 9 channels, 1 CubeSat. Both small/narrow vs. what JEPA-style world models are typically trained on — V-JEPA 2 used >1M hours of video; even its narrow fine-tuning stage needed 62 hours of unlabeled data. **Correction (2026-09-29): this is a feasibility argument, not a moat argument.** Public data proving the architecture works proves it for *any* competitor too — it lowers *our* technical risk, not copyability. Access to customer data is also not a moat on its own, since a rival can sign the same operators. The moat has to come from what the data access *compounds into*, ranked weakest → strongest:
1. *First-mover design partners* — few mid-size operators exist (item 11); a timing lead only, operators can dual-source.
2. *Access barriers* — ITAR/EAR deemed-export and clearances (items 15/22) block foreign/fast entrants, but **not** incumbents (Aerospace Corp, Booz Allen, primes) who already hold access.
3. *Compounding assets (the only durable one)* — federated cross-fleet model improving with each operator without raw data leaving (item 8); a proprietary labelled record of patch-rollout outcomes nobody else can buy; approval-workflow/audit-trail switching costs (item 24).
Chain for the report: public data → architecture de-risked → design partners → federated cross-fleet model + outcome data → moat that grows per customer. **State honestly that the moat is thin at cold start and strengthens with scale.**
Sources: [ESA-ADB (arXiv)](https://arxiv.org/abs/2406.17826) · [OPS-SAT-AD (Nature Sci Data)](https://www.nature.com/articles/s41597-025-05035-3) · [V-JEPA 2 (arXiv)](https://arxiv.org/abs/2506.09985)

**Item 8 — Federated learning under heterogeneous fleets [general ML literature, applied by analogy]**
Confirmed: naive FedAvg suffers "client drift" under non-IID data (Li et al.). Standard fixes: **FedProx** (proximal term, handles both statistical and systems heterogeneity — directly relevant to fleets with different compute/comms budgets), **personalization layers/adapters** (shared backbone + per-platform heads), **clustered FL** (higher comms cost). None of this is satellite-specific — state as "known techniques, applied," not invented in-house.
Sources: [FedProx (arXiv)](https://arxiv.org/pdf/1812.06127) · [Clustered FL survey](https://link.springer.com/article/10.1007/s11042-026-21541-x)

**Item 9 — DP/secure aggregation overhead [general ML literature]**
**Practical at "dozens of clients" scale, not research-stage.** Modern DP-SGD implementations (Opacus, JAX vmap): ~1.5–3x compute overhead (down from historical 10–100x). Secure aggregation (Bonawitz et al., the foundational protocol): ~1.7–2x comms expansion even at 1,000–16,000 clients — smaller expected at dozens. **Real open risk is DP's privacy-utility trade-off** (accuracy loss on small/heterogeneous per-operator datasets — exactly this project's regime), a modeling risk, not an infrastructure-cost risk. State both honestly.
Sources: [Bonawitz et al., Practical Secure Aggregation (ACM CCS 2017)](https://dl.acm.org/doi/10.1145/3133956.3133982) · [How to DP-fy ML](https://arxiv.org/pdf/2303.00654)

**Item 10/13 — Competitor "whole loop" refresh [mixed primary/secondary]**
No public competitor automates the full loop (orbit-aware prioritization → patch scheduling → twin validation → fleet rollout) as one AI platform. **Two must be named explicitly in the report, not omitted:**
- **Aerospace Corp SPARTA** — published countermeasure-prioritization scoring methodology (Feasibility × Cost / Efficacy), DHS-backed, with an autonomous on-orbit extension (SPARTEND). Closest public overlap. Differentiator: static reference framework, not a live per-operator AI platform with twin validation + auto-rollout.
- **CT Cubed (IRON GALAXY + Terrain Trace)** — commercial cyber-range + AI risk assessment. Differentiator: training/exercise-positioned, not an operational remediation pipeline.
Also confirmed adjacent/partial, lower risk: Deloitte Silent Shield (detection only), Booz Allen Reflect Secure (twin validation, consulting-delivered), AMI/Nucleus Security (generic, no orbit awareness), Xage/SpiderOak/Kratos (access control/comms/infra, not prioritization).
Checked, no overlap: Slingshot Aerospace, Voyager Technologies, Kayhan Space, Space ISAC (intel-sharing, potential data partner not competitor). Axiom Space builds vulnerability management **internally** for its own orbital data centers (not sold to others).
**Note: SBIR/STTR statutory authority lapsed 30 Sept 2025, not renewed in FY2026 NDAA** — the "manufacturers/government funding channel" argument needs updating; SpaceWERX/AFWERX awards are currently on hold.
Sources: [SPARTA countermeasures guide](https://newspaceeconomy.ca/2026/04/11/sparta-countermeasures-the-complete-guide-to-defending-spacecraft-from-cyber-and-counterspace-threats/) · [CT Cubed](https://ctcubed.com/) · [SBIR standoff (SpaceNews)](https://spacenews.com/congresss-sbir-standoff-is-slowing-space-force-innovation-it-must-act-now/)

**Moat/defensibility bottom line:** pooled patch-outcome data (as already concluded in `topic/Topic_Brainstorm_Report.md` §7.5) remains the right moat story; items 7–9 above make the *technical* feasibility of building it honest and defensible rather than asserted.

---

## A.3 Porter's Five Forces

**Item 11 — Buyer concentration / mid-size operators named [secondary: web trackers]**
Named mid-size operators (50–300 range): **Planet Labs** (~200+), **Spire Global** (~100+), **Iridium** (~75), **SES**/**Intelsat** (~50 each), **ICEYE** (borderline, ~52–72). Below range: Globalstar (~24), BlackSky (~18). Confirmed out-of-range (mega, not target): Starlink (~9,900+, ~53% of all payloads), OneWeb/Eutelsat (648, targeting 1,300 by 2030).
Source: [Orbital Radar — satellites by operator](https://orbitalradar.com/satellites-by-operator)

**Item 12 — Supplier power [mixed primary/secondary — full detail already relayed]**
**Verdict: low-to-moderate, trending moderate.** Manufacturer market fragmented today (Spire, Airbus, Thales Alenia, York, Blue Canyon, Terran Orbital) but consolidating under primes (Lockheed acquired Terran Orbital Oct 2024; RTX owns Blue Canyon; Boeing owns Millennium) — flag as forward-looking upward pressure. Ground-station market fragmented and actively de-fragmenting via aggregator/reseller models (Atlas resells AWS Ground Station with "zero software changes") — evidence *against* high switching costs, except KSAT's Svalbard polar site is a narrow pocket of leverage for polar-heavy operators. **Confirmed gap: no evidence any bus manufacturer resells third-party security tooling** — the "manufacturers as resale channel" idea should rest on the ground-station reseller precedent (Atlas–AWS), not an unfound manufacturer precedent.
Only concrete manufacturer SBOM evidence: **Thales Alenia Space uses Black Duck SCA** to generate/maintain SBOMs (customer of the tool, not a reseller).

**Item 14 — Substitutes evidence [primary: WEF/CISA/White House reports + SpaceX case]**
"Doing nothing"/risk acceptance is **documented industry behavior** for legacy spacecraft (WEF, CISA). White House Jan 2025 report (300 participants, 125 companies): "holistic space cybersecurity practices are underdeveloped across the industry." **SpaceX built its own OTA fleet-update system in-house** for 4M+ Starlink terminals (canary + phased rollout + auto-rollback, zero satellites lost across 200+ updates) — strong real evidence a well-capitalized operator builds rather than buys. **Gap: no public dollar figures for actual space-cyber consulting engagements** (Booz Allen/Deloitte) — can't quantify "substitutes cost more" with real numbers; flag as unquantified in the report.

**Item 15 — Entry barriers [primary: eCFR, secondary: legal/industry summaries]**
Real and well-sourced: (1) facility clearances can't be self-sponsored, need agency/cleared-contractor sponsorship; (2) FOCI restrictions constrain non-US-controlled cap tables — a real fundraising constraint for a new entrant; (3) ITAR/EAR genuinely restrict spacecraft technical data to foreign persons (see item 22 below); (4) domain data access is a trust/chicken-and-egg problem — operators are reluctant to hand sensitive fleet data to an unproven vendor; (5) credible digital-twin/cyber-range capability requires deep SME familiarity with real spacecraft C2 protocols (Yamcs, COSMOS), not just software talent; (6) SBIR/STTR non-dilutive funding channel currently lapsed (see item 10). New: a **Satellite Cybersecurity Act of 2025 (S.3404)** is pending in Congress — not previously in the brainstorm report, worth adding as regulatory-tailwind context.

---

## A.4 Persona & Customer Journey

**Item 16 — Real persona [primary: live job posting]**
**Planet Labs — "VP & Chief Information Security Officer"** (live Greenhouse posting, ~Aug 2026): owns departmental budget, security strategy, ISO 27001/ISO 42001/CMMC certifications, physical security of manufacturing/R&D facilities, international clearance reciprocity, **and AI governance/secure ML pipeline oversight** — one exec role spans cyber + mission assurance + compliance + AI governance. Strong, concrete, citable persona anchor. Spire has a distinct "Security Operations Engineer" role scoped to "mission systems" specifically (confirms a mission-systems security function exists as a distinct scope, though seniority/reporting line unconfirmed).

**Item 17 — Procurement pattern [primary: AFWERX/SpaceWERX/SDA program sites]**
Standard on-ramp for small vendors selling to Space Force: **SBIR Phase I (feasibility) → Phase II (development) → Phase III (production/sole-source)** — a real, citable GTM pathway (e.g., LMI's $100M Phase III award). A live SpaceWERX cyberspace-warfare SBIR topic (opened Sept 2026, up to $2M/24mo) covers software supply-chain vetting and on-orbit cyber defense — directly analogous to this product category, though **note the SBIR/STTR authority lapse (item 10/15) currently pauses new awards.** Gap: no GSA Schedule or clearance-threshold specifics found for a commercial (non-SBIR) sale.

**Item 18 — Onboarding journey pattern [secondary, triangulated]**
No single named company publishes the full "design partner → shadow mode → automation → renewal" funnel as one case study, but the pattern is real and multiply-attested: Credo AI runs a formal Design Partner Program; Cloudflare launched a "Design Partner Designation" program (2026); security vendors commonly use a "monitor mode" (observe-only) first-production phase specifically to de-risk customer trust before enforcement (Akamai partner guidance). Use as a triangulated pattern, not a single cited case.

---

## A.5 Governance, Guardrails & Regional Compliance (US)

**Item 19 — NIST AI RMF four functions mapped [primary: airc.nist.gov, NIST's own resource site]**
- **Govern** → accountability structures / clear roles (Govern 2) → maps to **human-in-the-loop uplink approval** and escalation-policy ownership.
- **Map** → context/scope of what the AI is authorized to do → maps to defining "recommend vs. execute" boundaries (AI never uplinks directly).
- **Measure** → quantitative/qualitative risk tracking, trustworthiness evaluation, drift over time → maps directly to **hallucination/reliability safeguards and ongoing monitoring**.
- **Manage** → risk-treatment, response, recovery, communication plans → maps to **escalation/stop rules and incident response**.
*(Flag: verbatim PDF text wasn't extractable this session; definitions pulled from NIST's own official resource-center mirror — verify against the AI 100-1 PDF before final citation.)*

**Item 20 — NIST IR 8270 / IR 8401 control specifics [weakest sourcing — flag before citing]**
IR 8270: crosswalks `ID.RA-1`("asset vulnerabilities identified/documented")/`PR.IP-12`("vulnerability management plan developed and implemented") to SP 800-53 controls including **SI-2 "Flaw Remediation"**; explicitly notes satellite software "can often be patched or modified from the ground." IR 8401: structured around all 5 CSF functions, 23 categories, 108 subcategories, built to "address the goals of SPD-5"; relevant controls include access control for ground-segment assets (PR.AC), **dev/test environment separation from production** (directly relevant to patch-gating before uplink), and supply-chain/continuous monitoring (DE.CM). **Honest flag: specific control bullets came from secondary summaries, not a clean PDF extraction — recommend a direct read before final citation**, since both PDFs failed to render as text in this session.

**Item 21 — SPD-5 primary text [primary: Federal Register]**
Confirmed principles (Sept 2020, Federal Register 85 FR 56155): cybersecurity built in **before launch** (most satellites can't be serviced on-orbit); protect against unauthorized access "by physical means or electronic spoofing"; authentication/encryption for command-and-control links designed to "remain secure against existing and anticipated threats"; ground systems should adopt NIST CSF practices (patching, segregation, insider-threat training); supply-chain risk management (counterfeit/tampered component detection); ISAC-based information sharing. Applies to both government and commercial systems.
Source: [Federal Register 85 FR 56155](https://www.federalregister.gov/documents/2020/09/10/2020-20150/cybersecurity-space-systems-principles-space-policy-directive-5-of-september-4-2020)

**Item 30 — Is there a *binding* US vuln-management mandate for commercial operators? [primary: eCFR, Federal Register, FCC R&O, NIST SP 800-171; added after original plan — full detail `research/raw/06-us-binding-regs.md`]**
**Verdict: no general federal mandate.** "Operators are legally bound to manage vulnerabilities" is **false** as a general claim; only narrow, weaker hooks bind:
- **FCC licensees (all):** 47 CFR 25.271(d) — secure facilities and "satellite commands against unauthorized access and use." One sentence, no identify/prioritise/patch duty. Carried verbatim into proposed 47 CFR 100.202(d) by the Space Modernization R&O (adopted 22 Jul 2026, effective date pending); "cyber" appears 0 times in the R&O or NPRM. *(Flag: circulated text FCC-CIRC2607-02, not final released text.)*
- **NOAA Tier 2/3 remote-sensing licensees:** 15 CFR 960.9/960.10 — ≥256-bit NIST-approved encryption on TT&C links + unauthorized-access prevention. Encryption, not vuln management.
- **DoD contractors only:** DFARS 252.204-7012 + CMMC (32 CFR 170) pull in NIST SP 800-171 **3.14.1: "Identify, report, and correct system flaws in a timely manner"** — the only real flaw-remediation duty, but scoped to CUI-handling IT systems, not spacecraft/links; "timely" undefined, no risk-based prioritisation required. *(Flags: CMMC Phase 2 third-party audits reportedly suspended Jul 2026 — secondary only; whether Space Force/SDA/CASR contracts carry 7012 is unverified.)*
- **Not mandates:** FAA Part 450 (no cyber text); CIRCIA (reporting only, final rule not published as of 29 Sep 2026); space is not one of the 16 CISA critical-infrastructure sectors; S. 3404 Satellite Cybersecurity Act (unenacted, voluntary recommendations only); EO 14144 §3(e) (binds federal agencies/civil-space contracting, not commercial operators); SPD-5 and NIST IR 8270/8401 (voluntary).
**Implication:** the pitch must rest on operational risk (asset loss, bricked patches), not compliance. The 800-171 gap — "timely" with no prioritisation method — makes DoD contractors the natural beachhead. Suggested report wording: *"no general federal mandate; obligations arise only through licensing conditions (FCC, NOAA) addressing access control and encryption, and DoD contract flow-downs addressing CUI-handling systems."*
Sources: [47 CFR 25.271](https://www.ecfr.gov/current/title-47/part-25/section-25.271) · [FCC Space Modernization R&O](https://docs.fcc.gov/public/attachments/DOC-422740A1.pdf) · [15 CFR 960](https://www.ecfr.gov/current/title-15/part-960) · [DFARS 252.204-7012](https://www.ecfr.gov/current/title-48/section-252.204-7012) · [32 CFR 170](https://www.ecfr.gov/current/title-32/part-170) · [NIST SP 800-171r2](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-171r2.pdf) · [CIRCIA NPRM](https://www.federalregister.gov/documents/2024/04/04/2024-06526/cyber-incident-reporting-for-critical-infrastructure-act-circia-reporting-requirements) · [S. 3404 text](https://www.congress.gov/119/bills/s3404/BILLS-119s3404is.htm)

**Item 15/22 — ITAR/EAR [primary: eCFR + Federal Register]**
**Confirmed, not just assumed.** ITAR (22 CFR 120.33) covers spacecraft "technical data" broadly (design/development/operation/repair/testing/maintenance/modification documentation). 22 CFR 120.16 defines "foreign person" broadly (any non-US-person, including foreign corporations/governments). The **"deemed export" doctrine** means releasing technical data to a foreign person *even domestically* is legally an export — directly relevant to gating foreign-national employee/contractor access to customer telemetry. Most commercial comms/remote-sensing satellites were reclassified under **EAR ECCN 9A515** (dual-use, lighter regime than ITAR but still license-required for most destinations; a 2024 rule removed license requirements specifically for AUS/CAN/UK only). **Bottom line: the federated-learning-avoids-cross-border-data-movement argument is legally well-grounded**, not just plausible.

**Item 23 — CCPA/CPRA applicability [primary: Cal. Civ. Code]**
**Strong fit.** Cal. Civ. Code §1798.140(v)'s broad "personal information" definition plus a specific "precise geolocation" sensitive-data category (accurate within a 1,850-foot radius) plausibly covers subscriber-terminal location/identity/device data — assuming subscribers include California consumers/households (B2G/military terminals likely fall outside CCPA's "consumer" scope). Aggregated/deidentified data excluded.

**Item 24 — Escalation thresholds & audit trail [primary: NIST SP 800-53, secondary: SOC 2]**
NIST SP 800-53 Rev.5 **AU family** gives a ready-made design basis: AU-2 (which events must be logged — every uplink command, every AI escalation, every human override), AU-3 (record content schema: event type, timestamp, source, outcome, actor identity), AU-6 (review cadence — FedRAMP baselines commonly require **at least weekly** review, daily/near-real-time for privileged/remote-access events). SOC 2 CC7.2/CC7.3 (monitoring + evaluated alert thresholds with a named owner) as a complementary commercial-standard analogue; typical log retention 12–15 months.

**Item 25 — India fallback [primary: meity.gov.in, in-space.gov.in; secondary for CERT-In]**
DPDP Act 2023: "personal data" (§2(t)), "Data Fiduciary" (§2(j)), "Data Principal" (§2(k)), consent-based processing with enumerated legitimate-use exemptions (§7). IN-SPACe: any space activity within/from Indian territory needs authorization; **non-Indian entities must go through an Indian subsidiary/JV** — a real localization constraint relevant to the federated-design argument. CERT-In: 6-hour incident reporting under IT Act §70B(6), effective since June 2022 (confirmed via secondary legal sources only — the primary PDF wouldn't render; re-verify before final citation).

---

## Cross-cutting

**Item 26 — Smallsat failure-rate stat [primary: AIAA/USU conference paper]**
The "~40%" figure **holds up but needs rewording**. Langer & Bouwmeester (TU Delft, AIAA/USU SmallSat Conference 2016, 178 CubeSats analyzed): reliability falls to 48–65% at 2 years post-launch. A separate figure ("more than 40% of CubeSats launched since 2000 failed to accomplish their objectives") matches more closely but is framed as "since 2000," not a literal trailing-20-year window.
→ **Correction:** reword to "over 40% of CubeSats launched since 2000 have failed to fully accomplish their mission objectives" or "reliability falls to ~50–65% within 2 years of launch" — not "in the last 20 years."

**Item 27 — CVE volume [primary: cve.org Q1 2026 report + independent trackers]**
**Stale — needs updating, not just verifying.** 2024: 40,009 CVEs (matches the old "~40,000/year" claim exactly, but that was the 2024 figure). 2025: 48,185 (+20.6%). 2026 YTD (through Aug 31): 57,908, tracking toward a record year.
→ **Correction:** update "~40,000 CVEs/year" to **"~58,000 CVEs/year (2026 run-rate, up from ~40,000 in 2024)"** wherever it's used.

**Item 28 — Pricing comparables [primary: vendor pricing pages]**
CrowdStrike Falcon: per-endpoint/year + modular add-ons (EDR, Identity Protection, Cloud Security), quote-based. Datadog: per-host/month, publicly tiered ($15–$41/host/mo depending on tier/commitment). Both are strong, citable analogues for a "per-satellite base + per-module add-on" or "per-satellite, tiered-by-feature" pricing structure.

**Item 29 — Reference shortlist (finalized after research)**
Non-blog, verifiable, and directly load-bearing:
1. **NIST IR 8270** — Introduction to Cybersecurity for Commercial Satellite Operations (primary govt standard; re-verify control text directly from PDF before final citation).
2. **SIA 29th Annual State of the Satellite Industry Report (2026)** — primary industry-association market data (satellite count, revenue).
3. **Langer & Bouwmeester, "Reliability of CubeSats" (AIAA/USU SmallSat Conference, 2016)** — primary academic source for the failure-rate statistic.
4. **Space Policy Directive-5, Federal Register 85 FR 56155** — primary US government regulatory text.
Backup candidates: NIST IR 8401 (ground segment); Bonawitz et al., "Practical Secure Aggregation" (ACM CCS 2017) if the technical/moat section needs a federated-learning citation.

---

## Open items still needing action before drafting

1. Directly re-read NIST IR 8270/8401 PDFs (fetch tool couldn't render them as text this session) to pull verbatim control language for item 20/29 citations.
2. Directly re-read SPD-5 Federal Register PDF for verbatim Section 4 quoting (currently a close paraphrase from an archived White House memorandum page).
3. Company name/mission/vision — still an open creative decision (item 3), not research.
4. Confirm final jurisdiction choice (US recommended, per `topic/Topic_Brainstorm_Report.md` §4 Q16) — this research assumed US.
