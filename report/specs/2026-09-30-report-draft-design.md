# Report Draft — Design Spec

**Date:** 2026-09-30 · **Deadline:** 1 Oct 2026, 23:59 · **Status:** awaiting user review

## 1. Decisions (from the brainstorming session)

| Decision | Choice | Note |
|---|---|---|
| Company name | **Phylax** (Greek: guardian, watchman) | Web-check for an existing company of the same name before final (possible clash with "Phylax Systems"; fallback "Phylax Orbital"). |
| Format | Word/PDF doc, 4 pages + 1-page appendix, 2 visuals | Draft in markdown → convert to .docx at the end. |
| Draft depth | Full prose, **user rewrites in own voice** | Brief §F prohibits submitting AI text unrevised; viva possible. Every factual sentence carries a source tag `[RF n]` / `[Q n]` in the draft so it can be defended, and the tags are stripped at conversion. |
| Jurisdiction | **United States** (main) | India = a one-line "next market / engineering base" in the vision, backed by a separate research task (§7). |
| Structure | **Design-Thinking frame**: an empathy opening, one course concept anchoring each rubric section, a closing four-lens check (Feasibility / Usability / Desirability / Viability) | Each section is also designed to hit a named grading component (§3). |

## 2. Running threads (Storytelling)

1. **The ground-to-space loop.** It's the problem (Viasat: a ground VPN flaw → 30,000 modems, 5,800 turbines [RF 4]), the agentic workflow, the source of the moat's data, and the reason for the stop rules.
2. **Trust.** Subject-matter experts rely less on automation (Sanchez et al., S11). That drives human approval, outputs expressed in SPARTA IDs, and "decision support, not certified safe".

Each section ends with a one-line handoff to the next. Honest weaknesses get one line per section and are gathered in the four-lens close.

## 3. Section design (course anchor × grading target × content)

**Page budget:** opening + A.0 + A.1 ≈ 1 p · A.2 + A.3 ≈ 1 p · A.4 ≈ ¾ p · A.5 ≈ ¾ p · close + references ≈ ½ p.

### Opening scene (~⅙ p) — Empathy (S11) → Storytelling
A 2 a.m. advisory lands. A CISO at a mid-size operator has 200 satellites, a flaw in ground-station software, and the next pass window closing. Does the flaw reach the fleet? Is the vendor patch safe to uplink? Introduces the persona, who returns in A.4.

### A.0 Overview: Phylax — Gartner 8-layer stack; B2B/B2G → Content + Creativity
- Brand: name story, mission ("keep every fleet safely patchable"), vision ("the trusted decision layer for every software-defined spacecraft"; dream-big line).
- Stack position: **Layer 6 (AI Application) serving Layer 7 (Security & Risk)** for space missions.
- Market: 14,266 operational satellites end-2025, 4,434 deployed in 2025 (+65%) [RF 1]. Say plainly that growth is driven mostly by mega-constellations (R1) and that the target is the mid-size tier.
- Why ripe for AI: exposure is rising (CVEs 40,009 in 2024 → 48,185 in 2025; 57,908 by 31 Aug 2026 **YTD** [RF 27, R10]) and applies mainly to ground-segment software; triage stays manual and siloed.
- **Do not use:** "~16k satellites", "~58k/yr", "3-person team", "40% since 2000", a Starlink % share.

### A.1 Agentic AI & Value — agent vs agentic AI (S2–3); ReAct; efficiency vs innovation (S3) → Content + Presentation (Visual 1)
- **Architecture (reframed per R6/R8/R14/R31):**
  1. *Advisory agent* (LLM, ReAct-style): reads advisories and CVEs, proposes component matches; deterministic SBOM/CPE matching confirms; every match cites its inventory line; unmatched → human. Self-hosted open-weights model inside the US boundary.
  2. *Exposure graph*: ground → network → link → spacecraft → terminal consequence paths. This is the answer to Viasat: knowing *that* VPN flaw reaches the fleet, which generic vulnerability management tools don't model (R5).
  3. *Risk scorer*: exploitability + consequence, expressed in **SPARTA technique/countermeasure IDs**.
  4. *Fix planner*: constraint solver for pass windows, power and staged rollout (guaranteed feasibility) + a learned policy that improves rollout *order* from outcomes. **Change from the locked "constrained RL planner" — flag for user.**
  5. *Validation*: execution-level tests run in the manufacturer's emulator/testbed (as with ESA OBSM [RF 6]; Spire-style CI/testbed [RF 31]). **The JEPA world model does pre-uplink risk scoring from features plus post-uplink anomaly detection and rollback triggering**, not prediction of what new code will do.
  6. *Human approval gate* → uplink via the operator's existing update manager → monitor → auto-halt/rollback.
- Fix ladder: vendor patch → workaround → ground fix → accept and monitor → AI-drafted patch only as a suggestion to the manufacturer [TB 7.4].
- **Value**: *efficiency* = triage hours saved at equal coverage, and faster time-to-remediate. *Innovation* = safe-to-patch evidence packs that support insurance and defence-contract assurance (new capability, not cost-cutting).
- **Value ordering (R3/R4):** lead with **speed and coverage of triage** (frequent, measurable). A bricked satellite is a **tail risk**, not the headline: no base rate exists, and Viasat itself reported the attack as financially immaterial [RF 4]. Viasat is used for *disruption scale* (30,000 modems, 5,800 turbines) and the *ground→space path*, never as a dollar loss.
- **Evaluation (R17):** proxy metrics are named up front: analyst hours per finding at equal coverage; time-to-remediate for flaws later exploited on the ground segment (observable); agreement with red-team results in the testbed/cyber range; backtest against past Space ISAC advisories. Transfer of ground-trained exploitability to space is stated as an open validation risk.
- Honest line: rollout/rollback tooling already exists (Planet pipeline, Spire CMP [RF 31]). Phylax connects prioritisation to it; it doesn't replace it.
- **Visual 1:** loop/architecture diagram (six stages, human gate highlighted).

### A.2 Moat — Morningstar five moat sources; Foundation Capital "the model isn't the moat" → Content + Creativity
- "Would Phylax survive if the model changed tomorrow? Yes, because the moat is the workflow and the context graph."
- Ranked moats:
  1. **Context graph / patch-outcome record**: every decision, approval and outcome, including ground-segment patch outcomes (the frequent ones, R11). Nobody can buy it.
  2. **Switching costs**: the approval workflow, audit trail, integrations, and SPARTA-mapped history (platformization logic from the student moats PPT).
  3. **Efficient scale**: a niche too small for many players; the small buyer pool becomes a moat (turns R19 around).
  4. *Conditional upside*: a cross-fleet network effect, only if operators opt in via an SDA-style neutral model sharing minimum data [RF 31, Q22]. Named test before claiming it: **pooled vs local model on held-out anomalies in design-partner pilots**, since DP noise and per-fleet adapters may erase the gain (R12).
- **Data-volume caveat (R11):** spacecraft patch outcomes are rare and mostly "success". The record therefore counts any post-update anomaly/degradation plus ground-segment patch outcomes, and the report says the space-side label volume is unmeasured.
- Removed from the moat: public data (feasibility only [RF 7]) and manufacturer partnerships (unevidenced, R13).
- Honest line: thin at cold start, grows per customer; the product must work fully for one operator.

### A.3 Five Forces — Porter (S7); niche strategy (Thiel); "competitors = anyone meeting the same need" → Content + Presentation (Visual 2)
- **Strategic point:** *be the neutral decision layer on top of what operators already use.* Every force pushes Phylax toward integrating, not replacing.
- Buyers: few and capable → **high**. Honest count: Planet, Iridium, SES(+Intelsat), ICEYE [RF 11, 31]; all run formal in-house programs (SES 40+ staff). Globalstar out (Amazon). **Spire is not counted as a buyer**: it is the co-opetition case (a possible buyer, a supplier, and a rollout-tooling partner/rival at once, R15). Buyer HQ/US status is not verified (R19), so the text says "named mid-size operators", not "US buyers".
- Suppliers (Phylax's own inputs, R18): manufacturers' SBOMs, emulators and patches → **high**, consolidating under primes [RF 12]. Their incentive: lower support/warranty cost, and a customer-requested SBOM feed. Ground-station-as-a-service → low [RF 12].
- Rivalry: **low on the whole loop**. Named adjacents: **Aerospace Corp SPARTA/SPARTEND** (reference and on-orbit detection, not per-operator decisioning), **CT Cubed IRON GALAXY** (training range), Spire CMP (rollout only → partner), Deloitte Silent Shield (detection) [RF 10/13, 31]. Caveat: absence of public claims ≠ absence (R23).
- Substitutes: **the good-enough stack** = in-house program + SPARTA + vendor patches + Spire-style tooling; doing nothing [RF 14, 31] → **high**. SpaceX's in-house OTA system is cited only as a *secondary* source about *mega-operators*, and terminals and satellites are kept separate (R21).
- S.3404 appears, if at all, only as a policy-attention signal, never as a "tailwind" (R24).
- New entrants: primes and Booz Allen/Deloitte → **high threat**. Clearances/FOCI/ITAR block startups first (R22), so the entry path is commercial, unclassified, US-person team; a cleared partner later.
- Regulation cuts both ways: no binding US mandate [RF 30]. 800-171 3.14.1 "timely" with no prioritisation method is the opening for the ground-IT module.
- **Visual 2:** compact table: force · rating · evidence · what Phylax does about it.

### A.4 Persona & Journey — 2–3-word label + psychographics (S8); Diffusion of Innovation; Lemon & Verhoef; Puntoni's four AI experiences (S9–10) → Storytelling + Presentation (persona card)
- **Persona: "the Stretched Sentinel"**: a CISO/VP Security at a US mid-size operator that also holds DoD/government contracts (resolves R26: one actor). Grounded in Planet's VP & CISO posting (scope spans cyber, mission assurance, compliance, AI governance [RF 16]). Pains, goals, decision criteria (evidence, auditability, doesn't touch the command path, fits existing tools). Psychographic: an expert, therefore sceptical of automation.
- **Buying committee** (R27): economic buyer = CISO; approver = mission-ops lead; champion = SecOps engineer.
- Diffusion: early adopters = operators already running staged deploy pipelines (Planet-like).
- **Journey** (prepurchase → purchase → postpurchase, cyclical) mapped to Puntoni:
  - *Data capture*: onboarding builds the inventory (manufacturer data package + operator config) as a cost-to-serve (R14).
  - *Classification*: shadow mode, ranked findings next to the team's own triage.
  - *Delegation*: guarded execution. Ground-side fixes and plan drafting run automatically; uplinks are human-approved; pre-approved fix plans ahead of pass windows (R9).
  - *Social*: the explanations and evidence packs the CISO shows the board and insurer.
  - Renewal: triggered by hours saved plus zero unsafe uplinks.
- **Timeline (R28), labelled as an assumption:** design-partner paid pilot → shadow mode ~1 quarter → guarded ground-side automation → first uplink-assist decisions → renewal at 12 months. Runway from paid pilots and seed funding. Entry via the ground-IT module (800-171), with the space core as upsell. SBIR only "if authority is current" (R25, checked in §7).

### A.5 Governance (US) — Trust (competence, integrity, benevolence; distrust ↔ overtrust zone, S11); risk taxonomy, kill switch, audit log, drift, prompt injection, Air Canada (S5); NIST AI RMF → Content + Storytelling
- **Autonomy table** (R9): autonomous = ingest, map, score, draft plans, ground ticketing, monitoring, auto-halt · human-approved = ground-change execution, every uplink · **never automated** = changes to the command, boot or auth path; AI-written flight code uplink. Missing approval at pass close → **hold**.
- **Stop rules (T4):** anomaly score over threshold after canary; any telemetry loss after uplink; confidence under a floor; the flaw touches the command-authentication path → human-only; conflicting advisories → escalate.
- **Unrecoverable-failure class (T5, Q25):** A/B partition + watchdog as a precondition; canary on the least-critical satellite; limits on how far a bad patch can spread.
- **Hallucination and injection:** retrieval-grounded, citation-required mapping; advisories treated as untrusted input (indirect prompt injection, S5 + student PPT); insecure-output handling → structured outputs only.
- **Monitoring and audit:** drift monitoring (Zillow lesson); NIST SP 800-53 AU-2/3/6 audit trail [RF 24]; model cards.
- **Liability (T6, Q25):** "decision support with evidence and stated residual risk", never "certified safe"; the manufacturer warrants its own patch; contractual cap; audit trail as evidence. Air Canada lesson: companies are bound by their AI's output, so claims are worded carefully.
- **Jurisdiction:** NIST AI RMF Govern/Map/Measure/Manage mapping [RF 19]; CCPA: Phylax is a service provider; terminal location data minimised [RF 23, R32]; FTC: fairness risk low (machines, not people) but AI capability claims must not overstate (one line, no specific FTC case); **EAR 9A515 first, ITAR where applicable** [RF 22, R16]; federated pool limited to US + licence-exempt allies (AUS/CAN/UK); whether trained weights are controlled is flagged as open.
- **Customer exit / unlearning (R33):** a departing operator's local data and adapters are deleted; its past contribution to any shared model can't be removed selectively. It is handled by periodic retraining from retained contributions, and the limitation is stated.
- Ends the trust thread: calibrated trust = the zone between over- and under-trust.

### Close: four-lens check (~⅙ p) → Storytelling + Content
One line per lens with its honest risk: *Feasibility* (validation stays with the manufacturer's testbed; ground→space exploitability transfer unproven, R17), *Usability* (fits existing pipelines; approval inside pass windows), *Desirability* (in-house teams are capable → "connect and speed up", Q20–21), *Viability* (value-based pricing; revenue formula with labelled assumption: ACV ≈ 3–4 analyst-equivalents × buyers; weakest point, Q24). Then the dream-big vision line (+ India as next market/engineering base, pending §7).

### References (3–4 key, non-blog)
1. NIST IR 8270 (verify the control text in the PDF, R35) · 2. SPD-5, 85 FR 56155 (Federal Register, primary) · 3. NIST SP 800-171 Rev 2 (read directly in item 30) · 4. SIA 29th State of the Satellite Industry Report 2026 (cite the report, not the press release). Langer & Bouwmeester is dropped unless its exact 2-year reliability figure is used. Course frameworks (Porter, Lemon & Verhoef 2016, Puntoni et al. 2021, Lee & See 2004) are cited in-text.

### Appendix (1 page) → Creativity & Effort
1. Working evidence: **moat-evolution decision tree** (Q10 → Q12 → Q13 → Q18 → Q22: network effect → rare events → outcome data → context graph + switching costs).
2. AI tools: Claude Code (Opus) as main assistant; Sonnet/Opus subagents for sourced research and a red-team review; verification discipline (§10.1 log). ≥2 transcript links (from `logs/`; **the user must supply the shareable links**).
3. Hardest concept: **defensibility, i.e. who owns the data and why operators would share.** Options considered: federated network effect, public data, manufacturer partnerships, outcome record + switching costs. Why the last one was chosen.
4. Accepted / modified / rejected / independently developed: from TB §11.2 + Q17–Q25. Independently raised by the user: regulation double edge, the Item 7 disconnect, in-house teams, helping competitors, unit economics, undo = unreliable.

## 4. Numbers: use / avoid (Content accuracy)
Use: 14,266 sats [RF 1] · 4,434 deployed 2025 (+65%) · CVEs 40,009 / 48,185 / 57,908 YTD 31 Aug 2026 · Viasat ~30,000 modems, ~5,800 turbines, and "no material impact" (use honestly) · SES 40+ security staff · smallsat ~$0.5–1M (secondary, CubeSat-class) · analyst $115–159K (general-industry) · 800-171 3.14.1 exact text.
Avoid: ~16–17k sats · ~58k/yr · Starlink % · "3-person team" · "40% since 2000" · "fully tested" · "legally required to patch" · "nobody validates patches" · "crores per year".

## 4a. Review coverage matrix (every item in `research/Research_Findings_Review.md`)

"Fixed" = the draft changes the claim. "Caveat" = the claim stays but its limit is stated. "Avoid" = the claim is kept out of the draft.

| Item | Issue (short) | Handling | Where |
|---|---|---|---|
| K1 | No binding US mandate | Fixed: pitch on operational risk; regulation cuts both ways | A.3, A.5 |
| K2 | Public data ≠ moat | Fixed: removed from moat, kept as feasibility | A.2 |
| K3 | Static vs live is the wrong axis | Fixed: reference vs decision-and-execution; build on SPARTA | A.1, A.3 |
| K4 | Operators do it in-house | Fixed: "connect and speed up"; good-enough stack as substitute | A.3, close |
| K5 | Why share with rivals | Fixed: network effect conditional, SDA model | A.2 |
| R1 | Growth is mega-constellation growth | Caveat: say so; target is the mid-size tier | A.0 |
| R2 | Satellite numbers don't reconcile | Avoid: no Starlink %; SIA 14,266 only | A.0, §4 |
| R3 | Viasat "immaterial" | Fixed: disruption scale + path, not dollars | A.1 |
| R4 | No brick base rate | Fixed: triage speed leads; bricking = tail risk | A.1 |
| R5 | Viasat supports the commodity layer | Fixed: ground→space consequence modelling is the differentiator | A.1 |
| R6 | World model can't predict new code | Fixed: emulator validates; JEPA scores risk + detects anomalies | A.1 |
| R7 | Auto-rollback exists (Spire, SpaceX) | Fixed: integrate with existing update managers | A.1, A.3 |
| R8 | RL vs solver | Fixed: solver + learned ordering (user to confirm) | A.1 |
| R9 | Where does the agent act? | Fixed: autonomy table; hold on missing approval | A.4, A.5 |
| R10 | CVE arithmetic | Fixed: 57,908 stated as YTD; scoped to ground software | A.0 |
| R11 | Outcome-label volume unknown | Caveat: broadened label; volume unmeasured | A.2 |
| R12 | DP erodes pooled model | Caveat: pooled-vs-local pilot test named | A.2 |
| R13 | Manufacturer moat unevidenced | Fixed: removed from moat; moved to supplier power | A.2, A.3 |
| R14 | No SBOMs available | Fixed: onboarding builds inventory as cost-to-serve | A.1, A.4 |
| R15 | Spire triple role | Fixed: co-opetition case, not in buyer pool | A.3 |
| R16 | Export-control overstated | Fixed: EAR 9A515 first; allied pool; weights question open | A.5 |
| R17 | No evaluation method | Fixed: proxy metrics named; transfer risk stated | A.1, close |
| R18 | Supplier power from wrong side | Fixed: Phylax's own inputs = high | A.3 |
| R19 | Buyer pool tiny/unsourced | Caveat: named operators only; efficient-scale framing | A.2, A.3 |
| R20 | No unit economics | Caveat: value-based formula with labelled assumption | close |
| R21 | SpaceX evidence secondary | Caveat: tagged secondary, mega-operators only | A.3 |
| R22 | Barriers hit the startup first | Fixed: entry path stated | A.3 |
| R23 | Originality caveats dropped | Caveat: absence of claims ≠ absence | A.3 |
| R24 | S.3404 "tailwind" | Avoid: attention signal only | A.3 |
| R25 | SBIR contradiction | Caveat: conditional wording; status check in §7 | A.4 |
| R26 | Three first customers | Fixed: one actor (mid-size operator with DoD contracts) | A.4 |
| R27 | Buyer ≠ approver ≠ user | Fixed: buying committee | A.4 |
| R28 | No sales cycle | Fixed: labelled assumption timeline | A.4 |
| R29 | Liability | Fixed: decision-support wording, cap, manufacturer warranty | A.5 |
| R30 | No stop rules | Fixed: 5 stop rules + autonomy table | A.5 |
| R31 | LLM hosting + hallucination | Fixed: self-hosted, citation-required, deterministic match | A.1, A.5 |
| R32 | FTC + CCPA role | Fixed: one-line FTC; service-provider role | A.5 |
| R33 | Unlearning on exit | Caveat: retraining approach, limitation stated | A.5 |
| R34 | 40% statistic unsourced | Avoid: Langer dropped unless the exact figure is used | §4, refs |
| R35 | Reference flags | Caveat: verify IR 8270 + cite the SIA report itself before final | refs |

## 5. Output files
- `report/Phylax_Report_Draft.md`: the draft, with source tags.
- Visuals built at the conversion step (diagram + table).
- Conversion to `.docx` is a later step, not in this draft.

## 6. Out of scope for this draft
New research (except §7), final formatting, the .docx build, stripping source tags, and the user's voice rewrite.

## 7. Parallel tasks
- **India research** (Sonnet subagent): mid-size operator count under IN-SPACe, security-team maturity, engineering cost base, DPDP/IN-SPACe/CERT-In constraints. Output → RF item 32 + raw/08. Feeds one vision line only.
- **Name check**: web search "Phylax" for company clashes in security/space.
- **SBIR status** (R25): quick check whether SBIR/STTR authority is current; one line in A.4 depends on it.
