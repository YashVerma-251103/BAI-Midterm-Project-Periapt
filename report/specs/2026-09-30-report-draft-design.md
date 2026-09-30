# Report Draft — Design Spec

**Date:** 2026-09-30 · **Deadline:** 1 Oct 2026, 23:59 · **Status:** v3, awaiting user review. It replaces v2 (still in git history). The changes are listed in §10.

**Why v3 exists:** v2 had grown into "known flaw → safe fix across the whole mission", with AI as a helper. That was too wide to deliver and had drifted from the listed topic. v3 cuts back to the original problem and puts AI at the centre (topic report Q31–Q39).

## 1. Decisions

| Decision | Choice | Note |
|---|---|---|
| Company name | **Periapt**: a protective amulet; echoes *periapsis*, an orbit's closest point ("protection at the closest point of risk") | Renamed from Phylax (Q30). |
| Topic | Defence, Space & Cybersecurity → **Day-Zero Vulnerability Prioritisation (Predictive ML)**: "autonomous systems scanning, scoring, and prioritising unpatched security flaws in critical infrastructure" | **The core is predictive prioritisation** (Q36). |
| Scope | Known flaws that could affect a satellite operator's fleet. Periapt **finds, scores, ranks and explains**. Ground systems count only as the way in. It does not write, test or send fixes. | The niche from the original 17 Sept problem (Q34). |
| Positioning | **A copilot for the three teams** (security, flight software, mission ops). The AI reads, predicts, ranks and drafts; each team keeps its decision. | Q35. It plugs into the team's own ranking method, so there's no migration. |
| Relation to Aerospace Corp | **Complement, not rival.** Periapt builds on SPARTA and speaks its IDs. Federal rules say an FFRDC like Aerospace should not use its privileged access to compete with the private sector (FAR 35.017). | Q39, RF 32. Don't say "banned from all commercial work". |
| Autonomy | Scan, score and rank run **on their own**. Humans can override at any time (**on the loop**). A human approves **before anything touches a satellite or a ground system** (**in the loop**). | Q37. |
| Ranking rule | The AI may **raise** a flaw's priority on its own. **Lowering** needs a human. If the world model is **outside its data**, impact counts as **high**. | Approved 2026-09-30. |
| Growth path | **Stage 1 = this report's product.** Later stages (fix-window planning, then validation/rollout with partners) come only after trust is earned. | Q39. Course: "think big, act small"; niche first, then adjacent (Porter deck, Thiel). |
| People-heavy start | Deliberate: forward-deployed engineers onboard each customer and build trust in shadow mode. | Q39. Experts rely less on automation (Sanchez et al., S11). |
| Format | Word/PDF doc, 4 pages + 1-page appendix, **3 visuals** | Draft in markdown → .docx at the end. |
| Draft depth | Full prose with `[RF n]`/`[Q n]` tags; **the user rewrites it in their own voice** | Brief §F; viva possible. The tags are stripped at conversion. |
| Jurisdiction | **United States** | **India: on hold (user decision pending).** SBIR: also held, so it's kept out of the text. |
| Revenue | **No revenue or ACV figure** (Q29). Pricing *structure* only: per-fleet annual subscription + one-time onboarding fee. | |
| Structure | Design-Thinking frame: empathy opening → one course concept per section → four-lens close → the opening scene resolved (bookend) | |
| Key references | SIA 29th State of the Satellite Industry **Report** 2026 · NIST SP 800-171 Rev 2 · NIST AI RMF 1.0 · Hundman et al. 2018 (KDD) | Approved 2026-09-30. NIST IR 8270 dropped (still unverified, R35). |

## 2. The product (the single source for every section)

**The problem.** Advisories arrive faster than teams can judge them (CVEs +20.6% from 2024 to 2025 [RF 27]). Existing tools already match known CVEs to listed software: scanners on ground IT, and SBOM tools where a parts list exists (Thales Alenia uses Black Duck [RF 12]). What remains mostly manual is **judging what a flaw means for each satellite**:
- space advisories that come as prose, not CVE entries;
- spacecraft parts lists that often don't exist (R14);
- whether a ground flaw can reach the fleet;
- what an attack would actually do to each satellite.

That judgement is split across security, flight software and mission ops.

**What Periapt does.** It watches advisories around the clock and turns each one into a **ranked, explained list for this operator's fleet**: which flaw first, on which satellites, and why.

### 2.1 How a ranking is made: three layers, and AI only where rules can't reach
| Layer | Question | How | AI? |
|---|---|---|---|
| 1. Facts | Which satellites and ground systems have the flaw? Can an attacker reach the fleet from it? | The **LLM agent** reads the advisory and proposes matches. A deterministic match against the parts list confirms each one and must cite the matching line; anything unmatched goes to a human. A **reach map** (ground → network → spacecraft paths) checks whether it's reachable. | LLM for reading; the rest is plain software |
| 2. Standard scores | How severe is it, and how likely is an attack? | CVSS, **EPSS** (FIRST's free ML exploitation forecast [RF 32]), SPARTA technique and countermeasure IDs | Existing tools, **used, not rebuilt** |
| 3. Impact per satellite | What would an attacker actually do to *each* satellite through this flaw? | The **world model** plays out "what if these commands were sent?" on each satellite in its current condition | **Periapt's own AI** |

- **Rank = likelihood (layers 1–2) × impact (layer 3).** This fills in the operator's *existing* method (e.g. Spire ranks by ISO 27005 likelihood × impact [RF 31]) instead of replacing it.
- **Authority:** layers 1–2 set a floor. Layer 3 can raise a flaw, but lowering it needs a human. Outside its data → "impact unknown" → high.

### 2.2 The world model (what it is, and what it isn't)
- **What it is:** a model learned from each satellite's own telemetry and command history, of the form "current state + command → next state". JEPA-style is the candidate design. JPL's LSTM (Hundman et al. 2018 [RF 32]) is the published precedent and the baseline it has to beat.
- **Job 1, impact:** real attacks often use *legitimate* commands at the wrong time or scale. Viasat's attackers used legitimate management commands [RF 32]. The model has seen those command types in normal operations, so it can predict the damage for *each* satellite. For example, an old satellite with a weak battery, heading into eclipse, is hurt more by "heaters off" than a new one in sunlight.
- **Job 2, margin forecast:** battery and thermal margin at upcoming passes, so a suggested fix window is safe. The scheduler itself is plain software, not AI.
- **What it is not:** it doesn't predict what a patch (new code) will do (R6, Q31). It doesn't trace ground→space reach (the reach map does that). It isn't a fleet-monitoring product (Aerospace Corp + Google are building that [RF 32]; it also sits near the sibling topic "Spacecraft Mission Operations… telemetry analytics").
- **Why a world model and not rules or a classifier:** rules give every satellite the same answer. A classifier needs many labelled failures, which are rare. A world model learns normal behaviour from unlabelled data (Q31).
- **Honest limits (label them as hypotheses):** predicting harm from command sequences it has never seen (so extreme cases get checked in the manufacturer's simulator where one is provided, and "unknown" means high); the margin forecast; exploit likelihood learned on IT carrying over to space (R17).

### 2.3 The agent (A.1's "agentic" part)
- **Pattern:** one orchestrator agent working ReAct-style (reason → call a tool → observe → repeat), with these tools: parts list, reach map, EPSS/CVSS feed, SPARTA, world model, and the team's ticket system. The loop is perceive (advisory) → process (match, score, what-if) → decide (rank) → act (brief and ticket), as taught in S2–3.
- **Multi-step workflow, running alone:** new advisory → match → reach → scores → what-if per satellite → rank → a brief for each team in its own terms (security: *why*; flight software: *what*; ops: *when*) → tickets → re-rank on news or overrides.
- **Reliability patterns** (Parth Garg deck): step limits, structured and validated outputs, the layer-1/2 floor acting as a check on layer 3, and retry on failure.
- **After a human-approved fix:** it reads the result from the operator's existing tools and stores it in the record. It doesn't monitor satellites itself.

### 2.4 Data and onboarding (we never start with full data)
- Everything comes from the client: parts lists and software versions, the ground-to-fleet network map, and telemetry and command history. Where available, the manufacturer's data package is added. Most operators have no ready parts list (R14), so **forward-deployed engineers build it**, paid for by the onboarding fee.
- Until a fleet's world model is trained, layer 3 answers "unknown", so ranking stays **conservative** (high by default).
- **Shadow mode does three jobs at once:** it earns trust (rankings shown next to the team's own), gathers data, and trains the world model.
- Label as an assumption: operators keep telemetry and command archives.

### 2.5 Value grows with time in orbit (Q39, Q40)
The world model earns its keep by **telling satellites apart**.
- **From day one:** identical hardware and software don't mean identical conditions. Each satellite has its own orbit position, sun and eclipse pattern, radiation exposure and workload.
- **Over time:** the differences grow. Batteries wear, sensors drift, and software versions split during staggered updates. New satellites are tested on the ground before launch, but space adds conditions that ground tests can't reproduce.
- **The catch:** the model needs some operating history per satellite before it can use those differences (cold start). So its value is lowest just after launch and **grows the longer the fleet flies**. That growth is also a moat, because a later rival starts with less history (A.2).
- **Label as assumptions:** how soon the model can tell satellites apart is a **pilot metric**, not a promise. The "3 months to a year" guess and service lives are not sourced; say "years in orbit" and don't give a number.
- **Before that point**, value comes from reading at scale, speed, and ranking *across* flaws.

→ The first customers are fleets with some time in orbit, older or mixed.

### 2.6 Out of scope for Stage 1 (becomes later stages or viva material)
Writing patches (the manufacturer's job) · testing patches in an emulator · running rollouts or rollbacks (Spire and SpaceX already sell or build these) · fleet monitoring (Aerospace + Google) · ground-IT patching as a product (Tenable, Qualys) · terminals as a product area · the RL planner (dropped, Q32).

## 3. Running threads (Storytelling)
- **Driving question:** *"Which flaw first, and why?"* Every section answers part of it.
- **Thread 1: the way in and the legitimate commands.** Viasat: a misconfigured ground VPN appliance → legitimate management commands → ~30,000 terminals knocked offline, ~5,800 wind turbines losing remote monitoring [RF 4, RF 32]. It is the problem, what the world model plays out, and why ground systems count as the way in.
- **Thread 2: trust, earned in stages.** Experts rely less on automation (S11), so Periapt is a copilot, the human decides, and trust grows shadow → assist → delegate. That is also why the company grows in stages. Use S11 fully: *emotions* drive trust (the 2 a.m. fear becomes confidence), *satisfaction* means performance above expectations (which drives renewal), and *reliability and validity* come before trust.
- Each section ends with a one-line handoff. Honest weaknesses get at most **one line per section**. The real ones are gathered in the four-lens close, and the full list goes to Viva_Prep.

## 4. Section design (course anchor × grading target × content)

**Page budget:** opening + A.0 + A.1 ≈ 1¼ p · A.2 + A.3 ≈ 1 p · A.4 ≈ ¾ p · A.5 ≈ ¾ p · close + references ≈ ¼ p. Cutting happens after the full draft (user, 2026-09-30).

### Opening scene (~⅙ p) — Empathy (S11) → Storytelling
2 a.m. An advisory lands: a flaw in the ground mission-control software could let an attacker send commands to the fleet. The CISO of a mid-size operator has 200 satellites and no patch yet. Which satellites are most at risk *tonight*, and what can be done before the vendor ships a fix? Fiction, marked illustrative. The persona returns in A.4, and the scene is resolved in the close.

### A.0 Overview — Gartner 8-layer stack; Foundation Capital (domain-specific AI); B2B/B2G → Content + Creativity
- **Brand:** the name story. Mission: *"Tell every operator, within minutes of a new flaw, what it means for each satellite, with reasons they can check."* Vision: *"the trusted decision layer for every spacecraft operator"*, with the staged path (A.5/close) as the dream-big line.
- **Stack position:** Layer 7, **AI Security & Risk**, where the course deck places CrowdStrike. The closest course analogue is CrowdStrike's Charlotte AI, which helps analysts triage. It is *strategic/domain-specific AI* in Foundation Capital's terms. *Viva nuance:* Gartner's Layer 7 is strictly about securing AI (TRiSM). The course places cybersecurity vendors there, and Periapt is an AI application (Layer 6) delivering Layer-7 security outcomes, while applying Layer-7 protections to its own LLM.
- **Market:** 14,266 operational satellites at end-2025; 4,434 deployed in 2025 (+65%) [RF 1]. Say that growth is mostly mega-constellations; the target is the mid-size tier (R1).
- **Why ripe for AI (sourced "why now"):** CVEs 40,009 (2024) → 48,185 (2025) → 57,908 **YTD to 31 Aug 2026** [RF 27]; manual triage doesn't scale with that; attackers can use legitimate commands (Viasat); ML already forecasts exploitation for IT (EPSS [RF 32]), but nothing predicts impact on a specific satellite.
- **Topic fit, worded carefully:** "day zero" = the day a flaw becomes known, often before a patch exists. "Critical infrastructure" = infrastructure that critical sectors depend on: Viasat cut wind-turbine monitoring [RF 4]; the EU lists space as a high-criticality sector [RF 2]; the US doesn't list it as a CISA sector [RF 30]. Don't claim it is one.

### A.1 Agentic AI & Value — agent vs agentic AI (S2–3); ReAct; efficiency vs innovation (S3) → Content + Presentation (Visual 1)
- **Workflow:** triage, from advisory to a ranked, explained decision, across three teams (§2).
- **Role of AI:** the LLM agent (reading, matching, briefing, orchestrating) + the world model (impact per satellite, margin forecast). Everything else is reused.
- **Agentic, multi-step:** §2.3, with the autonomy boundary (runs alone up to the ranking; a human approves anything that touches a satellite).
- **Why teams want it (Q27, Q35):** coverage (every advisory × every satellite), memory (the record stays when staff leave), consistency (the same at 2 a.m.), translation between the teams. **Versus a general assistant:** it can't trace fleet reach or play out commands on a specific satellite, and pasting fleet data into public tools is *shadow AI* (S5).
- **Value case in three layers (Q29), no revenue:**
  1. *Value table:* **efficiency** (analyst hours per advisory; time from advisory to ranked decision; coverage) · **risk** (fewer critical flaws missed; evidence behind every approval; smallsat ~$0.5–1M as a tail risk only [RF 4]) · **innovation** (evidence packs for insurers and DoD audits, giving 800-171 3.14.1's "timely" a documented method [RF 30]).
  2. *Before/after* of the opening scene: steps from research, durations marked **illustrative**.
  3. *Proof = renewal* on pilot metrics (links to A.4).
- **Evaluation (R17), named as tests:**
  - world model vs JPL's LSTM on ESA-ADB: fewer false alarms at the same detection rate [RF 7, RF 32];
  - predicted vs actual telemetry after real commands, on held-out operator logs;
  - predicted vs physics-simulator impact on replayed attack scenarios (NOS3-style [RF 32]);
  - ranking agreement with the team and red-team results in shadow mode;
  - backtest on past advisories: time to decision.

  If the world model loses to the plain forecaster, only the model choice changes (Q33).
- **Visual 1:** the loop: advisory → three layers → ranked list → per-team briefs → human gate, with the authority rule shown.

### A.2 Moat & Defensibility — the rubric puts "Core Product Architecture" here; Morningstar's five moat sources + platformization (student deck); Foundation Capital "the model isn't the moat" → Content + Creativity
- **Core product architecture (features):** advisory reader · parts and reach map · score layer · world-model what-if · ranking with the authority rule · per-team briefs and tickets · the record. (Visual 1 is referenced here too.)
- **"Would Periapt survive if the model changed tomorrow?"** Yes. The moat is what each customer's use builds up, not the architecture.
- **Moats, ranked:**
  1. **Intangible asset: the record.** Every flaw, ranking, override (with its reason) and outcome, tied to each satellite's history. Nobody can buy it. Overrides count as learning signal (R11: spacecraft outcomes are rare).
  2. **Switching cost: earned trust.** A new vendor must rebuild the parts list and reach map, train its own model, and sit through its own shadow mode before experts trust it. *Honest limit:* the telemetry archive belongs to the customer and leaves with them, so the moat is the time and trust needed to rebuild, not the data.
  3. **Switching cost: workflow and integrations.** Tickets, parts lists, approvals and audit trail run through it (platformization, in a light form).
  4. **Efficient scale:** a niche too small for many players (turns R19 around).
  5. *Conditional:* a cross-fleet network effect, only through opt-in, SDA-style minimum-data sharing [RF 31, Q22]. Test pooled vs local on held-out pilot data first (R12).
- **Removed:** public data (it proves feasibility only [RF 7]) and manufacturer partnerships (no evidence, R13).
- **Honest line:** thin at cold start; it grows per customer; the product must work fully for a single operator.

### A.3 Five Forces — Porter (S7); niche strategy (Thiel); "competitors = anyone meeting the same need"; streetlight effect → Content + Presentation (Visual 2)
- **Strategic point:** *be the neutral commercial layer that builds on public tools (SPARTA, EPSS) and plugs into the operator's own.* Every force pushes toward integrating, not replacing.
- **Buyers: high.** Few and capable: Planet, Iridium, SES(+Intelsat), ICEYE [RF 11, 31], all running formal programs (SES 40+ staff; Spire ranks by ISO 27005). Globalstar is out (Amazon). Spire is the co-opetition case (operator, manufacturer and tooling vendor), not counted as a buyer (R15). Say "named mid-size operators", not "US buyers" (R19).
- **Suppliers:** parts lists and manufacturer data are **high** power (primes are consolidating [RF 12]). Telemetry is the customer's own. Public feeds (advisories, EPSS, SPARTA) and open-weight LLMs are **low**.
- **Rivalry: low for satellite-specific impact ranking; crowded for IT prioritisation** (Tenable, Qualys, Nucleus, with EPSS). Named adjacents:
  - **Aerospace Corp SPARTA/SPARTEND** (reference framework and on-orbit detection);
  - **Aerospace + Google** (agentic anomaly monitoring for proliferated-LEO constellations [RF 32]);
  - **CT Cubed IRON GALAXY** (assessments, training, cyber ranges [RF 32]);
  - Deloitte Silent Shield (detection);
  - Spire CMP (rollout).

  Caveat (streetlight effect): we searched where the light is, in public claims. Absence of claims isn't proof (R23).
- **Substitutes: high.** The good-enough stack: in-house team + ISO 27005 ranking + scanners with EPSS + SPARTA.
- **New entrants: high.** Google (already working with Aerospace), the primes, Booz Allen and Deloitte. **Aerospace Corp itself is a partner, not a rival:** under FAR 35.017 an FFRDC is not meant to use its privileged access to compete with the private sector [RF 32]. Periapt builds on SPARTA; Aerospace's testbed access for ISAC members (ASC-100 [RF 31]) is a validation route. Entry path: a commercial, unclassified, US-person team; a cleared partner later (R22).
- **Regulation cuts both ways:** there is no binding US mandate [RF 30]. 800-171 3.14.1 says "timely" with no prioritisation method, which makes DoD contractors the beachhead. S.3404 is out (R24).
- **Visual 2:** a compact table: force · rating · evidence · what Periapt does about it.

### A.4 Persona & Journey — 2–3-word label + psychographics (S8); Diffusion of Innovation; Lemon & Verhoef; Puntoni's four experiences (S9–10); Gartner "pilot trap" (S1) → Storytelling + Presentation (Visual 3)
- **Persona: "the Stretched Sentinel".** The CISO/VP Security at a US mid-size operator that also holds DoD contracts (R26), grounded in Planet's VP & CISO posting [RF 16].
  - Pains: advisory overload, audit pressure, being blamed for the one flaw that was missed.
  - Goals: defend the fleet, show auditors a method.
  - Decision criteria: evidence, auditability, never touches the command path, fits the tools the team already has.
  - Psychographic: an expert, and so sceptical of automation.
- **Buying committee (R27):** the CISO holds the budget; a SecOps analyst is the daily user and champion; the mission-ops lead approves anything that touches a satellite.
- **Diffusion:** early adopters are operators with formal programs, **fleets with time in orbit, older or mixed** (§2.5) and DoD contracts. The category is at the *introduction* stage of the product lifecycle (S7), which is why the journey starts with a pilot and early adopters.
- **Journey, built to escape the pilot trap** (Gartner: 80%+ of AI initiatives stall at pilot, S1):
  - *Prepurchase:* advisory overload plus an audit or incident trigger.
  - *Purchase:* paid pilot → **data capture** (Puntoni): forward-deployed engineers build the parts list, reach map and history (§2.4).
  - *Postpurchase:*
    - **classification**: shadow mode, with rankings next to the team's own, while the model trains;
    - **delegation**: low-impact flaws are auto-triaged and ticketed, and humans own the top of the list;
    - **social**: explanations and evidence packs for the board, the insurer and DoD auditors;
    - **renewal** on hours saved, time to decision and no critical flaw missed;
    - the loop repeats with new advisories and Stage 2.
- **Timeline (R28), labelled an assumption:** paid pilot → shadow mode ~1 quarter → assisted triage → renewal at 12 months.
- **Visual 3:** persona card + journey strip.

### A.5 Governance (US) — trust (competence, integrity, benevolence; zone of trust, S11); risk tiers, HITL, kill switch, audit log, drift, prompt injection, agent access, shadow AI (S5); NIST AI RMF → Content + Storytelling
- **Autonomy table (risk tiers):**
  - *Runs alone:* ingest, match, score, what-if, rank, brief, ticket, re-rank.
  - *Human, any time:* override a ranking; overrides are logged with a reason.
  - *Human approval required:* any action that touches a satellite or a ground system.
  - *Never automated:* changes to the command, boot or authentication path.
- **Stop / escalate rules:**
  1. no cited parts-list line → human;
  2. world model outside its data → "impact unknown", ranked high, flagged;
  3. conflicting advisories → escalate;
  4. the flaw touches command authentication or the boot path → top priority, handled by humans only;
  5. drift (predictions stop matching real telemetry) → layer 3 paused and ranking falls back to layers 1–2 until retrained.
- **Kill switch:** the operator can switch off layer 3 or the whole agent, and ranking falls back to layers 1–2.
- **Hallucination:** citation-required matching, deterministic confirmation, structured outputs only.
- **AI security:**
  - advisories are untrusted input (indirect prompt injection, S5);
  - **least privilege:** the agent can read telemetry and write tickets, and has **no route to command systems**.
- **Why never auto-act:** CrowdStrike 2024 (8.5M devices hit by one bad update; student moat deck): being embedded everywhere cuts both ways.
- **Monitoring and audit:** drift monitoring as satellites age (Zillow); NIST SP 800-53 AU-2/3/6 audit trail with at least weekly review (Cruise: missing logs cost a permit) [RF 24]; model cards; a periodic safety review that re-runs the A.1 tests.
- **Bias (S6), in this domain:** the model can favour satellites with rich data and under-rank ones with thin data. The rule "unknown = high" guards against that, and the safety review checks it.
- **Liability (Q25):** decision support with evidence and a stated residual risk, never "certified safe". Exposure is smaller than in v2 because Periapt ranks and humans act. Air Canada: companies are bound by their AI's words, so claims are worded carefully.
- **Jurisdiction (US):**
  - NIST AI RMF: Govern = ownership of overrides and approvals; Map = the rank-vs-act boundary; Measure = the tests in A.1 plus drift; Manage = stop rules and the kill switch [RF 19].
  - CCPA: Periapt is a service provider, handling mostly machine data; terminal data only as aggregate counts (which CCPA excludes) [RF 23].
  - FTC: fairness risk is low, but capability claims must not overstate (one line).
  - Sector rules: EAR 9A515 first, ITAR where it applies, deemed export → US-person access to customer data [RF 22]; 800-171 [RF 30].
- **Customer exit:** that fleet's model and data are deleted. This is simple because models are per fleet. Only the conditional pooled model has the unlearning limit (R33).
- **Trust close:** calibrated trust sits between over- and under-trust, and is earned in stages.

### Close: four-lens check (~⅙ p) → Storytelling + Content
- *Feasibility:* the world model's impact prediction is the one unproven piece, with named tests and a safe fallback (layers 1–2, "unknown = high").
- *Usability:* it fits existing tools and methods, and each team gets its own brief.
- *Desirability:* capable teams → a copilot, not a replacement; value grows with time in orbit.
- *Viability:* a per-fleet subscription plus an onboarding fee; people-heavy on purpose at the start; a small buyer pool; compliance (EAR/ITAR, CMMC) is part of viability (S1). **This is the weakest point.**

Then the **staged vision** (dream big): Stage 2 = fix-window planning + outcome tracking; Stage 3 = validation and rollout integration with partners (Spire-style tools, manufacturer emulators). Each stage starts only when the previous one has earned trust. *(India: on hold.)* End on the 2 a.m. scene resolved: by 2:10 the CISO has a ranked list with reasons, approves the first work-around, and goes back to sleep (illustrative).

### References (3–4 key, non-blog, approved)
1. SIA 29th State of the Satellite Industry **Report** (2026): cite the report, not the press release (R35).
2. NIST SP 800-171 Rev 2 (read directly, RF 30).
3. NIST AI RMF 1.0 (AI 100-1): check the PDF text before final (RF 19 flag).
4. Hundman et al., "Detecting Spacecraft Anomalies Using LSTMs and Nonparametric Dynamic Thresholding", ACM KDD 2018 [RF 32].

Course frameworks (Porter; Lemon & Verhoef 2016; Puntoni et al. 2021; Lee & See 2004; Pavlou & Fygenson 2006) are cited in-text.

### Appendix (1 page) → Creativity & Effort
1. **Working evidence:** two decision trees.
   - *Moat:* Q10 → Q13 → Q18 → Q22 → per-fleet model + record.
   - *Where the AI sits:* predict patch effects ✗ (R6) → judge test runs (commodity, Q33) → predict flaw impact ✓ (Q36).
2. **AI tools:** Claude Code (Opus) as the main assistant; Sonnet/Opus subagents for sourced research and a red-team review; verification discipline (§10.1 log, RF 32). ≥2 transcript links: redacted `logs/TRANSCRIPT_LOG.md` chunks on Google Drive (user task).
3. **Hardest concept (recommended):** *what the AI should actually predict.* The options were patch effect, judge, and flaw impact; say why flaw impact won. Alternative: defensibility (who owns the data). The user picks one.
4. **Accepted / modified / rejected / independently developed:** TB §11.2 + Q17–Q39. Raised independently by the user: regulation cuts both ways, public data isn't a moat, in-house teams, helping competitors, unit economics, undo = unreliable, scope drift away from AI (Q34), replacement vs assistance (Q35), topic fit (Q36), autonomy (Q37), the Aerospace complement (Q39).

## 5. Numbers and wording: use / avoid
- **Use:**
  - 14,266 satellites; 4,434 deployed in 2025 (+65%) [RF 1];
  - CVEs 40,009 / 48,185 / 57,908 **YTD** [RF 27];
  - Viasat: *misconfigured* VPN appliance, *legitimate* commands, ~30,000 modems shipped, ~5,800 turbines, "no material impact" [RF 4, 32];
  - SES 40+ staff; 800-171 3.14.1 exact text;
  - smallsat ~$0.5–1M (secondary, tail risk only);
  - EPSS = probability of exploitation in the next 30 days [RF 32].
- **Avoid:**
  - ~16–17k satellites; ~58k CVEs/yr; any Starlink %; "3-person team"; "40% since 2000";
  - "fully tested", "certified safe", "legally required to patch", "nobody validates patches";
  - any revenue/ACV figure;
  - "Viasat was an unpatched flaw"; "satellites are US critical infrastructure";
  - "nobody simulates attacks on satellites" (NOS3 research exists);
  - "Terrain Trace / CT Cubed AI risk assessment"; SBIR; S.3404;
  - "predicts what a patch will do".
- **Also avoid:** "tools can't tell which satellites have a flaw" (they can, for listed CVEs); "FFRDCs are banned from commercial work"; any satellite service-life number; "the telemetry data is our moat".
- **Label as hypotheses:** how soon the model can tell satellites apart (a pilot metric); impact prediction for command sequences never seen; the margin forecast; IT → space exploit transfer; operators keep telemetry and command archives; satellites drift apart as they age; bus-type libraries reused across customers lower onboarding cost.

## 6. Review coverage matrix

"Fixed" = the draft changes the claim. "Caveat" = the claim stays with its limit stated. "Avoid" = kept out. "Cut" = out of Stage 1 scope.

| Item | Issue (short) | Handling in v3 | Where |
|---|---|---|---|
| K1 | No binding US mandate | Fixed: pitch on operational risk; 800-171 beachhead | A.3, A.5 |
| K2 | Public data ≠ moat | Fixed: feasibility only | A.2 |
| K3 | Static vs live is the wrong axis | Fixed: build on SPARTA; complement Aerospace | A.3 |
| K4 | Operators do it in-house | Fixed: fills in their own likelihood × impact method | §2.1, A.3 |
| K5 | Why share with rivals | Fixed: network effect conditional | A.2 |
| R1 | Growth is mega-constellations | Caveat: target mid-size | A.0 |
| R2 | Satellite numbers | Avoid: SIA 14,266 only | A.0 |
| R3 | Viasat "immaterial" | Fixed: used for the method (way in + legitimate commands), not dollars | Threads, A.0 |
| R4 | No brick base rate | Fixed: triage speed leads; loss is a tail risk | A.1 |
| R5 | Viasat supports the commodity layer | Fixed: generic tools don't know the way in reaches the fleet, or what the commands would do | §2.1 |
| R6 | World model can't predict new code | **Dissolved:** it predicts flaw impact from known commands; patches out of scope | §2.2 |
| R7 | Auto-rollback exists | Cut: rollout/rollback out of Stage 1 | §2.6 |
| R8 | RL vs solver | Cut: no RL; plain scheduler + forecast | §2.2 |
| R9 | Where does the agent act? | Fixed: autonomy table | A.5 |
| R10 | CVE arithmetic | Fixed: YTD stated | A.0 |
| R11 | Outcome labels rare | Caveat: world model learns unlabelled normal data; overrides count as signal | A.2 |
| R12 | DP erodes pooled model | Caveat: pooled vs local test | A.2 |
| R13 | Manufacturer moat unevidenced | Fixed: removed; supplier power | A.2, A.3 |
| R14 | No SBOMs | Fixed: forward-deployed engineers build them; onboarding fee | §2.4, A.4 |
| R15 | Spire triple role | Fixed: co-opetition, not a buyer | A.3 |
| R16 | Export control | Fixed: EAR first; deemed export | A.5 |
| R17 | No evaluation | Fixed: five named tests | A.1 |
| R18 | Supplier power from the wrong side | Fixed: Periapt's own inputs | A.3 |
| R19 | Buyer pool tiny | Caveat: named operators; efficient scale; staged growth | A.2, A.3 |
| R20 | No unit economics | Reframed: value case + pricing structure; people-heavy on purpose; weakest point | A.1, close |
| R21 | SpaceX evidence secondary | Avoid in the report (rollout cut); viva only | — |
| R22 | Barriers hit the startup first | Fixed: entry path | A.3 |
| R23 | Originality caveats | Caveat: streetlight effect | A.3 |
| R24 | S.3404 | Avoid | — |
| R25 | SBIR contradiction | Held (user); out of the text | — |
| R26 | Three first customers | Fixed: one actor | A.4 |
| R27 | Buyer ≠ approver ≠ user | Fixed: buying committee | A.4 |
| R28 | No sales cycle | Fixed: labelled timeline | A.4 |
| R29 | Liability | Fixed: decision support; smaller exposure | A.5 |
| R30 | No stop rules | Fixed: 5 rules + kill switch | A.5 |
| R31 | LLM hosting + hallucination | Fixed: self-hosted, citation-required | §2.1, A.5 |
| R32 | FTC + CCPA | Fixed: machine data; aggregate counts; FTC line | A.5 |
| R33 | Unlearning on exit | Fixed: per-fleet model deleted; pooled limit stated | A.5 |
| R34 | 40% stat | Avoid | — |
| R35 | Reference flags | Fixed: new list; SIA report + AI RMF PDF checks are user tasks | Refs |
| RF 32 | Viasat wording; EPSS; Aerospace+Google; CT Cubed; NOS3; critical infrastructure; FAR 35.017 | Fixed as listed in §5 and A.3 | A.0, A.3, §5 |

## 7. Output files
- `report/Periapt_Report_Draft.md`: the draft, with source tags.
- Visuals at the conversion step (loop diagram, Five Forces table, persona + journey strip).

## 8. Out of scope for this draft
New research, final formatting, the .docx build, stripping tags, and the user's voice rewrite.

## 9. Open items (user)
- India line: on hold. SBIR: held with it.
- Before final: check the NIST AI RMF PDF text and cite the SIA report itself (R35).
- Choose the appendix's hardest concept (recommended: what the AI should predict).
- Transcript links on Google Drive.

## 10. v3 changes (from Q31–Q39)
1. **Core:** predictive prioritisation, delivered as a copilot; fixing kept out of Stage 1 (Q34–Q36).
2. **World model:** predicts each flaw's impact per satellite + margin forecast; no longer judges patches (Q31, Q33, Q36).
3. **Planner:** RL dropped; plain scheduler fed by the forecast (Q32).
4. **Layers + authority rule:** existing tools for facts and scores; AI only for impact; the AI can raise, not silently lower (Q35, approved).
5. **Autonomy:** runs alone up to the ranking; on/in-the-loop split (Q37).
6. **Aerospace Corp:** complement, not rival (FAR 35.017); Google and the primes are the real entrants (Q39).
7. **Honest scope notes:** onboarding builds the data; people-heavy on purpose; value highest for older/mixed fleets; staged growth (Q39).
8. **Architecture moved to A.2** (rubric placement); **3 visuals**; course hooks added (pilot trap, CrowdStrike 2024, intangible assets, shadow AI, least privilege, Cruise, S11 emotions/satisfaction, Viability incl. compliance, Layer 7 like Charlotte AI).
9. **Corrections (RF 32):** Viasat wording, EPSS as input, Aerospace + Google adjacent, CT Cubed wording, critical-infrastructure wording.
10. **References:** SIA report, 800-171, NIST AI RMF, Hundman 2018.
11. **Q40 fixes:** the problem statement no longer says matching is manual (tools exist); value grows with time in orbit; the moat is the record + earned trust (the telemetry archive belongs to the customer); softer FAR 35.017 wording; bias line (S6); periodic safety review; product lifecycle (S7); Layer 6/7 nuance.
