# Periapt — Viva Prep

Compiled 2026-09-30 from every challenge in `topic/Topic_Brainstorm_Report.md` §4 (Q1–Q29) and every grader question in `research/Research_Findings_Review.md` (K1–K5, R1–R35).

**How to use it:** say the answers in your own words, not verbatim. Each answer is short enough to say in about 20 seconds. Tags point to the evidence: `[RF n]` = research finding, `[Q n]` = challenge log, `[R n]` = review item. A **conceded** point is a strength. The viva checks that you understand your work, and naming a known limit shows that.

---

## 0. The 30-second pitch

Satellite operators carry known flaws across ground stations, networks, radio links, spacecraft and user terminals. Fixing one safely today means a slow handoff: security finds it, flight software or the manufacturer patches it, mission ops fits it into a pass window, and someone decides whether it's safe. **Periapt is a domain copilot that owns that workflow.** It checks whether a flaw actually reaches the fleet, drafts a ranked fix plan that respects passes and power, has the manufacturer's emulator run the fix while our world model judges the result, then watches the canary and halts if anything drifts. **Humans approve every uplink.** We make expert teams faster. We don't replace them.

## 1. Numbers you may be asked for (and ones to never say)

| Say | Source |
|---|---|
| 14,266 operational satellites (end-2025); 4,434 deployed in 2025 (+65%) | SIA 2026 [RF 1] |
| CVEs: 40,009 (2024) → 48,185 (2025, +20.6%) → 57,908 by 31 Aug 2026 (**year to date**) | [RF 27, R10] |
| Viasat KA-SAT 2022: ~30,000 modems shipped, ~5,800 wind turbines lost remote monitoring; entry via a **misconfigured** ground VPN appliance (not an unpatched flaw), then *legitimate* management commands wiped modem flash; the satellite was never touched; **Viasat's 10-K called it financially immaterial** | [RF 4] |
| SES: "over 40" security professionals | SES AR 2025 [RF 31] |
| NIST SP 800-171 3.14.1: "Identify, report, and correct system flaws in a timely manner" | [RF 30] |
| Smallsat ~$0.5–1M (secondary, CubeSat-class); GEO ~$300M | [RF 4] |

**Never say:** "~16,000 satellites", "58,000 CVEs a year", a Starlink percentage, "a 3-person team manages 300 satellites" (no source exists), "40% of CubeSats since 2000", "fully tested", "operators are legally required to patch", "nobody validates patches", any revenue or ACV figure.

---

## 2. Overview & originality

**"Is Periapt an existing company?"** No. We first called it Phylax, then found an EU firm, Phylax Intelligence, selling AI situational awareness for physical threats to critical infrastructure (a different product, same name). We also rejected Amyntor, used by two Indian cybersecurity firms. A deep web check found no security or space company named Periapt, only unrelated uses such as audio cables and a health app [Q30]. *Name story:* a periapt is a protective amulet, and the word echoes *periapsis*, an orbit's closest point: "protection at the closest point of risk."

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

**"Viasat said the attack was immaterial. Why would anyone pay?"** We don't use Viasat as a dollar loss. We use it for the **path** (a misconfigured ground VPN appliance let the attacker send legitimate commands to tens of thousands of terminals) and the **scale of disruption**. Our value leads with triage speed and coverage. A bricked satellite is a tail risk, and SpaceX reports zero losses from its updates (a secondary source) [R3, R4, R5].

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

**The strategic point:** every force pushes Periapt to be **the neutral layer that integrates with what operators already have**, not a replacement.

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

---

## 9. Re-centring (Q31–Q38): the current concept

*Added 2026-09-30 evening. This supersedes the older answers above wherever they differ, especially on the world model, the planner and the scope. Sections 3–5 get rebuilt when spec v3 is written, and cut material moves here.*

**The concept in one breath:** Periapt watches new security advisories around the clock. For every flaw it finds which satellites have it, whether an attacker could reach them, how likely an attack is, and what the attack would actually do to each satellite. It ranks the flaws, says why, and briefs each team in its own terms. Humans can override any ranking. Nothing touches a satellite without a human's approval.

**"What does the AI actually do?"** Two things. An **LLM agent** reads advisories and matches them to each satellite's parts list, citing the line it matched. A **world model**, learned from each satellite's own telemetry and command history, plays out "what if an attacker sent these commands?" to predict the damage per satellite. Everything else (CVSS, EPSS, SPARTA IDs, reach checks) is existing software that we use, not rebuild [Q35, Q36].

**"Why a world model and not rules or a classifier?"** Rules give every satellite the same answer, but the same flaw hurts an old satellite with a weak battery more than a new one. A classifier needs many labelled failures, and those are rare. A world model learns normal behaviour from unlabelled data [Q31].

**"Can it predict an attack it has never seen?"** Partly, and I say so. Real attacks often use *legitimate* commands at the wrong time or scale: Viasat's attackers used legitimate management commands [RF 32]. The model has seen those command types. For extreme cases outside its data, we lean on the manufacturer's physics simulator, and "unknown" is treated as **high** priority, never low [Q36, Q38].

**"Isn't EPSS already doing this?"** EPSS predicts *whether* a flaw will be exploited, for ordinary IT. It says nothing about what the flaw does to a specific satellite. We use EPSS as an input [RF 32].

**"Isn't this just replacing your analysts?"** No. The analysts still decide. The AI does the reading, cross-checking and "what-if" work that doesn't scale with people, and it plugs into their existing ranking method (Spire, for example, ranks by ISO 27005 likelihood × impact). It fills in that method with evidence rather than replacing it [Q35, RF 31].

**"Is it autonomous if humans approve things?"** Yes. Scanning, scoring and ranking run on their own around the clock, because they only produce information. Humans supervise and can override ("on the loop"). The only hard stop is before anything touches a satellite ("in the loop") [Q37].

**"Isn't this Spacecraft Mission Operations (telemetry analytics), not vulnerability prioritisation?"** No. The world model's output is a **security ranking**: which flaw to fix first and why. We deliberately don't sell fleet monitoring. Aerospace Corp and Google are building that [Q36, RF 32].

**"Aerospace Corp has SPARTA and an AI anomaly tool with Google. Why won't they build this?"** Aerospace is an FFRDC. Federal rules (FAR 35.017) say an FFRDC should not use its privileged access to compete with the private sector. They publish frameworks like SPARTA and build prototypes for government. We build on SPARTA and speak its IDs, so we complement them. The real threat is the commercial side: their partner Google, the primes, Booz Allen and Deloitte [Q39, RF 32].

**"Viasat was a misconfiguration, not an unpatched flaw. Why use it?"** Correct, and I say so. I use it for the path and the method: getting in on the ground, then using legitimate commands to harm tens of thousands of terminals. That is exactly the kind of harm our world model plays out [RF 32].

**"Is this really 'day zero'?"** Day zero is the day a flaw becomes known, often before a patch exists. That is when our clock starts: rank it, explain it, and suggest a safe work-around until a patch arrives. The listed topic itself says "unpatched security flaws" [Q36].

**"Satellites aren't a US critical-infrastructure sector."** True: they aren't one of CISA's 16 [RF 30]. They are infrastructure that critical sectors depend on. Viasat's outage cut remote monitoring of ~5,800 wind turbines [RF 4], and the EU lists space as a high-criticality sector [RF 2].

**"How do you prove the world model beats a simple forecaster?"** With a test that can fail: fewer false alarms than JPL's published LSTM forecaster (Hundman et al. 2018) at the same detection rate, on ESA's public anomaly benchmark (ESA-ADB). If it loses, only the choice of model changes. The product works the same with the forecaster inside [Q33, RF 7, RF 32].

**"Why no RL planner any more?"** The review showed RL would learn from rollout outcomes that are rare and mostly successes. Once we focused on prioritisation, the planner shrank to a suggested fix window: a plain scheduler fed by the world model's battery and thermal forecast [Q32, Q34].

**"What did you cut, and why?"** Writing patches (the manufacturer's job). Running rollouts and rollbacks (Spire and SpaceX already sell or build them). Fleet monitoring (Aerospace Corp + Google). Ground-IT patching as a product (Tenable, Qualys). Terminals as a separate product area. The RL planner. Every cut was either already sold by someone else or not part of the original problem [Q34].

**"Does it work for a brand-new fleet?"** Partly at first, and better over time. Identical hardware doesn't mean identical conditions: each satellite has its own orbit position, eclipses, radiation and workload, and the differences grow as batteries and sensors age. But the model needs some operating history per satellite first. So the value grows the longer the fleet flies, and how fast is something we measure in the pilot, not a promise. Until then, we still help with reading, speed and ranking across flaws [Q39, Q40].

**"Isn't this just a scanner? Tools already match CVEs to software."** Yes, they do, and we use them. What they don't do is judge what a flaw means for each satellite: space advisories that aren't CVE entries, missing spacecraft parts lists, whether a ground flaw reaches the fleet, and what an attack would actually do [Q40].

**"The customer owns the telemetry. How is that a moat?"** It isn't; the data leaves with them. The moat is the record (every decision, override and outcome) and the time and trust a new vendor needs to rebuild everything and pass its own shadow mode with sceptical experts [Q40].

**"Isn't people-heavy a bad business?"** It's a cost, and I name viability as the weakest point. But it's deliberate: experts don't trust new automation, so trust has to be earned in shadow mode first. It gets cheaper per customer if the parts library for a satellite design can be reused, which is a hypothesis [Q39].

**"Where does your data come from on day one?"** From the client, at onboarding: parts lists, software versions, the ground-to-fleet network map, and telemetry and command history. Until the model is trained, it says "unknown", so rankings stay high by default. Shadow mode builds trust and trains the model at the same time [Q39].

**"Why not build the whole patch pipeline?"** Stage 1 has to earn trust first. Once the rankings are trusted, we add fix-window planning, then validation and rollout with partners. Think big, act small [Q39].

**"Is Periapt really Gartner Layer 7?"** Strictly, no. Layer 7 is about securing AI (guardrails, TRiSM). Periapt is a Layer 6 AI app that delivers security outcomes, the layer where the course lists CrowdStrike, and it applies Layer 7 guardrails to its own LLM [Q41].

**"How big is the market?"** No official number exists for this niche, so I estimate it by counting satellites: the named mid-size buyers fly about 430–450 satellites across 5 operators (public tracker, RF 11). It's small, and I say so. I don't give a dollar figure because I have no sourced price per customer [Q41, Q29].

**"If the satellites are identical and new, why rank them differently?"** Because their conditions aren't identical: sun, eclipse, radiation and workload differ from day one. The model still needs some history per satellite to use that, which is a pilot metric [Q41, Q40].

**"Is it really agentic if it only writes briefs and tickets?"** *(prepare this one)* Yes. It does the whole multi-step job on its own: read the advisory, match it, trace reach, pull scores, play out the attacker's commands per satellite, rank, brief each team, and re-rank when news or an override arrives. Stopping before anything touches a satellite is a deliberate trust choice, not a missing ability: experts rely less on automation (Sanchez et al., 2011), and one bad automatic action could hurt a whole fleet (CrowdStrike 2024). Autonomy grows in stages as trust is earned [Q37, Q42].

**"After you hand over the ranking, why not test the team's fix too?"** Because the teams already do that well: Planet tests on the ground, then in orbit, then rolls out; Spire has an update manager with rollbacks and a testbed. Also, our model learns from normal commands and can't predict new code. What we give back after the handoff is a safe fix window, the outcome stored in the record, and a re-ranked list. Fix planning and outcome tracking come in Stage 2, once trust is earned [Q42, RF 31].

**"Is your $85K–120K figure real?"** It's a rough starting estimate per operator, and I say so: 20 advisories × 3 hours × half handled alone = 30 hours a week, about 0.75 of an analyst. Only the salary range is sourced, and it's general-industry. The pilot measures the real numbers [Q42, RF 5].

**"If the customer leaves, don't they take everything?"** They take their data: telemetry, command history and the record. They don't take the working system. The base model and software are ours; their fleet layer is licensed during the subscription and deleted on exit. A rival, or their own team, has to rebuild the models and integrations and win their experts' trust again [Q43].

**"The model was trained on their data. What if a big customer demands it?"** It's a common fight in AI contracts, and I can't promise we'd always win it. Three hedges: the contract (data theirs, model ours); the design (the fleet layer is a thin add-on that doesn't work without our base, which never sees customer data); and time (a frozen copy goes stale as satellites age). I don't claim nobody could ever build better; a rich operator could [Q43].

**"Your market is tiny. Then what?"** Efficient scale cuts both ways: few rivals bother, but growth is capped. The path out is abroad, in stages. Two of my named buyers already aren't US companies (SES, ICEYE). Export rules decide the order: UK, Canada and Australia first (licence-free since 2024), Europe later. Demand there is unproven [Q43, RF 22, RF 2].

**"You plan to go abroad, but your team is US-persons only. Isn't that a contradiction?"** No. The US-person team is about export rules: spacecraft technical data can't be shown to foreign persons without a licence, even inside the US (deemed export). That team can still serve UK, Canadian and Australian operators, which need no licence since 2024. What has to wait is hiring foreign staff, or serving countries that need a licence [Q44, RF 22].

**"What does 'high' mean in your Five Forces table?"** High = that force has strong power to squeeze our profits (buyers push prices down, substitutes let customers skip us, entrants take the market). Four of five are high, so it's a hard industry; that's why the strategy is to integrate rather than fight [Q44].

**"Is every customer getting a custom product?"** Configured, not custom-built. The base model is shared; the fleet layer learns each customer's satellites; the copilot layer is set up to their ranking method, tools and team roles. Custom code per customer would turn us into a consultancy and hurt viability [Q44].

**"Your persona is a CISO. Is this US-only?"** No. The role exists everywhere, and two of my five named buyers are European. What anchors the beachhead is serving US defence customers, because NIST SP 800-171's "timely" flaw rule comes with DoD contracts, and a European operator can hold those too [Q45, RF 30].

**"If you go to Europe, what about GDPR?"** It would apply there. The report's jurisdiction is the US, so I don't cover it. The personal data we hold is small anyway (staff names in the audit trail), and the per-fleet design keeps each customer's data separate [Q46].

**"What stops someone poisoning your model?"** Three layers. Training data and overrides are logged and vetted. Every retrained model must pass a release test in simulation before it ranks anything, including a fixed set of known critical flaws it must still rank high. And the authority rule: the AI can only raise a priority, so a poisoned model can't push a flaw below the standard scores. It can't touch a satellite either; it only predicts [Q46].

**"Why is viability your weakest point?"** Because it rests on assumptions, not evidence: about five named buyers, engineers onboarding every customer, slow trust-based sales, compliance and upkeep costs, and no sourced price. I manage it: a one-time onboarding fee covers the setup work so each new customer doesn't start at a loss, the product is configured rather than custom-built so it scales, and growth goes abroad in stages [Q47].

