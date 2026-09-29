# Mid-Sem Project — Research Plan

**Purpose:** turn every open question in `topic/Topic_Brainstorm_Report.md` (§9) into a research task tagged to the rubric marker it feeds (`brief/Instructions.md` §A), so drafting can start straight from sourced findings instead of model memory. Deadline: 1 Oct 2026, 23:59.

**Company (locked):** AI platform prioritising and safely resolving vulnerabilities across satellite missions — JEPA-style world model + constrained RL rollout planner + LLM agent, human-approved uplinks. Topic: Day-Zero Vulnerability Prioritisation, Defence/Space/Cybersecurity segment (`brief/Project Topics.md` §1).

Each row below is tagged:
- **[gap]** — nothing in hand yet
- **[verify]** — a claim already stated from model knowledge (`topic/Topic_Brainstorm_Report.md` §10) that needs a real citation
- **[deepen]** — partially covered, needs more

---

## 1. Marker map: rubric section → research tasks

### A.0 Company Overview (brand identity, market opportunity)
| # | Task | Tag | Candidate sources |
|---|---|---|---|
| 1 | LEO/satellite market growth numbers, current active-satellite count, why the sector is "ripe" now | deepen | Orbital Radar, azmth.space, SpaceNexus (already in §13) — cross-check against one industry report (Euroconsult / SIA State of Satellite Industry) |
| 2 | Regulatory pressure trend (space added to critical-infrastructure lists) driving urgency | gap | EU NIS2 space-sector inclusion, proposed EU Space Act, SPD-5 — verify primary text, not just secondary blog mentions |
| 3 | Company name/mission/vision | gap | Internal decision, not research — needed before drafting §0 |

### A.1 Agentic AI & Value Proposition
| # | Task | Tag | Candidate sources |
|---|---|---|---|
| 4 | Cost of a patch-related failure: bricked satellite value, Viasat KA-SAT recovery cost, insurance payout if known | gap | Viasat public statements/10-K, ResearchGate lessons-learned paper (§13), insurance trade press |
| 5 | Analyst/consulting cost baseline (small security team cost, Deloitte/Booz Allen day rates if published) to quantify "efficiency" claim | gap | Public consulting rate benchmarks, space-sector job postings for salary ranges |
| 6 | Multi-step agentic workflow detail: ingest → map → score → twin-test → plan → approve → uplink → monitor → rollback — confirm each step maps to a real operational analogue | deepen | NIST IR 8270 (already sourced), ESA on-board software maintenance concept doc |

### A.2 Moat & Defensibility
| # | Task | Tag | Candidate sources |
|---|---|---|---|
| 7 | Is ESA-ADB / OPS-SAT telemetry sufficient to bootstrap a JEPA world model from cold start? | gap | ESA-ADB benchmark paper, OPS-SAT PMC paper (§13), any JEPA-on-time-series training-data-size discussion (MTS-JEPA paper) |
| 8 | Federated learning across heterogeneous satellite platforms — does naive averaging fail in practice, what's the fix (shared base + per-platform adapters)? | gap | Federated learning heterogeneity literature (FedProx, personalization surveys), not satellite-specific if none exists — say so explicitly |
| 9 | Differential privacy / secure aggregation cost overhead — is it practical at this data volume? | gap | Standard DP-SGD / secure aggregation overhead papers |
| 10 | Re-confirm no existing company does the *whole* loop (orbit-aware prioritisation + patch scheduling + twin validation + fleet rollout) — refresh the competitor search since this is the load-bearing originality claim | deepen | Repeat searches from §6 plus: Slingshot Aerospace, Voyager Technologies, Axiom Space, Space ISAC advisories, SBIR/STTR award database, Crunchbase/PitchBook for "satellite cybersecurity" funding rounds (2025–26) |

### A.3 Porter's Five Forces
| # | Task | Tag | Candidate sources |
|---|---|---|---|
| 11 | **Buyer power:** how many mid-size operators (50–300 satellites) actually exist, who are they by name | gap | Orbital Radar "satellites by operator" (§13), SIA/Euroconsult operator lists |
| 12 | **Supplier power:** which manufacturers (Spire, Airbus, Thales Alenia, Terran Orbital, York Space) and ground-station-as-a-service providers (AWS Ground Station, KSAT, Leaf Space) are relevant; is any one dominant | gap | Manufacturer investor pages, AWS Ground Station pricing page, KSAT service pages |
| 13 | **Rivalry:** confirm current rivalry is low — cross-check item 10 | deepen | same as item 10 |
| 14 | **Substitutes:** cost/adoption evidence for consulting engagements vs. in-house teams vs. doing nothing | gap | Deloitte Silent Shield press (have), Booz Allen digital twin page (have) — need one data point on actual adoption/cost if publicly available |
| 15 | **New entrants:** barriers to entry — clearance requirements, ITAR, domain data access — as a defensibility argument | verify | ITAR/EAR scope on spacecraft technical data (claimed in §10, needs primary-source citation, e.g. 22 CFR 121) |

### A.4 Persona & Customer Journey
| # | Task | Tag | Candidate sources |
|---|---|---|---|
| 16 | Exact persona: job title (e.g. "Director of Mission Assurance" / "Head of Cybersecurity"), team size, reporting line, budget authority at a mid-size operator | gap | LinkedIn/job-posting research for actual titles at mid-size operators (Spire, ICEYE, Planet, BlackSky) — use as pattern evidence, not the company itself as a persona source |
| 17 | Decision-making criteria: what would make a security lead choose/reject a vendor (budget cycle, procurement process, security clearance requirements for defence customers) | gap | Government/defence procurement pattern research (GSA schedules, Space Force SBIR structure) |
| 18 | Full onboarding → shadow-mode → automation → renewal journey, filled in with realistic timeframes | gap | Enterprise security-tooling onboarding patterns (analogous SaaS security products) as a reference pattern |

### A.5 Governance, Guardrails & Regional Compliance (US recommended)
| # | Task | Tag | Candidate sources |
|---|---|---|---|
| 19 | Map NIST AI RMF's four functions (Govern/Map/Measure/Manage) explicitly to each guardrail (HITL uplink approval, rollback, escalation) | verify | NIST AI RMF 1.0 primary document |
| 20 | NIST IR 8270 (satellite ops) and NIST IR 8401 (ground segment) — pull the specific control items relevant to patch/vulnerability management | verify | Already sourced PDFs (§13) — needs a close read, not just citation |
| 21 | SPD-5 (Space Policy Directive-5) actual content on cybersecurity principles | verify | Primary text of SPD-5 (whitehouse.gov archive / federal register) |
| 22 | ITAR/EAR constraint on federated learning with foreign operators — is this a real legal constraint or an assumed one? | verify | 22 CFR 120-130 (ITAR) scope, EAR Category 9 (spacecraft) |
| 23 | CCPA/CPRA applicability to subscriber-terminal location/identity data specifically | gap | CCPA/CPRA statutory text — scope test against telemetry-adjacent personal data |
| 24 | Concrete escalation thresholds and audit-trail format (currently unanswered in §9.4) | gap | Design decision informed by NIST IR 8270 controls + analogous SOC2/audit-log standards |
| 25 | *(Optional fallback)* India alternative — DPDP Act, IN-SPACe authorisation, CERT-In 6-hour rule, Indian Space Policy 2023, in case US is not finally confirmed | gap | DPDP Act 2023 text, IN-SPACe official site, CERT-In directives |

---

## 2. Cross-cutting research (not tied to one marker but load-bearing)

| # | Task | Tag | Why it matters |
|---|---|---|---|
| 26 | Failure-rate statistic (~40% of small-sat missions have partial/total failure) — find the actual study, not the secondhand mention | verify | Used as a headline stat in Overview/Value; if wrong, undermines credibility in the viva |
| 27 | CVE volume (~40,000/year) — confirm current year figure | verify | Used to justify continuous-triage value prop |
| 28 | Pricing model sanity check: per-satellite vs. per-fleet-tier vs. enterprise licence, against comparable B2B security SaaS pricing (e.g. per-asset security tooling) | gap | Needed to make the "why customers pay" section concrete instead of hand-waved |
| 29 | 3–4 key non-blog references, shortlisted from `topic/Topic_Brainstorm_Report.md` §12, confirmed accessible and correctly cited | deepen | Explicit assignment requirement (§F) |

---

## 3. Method

1. **Parallel research threads**, each a separate focused pass (web search + read primary sources, not just headlines): (a) market/customers/pricing, (b) suppliers/manufacturers, (c) competitors/rivalry refresh, (d) US regulation primary texts, (e) technical feasibility (JEPA/federated learning/data volume).
2. **Every claim gets sourced or flagged.** No number goes into the deck without a link; anything that can't be sourced is marked as an explicit assumption with its reasoning shown, never presented as fact.
3. **Output:** findings get written into `research/Research_Findings.md` in the project folder, organized by the same numbered items as this plan, each with: finding, source link, and the rubric marker it feeds. The §10 "verify before citing" list in `topic/Topic_Brainstorm_Report.md` gets resolved item-by-item (confirmed with citation, or struck and replaced).
4. **Reference shortlist** (item 29) gets finalized last, once findings show which sources actually held up.
5. Skipped: primary interviews / surveys of real satellite operators — not feasible for a mid-sem assignment; public-source research only. Skipped: exhaustive Porter's-Five-Forces literature review — the framework serves the strategic point (§A.3 note in `brief/Instructions.md`), not a standalone analysis.

---

## 4. Out of scope for this plan

- Actual drafting of the 4-page submission (separate task, after findings land).
- Company name/mission/vision brainstorm (item 3) — creative decision, not research.
- Format choice (doc/slides/video) — separate decision.
