# Phylax — Viva Prep

Compiled 2026-09-30 from every challenge in `topic/Topic_Brainstorm_Report.md` §4 (Q1–Q29) and every grader question in `research/Research_Findings_Review.md` (K1–K5, R1–R35).

**How to use it:** say the answers in your own words, not verbatim. Each answer is short enough to say in about 20 seconds. Tags point to the evidence: `[RF n]` = research finding, `[Q n]` = challenge log, `[R n]` = review item. A **conceded** point is a strength. The viva checks that you understand your work, and naming a known limit shows that.

---

## 0. The 30-second pitch

Satellite operators carry known flaws across ground stations, networks, radio links, spacecraft and user terminals. Fixing one safely today means a slow handoff: security finds it, flight software or the manufacturer patches it, mission ops fits it into a pass window, and someone decides whether it's safe. **Phylax is a domain copilot that owns that workflow.** It checks whether a flaw actually reaches the fleet, drafts a ranked fix plan that respects passes and power, has the manufacturer's emulator run the fix while our world model judges the result, then watches the canary and halts if anything drifts. **Humans approve every uplink.** We make expert teams faster. We don't replace them.

## 1. Numbers you may be asked for (and ones to never say)

| Say | Source |
|---|---|
| 14,266 operational satellites (end-2025); 4,434 deployed in 2025 (+65%) | SIA 2026 [RF 1] |
| CVEs: 40,009 (2024) → 48,185 (2025, +20.6%) → 57,908 by 31 Aug 2026 (**year to date**) | [RF 27, R10] |
| Viasat KA-SAT 2022: ~30,000 modems replaced, ~5,800 wind turbines lost remote monitoring; entry via a ground VPN flaw; **Viasat's 10-K called it financially immaterial** | [RF 4] |
| SES: "over 40" security professionals | SES AR 2025 [RF 31] |
| NIST SP 800-171 3.14.1: "Identify, report, and correct system flaws in a timely manner" | [RF 30] |
| Smallsat ~$0.5–1M (secondary, CubeSat-class); GEO ~$300M | [RF 4] |

**Never say:** "~16,000 satellites", "58,000 CVEs a year", a Starlink percentage, "a 3-person team manages 300 satellites" (no source exists), "40% of CubeSats since 2000", "fully tested", "operators are legally required to patch", "nobody validates patches", any revenue or ACV figure.

---

## 2. Overview & originality

**"Is this an existing company?"** No. The closest adjacents are named in the report: **Aerospace Corp's SPARTA/SPARTEND** (a reference framework plus on-orbit detection) and **CT Cubed's IRON GALAXY** (a training cyber range). Neither decides per operator, validates fixes in a testbed, or schedules rollouts [RF 10/13]. *Conceded:* absence of public claims isn't proof of absence. We couldn't query Crunchbase, and stealth or classified programmes can't be seen [R23, Q5].

**"Why satellites inside 'Day-Zero Vulnerability Prioritisation'?"** Generic vulnerability management fails the "no existing company" rule. Novelty comes from the intersection with an unserved setting [Q3–Q4].

**"Your growth numbers are Starlink's."** True. Growth is driven by mega-constellations. Our target is the mid-size tier, and the relevant trend is fleets becoming software-defined and patchable [R1].

## 3. Agentic AI & value

**"What does the AI actually do? Remove it: what breaks?"** Four jobs: (1) an LLM agent reads advisories and proposes component matches, with deterministic SBOM matching confirming them; (2) an exposure graph with learned scoring decides whether a ground flaw reaches the fleet; (3) a planner orders the rollout; (4) a world model judges emulator and canary runs against normal behaviour. Remove the AI and you're back to the manual handoff chain [Q6, Q26].

**"Scoring and monitoring already exist (Deloitte, scanners). What's new?"** *Conceded:* each piece exists. Silent Shield detects attacks in progress, scanners score IT flaws, and Spire's platform monitors health and rolls out updates. What's new is the **flow from a known flaw to a safe, scheduled fix across the whole mission**. Detection handles attacks in progress. We handle flaws *before* exploitation [Q7, Q26].

**"How does a model trained on past telemetry know what new flight code will do?"** It doesn't, and we don't claim it does. The manufacturer's emulator **runs** the new code, as ESA's OBSM process does. The world model **judges** the run, comparing its telemetry, then the canary satellite's, with how that satellite normally behaves [R6, Q26].

**"Why RL instead of a constraint solver?"** A solver guarantees hard constraints: pass windows, power, staged rollout. The learned part only improves the *order* of rollouts from past outcomes. Pure RL inside a learned model tends to exploit the model's errors [R8]. *(If the final report keeps the original "constrained RL planner", defend it as RL for ordering under uncertainty, and name model exploitation as the risk.)*

**"The teams already do this. Why pay you?"** We take on what doesn't scale with people: **coverage** (every channel, satellite and pass), **memory** (outcomes stay when staff leave), **consistency** (the same at 2 a.m., which counters automation bias), and **joining the pieces** across four groups. The team still decides [Q27, Q20–Q21].

**"Why not just use ChatGPT/Claude?"** A general assistant can't trace ground→fleet reachability, plan around passes and power, or judge emulator telemetry against a specific satellite's normal behaviour [Q27].

**"Viasat said the attack was immaterial. Why would anyone pay?"** We don't use Viasat as a dollar loss. We use it for the **path** (a ground VPN flaw reached tens of thousands of terminals) and the **scale of disruption**. Our value leads with triage speed and coverage. A bricked satellite is a tail risk, and SpaceX reports zero losses from its updates (a secondary source) [R3, R4, R5].

**"Spire already sells automated rollout and rollback. What's left that's yours?"** Prioritisation and cross-domain decisions: which flaw, whether it reaches the fleet, which fix, in what order. We hand the approved plan to the operator's existing update manager rather than replacing it [R7, RF 31].

**"How would a customer know your ranking beats their analyst's?"** Pilot metrics: analyst hours per finding at equal coverage, time from advisory to approved plan, agreement with red-team results in the testbed, and a backtest against past Space ISAC advisories. *Conceded:* transferring exploitability learned on the ground to space is an open validation risk [R17].

**"How do you show value without revenue?"** Three layers: a value table (efficiency, risk reduction, innovation), a before/after of the 2 a.m. scene, and renewal triggered by measured pilot metrics. The innovation value is assurance evidence for insurers and defence contracts [Q29].

**"What's your revenue / ACV?"** ACV means annual contract value, what one customer pays per year. We deliberately don't print a figure. The rubric asks for value to the customer. Pricing is a per-fleet subscription plus a one-time onboarding fee that pays for integration work. *Conceded:* viability is our weakest point: a small buyer pool and people-heavy delivery [Q24, Q29, R20].

**"Isn't compute your big cost?"** No. Telemetry is small time-series data, and inference is event-driven (a handful of decisions a week per operator). The big cost is people: integration per customer, cleared domain engineers, testbeds per satellite bus, and compliance [Q24].

## 4. Moat

**"What makes you hard to copy?"** Ranked: (1) the **context graph**, a record of every decision, approval and outcome, which can't be bought; (2) **switching costs**, since approvals, audit trail and integrations run through us; (3) **efficient scale**, since the niche is too small for many players. A cross-fleet network effect is a *conditional* bonus [Q18, Q22].

**"Public data proves your model works. So can't anyone copy it?"** Yes. Public data proves *feasibility*, for us and for competitors. That's why it isn't in our moat [Q18, K2].

**"Why would operators help competitors by feeding a shared model?"** Mostly they won't. Operators share only anonymised alerts (Space ISAC) or minimum orbit data through a neutral party (Space Data Association). Nobody pools security telemetry [RF 31]. So the product must work fully for one operator. Sharing is an opt-in bonus on the SDA model, tested by comparing pooled and local models in pilots [Q22, R12].

**"How much outcome data will you actually get?"** *Conceded:* spacecraft patch outcomes are rare and mostly successful. We count any post-update anomaly plus ground-segment patch outcomes, which are far more frequent, and we state that space-side volume is unmeasured [R11].

**"Manufacturers as an early moat?"** Dropped. There's no evidence they resell security tools, and the primes that own them are likely entrants [R13].

**"If a customer leaves, can you delete what the model learned from them?"** Their local data and adapters are deleted. Past contributions to a shared model can't be removed selectively, so we retrain periodically from the retained contributions. The limitation is stated [R33].

## 5. Porter's Five Forces

**The strategic point:** every force pushes Phylax to be **the neutral layer that integrates with what operators already have**, not a replacement.

- **Buyers: high.** A few capable operators (Planet, Iridium, SES+Intelsat, ICEYE), all with formal in-house programs [RF 11, 31]. "Name your first ten customers" → we name the few in range honestly, then the widening segments [R19].
- **Suppliers: high (our inputs).** Manufacturers' SBOMs, emulators and patches, from firms consolidating under the primes. Their incentive to cooperate: lower support and warranty cost, and customers asking for SBOM feeds [R18].
- **"Is Spire your customer or your competitor?"** Both, plus a supplier. It's our co-opetition case, a rollout partner, and not counted as a buyer [R15].
- **Rivalry: low on the whole loop.** SPARTA, IRON GALAXY, Silent Shield and Spire CMP are each partial [RF 10/13].
- **Substitutes: high.** The "good-enough stack": in-house program + SPARTA + vendor patches + rollout tooling, or doing nothing [Q20].
- **New entrants: high threat.** Primes, Booz Allen, Deloitte. "If entry is this hard, how do *you* get in?" → a commercial, unclassified, US-person team first, then a cleared partner for government work. The barriers only protect us once we're past them [R22].
- **"Doesn't regulation force customers to buy?"** No. There's no binding US vulnerability-management mandate for commercial operators. Only narrow hooks exist (an FCC access-control duty, NOAA encryption, DoD 800-171 for systems handling controlled information). Regulation cuts both ways [Q17, RF 30]. S.3404 is unenacted and voluntary, so it's a policy-attention signal, not a tailwind [R24].

## 6. Persona & journey

**"Who is your first customer?"** One actor: a US mid-size operator that also holds DoD contracts. Its CISO is "the Stretched Sentinel", an expert and therefore sceptical of automation. The 800-171 duty pays for the ground-IT module, and the space core is the upsell [R26].

**"Does the CISO even control spacecraft uplinks?"** No, which is why there's a buying committee: the CISO holds the budget, the mission-ops lead approves, and a SecOps engineer champions the product [R27].

**"What does the agent do alone at full maturity? What if nobody approves before the pass closes?"** Alone: ingest, map, score, draft plans, ground-side tickets, monitoring and auto-halt. Human approval: ground-change execution and every uplink. Fix plans can be pre-approved ahead of the window. **If no approval arrives, the default is hold** [R9].

**"How long to first revenue?"** A labelled assumption: paid pilot → shadow mode (about a quarter) → guarded ground automation → uplink-assist → renewal at 12 months [R28]. SBIR only "if authority is current", because the research contradicts itself on its status [R25].

**"Where does the SBOM come from?"** Onboarding builds the inventory from the manufacturer's data package, the operator's configuration and analysis. It's a cost-to-serve, covered by the onboarding fee [R14].

## 7. Governance (US)

**"Your model says safe, the operator approves, the satellite dies. Who pays?"** We never claim "certified safe". The output is **decision support with evidence and a stated residual risk**. The manufacturer warrants its own patch, the operator approves, liability is capped by contract, and the audit trail is the evidence. The Air Canada case shows companies are bound by their AI's output, so our claims are worded carefully [Q25, R29].

**"If you ever need undo, aren't you unreliable?"** No safety-critical industry claims complete testing. Reliability means failures that are rare, caught at the canary and recoverable, and operators already run canary and rollback pipelines (Planet, Spire). *Your sharper point, conceded:* a patch that breaks the command receiver can't be undone from the ground. So those changes are **never automated**, and an A/B partition plus watchdog fallback is a precondition [Q25].

**"Give me one rule under which the AI halts."** Any of: the anomaly score rises above the threshold after the canary; telemetry is lost after uplink; confidence falls below a floor; the flaw touches the command-authentication path (human-only); advisories conflict (escalate) [R30].

**"What stops the LLM from inventing a component match? Who sees the data?"** The model is self-hosted and open-weights, inside the US boundary. Matches must cite an SBOM line, deterministic matching confirms them, and anything unmatched goes to a human. Advisories are treated as untrusted input to guard against indirect prompt injection [R31].

**"Are your model weights export-controlled?"** *Open, and stated as open.* Most commercial satellites fall under EAR 9A515 (ITAR only where it applies). The federated pool is limited to US and licence-exempt allies (AUS/CAN/UK) [R16].

**"What does the FTC have to do with you?"** Fairness risk is low, because decisions concern machines, not people. But AI capability claims in marketing must not overstate. Under CCPA we're a service provider, and terminal location data is minimised [R32, RF 23].

**"NIST AI RMF?"** Govern = human approval and ownership of escalation. Map = the boundary between recommending and executing. Measure = drift, reliability and hallucination checks. Manage = stop rules and incident response [RF 19].

## 8. Process & ownership (appendix questions)

**"What was the hardest concept?"** Defensibility: who owns the data, and why operators would share it. The options, in the order tried: a federated network effect → rare events (retracted: too rare) → public data (only proves feasibility) → manufacturer partnerships (no evidence) → **the outcome record plus switching costs**, chosen because it needs no one's cooperation [Q10–Q13, Q18, Q22].

**"What did you reject or change after using AI?"** My own challenges changed the design:
- regulation isn't a guarantee [Q17];
- public data isn't a moat [Q18];
- operators already do this in-house [Q20];
- they won't help competitors [Q22];
- the unit economics don't close at SaaS rates [Q24];
- "undo" needs rethinking [Q25];
- detection alone isn't new [Q26];
- the product should help researchers, not replace them [Q27];
- no revenue figure [Q29].

I also rejected the unsourced "3-person team" claim and the stale numbers after verification [Q20, §10.1].

**"Which AI tools, for what?"** Claude Code (Opus) as the thinking partner; Sonnet and Opus subagents for sourced research and a red-team review of our own findings (35 weaknesses found). Every number was checked against a source before use.

**"Did you read your own references?"** Before submission: NIST SP 800-171 was read directly. SPD-5 is quoted from the Federal Register. NIST IR 8270's control text must be checked in the PDF, and the SIA reference must cite the report itself, not the press release. *(Complete these checks before you say yes.)* [R35]

**"Why this topic, if the research kept finding problems?"** Everything that failed was an **overclaim**, not the core idea. What survived has evidence: no one claims the whole loop, and the ground-to-space path is real (Viasat) [Q23].
