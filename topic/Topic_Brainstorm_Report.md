# Mid-Sem Project — Topic Brainstorm Report

**Course:** The Business of AI — Mid-Semester Assignment (20 marks)
**Session date:** 17 September 2026
**Submission deadline:** 1 October 2026, 11:59 PM
**AI tool used in this session:** Claude Code (Claude Opus 5), with web search

---

## 0. Final Decision (Locked In)

| Field | Value |
|---|---|
| **Industry** | Defence, Space & Cybersecurity (B2B / B2G) — *Regulated Industries* |
| **Topic (from approved list)** | Day-Zero Vulnerability Prioritisation (Predictive ML) |
| **Official topic description** | "Autonomous systems scanning, scoring, and prioritising unpatched security flaws in critical infrastructure." |
| **Company angle** | An AI platform that prioritises and safely resolves vulnerabilities across **satellite missions**, from ground stations to spacecraft in orbit. |
| **One-line pitch (current)** | A world model of satellite fleets that predicts how a vulnerability, or a patch, will change a satellite's behaviour; a safety-bounded RL agent plans the rollout, and humans approve every uplink. |

---

## 1. Context: What the Assignment Is

### 1.1 Task
Invent a **fictitious company** with AI at its core and tell its **story**: what it solves, how AI creates value, why it succeeds, who it serves, and how it manages AI risk. No code or product needs to be built.

### 1.2 Required components (must connect, not stand alone)
| # | Section | Core question |
|---|---|---|
| 0 | Company Overview | Brand identity (name, mission, vision); market opportunity (why the sector is ripe for AI) |
| 1 | Agentic AI & Value Proposition | What workflow? What does AI do? Where can agentic AI run multi-step work? What economic value (efficiency, cost, speed)? |
| 2 | Moat & Defensibility | Core product architecture; long-term moat (data flywheels, integrations, switching costs) |
| 3 | Porter's Five Forces | Buyer power, supplier power, rivalry, substitutes, new entrants — used to make a strategic point |
| 4 | Persona & Customer Journey | Ideal buyer (pains, goals, decision criteria); journey from onboarding → agentic automation → value → renewal |
| 5 | Governance, Guardrails & Compliance | Human oversight, HITL overrides, stop/escalate rules, hallucination safeguards, monitoring/audits, privacy; one jurisdiction: **US / UK / India** |

### 1.3 Format, length, rules
- Any format (doc, slides, Canva, Figma, 3–4 min video/podcast, or a combination).
- **4 pages + 1-page appendix.**
- **Mandatory appendix:** working evidence (sketches, drafts, decision trees); AI tools used and why, with **≥ 2 transcript links**; the most difficult concept and the approaches considered; what was accepted, modified, rejected, or developed independently after using AI.
- **Grading:** Content 8 · Presentation 4 · Storytelling 4 · Creativity & Effort 4.
- Company must be new and fictitious; plagiarism < 10%; **3–4 key references (blogs don't count)**.
- Possible **three-tier review → viva** to verify understanding.
- Off-list topics needed approval by **17 Sept, 6:00 PM** (the day of this session), so the topic had to come from the list.

### 1.4 Professor's guidance (brief/GC_instructions.txt)
"Dream big": resources aren't the limit, imagination is. Deliver an experience that genuinely excites the user.

### 1.5 Constraint discussed in person (reported by me)
> **The company, or the work it does, must not already be done by any existing company.**

### 1.6 What the assignment develops (explained during the session)
1. Business thinking about technology (who pays, why, why us).
2. Judgement about where agentic AI should act alone and where humans must approve.
3. Governance and regulatory literacy (DPDP, NIST, GDPR).
4. Using strategy frameworks as tools, not as theory.
5. Storytelling and pitching to non-engineers.
6. Using AI as an assistant and showing ownership (the appendix).

---

## 2. My Profile (answered during the session)

- **Area preference:** Regulated (high-stakes) industries.
- **Background:** BTech in Computer Science & Applied Mathematics; research experience in **low-level system building**; currently **learning cloud**.

---

## 3. Timeline of How the Decision Evolved

### Stage 1 — Initial shortlist (matched to my background)
| Option | Industry → Topic | Initial verdict |
|---|---|---|
| **1** | Defence/Space/Cyber → Day-Zero Vulnerability Prioritisation (critical-infrastructure OT/ICS) | Recommended: clear agentic workflow, data moat, strong governance, systems-adjacent |
| 2 | FinTech → Agentic Commerce & Payment Governance | Most creative and timely, but harder to find academic references |
| 3 | Defence → Encrypted Edge Communications | Most low-level, but weakest business story (few government buyers) |

### Stage 2 — Is the choice mine or the AI's?
- I asked whether Claude had "decided". **Clarified: it was only a recommendation, and the decision is mine** (important for the appendix and viva).
- Rubric check exposed **Creativity as the weakest point** of generic vulnerability prioritisation (a crowded market: Tenable, Qualys, Palo Alto).
- Naming nuance found: a true "zero-day" is unknown with no patch, but the topic describes *unpatched known* flaws. The story must handle this.

### Stage 3 — The "no existing company" rule forces a niche
Generic vulnerability management failed the rule. New ideas were built by **combining a listed topic with an unserved setting**:
| Option | Idea | Outcome |
|---|---|---|
| **1** | Vulnerability prioritisation for **satellites in orbit** (patch uplinks limited by ground-station pass windows, power budgets and brick risk; digital-twin testing; staged rollout) | **Carried forward** |
| 2 | **Liability and dispute resolution for purchases made by AI agents** (FinTech) | Kept as the backup |
| 3 | Vulnerability prioritisation for **implanted medical devices** | **Dropped**: Medcrypt and Asimily already nearby, and no clean mapping to a listed sub-topic |

### Stage 4 — "But I must choose from the list"
Clarified: the list defines the **segment**, and the company inside it is mine. Satellite constellations are defensible as **critical infrastructure** (GPS timing, communications, defence links), and "Space" is in the industry's name. **Recommended to confirm with the TA** in case "choose from the list" is read strictly.

### Stage 5 — Competitor search
No product found that does the **whole** job (orbit-aware prioritisation + patch scheduling + twin validation + fleet rollout). Adjacent players exist (see §6).

### Stage 6 — Stress tests (my challenges, §4) reshaped the idea
Orbit-only patch scheduler → AI-centred world-model architecture → fix ladder with manufacturers as partners → whole-mission scope (Viasat lesson) → federated learning → rare-event moat → data pyramid and market-size reality.

### Stage 7 — Final check and lock-in
Verdict: still feasible and still the best fit. Accepted trade-offs: a small specialised market, a moat that is weak early and strong at scale, and about 2–3 evenings of domain reading.

---

## 4. Every Challenge I Raised: Answer, Change, Correction

### Q1. "What exactly is the assignment, and what do I get from it?"
**Answer:** See §1. **Change:** none; this set the shared understanding.

### Q2. "So based on this, you decided Day-Zero Vulnerability Prioritisation?"
**Answer:** No, it was a recommendation. Rubric check: strong on content and viva defence, **weak on creativity**, naming nuance (zero-day vs unpatched), crowded market.
**Change:** made clear that ownership of the decision is mine.

### Q3. "In person we were told the work must not be done by any existing company, and creativity is already the weakest point."
**Answer:** Correct, generic vulnerability management fails the rule. Novelty comes from **intersections** (topic × unserved setting). Three new options proposed (§3, Stage 3).
**Change:** pivot to satellites.

### Q4. "But I still have to choose from the provided list."
**Answer:** All options sit *inside* listed sub-topics; the niche is the company, not a new topic. The medical-device option failed the mapping and was dropped.
**Change:** option 3 dropped; TA confirmation recommended.

### Q5. "Search for existing competitors first."
**Answer:** Five searches run. There is a gap for the integrated product; neighbours exist in detection, digital twins, updatable satellites, generic firmware vulnerability management, and research frameworks.
**Change:** positioning set as "detection exists; nobody turns known flaws into safe, orbit-aware patch decisions." Caveat recorded: web search can't see stealth startups or classified programmes.

### Q6. "Wouldn't an operator just contract Silent Shield + Booz Allen + Hypergiant and solve it? And how is this centred on AI?"
**Answer (vendors):** combining them gives three tools with **nobody making the decision** (which flaw, is it reachable in orbit, patch risk vs waiting, which pass window, go/no-go). That decision layer is the product. Moat: cross-operator data, neutrality, affordability for mid-size operators.
**Answer (AI):** conceded that **scheduling is optimisation and a digital twin is simulation, not AI**. AI was re-centred on: an LLM agent that reads advisories and maps flaws to components; predictive ML for in-orbit exploitability; predictive ML for patch risk; agentic orchestration; anomaly detection for rollback.
**Change:** pitch shifted from "patch scheduler" to "AI security analyst for satellite fleets". Viva test adopted: *"Remove the AI — what breaks?"*
**Corrections:** Hypergiant is not really a hireable vendor (it was a US Air Force programme).

### Q7. "Detection vendors in critical domains must give detailed analysis, not just 'something is wrong'. And why not a new foundation model like JEPA, or a custom RL architecture?"
*(I wrote "JEW"; Claude assumed JEPA — Joint Embedding Predictive Architecture.)*
**Answer (vendors):** conceded the oversimplification. **Silent Shield is Deloitte's product**, is out-of-band behind a one-way diode (**cannot send commands to the satellite**), and was tested against 40 attacks. Distinction: detection handles attacks **in progress**; prioritisation handles flaws **before** exploitation and can act (with approval). Deloitte flagged as a potential **new entrant**.
**Answer (architecture):**
| Job | Build custom? | Reason |
|---|---|---|
| Read advisories and docs | No, use an existing LLM + retrieval | Language is solved; training our own is waste |
| Understand satellite behaviour | **Yes: JEPA-style world model** on multi-fleet telemetry | Predicts in embedding space and ignores noise; grounded by MTS-JEPA and V-JEPA satellite monitoring research |
| Predict patch effects | **Yes, via the world model** | A learned digital twin that improves with every patch = moat |
| Plan the rollout | **Yes: model-based, constrained RL trained inside the world model** | Can't explore on real satellites; hard safety constraints |
| Final approval | **Human, always** | Governance |
Trade-offs noted: cold start, JEPA explainability, training cost.
**Corrections:** Silent Shield was earlier listed as a separate company; it is Deloitte's.

### Q8. "Even once I know what to patch, how is it fixed? Do I always go to the US military for Hypergiant? Deloitte must have other products, or operators must have internal teams."
**Answer (who fixes):** bus software is written and patched by the **satellite manufacturer**; operators uplink it with their own on-board software maintenance tools. **Our company never writes flight software.** Fix ladder:
1. Vendor patch → we validate in the twin and schedule; the operator approves the uplink.
2. No patch → workaround without new code (disable command or service, ground-station command filtering, key rotation, restrict command windows).
3. Flaw in ground station, network or terminals → ordinary IT patching.
4. Nothing safe to change → accept risk and monitor (alert detection vendors).
5. AI-drafted patch → **suggestion to the manufacturer only, never uplinked directly.**
Manufacturers become **key partners** (parts lists, patches, reseller channel), which feeds the supplier-power analysis.
**Answer (Hypergiant):** not needed. **Every satellite already has a command uplink**; the product plugs into the operator's existing mission control and its ground stations (own or rented, e.g. AWS Ground Station, KSAT). Limitation: some older satellites have firmware that can't be changed in orbit, so only fixes 2–4 apply.
**Answer (Deloitte / internal teams):** Deloitte's space offerings found were Silent Shield, Project Constellation (its own cyber-payload satellites) and space data services. **No prioritisation product found**, but Deloitte could deliver it as a consulting engagement (substitute). Internal teams are **users, not replacements** ("a 3-person team manages 300 satellites + 12 ground stations") *(**Unsourced — searched 2026-09-30, NOT FOUND anywhere; do not cite.** See Q20.)*. The largest operators may build in-house, so they are not the first market.
**Key discovery — Viasat KA-SAT attack (24 Feb 2022):** tens of thousands of modems across Europe were wiped (AcidRain) through a **misconfigured VPN appliance in the ground network**. **The spacecraft itself was never touched.**
**Change:** scope widened to the **whole mission system** (ground → network → link → satellite → terminals), with a world model that understands how ground flaws spread to space. Most fixes happen on the ground; in-orbit patches become the rare, closely controlled case.
**Corrections:** the orbit-only focus was too narrow; Hypergiant is not a required partner.

### Q9. "Based on this, is the satellite idea still feasible or a good choice?"
**Answer:** Yes. Every challenge changed it and none broke it.
**Weaknesses recorded:**
1. **Widening scope dilutes novelty**: "whole mission" risks sounding like generic OT security (e.g. Claroty). **Keep the space-specific core**; ground patching is a supporting feature.
2. **Data cold start** (the biggest business risk): public data (ESA anomaly benchmark, OPS-SAT), 2–3 design partners, federated learning.
3. **Small market**: justified by high contract value and manufacturers as resellers.
4. **I'm new to the domain**: read NIST IR 8270 and one Viasat analysis (2–3 evenings).
Switching to Agentic Commerce was judged to reset progress without lowering risk (Visa, Mastercard, Stripe and Google are already there).

### Q10. "What if the owner company sells my platform to others? Would the AI's structure protect it?"
**Answer:** partly. Layered protection:
- **Structure:** hosted core model (customers receive decisions, not weights); federated design (the customer holds only a small local model); value decays quickly for a frozen copy.
- **Where structure isn't enough:** on-premise or air-gapped defence deployments → encrypted weights, confidential computing, licence keys, model watermarking. Cloning via queries → rate limits, decisions instead of full probabilities, monitoring query patterns. Workflow copying → contracts (no resale or sublicensing, audit rights) and trade secrets; **India's Patents Act s.3(k) makes pure software hard to patent**.
- **Business logic:** operators don't want software-vendor liability; rivals won't buy from a competing operator (**neutrality is the product**); turn resellers into an official partner programme.
- **Mirror concern (governance):** federated learning + differential privacy protect each customer's telemetry from others.

### Q11. "I'm still not sure about federated learning or the 'photograph vs live feed' statement."
**Answer:** federated learning explained: the model travels to each operator, trains locally, and only weight updates come back to be averaged. Analogies: students returning only corrections to a teacher; Google's Gboard keyboard.
The metaphor: a copied model is a **snapshot**, while the platform keeps learning from all fleets.
**Weaknesses recorded:** weak moat with few customers; very different fleets make naive averaging fail (→ shared base model + per-platform adapters); updates can leak data (→ differential privacy + secure aggregation); customer-side compute (→ managed on-site box / adapter-only training); some defence customers won't join (they use the product without contributing).
**Change:** federated learning kept as a **supporting idea** (moat + governance), not the headline. A plainer line was offered: *"Customers can copy what our model knows today, but not what it will learn tomorrow from every other fleet."*

### Q12. "But the data feed also depends on that thief."
**Answer:** conceded. A departing customer takes its own feed and can keep retraining on its own data. The loss is uneven: the thief loses N−1 feeds and we lose 1. **With 2 customers it's roughly even (weak moat); with 30 it strongly favours us.**
Better argument: **rare events** (patches that break satellites, exploited flaws, ground-to-space attacks) are too rare for any single operator to learn from, and only pooled data has enough. Analogies: aviation incident sharing, insurance.
**Remaining weaknesses:** weak early moat; the largest operators can go it alone (not the target); dependence on one dominant contributor (business rule: no single operator dominates training data); a thief turning competitor must build its own network (unlikely).
**Correction:** the "photograph vs live feed" claim was replaced.

### Q13. "Are combined failures large and frequent enough for retraining, and for customers to hire (pay for) the platform?"
*(Claude read "hiring me" as "customers paying for the platform"; I have not confirmed this.)*
**Answer:** **No, real in-orbit cyberattacks are far too rare even when pooled.** The rare-events claim overreached. The model doesn't depend on them:

| Data layer | Volume | Trains |
|---|---|---|
| Normal telemetry | Huge (~16,000 active satellites, around the clock) | Self-supervised JEPA world model (**why JEPA fits**) |
| General anomalies (non-cyber) | Common (~40% of small-satellite missions in the last 20 years had partial or total failure; software and integration issues are a major cause) | What "abnormal" looks like |
| Patch and update outcomes | Moderate | Patch-risk prediction (**the real pooled moat**) |
| Simulated attacks / injected faults | Unlimited (twin, red teams) | Attack patterns, safely |
| Ground-based security data | Large (~40,000 CVEs/year, EPSS, ICS exploits) | Exploitability, transferred to space |
| Real in-orbit cyberattacks | Almost none | **Evaluation only** |

Retraining is continuous and does not wait for failures.
**Why customers pay regularly:** weekly triage of new flaws (especially ground software), regulatory evidence, insurance, and rare-attack protection as the premium layer ("smoke detector").
**Market reality discovered:** ~16,000–17,000 active satellites; **SpaceX ~54% (builds its own security, not a customer)**; ~200 distinct operators; realistic first market = **dozens of customers**, so high price per customer is necessary; growth via manufacturers, ground-station-as-a-service providers, space insurers, and government/defence (B2G).
**Corrections:** the "rare events" moat was restated as "pooled patch outcomes and anomaly behaviour, not attacks".

### Q14. "Do I still choose this as the topic?"
**Answer:** Yes. Survived every challenge; genuinely new; exact list fit; matches my skills; rich material for every rubric section. **Don't choose it** only if the domain feels draining rather than interesting.

### Q15. "Lock it in and write a detailed report."
**Done:** this document.

### Q16. "Which jurisdiction fits best for this idea?"
**Key insight first:** all three listed jurisdictional frameworks centre on **personal data** (DPDP, UK GDPR, CCPA), but the platform mainly processes **non-personal machine telemetry**. Personal data enters in only three places, and governance must name them:
1. **User terminals**: subscriber identity and location (in scope because of the whole-mission design).
2. **Operator staff**: approver identities, audit logs of who approved which uplink.
3. **Ground-station access logs.**

So the best jurisdiction is the one whose framework also covers **AI risk and cybersecurity**, not only privacy.

| | 🇺🇸 United States | 🇮🇳 India | 🇬🇧 United Kingdom |
|---|---|---|---|
| **Listed AI framework** | **NIST AI RMF** covers any AI system; its functions (Govern, Map, Measure, Manage) map to oversight, escalation, monitoring and audits | No AI-specific law; IT Rules target online intermediaries (weak fit) | AISI benchmarks aim at frontier models (weak fit) |
| **Privacy** | CCPA/CPRA for subscriber and staff data | **DPDP Act**; **data localisation** fits federated learning (raw data stays in-country) | UK GDPR / DPA 2018; **Art. 22** concerns decisions *about people*, not patch decisions |
| **Space and cyber rules** | **NIST IR 8270, NIST IR 8401**, **Space Policy Directive-5**, NCCoE space project | CERT-In 6-hour reporting, IN-SPACe authorisation, Indian Space Policy 2023 | NCSC guidance, Space Industry Act 2018 |
| **Market fit** | Largest commercial space market and largest government buyer (matches B2G) | Fast-growing private sector, few mid-size constellation operators today | Small |
| **References in hand** | NIST IR 8270 + NCCoE (from searches) | New research needed | New research needed |
| **Extra depth** | **Export controls (ITAR/EAR)** limit sharing spacecraft technical data with foreign persons, which constrains federated learning across foreign operators | Localisation vs cross-border model updates | Little |
| **Overall fit** | **Strongest** | Good alternative | Weakest |

**Recommendation: United States.**
1. **One coherent reference family:** NIST AI RMF (AI governance) + NIST IR 8270 (satellite security) + NIST IR 8401 (ground segment).
2. **Matches the business:** the biggest pool of mid-size operators plus government buyers.
3. **Original depth:** *"Our federated design lets us learn from foreign fleets without moving controlled technical data across borders."* This ties governance back to the moat (storytelling marks).

**When to pick India instead:** for local relevance and viva comfort ("built for India's private space sector under IN-SPACe", with localisation justifying the federated design). Trade-off: weaker AI-specific regulation and fewer references in hand.

**UK rejected:** smallest market, and its distinctive item (Art. 22) doesn't apply to non-personal patch decisions.

**Status:** US recommended; **final confirmation pending**.

*Q17–Q23 below come from the 2026-09-29/30 session that stress-tested the research findings. Each entry records where the doubt came from, the reasoning, the conclusion and what changed.*

### Q17. "Isn't regulation a double-edged sword? If companies must test for vulnerabilities, they don't need us — but once launched, we survive because they're legally bound to do security."
**Origin of doubt:** RF item 2. The proposed EU Space Act, Art. 88, mandates threat-led penetration testing before launch and every 3 years.
**Reasoning:**
- *First edge (they won't need us):* rejected. Testing *produces* findings, and we *prioritise and resolve* them. A mandated test makes the backlog bigger, so testing is a complement, not a substitute. The 3-year cycle leaves a 36-month gap where only continuous tooling helps.
- *Second edge (legally bound, so we survive):* too comfortable, for three reasons. Compliance buyers buy the cheapest thing an auditor will accept. Whoever runs the mandated test is best placed to bundle prioritisation. And the finding is EU (not before 2030), while our jurisdiction is the US.
- *Research (Sonnet subagent → RF item 30, raw/06):* **no binding US vulnerability-management mandate exists for commercial operators.** Only narrow hooks bind: FCC 47 CFR 25.271(d) (a one-line duty to prevent unauthorised access), NOAA Tier 2/3 encryption, and DoD DFARS 7012/CMMC → NIST 800-171 3.14.1 "correct system flaws in a timely manner" (CUI IT systems only).
**Conclusion:** "legally bound" is **false** in the US. The pitch rests on operational risk; regulation is only a tailwind. The one real opening: 800-171 says "timely" but gives no method for deciding what to fix first, which makes **DoD contractors** the natural first customers.
**Change:** RF item 30 added. Porter's Five Forces should show regulation cutting both ways: it lowers the threat of new entrants but raises the threat of bundling by incumbent auditors.

### Q18. "Item 7 (public data sufficiency for JEPA) — how does it show we're hard to copy? If public data proves it works and the real product depends on the data provider, it doesn't connect."
**Origin of doubt:** RF item 7 called public-data sufficiency "a legitimate, honest moat argument".
**Reasoning:** the user was right. Public data proving the architecture works proves it **for every competitor too**. It lowers *our* technical risk, not how easy we are to copy. And customer data alone isn't a moat, because a rival can sign the same operators. A moat can only come from what data access *builds up into*: (1) signing design partners first (weak, only a timing lead); (2) ITAR/EAR and clearance barriers (medium; they stop foreign and fast entrants but not incumbents like Aerospace Corp, Booz Allen or the primes); (3) assets that build up over time (strongest).
**Conclusion:** item 7 is a **feasibility argument, not a moat argument**. Say honestly that the moat is thin at the start and strengthens with scale.
**Correction:** RF item 7 rewritten (first correction), then re-ranked again after Q22.

### Q19. "Why is a live framework better than a static one, and why would static be better? Does moving to live give enough value to break the traditional approach, and where does it fall short?"
**Origin of doubt:** RF item 10/13 differentiates us from Aerospace Corp's SPARTA as "static reference framework, not a live per-operator AI platform".
**Reasoning:**
- *Static wins on:* transparency and auditability; no data sharing (ITAR-friendly); no new attack surface (a matrix can't be poisoned); free and comparable across operators; and speed matters less when patches wait for ground passes and human approval.
- *Live wins on:* context (whether the vulnerable component is on this bus, whether it's reachable this pass, the satellite's power and thermal state, how critical its mission is); scale versus headcount as CVE volume rises; and the one thing static can't do at all, **proving a fix is safe before uplink**.
- *Live falls short on:* we can't prove its value early (almost no real attacks to serve as ground truth); cold start (on day one it's roughly SPARTA plus noise); an explainability gap; and it becomes an attack target itself.
- *Factual catch:* SPARTEND already delivers SPARTA's knowledge to orbiting assets, so "static" is shaky wording.
**Conclusion:** the right axis is **reference vs decision-and-execution**, not static vs live. **Build on SPARTA rather than fight it:** use it as the knowledge base and express our outputs in SPARTA technique and countermeasure IDs. That turns explainability into auditability, lowers switching resistance, and makes SPARTA a complement in Porter's.
**Still open:** the RF item 10/13 differentiator wording hasn't been updated yet. Suggested: *"SPARTA/SPARTEND provide general-purpose threat knowledge and on-orbit detection; neither performs per-operator patch decisioning, digital-twin validation of fixes, or scheduled fleet rollout."*

### Q20. "Why did we assume the companies we cater to aren't doing the work internally?"
**Origin of doubt:** Q8 answered "internal teams are users, not replacements", resting on a "3-person team manages 300 satellites + 12 ground stations" line. RF item 14 already showed SpaceX builds in-house.
**Reasoning:** the evidence already in hand pointed the other way: SpaceX (full rollout in-house), Axiom (hiring for vulnerability management and patching), Spire (built an On-Orbit Update Manager and sells it), Planet (a mature CISO organisation), and every DoD contractor (800-171 3.14.1). The counter-evidence (White House and WEF reports) is industry-level only.
**Research (Sonnet subagent → RF item 31, raw/07):**
- every target runs a formal program (SES has over 40 security staff; Planet has a Satellite Security team; Spire ranks vulnerabilities by ISO 27005);
- Planet and Spire already validate software before uplink and roll it out in stages;
- Spire's platform covers deployment only, so it's a partner, not a rival;
- the **"3-person team" quote was NOT FOUND anywhere**;
- Globalstar is out as a customer (Amazon acquisition).
**Conclusion:** the assumption was wrong. Operators do this work, formally. What's still arguable is that no one publicly claims **cross-domain prioritisation tied to validated rollout**, and that's an absence of claims, not proof of a gap. The real substitute is the **good-enough stack**: in-house program + SPARTA + vendor patches + Spire-style rollout tooling.
**Correction:** the Q8 quote is marked unsourced. The pitch becomes "we connect and speed up what your team already does," not "you lack a team".

### Q21. "If companies do it internally, they're probably doing it better and more efficiently."
**Origin of doubt:** follows from Q20.
**Reasoning:**
- *Internal is better at:* knowing its own buses, priorities and risk tolerance; sharing no data; and handing no uplink path to a vendor. At SpaceX scale, internal clearly wins.
- *"Better" doesn't follow automatically:* a world model, twin and planner are a large fixed cost. Paid off across one fleet versus many, that's the usual reason firms buy security tooling rather than build it. A single fleet also sees few incidents. And mid-size security roles are stretched: Planet's CISO scope spans IT, physical security, compliance and AI governance.
- *Research partly confirmed the doubt:* SES's 40+ staff and Planet's staged deploy pipeline show more maturity than we assumed.
**Conclusion:** **half confirmed.** Internal teams have context we can't get on our own, so the product must take in their priorities, not override them. We're a tool for their team (human-approved uplinks already fit this), not a replacement. Whether "better and more efficient" is true for mid-size operators is still unmeasured, in both directions.

### Q22. "Why would companies want to help their competitors?"
**Origin of doubt:** the moat relied on a federated cross-fleet model, where each operator improves the shared model for all (RF item 7 correction, TB §7.5 point 1, Q11–Q12).
**Reasoning:**
- *For sharing:* security is often treated as non-competitive (ISACs); after Viasat, an attack on one operator hurts everyone's insurance and regulatory position; federated learning shares updates, not raw data; and private per-operator layers keep each operator's edge.
- *Against sharing:* free riders (big contributors gain least); leakage through model inversion (DP costs accuracy on small datasets, RF item 9); ITAR/EAR splitting the pool by country; and ISACs share threat indicators, not training signal.
- *Research (RF item 31):* operators share only anonymised, TLP-gated alerts (Space ISAC) or minimum orbit data through a neutral third party (Space Data Association). Documented reluctance: sharing can "hand competitors an advantage". **No federated or pooled security-telemetry program exists.**
**Conclusion:** **strongly confirmed.** The network effect is a **conditional upside, not the main moat**. The product must deliver full value to a single operator on its own. The moats that need no cooperation come first: the patch-outcome record and workflow switching costs. The best precedent for later sharing is the SDA model (neutral third party, minimum data, participation incentives such as contribution-weighted pricing).
**Correction:** RF item 7 second correction (moat re-ranked). TB §7.5 is flagged below.

### Q23. "Why do I feel like the more I research, the more I realise I've chosen the worst topic?"
**Origin of doubt:** the accumulated corrections from Q17–Q22, plus a red-team review listing 35 more doubts.
**Reasoning:** the feeling comes from the process: two days spent attacking one idea, compared against topics nobody examined. **What died:** the legal-mandate tailwind, public data as a moat, the network effect as the main moat, "operators lack teams", "nobody validates patches". **What survived with evidence:** no one claims the whole loop; reference vs decision-and-execution against SPARTA; Spire as partner; the 800-171 prioritisation gap; Viasat's ground→space path; outcome data and switching costs as a moat. Everything that died was an overclaim, not the core. *Honest concession:* as a real business it's hard (small market, long sales cycles, capable in-house teams).
**Conclusion:** the rubric grades analysis, not investability. Honest moat/Porter's reasoning with named weaknesses scores better than unchecked claims. Switching topics a day before the deadline is not a real option.
**Decision:** make this the last research pass. Fix the red-team review's top 5 (`research/Research_Findings_Review.md`), then draft.

### Q24. "At ~$90K a year per customer, is the business even feasible? Training, continuous compute, aggregation and inference would push costs way up. Charging this little doesn't match the value I'd need to deliver or the cost of delivering it."
**Origin of doubt:** review R20 (`research/Research_Findings_Review.md`) gave $36K–98K/yr by multiplying Datadog's $15–41/host/month (RF item 28) by ~200 satellites.
**Reasoning:**
- *The anchor is wrong:* that figure prices a satellite worth $0.5M–$300M (RF item 4) like a $15/month cloud server. Item 28 gives a pricing *structure*, not a *level*.
- *Compute is probably not the main cost (reasoning, not sourced):* telemetry is low-rate time series, not video, so the model is far smaller than V-JEPA 2 (RF item 7). Inference runs per advisory or patch decision, a handful a week per operator. Federated overhead at a few dozen clients is 1.5–3x compute and 1.7–2x communication (RF item 9).
- *The real cost is people:* cleared domain engineers, per-customer integration (every bus and mission control setup differs), a digital twin per satellite platform, and compliance (CMMC, possibly FedRAMP). That makes it a business heavy on services and specialist labour.
**Conclusion:** **the user is right about the outcome, for a different reason.** At ~$90K × a few dozen customers the business is not feasible. It is only viable if (1) pricing is value-based: e.g. saving 10% of SES's 40+ person team's triage time ≈ 4 people × $115K–159K (RF item 5, general-industry) ≈ **$460K–640K/yr**, or a one-time avoided smallsat loss of $0.5M–1M; (2) twin cost is paid once per satellite bus type and shared across operators flying that bus (this needs manufacturer cooperation, which is unevidenced, see review R13/R14); and (3) the market widens beyond commercial operators (government programmes, ground-station-as-a-service, manufacturers pre-launch; review R19). All three are hypotheses.
**Change:** drafting tasks T1–T3 (§9.6). The report shows a one-line revenue model with its assumptions and names this as the business's weakest point.

### Q25. "Liability: we'd be claiming we've correctly and completely tested everything. Even if we magically had an undo option, needing to use it means we're not reliable in a highly critical sector."
**Origin of doubt:** review R29 (liability unresearched; TB §9.4 Q23 open) and the rollback step in the architecture.
**Reasoning:**
- *The premise is the error:* no safety-critical industry (aviation, medicine, nuclear) claims complete testing. They assume failures will happen and design to **detect them early, limit the damage and recover**. A rollback plan signals maturity. A vendor claiming it needs none would be the untrustworthy one.
- *Operators already expect it:* Planet runs ground test → on-orbit staging → fleet, with an "un-spaceworthy" reject path. Spire's tool has automated rollbacks (RF item 31). SpaceX uses canary plus auto-rollback with zero losses reported (secondary source, review R21). Not acting on ground-side weaknesses is also a risk (Viasat's entry point was a misconfigured ground VPN appliance; *corrected 2026-09-30, Q38: it was not an unpatched flaw*).
- *The user's real point, sharper than R29:* undo only works if the satellite is still listening. A patch that breaks the command receiver or boot path **cannot be undone from the ground**.
**Conclusion:** reliability in this sector means **failures that are rare, caught at the canary stage and recoverable**, not zero failures. Unrecoverable failure classes must be *prevented*, not undone:
- never auto-schedule changes touching the command, boot or authentication path;
- require an A/B software partition plus a hardware watchdog that falls back to a known-good image (a manufacturer feature, so a precondition for us to operate);
- canary on the least-critical satellite first;
- hard stop rules.
Liability follows the wording: we don't write patches (Q8), the operator approves each uplink, and our output is **"decision support with evidence and a stated residual risk"**, never "certified safe". Back that with a contractual liability cap and the full audit trail (RF item 24).
**Correction:** remove any "fully/completely tested" language from the concept and report. Drafting tasks T4–T6 (§9.6). This answers rubric A.5 "what happens when the AI is wrong".

*Q26–Q29 come from the report-design discussion (2026-09-30), after the draft spec (`report/specs/2026-09-30-report-draft-design.md`) was checked against every review item.*

### Q26. "If the model scores risk before applying and detects anomalies after, how is it different from current workflows? Detection and monitoring already exist in normal software (e.g. Deloitte)."
**Origin of doubt:** the spec's reframe of the world model (review R6): it stopped predicting what new code does and became a pre-uplink risk scorer and post-uplink anomaly detector.
**Reasoning:** conceded. Scoring (IT scanners, SPARTA), health monitoring (Spire CMP) and attack detection (Deloitte Silent Shield) all exist. The reframe had made the world model sound like the product. What no existing tool does is take a **known flaw to a safe, scheduled fix across the whole mission** in one flow: ground→fleet reachability, then a ranked plan (satellites, order, pass, or a workaround), then validation, approval, watch and halt. Today that is a handoff chain across security, flight software/manufacturer and mission ops.
**Stronger role for the world model:** the manufacturer's emulator *runs* the fix, but a test run needs something to judge the results. The world model compares the emulator's simulated telemetry, then the canary satellite's real telemetry, against how *that* satellite normally behaves, catching drift that scripted tests miss. It judges code that has run; it doesn't predict unseen code.
**Conclusion:** the product is the agentic flaw→safe-fix flow. The world model is its judge and safety net, not the headline.
**Change:** spec v2 (A.1 architecture step 5 + "what is new" line).

### Q27. "How is this safety net valuable enough against the companies' own researchers and teams? That is what they were hired to do. The main thing is to make the researcher's life easier and more productive."
**Origin of doubt:** follows from Q26 and Q20–Q21 (operators run capable in-house programs).
**Reasoning:** the user's reframe was adopted. Periapt (then called Phylax) shouldn't compete with teams. It should take on the parts of their job that don't scale with people: *coverage* (every channel, satellite and pass during a rollout), *memory* (outcomes stay in the context graph when staff leave), *consistency* (the same at 2 a.m.; counters automation bias and fatigue) and *joining the pieces* across the four groups. It fits the trust thread: experts rely less on automation (Sanchez et al., S11), so a copilot that supports judgment is adopted and a replacement is rejected. *Pushback:* "why not a general AI assistant?" Because a general assistant can't trace ground→fleet reachability, plan around passes and power, or judge emulator runs against a satellite's normal behaviour.
**Conclusion:** the positioning is **"a domain copilot that owns the workflow"** (Foundation Capital: own the workflow, not the model). Demand line limited to what's sourced: CVEs +20.6% from 2024 to 2025 (RF item 27). No claim about how fast teams grow.
**Change:** spec v2 decisions table (positioning) and A.1.

### Q28. "What exactly needs my attention? Did you create the persona, or do I need to do something? And for transcripts, I'll split the log into chunks and attach Google Drive links."
**Origin of doubt:** the spec review listed "points needing attention" without saying which were decisions and which were tasks.
**Answer:** the persona was a **decision to confirm**, not a task. The spec picks the first customer (a US mid-size operator holding DoD contracts; its CISO is "the Stretched Sentinel", with a buying committee). The user confirmed it: "Looks okay to me. Do the best you can think of." The only real user tasks are the transcript links and the final voice rewrite. For transcripts: use the **redacted** `logs/TRANSCRIPT_LOG.md`; run `/export` + `/transcript` for this session first; set Drive sharing to "anyone with the link can view".
**Change:** spec v2 (persona confirmed; appendix transcript method).

### Q29. "Is revenue even necessary? What is ACV? The 3–4 analyst-equivalents × buyers figure is low, and our main cost is the people who validate and correct our models. If we don't use ACV, how do we show the value created?"
**Origin of doubt:** the spec's close used "ACV ≈ 3–4 analyst-equivalents × buyers" to answer review R20.
**Reasoning:**
- *ACV* = annual contract value, what **one customer pays per year**. Total revenue = ACV × customers.
- *Not required:* the rubric's "Economic Value" asks for value **to the customer** (efficiency, cost, speed), not the company's revenue.
- *The user's objection shows the formula was weak anyway:* priced on analyst time saved, one customer pays a few hundred thousand a year, while the main cost is skilled people integrating each customer and validating the models. The numbers don't close, and printing them invites that attack.
- *Value without ACV, in three layers:* (1) a value table split into efficiency, risk reduction and innovation (S3), with pilot-measurable metrics; (2) a before/after of the opening scene (steps from research, durations marked illustrative); (3) value proven through renewal triggered by pilot metrics.
- *Pricing structure without numbers:* per-fleet annual subscription + a one-time onboarding/integration fee that pays for the people-heavy integration work.
**Conclusion:** drop the revenue and ACV figures. Show customer value in three layers and pricing structure only. Viability stays named as the weakest point.
**Change:** spec v2 (A.1 value case, close, review matrix R20 row).

### Q30. "What are the odds: how did we land on a company with our idea and the same name? phylax-intelligence.com"
**Origin of doubt:** the user found an existing company named Phylax after the name had been chosen.
**Check (fetched 2026-09-30):** Phylax Intelligence (EU) sells "AI-powered Situational Awareness and Decision Support For Security & Crisis Teams" for physical threats and hazards (sabotage, drones, floods, fires, intrusions, misinformation), with satellites only as an imagery source. It does no vulnerability prioritisation, patching, spacecraft software or rollout. **Same name, different idea, so originality holds.**
**Reasoning:** "Phylax" (guardian) is an obvious word for security founders; a blockchain firm, Phylax Systems, also exists (from memory, unverified). Brief §F forbids using an existing company, and a TA googling the name would find an AI security firm that mentions satellites, which invites an originality flag. So the name was changed.
**Candidates checked:** PassWarden (taken: KeepSolid password manager) · **Amyntor (taken: two cybersecurity firms in Thiruvananthapuram, India; missed by the quick search and found by the deep one)** · Nightpass (several nightlife apps) · Kessler Shield (no company, but reads as debris shielding) · **Periapt: no security/space use; only unrelated uses (audio cables, AU financial advisory, IL ADHD health startup, RPG publisher, dissolved UK software firm).**
**Conclusion:** renamed to **Periapt**, a protective amulet that echoes *periapsis*, an orbit's closest point ("protection at the closest point of risk"). Test applied: *no security/space company uses the name, and nothing a TA finds could be confused with the idea.*
**Lesson:** a quick search isn't a name check. Amyntor passed the quick search and failed the deep one.

*Q31–Q38 come from the spec-v2 review session (2026-09-30, evening). They cut the scope back to the original problem and put AI back at the centre. Q33 comes from my separate study session, saved as `Discussion on the World model.txt`.*

### Q31. "Is JEPA-style the only kind of world model? I chose a world model because it can understand and connect the components, link RL outcomes and the digital twin, test on it, and plug into physics engines, unlike classifiers or LLMs that work on text. Is my thinking right?"
**Origin of doubt:** spec v2 named a JEPA world model as the judge of test runs, and I wasn't sure the style mattered.
**Reasoning:**
- *Right:* "world model" is the category (a learned model of how a system's state changes). JEPA is one family; others are Dreamer-style models, physics-informed hybrids and plain forecasters. JPL already learns spacecraft telemetry from commands and past values with LSTMs (Hundman et al. 2018, RF item 32).
- *Right:* telemetry is numbers over time, not text, so an LLM is the wrong tool for it.
- *Flaw 1:* telemetry links subsystems inside one satellite, but it holds nothing about ground networks. The ground→space link comes from the exposure graph, not the world model.
- *Flaw 2:* it can't test new code. "Digital twin" names two different things: the manufacturer's emulator runs code, a learned model can't (R6, Q26).
- *Overreach:* coupling to a physics engine is harder for JEPA, whose state is an abstract embedding. Unsourced, so vision line only.
- *A stronger reason than mine:* failures are rare, so there aren't enough labelled failures to train a classifier. A world model learns normal behaviour from unlabelled data.
**Conclusion:** call it "a learned world model (JEPA-style as the candidate)". Its jobs were set in Q34–Q36: predict what a flaw would do to each satellite, and forecast battery/thermal margin. It does not predict what new code does, and it does not trace ground→space reach.
**Change:** spec v3.

### Q32. "Explain the planner contradiction. How severe is it, how does each option change the company's path, and are there only two options?"
**Origin of doubt:** Claude's review of spec v2 (R8, R11).
**Reasoning:** v2 said a learned policy improves rollout order "from outcomes", while A.2 concedes spacecraft patch outcomes are rare and mostly successes (R11). It would learn from data we said we don't have. Severity: medium, a logic gap rather than a factual error; the solver still guarantees a safe plan. Five options, not two: (A) solver + risk-score order, (B) learned from past outcomes (v2), (C) adaptive order within one rollout, (D) constrained RL inside the world model (the original lock), (E) solver only. They differ in data needed, hiring, auditability and viva risk.
**Conclusion:** Claude first recommended C starting from A. **Superseded by Q34:** once the scope was cut back to prioritisation, the planner stops being an AI component. What remains is a suggested fix window from a plain scheduler, fed by the world model's battery/thermal forecast.
**Change:** the "constrained RL planner" lock in CLAUDE.md is dropped, pending spec v3 approval.

### Q33. "If the emulator already runs the patch, isn't the world model useless? What are the alternatives, does a layered approach solve it, and what are its flaws?" *(separate study session)*
**Origin of doubt:** my own study of what a world model is.
**Reasoning:** the judging job has cheaper tools: limit checks, comparing patched and unpatched emulator runs, statistical tests, a learned forecaster, a JEPA model. **Layered design:** rules and run comparison first, the learned model as the safety net. Flaws and counters:
- intended changes set off alarms → the patch ships with a list of expected changes;
- the canary has no control group → compare with sister satellites and with its own pre-patch behaviour;
- the emulator isn't the real satellite → that's what the canary is for;
- slow failures → a soak period plus a long watch;
- too many alarms → each layer gets different authority (a limit breach halts, an unexpected difference holds, a learned-model flag only flags; any layer can stop, only a human can clear);
- the learned layer is unproven → a test that can fail: fewer false alarms than a plain forecaster at the same detection rate on ESA-ADB, with Hundman 2018 as the forecaster (RF item 32);
- forged data from a hacked ground segment → a shared-responsibility split (the customer secures the ground and keys; Periapt cross-checks data, refuses unsigned patches and secures itself).

*Pushback I received:* "if a simple forecaster worked it would already be published" is wrong, because forecasters are published (Hundman 2018, now verified), so keep the test and drop that argument. "The adversarial blind spot isn't my problem" is wrong too, because Periapt's all-clear would become part of the attack.
**Conclusion:** the layered check was adopted. After Q34–Q35 the safety check stays small, and the layering principle moved into the ranking itself (Q35).
**Change:** spec v3 and Viva_Prep.

### Q34. "The original workflow was: read advisories, score how dangerous each flaw is, predict what would happen, plan the rollout and rollback. Which of these wasn't feasible, and why? The current scope is way too big, we can't deliver it, and AI has become secondary, which is the exact opposite of what's needed."
**Origin of doubt:** I compared spec v2 with the 17 Sept problem statement (§0, §7.1–7.3).
**Reasoning:** step by step:
- reading advisories works (the parts list has to be built at onboarding, R14);
- scoring works (whether ground-trained scores carry over to space is unproven, R17);
- predicting what a *flaw* does works;
- predicting what a *patch* does fails, because a patch is new code (R6);
- planning the rollout works, but not with RL (R8);
- rollback works, but it is already sold (Spire, SpaceX; R7) and impossible if the radio breaks (Q25).

Only two ideas failed. The scope grew from the work-arounds (emulator judge, solver, whole mission, rollout tooling), not from the original idea. *Conceded:* the product had become "known flaw → fix across the whole mission" with AI as a helper, which is backwards for an AI course and for a topic called prioritisation. *Pushback:* keep the ground→space reach (Viasat) as one input, not as a product area.
**Conclusion:** cut back to the original niche. Out: ground-IT patching as a product, terminals as a product area, building rollout/rollback, the RL planner, and fleet monitoring as a product.
**Change:** spec v3. The §0 one-line pitch will be updated with v3.

### Q35. "I don't want to build fancy decisions that simple, existing software can already do. A prioritiser (even with a safety check) just replaces the humans and software they already have. It's not worth the switching cost or the risk. The goal was to assist the people doing these steps and tie them together with AI."
**Origin of doubt:** Claude's options A (pure prioritiser) and B (prioritiser + safety check).
**Reasoning:** *conceded:* teams already rank flaws (Spire ranks by ISO 27005 likelihood and impact, RF item 31; SES has 40+ staff). *Pushback:* "tying teams together" alone can be done by a ticket tool such as Jira, without AI. So the AI must do something at each handoff that a ticket tool can't: read advisories, translate between security, flight software and ops, draft, predict. **Principle adopted:** simple software does what it can (parts matching, CVSS, EPSS, SPARTA IDs), and those are used, not rebuilt. AI works only where rules can't reach, which is the impact on each specific satellite. It plugs into the team's own tools and ranking method, so there is no migration to justify.
**Conclusion:** a copilot for the three teams, where each keeps its own decision.
**Change:** see Q36 for the topic-fit correction.

### Q36. "Is this goal still in the topic's category, Day-Zero Vulnerability Prioritisation (Predictive ML)? I feel it isn't."
**Origin of doubt:** the copilot description in Q35 was centred on handoffs.
**Reasoning:** checked against the listing's words. Scanning fits. Scoring with predictive ML was weak, and prioritising wasn't central, so the copilot had drifted toward fixing. The same segment also lists "Spacecraft Mission Operations (… telemetry analytics)", and IT lists "Threat Detection & Incident Response (SOAR)". Pitching the world model as monitoring would drift into those.
**Conclusion:** the **core is predictive prioritisation** (scan → score → rank with reasons), **delivered as a copilot**, with fixing kept small. Per flaw it predicts:
- will attackers use it (FIRST's EPSS, an existing input, RF item 32);
- can it reach the satellites (the graph);
- what would it do to each satellite (the world model: ours);
- how risky is fixing now (the world model's battery/thermal forecast).

**Change:** spec v3.

### Q37. "It scans, scores and prioritises, but a human intervenes at each stage. Is it autonomous?"
**Reasoning:** if a human had to act at every stage, no; that's a tool. Autonomy means the system does the work on its own. Scanning, scoring and prioritising only produce information, so they run on their own around the clock. Humans supervise and can override at any time ("human on the loop"). A hard approval is needed only before anything touches a satellite ("human in the loop").
**Conclusion:** "autonomous in deciding what matters; a human approves every action on a satellite." This fits the topic's "autonomous", the course's rule of human oversight for high-stakes actions, and rubric A.5.
**Change:** spec v3 autonomy table.

### Q38. "Before we lock it: a hard review of the whole conversation, the scope and the revised concept against the grading components, the course concepts and the topic listing, and a check of every claim."
**Origin of doubt:** one final check before spec v3, with no time left for another round.
**Findings (verified 2026-09-30, RF item 32):**
- *Viasat:* the attacker got in through a **misconfigured** VPN appliance (not an unpatched flaw). The satellite and ground infrastructure were not affected. Legitimate management commands overwrote modem flash, and the modems could be restored by a factory reset (~30,000 shipped). The Q25 line and Viva_Prep were corrected. Useful: real harm came from *legitimate commands*, which is exactly what the world model plays out.
- *EPSS* (FIRST) already predicts, with ML, whether a CVE will be exploited within 30 days, for free. It is an input, not our novelty.
- *Aerospace Corp + Google Public Sector* (April 2026) are building agentic AI that monitors every satellite in large LEO constellations for anomalies. Monitoring is taken; name them, and Aerospace Corp becomes the top new-entrant threat (SPARTA + SPARTEND + this).
- *CT Cubed:* the homepage now lists assessments, training and cyber ranges, and "Terrain Trace" can't be found. Keep IRON GALAXY named; drop the "AI risk assessment" wording unless it is found again.
- *Hundman et al. 2018* (JPL, KDD) confirms that learned command-and-telemetry models exist, and gives the baseline for the world-model test.
- *Simulating attack impact on satellites* is done in research with physics simulators (NASA NOS3, arXiv 2603.10388). Claim only that no one publicly does it automatically, per satellite, from live data, to rank flaws.
- *"Critical infrastructure":* space is not a US CISA sector (RF item 30). Word it as "infrastructure that critical sectors depend on".

**Conclusion:** the revised concept holds, and the fixes are wording and competitor naming. The scores and the remaining open decisions are in the session review; spec v3 is pending approval.

### Q39. "Can we be a complement or sit in an adjacent space instead of competing with Aerospace Corp? How exactly is the value smaller for new, identical fleets? I'm keeping it people-heavy because this industry doesn't trust new automation: you have to earn trust first, then grow into the scope we cut. And we'll never have full data at the start; it all comes from the client at onboarding."
**Origin of doubt:** the weak spots listed in the Q38 review.
**Reasoning:**
- *Aerospace Corp:* **yes, a complement.** Under FAR 35.017 an FFRDC is not meant to use its privileged access to compete with the private sector (RF item 32; wording softened in Q40). It publishes frameworks (SPARTA) and builds government prototypes. Periapt builds on SPARTA, speaks its IDs, and can validate through Aerospace's ASC-100 testbed access (RF item 31). *The real entrant threat moves* to its partner Google and to the primes and consultancies.
- *Identical fleets:* the world model earns its keep by telling satellites apart. In a new fleet of identical, healthy satellites, "what would this attack do?" gives nearly the same answer for each, so it adds little over a rule, and the history is short. The value left is reading at scale, speed, and ranking *across* flaws. Satellites drift apart as they age (reasoning, not sourced). → Early adopters are older or mixed fleets.
- *People-heavy:* **agreed as a strategy**, and backed by the course: experts rely less on automation (Sanchez et al., S11), and forward-deployed engineers are in demand (S1 note). *Pushback:* it's still a cost, so viability stays the weakest point. Onboarding gets cheaper only if parts libraries per satellite bus type can be reused across customers, which is a hypothesis that needs manufacturer data (R13/R14).
- *Staged growth:* **agreed.** Prove Stage 1, then add fix-window planning, then validation and rollout with partners. This is the course's "think big, act small" and "dominate a niche, then adjacent markets" (Porter deck, Thiel).
- *Data:* **correct.** Onboarding builds the parts list, the reach map and the history from the client (R14). Until a fleet's model is trained, layer 3 says "unknown", so rankings stay high by default. Shadow mode earns trust, gathers data and trains the model at the same time.
**Conclusion:** all five folded into spec v3 (§1, §2.4–2.6, A.3, A.4, close).
**Change:** spec v3 written 2026-09-30. User approved: the re-centred concept and cuts, the ranking authority rule, and the reference list. India and SBIR are on hold.

### Q40. "Saying someone works out by hand which satellites have a flaw is an overstatement; software exists for that. And for new fleets: satellites are tested on the ground, but after some months in space unknown conditions make them differ, they fly for years, and even 12 identical satellites have different locations and conditions. Is that plausible? Then a final check that nothing in the design will blow up later."
**Reasoning:**
- *Overstatement:* **conceded.** Scanners and SBOM tools already match listed CVEs to software (e.g. Thales Alenia uses Black Duck, RF item 12). What's still manual is judging what a flaw *means* for each satellite: prose space advisories, missing spacecraft parts lists (R14), reach from ground to fleet, and the actual impact.
- *New fleets:* **plausible, with two limits.** Right: identical hardware ≠ identical conditions (orbit position, eclipses, radiation, workload), and differences grow with age. So value **grows with time in orbit**, which is also a moat. Limit 1: the model still needs some operating history per satellite, so "3 months to a year" is a guess to measure in the pilot, not a claim. Limit 2: service life varies a lot by satellite class and isn't in our sources, so don't give a number.
- *Hidden problems found in the final check:*
  - (1) the moat said the per-fleet model was a switching cost, but the telemetry archive belongs to the customer and leaves with them → the moat is now the record + the time and trust needed to rebuild;
  - (2) "FAR 35.017 bars FFRDCs from competing with industry" overstated the rule → softened to "not meant to use privileged access to compete with the private sector";
  - (3) "the manufacturer's simulator" assumed access → "where one is provided".
- *Course gaps closed:* bias (S6: data-poor satellites under-ranked → "unknown = high"), a periodic safety review, the product lifecycle (S7), and the Layer 6/7 nuance.
**Change:** spec v3 §2, §2.5, A.0, A.2, A.3, A.4, A.5, §5, §10; Viva_Prep §9.

### Q41. Morning review of the opening + A.0 (1 Oct): "Check the Layer 7 claim first, then hedge it as a Layer 6 app delivering Layer 7 outcomes. Add that environmental conditions differ even for newly launched satellites. Give a market size, worded clearly as our own estimate from a formula, since no official number exists."
**Reasoning:**
- *Layer 7:* **checked and conceded.** The course's Gartner notes define Layer 7 as "Guardrails, TRiSM, governance, and threat protection" (securing AI) and Layer 6 as "AI Applications". CrowdStrike is listed at Layer 7 as a vendor. So Periapt is a Layer 6 app delivering Layer 7-style outcomes, and it applies Layer 7 guardrails to its own LLM.
- *New satellites differ:* **agreed.** Two satellites launched together still sit in different sun, eclipse, radiation and workload. That's now in the opening, so the reader sees early why one flaw can rank differently per satellite.
- *Market size:* **agreed, with one pushback.** A dollar figure needs a price per customer, which we cut in Q29 (no sourced price). So the estimate counts satellites instead: the sum of the named mid-size buyers' fleets (Planet, Iridium, SES, Intelsat, ICEYE; RF 11) ≈ 430–450 satellites across 5 operators. It's labelled as our estimate from a public tracker, not an official figure, with the $303B commercial satellite industry (RF 1) as scale only.
- Also accepted: "no *product* predicts per-satellite impact" (research does simulate attacks: NOS3, RF 32), and B2B2G instead of B2G.
**Change:** draft opening + A.0. A.0 is now ~100 words over target; the cut happens at the 4-page step.

### Q42. Review of A.1 (1 Oct): "Name the layers by the problem they solve and add what each gives the team. 'Hand-checking' is wrong, since software and a thin night shift do most of the watching. Is the rough estimate per analyst? A lost smallsat is a big tail risk; keep it or not? And after we hand the ranking to the internal teams, should we also test their fixes, plan them and send feedback, or are the teams good enough without us?"
**Reasoning:**
- *Layer table:* **agreed.** Renamed to Exposure / Likelihood / Mission impact, with a "What the team gets" column.
- *Hand-checking:* **conceded.** Scanners already match listed CVEs (Q40). The value is catching what they miss (prose advisories, no parts list) and whether the flaw really reaches the fleet.
- *Estimate scope:* it's per operator (the team's total), shown as a share of one analyst's time. It counts security-analyst time only, so it's conservative. All inputs except the salary range (RF 5, general industry) are our assumptions.
- *Tail risk:* **kept, reworded.** It's the customer's risk, not Periapt's, and we have no base rate for how often it happens (R4). So it's shown as "what's at stake", not counted in the value case.
- *Testing the teams' fixes:* **not in Stage 1.** The teams are capable, not lacking (SES 40+ staff; Planet ground test → staging → rollout; Spire's update manager with rollbacks and a testbed; RF 31), and the world model can't predict new code (R6). What Stage 1 gives back after the handoff: a safe fix window (the margin forecast), the outcome stored in the record, and a re-ranked list. Planning and outcome tracking is Stage 2; validation and rollout with partners is Stage 3, once trust is earned (Q34, Q39).
**Change:** draft A.1 (table, command chain, rough estimate, after-fix line, risk wording); Viva_Prep §9.

### Q43. Review of A.2 (1 Oct): "Even combined, the moat isn't strong. If the customer leaves with the record, do we keep the model? Is the 'rival' possibly the customer itself? Can we go international once the US niche is won? Don't repeat things, refer back to earlier sections instead. Trust isn't one moat among many; trust is what keeps the customer, the workflow and the growing value. And if the model was trained on their data, how do we stop them owning it, or doing better than us?"
**Reasoning:**
- *Moat strength:* **agreed it's weak**, and it stays labelled thin at the start. The rewrite makes it more honest, not bigger.
- *Trust as the root:* **agreed.** Earned trust (an intangible asset, earned per customer in shadow mode) keeps the customer, and staying builds the record in use, the workflow switching cost and value that grows with time in orbit. Efficient scale is market structure, not caused by trust.
- *Who owns what:* the customer owns telemetry, command history and the record (exportable). Periapt owns the base model and software. The fleet layer is licensed only during the subscription and deleted on exit. The rival can be the customer's own team (the in-house substitute); either way they must rebuild the models and integrations and win trust again.
- *"They can't do better than us":* **can't be promised** (a rich operator could build better). Three hedges instead: (1) the contract (data theirs, model ours); (2) the design: a shared base trained only on public data and open simulators plus a thin per-fleet layer (adapter technique, RF 8), so the fleet layer is useless alone and exit deletion is clean; (3) time: a frozen copy goes stale as satellites age.
- *International:* **viable in stages, demand unproven.** Two named buyers are already non-US (SES, ICEYE). Export control decides the order: a 2024 EAR rule removed licence needs for the UK, Canada and Australia (RF 22); Europe later (EU Space Act not before 2030, RF 2). Kept as a one-line hint in A.2.
- *No repetition:* A.2's architecture now lists only features A.1 didn't cover. A whole-draft repetition pass comes before the 4-page cut.
**Change:** draft A.2 rewritten; A.5 customer-exit line aligned; Viva_Prep §9.

### Q44. Review of A.3 (1 Oct): "What does a 'high' rating mean: more power to hurt us? I chose the best topic to screw me. Can't we customise the application layer per customer, with the world model shared and the copilot wrapper per customer?"
**Reasoning:**
- *"High":* yes. High = that force can squeeze our profits. Four of five are high, so it's a hard industry; the strategic point (integrate, don't replace; go niche) is the answer. The table header now says "high = bad for us".
- *"Worst topic":* **pushed back.** Reports that make every force friendly look unanalysed. A hard industry with a clear answer to each squeeze is the stronger story.
- *Customise per customer:* **yes, as configuration.** Shared base model → per-fleet layer (their data) → copilot layer configured to their ranking method, tools, roles and thresholds. Not custom code per customer, which would turn us into a consultancy and hurt viability.
- Also fixed: supplier power high → **medium** (we build parts lists with the customer, so manufacturer concentration hurts less); the Buyers row points back to A.0's five named buyers (no repetition); a one-line "Net" verdict. US-person team vs going abroad → viva sheet.
**Change:** draft A.3; Viva_Prep §9.

### Q45. Review of A.4 (1 Oct): "Add the flight-software lead, a persona quote, and drop the repeated Sanchez cite. Remove 'US' from the persona: a CISO / VP Security isn't limited to the US."
**Reasoning:**
- *Remove US:* **agreed, with one hook kept.** The persona is now "a mid-size operator that also serves US defence customers". The nationality goes, but the US-defence link stays, because A.3's beachhead rests on NIST SP 800-171 (it comes with DoD contracts, which non-US operators can hold too). Two of the five named buyers are European (SES, ICEYE), so this is more consistent.
- Also: the flight-software lead added to the buying committee (reads the *what* brief; can block adoption); an illustrative persona quote; the psychographic points back to A.2 instead of repeating Sanchez.
**Change:** draft A.4; Viva_Prep §9.

### Q46. Review of A.5 (1 Oct): "Logging overrides and reviewing them isn't enough against model poisoning; test in simulation, or even on a decommissioned satellite, and count it as a cost. What does the CCPA line actually mean? If the only personal data is staff names, is CCPA worth the space?"
**Reasoning:**
- *Poisoning:* **agreed that logging alone isn't enough.** (The world model never runs on a real satellite; it only predicts, and the agent has no route to command systems, so poisoning skews rankings rather than hurting satellites.) Fix: vetted training data and overrides, plus a release test in simulation for every retrained model: replayed attacks (NOS3-style, RF 32), held-out logs, and a fixed set of known critical flaws it must still rank high (the tripwire). Backstop: the authority rule (the AI can only raise), so a poisoned model can't push a flaw below layers 1–2. Release tests are added to the close's viability line as a running cost.
- *Decommissioned satellites:* kept out. They're rarely offered, commanding them carries risk (debris, licence terms), and we have no source.
- *CCPA:* explained. The old line covered terminal data, which Stage 1 never touches; telemetry is machine data; the only personal data is staff names in the audit trail. **Pushback on dropping it:** the rubric's US option names CCPA/CPRA, so one short line stays (same length as before).
- Also: Zillow and Cruise get a clause each; GDPR (if we go to Europe) goes to the viva sheet; the repetition pass is deferred to the end.
**Change:** draft A.5 and close; Viva_Prep §9.

### Q47. Review of the close (1 Oct): "Doesn't 'impact prediction is unproven' make it sound unfeasible? Why is viability the weakest point? Don't claim customers 'want a copilot'; we're a facilitator, not a replacement. What does 'the onboarding fee pays for the engineers' mean?"
**Reasoning:**
- *Feasibility:* **agreed, a wording problem.** It now opens with what's proven (layers 1–2 on existing tools; learned spacecraft models exist, Hundman 2018), then the one open question (damage from never-seen command sequences), the tests, and the fallback (rank on exposure and scores).
- *Viability:* it's weakest because it rests mostly on assumptions: ~5 named buyers, people-heavy onboarding, slow trust-based sales, compliance and upkeep costs, and no sourced price (Q29). The other lenses have evidence. It's now framed as "the biggest risk, and how we manage it".
- *Desirability:* **agreed.** No claim about what customers want (no survey). It states the need (formal programs, rising volume, undefined "timely") and our role (a copilot that supports, not replaces).
- *Onboarding fee:* the one-time fee covers the engineers' setup work (parts list, reach map), so each new customer doesn't start at a loss before the yearly subscription pays back. Like a security system's installation fee.
- Also: the 2 a.m. bookend now says the CISO approves the work-around *the flight-software brief suggests* (Stage 1 doesn't plan fixes).
**Change:** draft close.

---

## 5. Questions Claude Asked Me

| # | Question | My answer |
|---|---|---|
| 1 | Which broad area: Regulated / Lightly regulated / No preference? | **Regulated (high stakes)** |
| 2 | What domain familiarity or experience do you have? | **BTech CS & Applied Maths; low-level systems research; learning cloud** |
| 3 | Which option do you want (1/2/3 or other)? | Challenged the recommendation instead; eventually chose option 1 (satellites) |
| 4 | Lock in option 1, or search competitors first? | **Search competitors first** |
| 5 | Lock in the sharper version, or test Agentic Commerce against the same questions? | Raised further challenges |
| 6 | Where should the report go? | **Markdown file in the project folder** |
| 7 | Jurisdiction: US, UK or India? | Asked for a recommendation → **US recommended**, confirmation pending (see Q16) |
| 8 | Record US or India in the report? | "Save this" → saved US as the recommendation |

---

## 6. Competitive Landscape Found

| Area | Players | Relation to us |
|---|---|---|
| On-orbit intrusion **detection** | **Deloitte Silent Shield** (out-of-band, one-way diode, can't command the satellite; Deloitte-1 launched Mar 2025; Project Constellation with 8 Spire-built satellites), Proof Labs, BigBear.ai, Redwire; **SpaceCOP** (DHS S&T + Aerospace Corp, planned open source); Aerospace Corp SPARTEND | **Complementary.** Handles attacks in progress. Deloitte is a possible **new entrant** and consulting substitute. |
| Satellite **digital twins** for cyber testing | Booz Allen (GPS IIR cyber test bed), Zendir; academic runtime-verification twins (IEEE) | Partial; test environments, not autonomous patch validation |
| **Rapidly updatable satellites** | Hypergiant with the US Air Force | An enabler, not a vendor we depend on |
| Generic **firmware / vulnerability management** | AMI VMS/SBOM, Nucleus Security | General-purpose; no orbit, pass window or power awareness |
| **Space risk scoring research** | Aerospace Corp SPARTA Notional Risk Scores; SatGuard (MDPI, LLM-based pen-testing and risk assessment) | Frameworks and research, not products; good references |
| Large operators' **in-house teams** | e.g. SpaceX | Build their own; not the target market |
| Generic enterprise vulnerability management (mentioned from model knowledge) | Tenable, Qualys, Palo Alto Networks; OT security e.g. Claroty | Why the generic idea failed the novelty rule; the novelty-dilution risk |

**Positioning statement:** *"Detection exists. Nobody turns known flaws into safe, orbit-aware patch decisions across the whole mission."*

---

## 7. Refined Company Concept (current state)

### 7.1 Problem
Satellite operators carry a growing backlog of known flaws across ground stations, networks, radio links, spacecraft and user terminals. They can't patch satellites like laptops: uplinks are limited to ground-station pass windows and power budgets, a bad patch can brick a satellite worth crores, and a ground flaw can cascade into the fleet (Viasat 2022). Triage today is slow manual work by small, expensive teams.

### 7.2 What the company does
Decides **which flaws matter, what the safest fix is, when and where to apply it, and whether it worked**, with humans approving every in-orbit action.

### 7.3 AI architecture
```
Advisories / CVEs / SBOMs ──► LLM agent (existing model + retrieval) ──► "Flaw X affects component Y on sats 12, 47, 88"
                                                                         │
Telemetry from all fleets ──► JEPA-style world model (custom core) ◄─────┤ "Effect if exploited? Effect if patched?"
  (federated; raw data never leaves the operator)                         │
                                                                         ▼
                                 Constrained RL rollout planner (trained inside the world model)
                                                                         │
                                   Human approval ──► Uplink ──► World model monitors ──► Rollback?
                                                                         │
                                            Outcomes feed back into the world model (flywheel)
```
Supporting pieces: predictive ML for in-orbit exploitability (transferred from ground data), anomaly detection for rollback, an explanation layer for JEPA decisions, and scheduling optimisation (not AI; supporting only).

### 7.4 Fix ladder
Vendor patch → workaround without new code → ground-side fix → accept and monitor → AI-drafted patch (**suggestion to manufacturer only**).

### 7.5 Moat (final form)
*(**Superseded 2026-09-30** — see Q18, Q22 and RF item 7. Point 1's cross-fleet pooling is now a conditional upside; the patch-outcome record + switching costs lead. Point 2's manufacturer partnerships are unsupported by evidence — see review R13/R14.)*
1. **Pooled patch outcomes and anomaly behaviour across fleets**: weak early, strong at scale.
2. **Manufacturer partnerships and mission-control integrations**: the early moat.
3. **Neutrality**: no operator can offer this to rivals.
4. **Deployment protection**: hosted core, federated local models, encrypted/watermarked weights on-prem, contracts and trade secrets.

### 7.6 Target customer
**Mid-size commercial constellation operators** (roughly 50–300 satellites, small security teams). Expansion: satellite manufacturers, ground-station-as-a-service providers, space insurers, government/defence space agencies (B2G). Not the target: mega-operators such as SpaceX.

### 7.7 Why customers pay
Continuous triage, regulatory evidence, insurance support, and premium protection against rare catastrophic events.

### 7.8 Governance hooks already identified
- Humans approve every uplink; the RL agent only proposes.
- Abort and rollback rules based on world-model anomaly signals.
- AI-drafted patches are never uplinked.
- Explainability layer for opaque JEPA predictions.
- Federated learning + differential privacy + secure aggregation for customer data.
- No single operator dominates training data.

---

## 8. Mapping to the Rubric Sections (head start)

| Section | Material already available |
|---|---|
| **0. Overview** | Viasat hook; LEO growth (~16k satellites); software-defined satellites; ground-to-space risk; regulatory pressure |
| **1. Agentic AI & Value** | Multi-step loop: ingest → map → score → twin-test → plan → approve → uplink → monitor → rollback. Value: small team covers a large fleet; fewer bricked satellites; faster triage; compliance evidence |
| **2. Moat** | §7.5; data pyramid; "remove the AI — what breaks?" |
| **3. Porter's Five Forces** | **Buyers:** few and concentrated → high power. **Suppliers:** satellite manufacturers (parts lists, patches), ground-station providers, compute. **Rivalry:** low today (a gap), adjacent detection players. **Substitutes:** Deloitte/Booz Allen consulting, in-house teams, doing nothing. **New entrants:** Deloitte, defence primes, OT-security vendors |
| **4. Persona & Journey** | Mid-size operator's security or mission-operations lead; pains: backlog, bricking fear, tiny team, regulators. Journey: design partner → federated onboarding → shadow mode → approved automation → renewal. *Needs full mapping* |
| **5. Governance** | §7.8; jurisdiction still to choose |

---

## 9. Still Unanswered / Open Questions

### 9.1 Decisions I still need to make
1. **Jurisdiction:** **US recommended** (see Q16); India is the alternative. Confirm the final choice. Still to work out under the US: which NIST AI RMF actions map to each guardrail, how CCPA/CPRA applies to subscriber-terminal data, and how ITAR/EAR shapes federated learning with foreign operators.
2. **Company name, mission, vision.**
3. **Submission format** (document, slides, video, or a mix).
4. **Exact persona**: job title, company size, region.
5. **Scope boundary**: how much ground-segment coverage before the novelty dilutes?
6. Confirm whether "JEW" meant **JEPA** (assumed).
7. Confirm what "hiring me" meant (assumed: customers paying for the platform).

### 9.2 Business questions not yet worked out
8. *(→ Q24, task T1)* **Pricing model**: per satellite, per fleet tier, or enterprise licence? The "crores per year" figure is unvalidated.
9. *(→ Q24, task T3)* **Market size in revenue terms**: how many mid-size operators exist, and what's the realistic total addressable revenue?
10. **Manufacturer incentives**: why would manufacturers share parts lists and patches or resell us?
11. **Design partners**: who are the first 2–3, and what do they get?
12. **Go-to-market** sequence: commercial first, or government first?
13. Revenue from **space insurers**: is it realistic?

### 9.3 Technical questions not yet worked out
14. Is public data (ESA anomaly benchmark, OPS-SAT) enough to bootstrap the world model?
15. How is transfer of exploitability prediction from ground systems to space validated?
16. How is the **JEPA explanation layer** designed so operators and regulators trust it?
17. How do federated updates handle very different satellite platforms in practice?
18. **Data deletion / "unlearning"** when a customer leaves or withdraws consent (relevant under DPDP/GDPR).
19. Deployment for defence customers who refuse to contribute data.

### 9.4 Governance questions not yet worked out
20. *(→ Q25, task T4)* Concrete **escalation thresholds**: when must the agent stop?
21. **Who** at the operator approves which class of action?
22. **Audit trail** format and safety audit cadence.
23. *(→ Q25, task T6)* Liability when an approved patch still bricks a satellite.

### 9.5 Things that can't be fully verified
24. Whether a **stealth startup or classified programme** already does this.
25. ~~Whether the professor accepts a niche inside a sub-topic.~~ **Resolved (17 Sept):** the official DES530 topic-selection sheet states *"Multiple students may select the same topic... Topic selection does not reserve an idea or solution. Students are expected to develop their own company and approach within the selected topic."* Topic submitted on the sheet.
    - **New implication:** other students may pick Day-Zero Vulnerability Prioritisation too, so the satellite-mission angle is what differentiates this submission. Keep the idea private until submission.

### 9.6 Drafting tasks (added 2026-09-30, from Q24–Q25 and the red-team review)
Design and framing decisions to make while drafting. These are **not new research** (Q23 decision).
- [ ] **T1 — Revenue model (A.0/A.3):** one line: buyers × annual contract value, with the assumption shown, plus the break-even customer count. Value-based anchor (≈$460K–640K/yr team-time saving for an SES-scale team, or a $0.5M–1M avoided smallsat loss). State that per-host analogues (item 28) give the structure only. Name it as the weakest point.
- [ ] **T2 — Cost structure (A.2/A.3):** state that people, per-customer integration, per-bus twins and compliance dominate cost, and that compute is minor (event-driven inference, small telemetry). Flag it as reasoning, not sourced figures.
- [ ] **T3 — Honest buyer count and expansion path (A.3/A.4):** the 6 named in-range operators (item 11) minus Globalstar (item 31), then the widening segments (government programmes, ground-station-as-a-service, manufacturers pre-launch). No unsourced "dozens"/"~200".
- [ ] **T4 — Stop rules + approval matrix (A.5):** 3–5 concrete halt rules (e.g. world-model anomaly score over a threshold after the canary; any telemetry loss after uplink; model confidence under a floor; a flaw touching the command-authentication path → human-only) and who approves which class of action.
- [ ] **T5 — The unrecoverable-action class (A.1/A.5):** never auto-schedule command/boot/auth-path changes; A/B partition + watchdog fallback as a precondition; canary on the least-critical satellite; limit how far a bad patch can spread.
- [ ] **T6 — Liability position (A.5):** wording is "decision support with evidence and stated residual risk", not a warranty; contractual cap; the manufacturer warrants its own patch; the audit trail (item 24) is the evidence. Remove "fully tested" language everywhere.
- [ ] **T7 — Remaining review top-5 (`research/Research_Findings_Review.md`):** R6/R17 (what the model can know, and how to evaluate it), R25/R26 (one first customer; the SBIR contradiction between items 10/15 and 17), R13/R14 (dependence on manufacturers).
- [ ] **T8 — Quick number fixes before citing:** R10 (57,908 CVEs is year-to-date through Aug 31, not annual), R2 (Starlink share: use one source's denominator), R7 (item 6 says "no automated rollback documented", contradicted by items 14/31), plus the stale TB figures listed in R2.

---

## 10. Claims Stated from Model Knowledge — Verify Before Citing

These came from Claude's general knowledge, **not** from the web searches in this session:
- Generic vulnerability management leaders: Tenable, Qualys, Palo Alto; OT security: Claroty; medical-device security: Medcrypt, Asimily.
- Agent payment rails by Visa, Mastercard, Stripe, Google.
- ~40,000 CVEs published per year.
- **EU NIS2** lists space as a critical sector; the **proposed EU Space Act** includes cybersecurity rules; **US Space Policy Directive-5**; **CERT-In** 6-hour incident reporting (India).
- **India Patents Act s.3(k)** limits software patents.
- Google Gboard uses federated learning.
- AWS Ground Station and KSAT as rentable ground stations.
- *(Jurisdiction analysis, Q16)* NIST AI RMF's four functions (Govern, Map, Measure, Manage); **NIST IR 8401** scope (satellite ground segment); **SPD-5** content; **ITAR/EAR** limits on sharing spacecraft technical data with foreign persons; IN-SPACe authorisation and Indian Space Policy 2023; UK Space Industry Act 2018; the UK GDPR Art. 22 scope.

---

## 10.1 §10 Claims Resolved (2026-09-29 research pass)

Full sourced detail in `research/Research_Findings.md`. Status of each §10 claim:

| Claim | Status | Correction |
|---|---|---|
| ~16,000–17,000 active satellites | **Corrected** | **14,266** (SIA 29th Annual Report, end-2025, primary) |
| ~40,000 CVEs/year | **Corrected — stale, not wrong** | 40,009 was the **2024** figure; 2026 run-rate is **~58,000/year** |
| ~40% of small-sat missions failed | **Confirmed, reword** | Real (Langer & Bouwmeester, AIAA/USU 2016), but framed as "since 2000" / "within 2 years of launch," not "last 20 years" |
| Generic vuln-mgmt leaders (Tenable, Qualys, Palo Alto, Claroty, Medcrypt, Asimily) | Not re-verified this pass | Low-stakes, general industry knowledge — fine to keep |
| Agent payment rails (Visa, Mastercard, Stripe, Google) | Not applicable | Belongs to the dropped FinTech option, not the satellite idea |
| EU NIS2 lists space as critical sector | **Confirmed [primary]** | Annex I, sector 11 — ground infrastructure supporting space services |
| Proposed EU Space Act cybersecurity rules | **Confirmed [primary]** | COM(2025) 335 final, Arts. 75–95; not in force before ~2030 |
| US Space Policy Directive-5 | **Confirmed [primary]** | Federal Register 85 FR 56155 — see `research/Research_Findings.md` item 21 for the actual principles |
| CERT-In 6-hour reporting (India) | **Confirmed [secondary only]** | PDF wouldn't render; confirmed via legal-analysis secondary sources — re-verify primary before citing |
| India Patents Act s.3(k) limits software patents | Not re-verified this pass | Low-stakes for the US-jurisdiction path |
| Google Gboard uses federated learning | Not re-verified this pass | Illustrative analogy only, not load-bearing |
| AWS Ground Station / KSAT as rentable ground stations | **Confirmed + deepened [primary/secondary]** | Full pricing-model and supplier-power detail in `research/Research_Findings.md` item 12 |
| NIST AI RMF four functions (Govern/Map/Measure/Manage) | **Confirmed [primary]**, mapped to guardrails | See `research/Research_Findings.md` item 19 |
| NIST IR 8401 scope (ground segment) | **Confirmed [weak sourcing]** | Title/structure primary; specific control text is secondary-sourced — PDF should be re-read directly before final citation |
| ITAR/EAR limits on spacecraft technical data to foreign persons | **Confirmed [primary]** | 22 CFR 120.33/120.16, "deemed export" doctrine — the federated-learning cross-border argument is legally well-grounded, not just plausible |
| IN-SPACe authorisation, Indian Space Policy 2023 | **Confirmed [primary]** | Non-Indian entities must go through an Indian subsidiary/JV |
| UK Space Industry Act 2018 / GDPR Art. 22 scope | Not re-verified this pass | UK path already rejected; low priority |

**New finding not in the original list:** a **Satellite Cybersecurity Act of 2025 (S.3404)** is pending in the US Congress — add as regulatory-tailwind context. SBIR/STTR statutory authority **lapsed 30 Sept 2025** and was not renewed in the FY2026 NDAA — any "government funding channel" or SpaceWERX/AFWERX argument needs this caveat.

---

## 11. Appendix Material (ready to use)

### 11.1 Candidates for "most difficult concept"
1. **Defensibility / moat (strongest candidate).** It evolved through five versions:
   "glue between vendors" → "cross-operator data" → "photograph vs live feed" → *(my challenge: the thief keeps its own feed)* → "pooled rare events" → *(my challenge: are there enough failures?)* → **"pooled patch outcomes and anomaly behaviour, bootstrapped by self-supervised learning on normal telemetry and simulation."**
2. **How AI-centred the product really is:** rule-based scheduler vs LLM-only vs custom foundation model (JEPA + constrained RL + existing LLM + human approval). Chose the hybrid: build custom only where it creates the moat.
3. **Scope:** orbit-only (novel but narrow) vs whole-mission (realistic but risks being generic). Chose whole-mission with a space-specific core.
4. **Autonomy:** a fully autonomous uplink was rejected; the RL agent proposes, a human approves, and AI-drafted patches are never uplinked.

### 11.2 Accepted / Modified / Rejected / Independently developed
| Status | Item |
|---|---|
| **Accepted** | Satellite niche inside Day-Zero Vulnerability Prioritisation; the fix ladder; the data pyramid; mid-size operators as the target |
| **Modified (by my challenges)** | Vendor-glue moat → decision layer + data; orbit-only → whole mission; scheduler-centred → world-model-centred AI; "photograph" moat → rare events → pooled patch outcomes; detection vendors "just alert" → detailed but complementary |
| **Rejected** | Generic vulnerability management (not novel); implanted medical devices (not on the list, competitors nearby); Hypergiant as a required partner; AI-generated patches uplinked directly; training a custom LLM for documents; RL exploring on real satellites |
| **Independently raised by me** | "No existing company" constraint; integrating vendors as a substitute; detection vendors' depth; JEPA / custom RL architecture; who actually writes the fix; internal teams; resale protection; the thief's own data feed; whether failure data is sufficient |

### 11.3 Transcript
Save this conversation's link as **transcript #1** for the appendix. One more transcript is needed (e.g. from the drafting or Porter's analysis session).

---

## 12. Recommended Reading (before drafting)
1. **NIST IR 8270**: Introduction to Cybersecurity for Commercial Satellite Operations.
2. One **Viasat KA-SAT** analysis (ResearchGate lessons-learned paper or the SPARTA breakdown).
3. **Aerospace Corp SPARTA** and the Notional Risk Scores paper.
4. **IEEE: Patch Management of Satellite Flight Software.**
5. *(Architecture)* MTS-JEPA paper, for time-series world models.

Candidate **key references** (non-blog): NIST IR 8270; SPARTA risk-score paper (arXiv 2402.02635); SatGuard (MDPI Aerospace 12/5/431); IEEE satellite patch management (9659638); ENISA commercial satellite security guide; Viasat lessons-learned paper.

---

## 13. Sources (from this session's web searches)

**Satellite security, competitors, research**
- [SatGuard: Satellite Networks Penetration Testing and Vulnerability Risk Assessment (MDPI)](https://www.mdpi.com/2226-4310/12/5/431)
- [Rethinking Satellite Security in the COTS Era (ESA)](https://indico.esa.int/event/528/attachments/5988/10198/Orbital_Shield_Rethinking_Satellite_Security_in_the_Commercial_Off_the_Shelf_Era.pdf)
- [NIST IR 8270: Cybersecurity for Commercial Satellite Operations](https://nvlpubs.nist.gov/nistpubs/ir/2023/NIST.IR.8270.pdf)
- [NCCoE Cybersecurity for the Space Domain (NIST)](https://www.nccoe.nist.gov/cybersecurity-space-domain)
- [ENISA: Securing Commercial Satellite Operations](https://www.enisa.europa.eu/news/from-cyber-to-outer-space-a-guide-to-securing-commercial-satellite-operations)
- [Towards Principled Risk Scores for Space Cyber Risk Management (arXiv)](https://ar5iv.labs.arxiv.org/html/2402.02635)
- [Aerospace Corporation: Software Cybersecurity](https://aerospace.org/software-cybersecurity)
- [Aerospace SPARTEND autonomous detection](https://aerospace.org/article/aerospaces-spartend-integrates-space-cyber-threat-knowledge-autonomous-detection)
- [Cybersecurity in Orbit (Aerospace Corporation)](https://aerospace.org/article/cybersecurity-orbit-how-aerospace-evolving-defenses-against-emerging-space-threats)
- [The Newest Space Race Is Cyber (GovInfoSecurity)](https://www.govinfosecurity.com/newest-space-race-cyber-a-31717)
- [The Space Industry's 5 Billion Dollar Blind Spot](https://blog.spacecomputer.io/the-5-billion-blind-spot-in-space-cybersecurity/)
- [AMI Vulnerability Management / SBOM](https://www.ami.com/products/vms-sbom/)
- [Nucleus Security](https://nucleussec.com/)
- [Satellite Cybersecurity Across Orbital Altitudes (arXiv)](https://arxiv.org/pdf/2512.21367)

**Deloitte / Silent Shield**
- [Deloitte Builds Silent Shield (PR Newswire)](https://www.prnewswire.com/news-releases/deloitte-builds-silent-shield-to-detect-cyberattacks-on-satellites-302517241.html)
- [The race to defend satellites from cyberattacks (SpaceNews)](https://spacenews.com/deloittes-payloads-will-test-whether-satellites-can-defend-themselves/)
- [Spire to build eight satellites for Deloitte (SpaceNews)](https://spacenews.com/spire-to-build-eight-satellites-for-deloittes-on-orbit-cybersecurity-program/)
- [Spire to Build 8 Satellites for Silent Shield (Via Satellite)](https://www.satellitetoday.com/cybersecurity/2025/12/01/spire-to-build-8-satellites-for-deloittes-silent-shield-cyber-mission/)
- [Deloitte Selects Spire (Business Wire)](https://www.businesswire.com/news/home/20251201002992/en/Deloitte-Selects-Spire-to-Deliver-Advanced-Satellite-Capabilities-Expanding-Their-On-Orbit-Cyber-and-Data-Operations)
- [Deloitte Launches Two New Satellites (ExecutiveBiz)](https://www.executivebiz.com/articles/deloitte-satellite-launch-project-constellation)
- [New Satellite Will Train Cyber Defenders (Air & Space Forces)](https://www.airandspaceforces.com/new-satellite-cyber-attack-training/)

**Updates, patching, digital twins**
- [USAF satellites get fast software updates (Military Aerospace)](https://www.militaryaerospace.com/trusted-computing/article/14179959/satellites-update-software-cyber-security)
- [Patch Management of Satellite Flight Software (IEEE)](https://ieeexplore.ieee.org/document/9659638/)
- [Is Running Untrusted Code on a Satellite a Good Idea?](https://gazagnaire.org/blog/2026-02-25-satellite-software.html)
- [ESA Cluster On-Board Software Maintenance Concept](https://www.esa.int/esapub/bulletin/bullet91/b91deni.htm)
- [NASA SSRI Knowledge Base: Flight Software Development](https://s3vi.ndc.nasa.gov/ssri-kb/topics/27/)
- [The Software-Defined Future of Satellites (Via Satellite)](https://interactive.satellitetoday.com/the-software-defined-future-of-satellites/)
- [Securing Space with Digital Twin Technology (Booz Allen)](https://www.boozallen.com/markets/space/securing-space-with-digital-twin-technology.html)
- [How digital twins are transforming the space industry (Zendir)](https://zendir.io/latest-news/digital-twins-transforming-space)
- [Digital Twin Runtime Verification Framework for Satellites (IEEE)](https://ieeexplore.ieee.org/document/9763796/)

**Viasat KA-SAT attack**
- [Three Years Post KA-SAT Attack (Via Satellite)](https://www.satellitetoday.com/cybersecurity/2025/07/24/three-years-post-ka-sat-attack-viasat-exec-talks-lessons-learned-on-cybersecurity-posture/)
- [Space Cybersecurity Lessons Learned from the ViaSat Cyberattack (ResearchGate)](https://www.researchgate.net/publication/363558808_Space_Cybersecurity_Lessons_Learned_from_The_ViaSat_Cyberattack)
- [Five Takeaways From the Russian Cyber-Attack on Viasat (Infosecurity Magazine)](https://www.infosecurity-magazine.com/news/takeaways-russian-cyberattack/)
- [Lessons from the Viasat Cyberattack: SPARTA Analysis (Pwnsat)](https://pwnsat.org/blog/lessons-from-the-viasat-cyberattack-a-sparta-framework-analysis/)

**AI architecture (JEPA, anomaly detection)**
- [MTS-JEPA: Multi-Resolution JEPA for Time-Series Anomaly Prediction (arXiv)](https://arxiv.org/html/2602.04643v1)
- [V-JEPA v2 for Satellite AOI Monitoring (SSRN)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6521219)
- [Toward Deployable Satellite Anomaly Detection: ESA-ADB Benchmark (arXiv)](https://arxiv.org/pdf/2607.07335)
- [OPS-SAT benchmark for satellite telemetry anomalies (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12041257/)
- [awesome-jepa (GitHub)](https://github.com/AbdelStark/awesome-jepa)

**Market size and failure statistics**
- [How Many Satellites Are in Orbit? (Orbital Radar)](https://orbitalradar.com/how-many-satellites-in-orbit)
- [Satellites by Operator 2026 (Orbital Radar)](https://orbitalradar.com/satellites-by-operator)
- [How Many Satellites Are in Orbit? September 2026 (azmth)](https://azmth.space/stats)
- [How Many Satellites Are in Space? A 2026 Guide (SpaceNexus)](https://spacenexus.us/blog/how-many-satellites-in-space-2026)
- [Why Satellites Fail? It's Not (Only) the Hardware](https://spaceagency.prowly.com/404102-why-satellites-fail-its-not-only-the-hardware)
- [Satellite Reliability: Statistical Data Analysis and Modeling (AIAA)](https://arc.aiaa.org/doi/pdf/10.2514/1.42243)
- [SatAIOps: Full Life-Cycle Satellite Network Operations (arXiv)](https://arxiv.org/pdf/2305.08722)
