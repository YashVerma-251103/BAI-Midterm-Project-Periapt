# Research Findings — Red-Team Review

**Date:** 2026-09-30
**Purpose:** list every weak, unsupported or internally inconsistent claim in `research/Research_Findings.md` (items 1–30) that a sharp grader or viva panel could use to raise doubts. This is a list of doubts, not answers.
**Method:** each item was checked against (a) the evidence it cites and whether that evidence fits the claim's scope and population, (b) the raw subagent outputs in `research/raw/01–06`, for caveats the summary dropped, (c) `topic/Topic_Brainstorm_Report.md` (§4 Q&A, §7, §10/§10.1), for contradictions with the concept, (d) the other items, and (e) the rubric (`brief/Instructions.md` §A). Outside facts are phrased as questions to research, not asserted.
**Citations:** `RF` = `research/Research_Findings.md`, `TB` = `topic/Topic_Brainstorm_Report.md`, `raw/0N` = `research/raw/0N-*.md`. Line numbers are as of this date.

---

## Known (already raised, not re-derived here)

- **K1 — Regulation cuts both ways.** There is no binding US vulnerability-management mandate (item 30), so "legally bound customers" is false.
- **K2 — Item 7 is not a moat.** Public data proves feasibility for competitors too. Already corrected in the file.
- **K3 — SPARTA differentiator.** "Static vs live" is wrong because SPARTEND already delivers SPARTA to orbiting assets. The real difference is reference vs decision-and-execution.
- **K4 — In-house substitute.** The "3-person team, 300 satellites" line (TB Q8) is unsourced, and Spire sells its own On-Orbit Update Manager.
- **K5 — Federated incentives.** Why would operators feed a model that helps rivals? This covers free riders, leakage, and ITAR splitting the pool.

---

## A.0 Company Overview

**R1 — The growth story is mega-constellation growth, not target-segment growth [Items 1, 11] [severity: medium]**
- *Claim / assumption:* the sector is "ripe" based on 4,434 satellites deployed in 2025 (+65%) and broadband subscribers +62% (RF:10).
- *Why it's doubtful:* raw/01:70 says the subscriber growth was "driven by LEO constellations", and raw/01:71 says Starlink alone is ~9,900+ satellites. Both headline growth figures come from the segment TB §7.6:307 excludes ("Not the target: mega-operators such as SpaceX"). Nothing in the findings measures growth in the 50–300-satellite segment.
- *Question a grader would ask:* "Your market-growth numbers are Starlink's. What is the growth of *your* customer segment?"
- *What would resolve it:* research mid-size operator counts over time (e.g. Orbital Radar history), or reframe the evidence: growth makes software-defined fleets normal and raises risk for everyone, while the buyable market stays small (see R21).

**R2 — Satellite-count numbers don't reconcile across files [Items 1, 11; TB Q13, §8] [severity: low]**
- *Claim / assumption:* 14,266 operational satellites (RF:10), Starlink ~9,900+ at "~53% of all payloads" (RF:75), and "SpaceX ~54%" (TB:203).
- *Why it's doubtful:* 9,900 / 14,266 ≈ 69%, not 53%. The 53% must use a different denominator, since Orbital Radar counts all tracked payloads live while SIA counts operational satellites at end-2025. The body of TB still has stale figures that §10.1 corrected: "~16k satellites" (TB:326), "~16,000 active satellites" and "~40,000 CVEs/year" (TB:194, 198), and "~40%… last 20 years" (TB:195). A draft that pulls from TB §4/§8 will reintroduce them.
- *Question a grader would ask:* "Is Starlink 53% or 69% of the market? Which count are you using?"
- *What would resolve it:* use one source and date per number. Don't combine SIA with Orbital Radar percentages, and search-and-replace the stale TB figures before drafting.

---

## A.1 Agentic AI & Value Proposition

**R3 — The flagship incident was "immaterial" to its victim, which weakens urgency and willingness to pay [Item 4] [severity: high]**
- *Claim / assumption:* the Viasat KA-SAT attack is the hook (TB Q8:156, TB §8:326), and item 4 honestly reports the 10-K's "no material impact" (RF:26).
- *Why it's doubtful:* the finding is honest, but its implication isn't followed through. If the most-cited satellite cyberattack was financially immaterial to the operator, a CFO can argue that the expected loss from cyber risk is small. With K1 (no mandate), neither the loss argument nor the compliance argument currently justifies a budget line.
- *Question a grader would ask:* "Viasat itself says the attack didn't matter financially. Why would an operator pay you?"
- *What would resolve it:* move the value case to (a) the downstream disruption (5,800 turbines, 30,000 modems, RF:26) as societal and reputational cost, and (b) asset-loss avoidance (R4). Also research whether any operator has disclosed insurance premium or coverage effects from cyber posture (TB §9.2 Q13 is still open).

**R4 — "What a bricked satellite is worth" uses the wrong population and has no base rate [Items 4, 14] [severity: high]**
- *Claim / assumption:* "~$0.5–1M+ per constellation-class smallsat" (RF:27).
- *Why it's doubtful:* (1) The $500K figure is a 3U CubeSat from Sky and Space Global, sourced from Wikipedia and a NanoAvionics vendor blog (raw/01:84–89). The target list (Planet, Iridium, SES, Intelsat; RF:75) spans very different satellite classes, and no figure is given for them. (2) A value per satellite is useless without a probability. No finding estimates how often a patch bricks a satellite. (3) The only rate evidence points the other way: SpaceX lost "zero satellites… across 200+ updates" (RF:83). That weakens the "bricking fear" pain point (TB §8:330) and the patch-risk-prediction value proposition.
- *Question a grader would ask:* "How many satellites have actually been lost to bad patches? If SpaceX lost none, what risk are you pricing?"
- *What would resolve it:* research documented patch- or software-update-induced losses and anomalies. If the count is near zero, reframe the value around *speed and coverage of triage*, with brick risk as a tail risk, and say so.

**R5 — The Viasat hook motivates the non-differentiated half of the product [Item 4; TB Q8, Q9] [severity: medium]**
- *Claim / assumption:* Viasat justified widening the scope to the whole mission (TB:157), with the space-specific core kept as the novelty (TB:163).
- *Why it's doubtful:* the attack came through "a misconfigured VPN appliance in the ground network… the spacecraft itself was never touched" (TB:156). The fix for that is "ordinary IT patching" (TB:150), which is the generic part of the product that Tenable, Qualys and Nucleus already serve (RF:63). The story's best evidence supports the commodity layer.
- *Question a grader would ask:* "Your hook is a ground-IT misconfiguration. Why wouldn't a generic vulnerability-management vendor have prevented it?"
- *What would resolve it:* argue explicitly that the missing piece was *ground-to-space consequence modelling*, i.e. knowing that this VPN flaw reaches the fleet. Then show that this cross-segment reasoning is what generic tools lack. Otherwise pick a spacecraft-side hook.

**R6 — A telemetry world model cannot "predict the effect of a patch" it has never seen [Items 6, 7; TB §7.3, Q7] [severity: high]**
- *Claim / assumption:* the JEPA world model answers "Effect if patched?" (TB:286) and acts as "a learned digital twin that improves with every patch" (TB:140).
- *Why it's doubtful:* a patch is new code. Telemetry-trained models learn how the existing software behaves, so a code change is out of distribution by definition. The real validation analogue the findings cite is ESA OBSM, which runs the patch on an *emulated target processor* (SdeVF) and then a *full-spacecraft simulator* (SimVF) (RF:35, raw/05:71). Those are code-execution environments built from the manufacturer's design data, not learned telemetry models. No item researched whether any learned model can predict the behavioural effect of a code change.
- *Question a grader would ask:* "How does a model trained on past telemetry know what new flight code will do?"
- *What would resolve it:* reframe. Execution-level validation stays with the manufacturer's emulator or simulator, and the world model does *post-uplink anomaly detection and rollback triggering*, plus *pre-uplink risk scoring from features* (patch size, subsystem touched, past outcomes on similar buses). State this split in the architecture.

**R7 — The "no automated rollback exists" claim is contradicted by the project's own raw findings [Items 6, 10, 12, 14] [severity: medium]**
- *Claim / assumption:* "no documented automated rollback step anywhere in these sources… State this as an acknowledged limitation, not a solved problem" (RF:36).
- *Why it's doubtful:* raw/02:49 says Spire's On-Orbit Update Manager advertises "automated rollbacks", and it is sold to other operators. RF:83 and raw/03:113 say SpaceX runs "canary + phased rollout + auto-rollback". The caveat is true only for the NIST and ESA sources. Two more consequences follow. The scheduling and rollout piece of the "whole loop" already exists commercially, which narrows the novelty claim in item 10 (RF:60) to prioritisation and cross-segment decisioning. And Spire is also listed as a target buyer (RF:75) and a supplier (RF:79); see R15.
- *Question a grader would ask:* "Spire already sells automated rollout and rollback to operators. What's left that's yours?"
- *What would resolve it:* correct item 6, and name Spire's update manager alongside SPARTA and CT Cubed as a partial adjacent. Position rollout as *integration with* existing update managers, not a replacement.

**R8 — The RL planner conflicts with the earlier concession that scheduling is optimisation [TB Q6, Q7, §7.3] [severity: medium]**
- *Claim / assumption:* "constrained RL rollout planner (trained inside the world model)" (TB:141, 289).
- *Why it's doubtful:* TB Q6 already conceded that "scheduling is optimisation… not AI" (TB:128), and Q7 then reintroduced RL for the same job. Pass windows, power budgets and staged rollouts form a constrained scheduling problem that a solver can handle exactly. Two more problems: RL trained inside a *learned* model is known to exploit that model's errors, and the world model is weakest exactly on unseen patches (R6). No research item covers either point.
- *Question a grader would ask:* "Why RL rather than a constraint solver? Remove the RL and what breaks?"
- *What would resolve it:* either drop RL for a solver plus a learned risk score (honest, and it passes the TB "remove the AI" test through the risk model), or justify RL by sequential uncertainty (learning rollout order from outcomes) and add a caveat on model exploitation.

**R9 — "Agentic automation" vs "humans approve every uplink": where does the agent act? [Items 18, 19; TB §7.8] [severity: medium]**
- *Claim / assumption:* the journey reaches "shadow mode → approved automation" (TB:330), and item 18's pattern ends in "full enforcement/automation" (RF:99). Humans still approve every uplink (TB:313).
- *Why it's doubtful:* the rubric asks where agentic AI *executes* multi-step work. If every in-orbit action needs a human, the automation stage has to be defined as something else (e.g. ground-side fixes, ticketing, rescheduling). Otherwise the journey's end state contradicts governance. HITL also has an unexamined cost. Approvals must land inside pass windows lasting minutes. A missed approval delays the fix, and time pressure encourages rubber-stamping (automation bias), which weakens the safeguard.
- *Question a grader would ask:* "What exactly does the agent do on its own at full maturity, and what happens if nobody approves before the pass closes?"
- *What would resolve it:* publish an autonomy table (action class → autonomous / approve / never), pre-approval of fix *plans* ahead of the window, and an explicit default when approval is missing: hold, never proceed.

**R10 — CVE volume: the run-rate arithmetic is wrong and the metric doesn't apply to spacecraft [Item 27] [severity: medium]**
- *Claim / assumption:* "update to ~58,000 CVEs/year (2026 run-rate)" (RF:150), repeated at TB:396.
- *Why it's doubtful:* (1) 57,908 is *year to date through Aug 31* (RF:149), about 8 months. Annualised, that is ≈ 87,000, not 58,000. It is also +80% on 2025's 48,185, a jump nobody checked. (2) CVEs track commercial IT and OT software. The findings never establish how many apply to bespoke flight software, so this is a general-industry number presented as a space-sector driver. Like R5, it mostly supports the ground-IT half of the product.
- *Question a grader would ask:* "How many of those CVEs affect a satellite?"
- *What would resolve it:* fix the arithmetic or cite a full-year figure, and re-check the YTD number against cve.org. Scope the claim to "ground-segment software exposure", or research space-specific vulnerability counts (e.g. SPARTA or academic flight-software vulnerability studies).

---

## A.2 Moat & Defensibility

**R11 — The "real pooled moat" data layer has no volume evidence [Item 7; TB Q13] [severity: high]**
- *Claim / assumption:* the durable moat is "a proprietary labelled record of patch-rollout outcomes nobody else can buy" (RF:47), and the patch-outcome layer is "Moderate" in volume (TB:196) and "the real pooled moat".
- *Why it's doubtful:* no item estimates how many flight-software or firmware updates a 50–300-satellite operator actually performs a year, or how many produce a *bad* outcome. If updates are rare and failures rarer (R4: SpaceX had zero losses in 200+), the labels are almost all "success". That class imbalance is too extreme to train a patch-risk model, and it repeats the "rare events" overreach TB Q13 already retracted (TB:190).
- *Question a grader would ask:* "How many patch outcomes does your whole customer base generate per year, and how many are failures?"
- *What would resolve it:* research update frequency (Spire's update manager marketing, the SmallSat "Over-the-Vacuum Update" paper in raw/03:113). Then broaden the label to *any post-update anomaly or degradation* and add the ground-segment patch outcomes, which happen far more often. Be honest about the numbers.

**R12 — The privacy-utility trade-off in DP erodes the very asset the moat rests on [Items 7, 8, 9] [severity: medium]**
- *Claim / assumption:* the durable moat is the federated cross-fleet model (RF:47), protected by DP plus secure aggregation (TB:317).
- *Why it's doubtful:* item 9 says DP's accuracy loss is worst for "small/heterogeneous per-operator datasets — exactly this project's regime" (RF:56, raw/05:131). Item 8 adds per-platform adapters (RF:52), which pushes knowledge into local heads rather than the shared model. Together they suggest the pooled model may add little over each operator's own model, and that is what the moat needs to be large.
- *Question a grader would ask:* "After DP noise and per-fleet adapters, how much does the pooled model actually beat an operator's own model?"
- *What would resolve it:* state it as the key technical risk to the moat, name a measurable test (pooled vs local model on held-out anomalies in design-partner pilots), and consider where DP is really needed (e.g. only on cross-competitor aggregation).

**R13 — The manufacturer "early moat" has no evidence, and the partners are likely entrants [Items 12, 7; TB §7.5, Q8] [severity: high]**
- *Claim / assumption:* "Manufacturer partnerships and mission-control integrations: the early moat" (TB:302). Manufacturers act as "key partners (parts lists, patches, reseller channel)" (TB:153).
- *Why it's doubtful:* item 12 finds **no** manufacturer reselling third-party security tooling (RF:79). Spire sells its own update manager (raw/02:49, i.e. it competes on rollout). Bus makers are being absorbed by primes (Lockheed/Terran, RTX/Blue Canyon, Boeing/Millennium; RF:79), and item 7 lists those same primes as incumbents that entry barriers don't stop (RF:46). The early moat depends on the firms best placed to copy it. TB §9.2 Q10 ("why would manufacturers share?") is still unanswered.
- *Question a grader would ask:* "Why would Lockheed-owned Terran give you its parts lists instead of building this itself?"
- *What would resolve it:* give manufacturers a concrete incentive (lower warranty and support cost, a customer-requested SBOM feed, a revenue share) or drop manufacturer partnerships from the moat list. State the primes as the top new-entrant threat in the Five Forces section.

**R14 — The LLM agent's component mapping needs SBOMs that manufacturers don't publish [Item 12; TB §7.3] [severity: high]**
- *Claim / assumption:* the LLM agent outputs "Flaw X affects component Y on sats 12, 47, 88" (TB:284).
- *Why it's doubtful:* that output needs a per-satellite software and component inventory. Item 12 found SBOM evidence for **one** manufacturer (Thales Alenia, as a Black Duck *customer*, RF:80) and explicitly none for Airbus, Terran, York or Blue Canyon (raw/02:86). Without that input, the first step of the agentic loop has no data. This is also the "digital twin needs proprietary bus models" problem (R6).
- *Question a grader would ask:* "Where does your system get the software bill of materials for a satellite bus?"
- *What would resolve it:* research whether operators receive SBOMs contractually (e.g. do US government procurement SBOM requirements flow down to space buses?). Otherwise add an onboarding step that builds the inventory (manufacturer data package, operator config, binary analysis) and admit it's a cost-to-serve.

**R15 — Spire appears as customer, supplier and competitor [Items 11, 12; raw/02] [severity: low]**
- *Claim / assumption:* Spire is a named mid-size buyer (RF:75), a manufacturer and supplier (RF:79), and a Deloitte satellite builder (TB:262).
- *Why it's doubtful:* its update manager (raw/02:49) overlaps with the rollout piece. Listing it as a target buyer without noting this invites the "why wouldn't Spire just extend its own product?" question. This compounds K4.
- *Question a grader would ask:* "Is Spire your customer or your competitor?"
- *What would resolve it:* treat Spire as the illustrative "co-opetition" case in Five Forces. Don't count it in the buyer pool.

**R16 — The export-control story is overstated and possibly points the wrong way [Items 15/22; TB Q16] [severity: medium]**
- *Claim / assumption:* "ITAR (22 CFR 120.33) covers spacecraft technical data broadly… the federated-learning-avoids-cross-border-data-movement argument is legally well-grounded" (RF:129). The pitch line is "learn from foreign fleets without moving controlled technical data across borders" (TB:233).
- *Why it's doubtful:* (1) The same item says most commercial comms and remote-sensing satellites moved to EAR 9A515 (RF:129), so ITAR is the wrong headline regime for the target customers. (2) The claim that telemetry counts as technical data is an inference ("by extension", raw/04:83), and the deemed-export doctrine is secondary-confirmed only (raw/04:78). Yet the item is tagged "[primary]" and "Confirmed, not just assumed." (3) Direction: a foreign fleet's telemetry isn't US-controlled. The export risk is US-derived know-how going *out*. Whether model weights or gradient updates trained on controlled US data are themselves controlled "technology" was not researched. If they are, the federated model sent to foreign operators is the problem, not the solution. (4) The citation 22 CFR 120.16 vs the linked 120.63 (raw/04:76) suggests renumbered sections, so check which is current.
- *Question a grader would ask:* "Are your trained model weights themselves export-controlled when you ship them to a foreign operator?"
- *What would resolve it:* research EAR/ITAR treatment of ML models trained on controlled data. Lead with EAR for commercial satellites and soften "legally well-grounded" to "consistent with". Alternatively restrict the pool to US and allied (AUS/CAN/UK licence-exempt, RF:129) operators and say so.

**R17 — There is no evaluation method: better prioritisation can't be shown without ground truth [TB Q13, §7.3, §9.3 Q15] [severity: high]**
- *Claim / assumption:* "predictive ML for in-orbit exploitability (transferred from ground data)" (TB:295). Real in-orbit attacks are "Almost none — Evaluation only" (TB:199).
- *Why it's doubtful:* the evaluation set the concept names is almost empty by its own admission. EPSS-style exploitability is learned from IT exploitation in the wild, a different population from spacecraft, and TB §9.3 Q15 (how is the ground-to-space transfer validated?) was never researched. No item proposes a metric showing the platform prioritises *better* than SPARTA scoring or a human analyst.
- *Question a grader would ask:* "How would a customer know your ranking is better than their analyst's?"
- *What would resolve it:* define proxy metrics, e.g. time-to-remediate for flaws later exploited on the *ground* segment (observable), agreement with red-team results in the twin or cyber range, backtesting against Space ISAC advisories, and analyst hours saved at equal coverage. State that space-side exploitability transfer is an open validation risk.

---

## A.3 Porter's Five Forces

**R18 — Supplier power was assessed from the operator's side, not the company's [Item 12] [severity: high]**
- *Claim / assumption:* "Verdict: low-to-moderate, trending moderate" (RF:79).
- *Why it's doubtful:* the research prompt asked whether a supplier has "high bargaining power over a **mid-size operator**" (raw/02:14). The verdict describes the customer's supply chain. In a Five Forces analysis of *this company*, the suppliers are the holders of the inputs it needs: bus manufacturers (SBOMs, simulators, patches; R6, R14), the operators' own telemetry, and LLM and compute providers (R30). Those look *high* power: few, consolidating, and in some cases direct competitors (R13).
- *Question a grader would ask:* "Whose suppliers are these, yours or your customer's?"
- *What would resolve it:* redo the supplier force for the company. Manufacturers' design data is the high-power input and GSaaS is low-power (keep the Atlas/AWS evidence). The strategic point is that supplier power is why manufacturer incentives (R13) matter.

**R19 — The buyer pool is ~6 named firms of mixed types, and "dozens" is unsourced [Item 11; TB Q13, §7.6] [severity: high]**
- *Claim / assumption:* target = operators with 50–300 satellites (TB:307). The first market is "dozens of customers" out of "~200 distinct operators" (TB:203).
- *Why it's doubtful:* item 11 names **six** in range, one of them borderline (RF:75), from a secondary tracker. "~200 operators" and "dozens" have no source in the findings. The six are also unlike each other: GEO fleets (SES, Intelsat) of very different satellite classes versus LEO smallsats (Planet, Spire). Some may be headquartered outside the US, which matters for the US-jurisdiction and export-control story (verify HQ locations). Planet may build its own satellites (verify), which would make it a likely in-house builder like SpaceX (RF:83).
- *Question a grader would ask:* "Name your first ten customers."
- *What would resolve it:* count operators properly (e.g. 10–300 satellites, split US and non-US, LEO and GEO) from one tracker with a date. Widen the segment explicitly (government programmes, ground-segment-as-a-service providers, TB:307 expansion) and state the resulting count honestly.

**R20 — Price and willingness to pay: the only analogues imply a tiny contract value [Items 28, 5; TB Q13, §9.2] [severity: high]**
- *Claim / assumption:* "high price per customer is necessary" (TB:203), and "crores per year" (TB:347, unvalidated). Pricing structure analogues are CrowdStrike and Datadog (RF:153).
- *Why it's doubtful:* item 28 gives a *structure* but no *price level*. Datadog's $15–41/host/month × 200 satellites × 12 ≈ $36K–$98K/yr, which is Planet-scale revenue at SaaS per-asset rates. The analyst-replacement anchor (RF:31) caps the savings argument near one analyst salary ($115–159K) per operator. SPARTA and the CISA recommendations are free (RF:61, 83) and anchor the prioritisation piece at zero. With ~6–dozens of buyers (R19), total revenue may not support a company that also carries clearance, ITAR and SME costs (R22). No unit economics exist anywhere in the findings.
- *Question a grader would ask:* "What does one customer pay per year, and how many do you need to break even?"
- *What would resolve it:* build a one-line revenue model (buyers × annual contract value) with the assumption shown. Price on value at risk (fleet value × risk reduction) or on a per-mission/enterprise tier rather than per satellite. Say explicitly that the per-host analogues give the structure only, not the level.

**R21 — The substitutes evidence is secondary and mixes terminals with satellites [Item 14] [severity: medium]**
- *Claim / assumption:* "[primary: WEF/CISA/White House reports + SpaceX case]… 4M+ Starlink terminals… zero satellites lost across 200+ updates" (RF:83).
- *Why it's doubtful:* the SpaceX evidence comes from a hubble.com "community guide" (raw/03:113), a secondary and blog-like source, yet it sits under a "[primary]" tag. The sentence moves from *terminals* (4M+) to *satellites* (zero lost), and it's unclear which fleet the 200+ updates refer to. SpaceX is also outside the target (TB:307), so it proves mega-operators build in-house, not that mid-size ones do (that's K4).
- *Question a grader would ask:* "Is that a SpaceX statement or a third-party blog, and was it satellites or dishes?"
- *What would resolve it:* retag as secondary, split the terminal and satellite claims, and cite the SmallSat 2023 paper (raw/03:113) if it covers satellites.

**R22 — The entry barriers apply to the company first [Items 15, 7] [severity: medium]**
- *Claim / assumption:* clearances, FOCI, ITAR and SME depth are barriers that protect the company (RF:86, RF:46).
- *Why it's doubtful:* a startup can't self-sponsor a facility clearance (RF:86), FOCI limits *our* cap table (RF:86), deemed-export rules limit *our* hiring (RF:129), and the SBIR channel is lapsed (R25). Item 7 already admits these don't stop incumbents (RF:46). So the barriers mainly slow the fictitious startup relative to Booz Allen, Deloitte and the primes. This is the same double edge as K1, on the entry side.
- *Question a grader would ask:* "If entry is this hard, how do *you* get in?"
- *What would resolve it:* name the entry path, e.g. a commercial-only, unclassified, US-person team first, a cleared-contractor sponsor or partner for B2G later, and US-only investors. State that the barriers become a moat only once they're cleared.

**R23 — The originality evidence dropped its own caveats [Item 10] [severity: medium]**
- *Claim / assumption:* "No public competitor automates the full loop" (RF:60), and SPARTA is described via newspaceeconomy.ca (RF:66).
- *Why it's doubtful:* raw/03:104 says "absence of evidence is not evidence of absence — Crunchbase/PitchBook itself was not directly queryable", and raw/03:94 recommends a Claroty follow-up. Neither made it into the summary. The SPARTA methodology is cited through a news aggregator whose release date is disputed (Apr 2025 vs v3.2 on 11 Mar 2026, raw/03:71), not through sparta.aerospace.org. The closest competitor, which the "no existing company" rule depends on, rests on the weakest citation.
- *Question a grader would ask:* "Did you check funding databases, and have you read SPARTA itself?"
- *What would resolve it:* cite SPARTA directly with a verified version and date, add the Crunchbase caveat and a stealth/classified caveat (TB §9.5 Q24) to the report, and do a quick Claroty check.

**R24 — S.3404 is called a "tailwind" in one item and toothless in another [Items 15, 30] [severity: low]**
- *Claim / assumption:* "Satellite Cybersecurity Act… worth adding as regulatory-tailwind context" (RF:86).
- *Why it's doubtful:* item 30 says it is unenacted, offers only voluntary recommendations, and §6 rules out designating satellites as critical infrastructure (RF:124, raw/06:178).
- *Question a grader would ask:* "If the bill imposes no duties, how is it a tailwind?"
- *What would resolve it:* describe it as a "policy attention" signal only, or drop it.

---

## A.4 Persona & Customer Journey

**R25 — SBIR is "lapsed" in one item and has a "live topic opened Sept 2026" in another [Items 10, 15, 17] [severity: high]**
- *Claim / assumption:* "SBIR/STTR statutory authority lapsed 30 Sept 2025… awards are currently on hold" (RF:65), and "A live SpaceWERX cyberspace-warfare SBIR topic (opened Sept 2026, up to $2M/24mo)" (RF:96).
- *Why it's doubtful:* both can't be current. The lapse claim rests on a single **Dec 2025** SpaceNews opinion piece (raw/03:103), nine months old. The live topic (raw/01:138) is dated 23 Sept 2026 from a consultancy site (bwcoconsulting), which suggests authority may have been restored. The Phase III example (LMI $100M) is a *logistics* award (URL in raw/01:142), not cyber, so the analogy is stretched.
- *Question a grader would ask:* "Is SBIR open or closed right now?"
- *What would resolve it:* research the current SBIR/STTR reauthorisation status (congress.gov, sbir.gov) before drafting, fix items 10, 15 and 17 and TB §10.1:413 together, and replace the LMI example with a cyber or space award if possible.

**R26 — The recommended beachhead is the generic IT part, and it doesn't match the persona [Items 30, 16, 17; TB Q9] [severity: high]**
- *Claim / assumption:* "The 800-171 gap… makes DoD contractors the natural beachhead" (RF:125).
- *Why it's doubtful:* 800-171 3.14.1 is "scoped to CUI-handling IT systems, not spacecraft/links" (RF:123, raw/06:96). A beachhead built on it sells *IT flaw remediation*, which is the commodity layer (Nucleus is FedRAMP-authorised and used by DoD, raw/03:90). TB Q9 already warned against that dilution (TB:163). It also clashes with the persona: item 16's persona is a *commercial* operator CISO, item 17's journey is *B2G SBIR*, and item 30's beachhead is *DoD contractors*. That is three different first customers.
- *Question a grader would ask:* "Who is your first customer: Planet's CISO, Space Force, or a defence contractor's IT team?"
- *What would resolve it:* pick one. For example: commercial mid-size operators that also hold DoD contracts. Their 800-171 duty pays for the ground-IT module, and the space core is the upsell. Make the persona, journey and beachhead the same actor.

**R27 — The persona's buyer, approver and user are different people, and the budget is unknown [Item 16] [severity: medium]**
- *Claim / assumption:* Planet's VP & CISO "owns departmental budget… one exec role spans cyber + mission assurance + compliance + AI governance" (RF:93).
- *Why it's doubtful:* the posting lists facilities, ISO and CMMC compliance and AI governance. It doesn't show the CISO controls *flight-software uplinks*, which the concept assigns to mission operations and the manufacturer (TB:147). The reporting line is unconfirmed (raw/01:126). The persona therefore buys a product whose key action (uplink approval) belongs to another team. Budget size is unknown, and so is whether mid-size operators have spare security budget. The posting is also a *vacancy*.
- *Question a grader would ask:* "Does the CISO have authority, and money, over spacecraft software changes?"
- *What would resolve it:* model a buying committee in the journey (economic buyer = CISO, approver = mission-ops lead, champion = security ops engineer, raw/01:127), and flag budget as an assumption.

**R28 — Sales cycle, journey timings and runway are missing [Items 17, 18] [severity: medium]**
- *Claim / assumption:* journey = design partner → shadow → automation → renewal (RF:99).
- *Why it's doubtful:* Research_Plan item 18 asked for "realistic timeframes" (Research_Plan:52), and none were found. Item 17 has no non-SBIR procurement data ("Gap: no GSA Schedule or clearance-threshold specifics", RF:96). The story has a multi-stage trust funnel, a manufacturer-data onboarding step (R14), clearance sponsorship (R22) and a paused government channel (R25), but no time to first revenue. Item 18's evidence is vendor press releases and an Akamai partner blog (raw/01:156), so none of it is space-specific.
- *Question a grader would ask:* "How long from first meeting to first paid renewal, and how does a startup survive that long?"
- *What would resolve it:* give an explicit, labelled assumption timeline (e.g. months per stage) with the reasoning, and add a funding line (design-partner paid pilots, non-dilutive funding if R25 resolves).

---

## A.5 Governance, Guardrails & Regional Compliance

**R29 — Liability when an approved patch bricks a satellite has not been researched [TB §9.4 Q23; Items 6, 4] [severity: high]**
- *Claim / assumption:* humans approve every uplink, and "Our company never writes flight software" (TB:147, 313).
- *Why it's doubtful:* TB §9.4 Q23 is still open, and no research item covers it. When a manufacturer's patch, validated and scheduled by the platform, bricks a satellite after the operator approves it, it is unclear who pays. Rubric A.5 asks "What happens when the AI gets something wrong?", and this is the most likely viva question for a safety-critical product. Human approval doesn't transfer liability by itself. Contract terms, liability caps and insurance also matter. TB Q10 even cites "operators don't want software-vendor liability" (TB:173) without resolving it.
- *Question a grader would ask:* "Your model says 'safe', the operator approves, the satellite dies. Who pays?"
- *What would resolve it:* research how comparable safety-critical software vendors allocate liability (limitation-of-liability clauses, the manufacturer's warranty on its own patch, space insurance). State the company's position: a capped liability contract, recommendation-not-warranty wording, and a full audit trail as evidence (item 24).

**R30 — Stop and escalation thresholds are still unanswered; item 24 covers logging, not stopping [Item 24; TB §9.4 Q20–21] [severity: medium]**
- *Claim / assumption:* item 24 is presented as answering "Escalation thresholds & audit trail" (RF:135).
- *Why it's doubtful:* AU-2, AU-3 and AU-6 define *what to log and how often to review*. None defines *when the agent must stop*. Q20 ("when must the agent stop?") and Q21 ("who approves which class of action?") remain open. The weekly-review cadence comes via csf.tools, a secondary mirror (raw/04:160), and the SOC 2 figures are unverified (raw/04:163).
- *Question a grader would ask:* "Give me one concrete rule under which the AI halts a rollout."
- *What would resolve it:* this is a design decision, not research. Write 3–5 explicit stop rules (e.g. world-model anomaly score above threshold after the canary, any telemetry loss after uplink, model confidence below a floor, or a flaw touching the command-authentication path) and an approval matrix. Cite the NIST SP 800-53 PDF directly.

**R31 — The LLM agent handles controlled data, and neither its hosting nor its hallucination controls were researched [Items 19, 22, 30; TB §7.3] [severity: medium]**
- *Claim / assumption:* "existing LLM + retrieval" reads advisories and maps them to components (TB:138, 284).
- *Why it's doubtful:* the mapping input is SBOMs and bus technical data, possibly EAR/ITAR technical data (R16) or CUI for DoD-contractor customers (RF:123). Sending it to a commercial LLM API raises the export and CUI questions again, which suggests a US-hosted, self-hosted or government-cloud model. Nothing researched this. Hallucination safeguards (a rubric A.5 bullet) appear only as the NIST "Measure" mapping (RF:108), with no concrete control (e.g. citation-required outputs, deterministic CPE/SBOM matching with the LLM only proposing).
- *Question a grader would ask:* "Which LLM sees your customers' controlled spacecraft data, and what stops it from inventing a component match?"
- *What would resolve it:* state a deployment constraint (self-hosted open-weights model inside the customer or US boundary) and a concrete anti-hallucination design (retrieval-grounded, every mapping cites an SBOM line, and unmatched items escalate to a human).

**R32 — The rubric's US bullets are only partly covered [Items 19, 23; rubric A.5] [severity: low]**
- *Claim / assumption:* the US framework is NIST AI RMF plus CCPA (RF:105, 132).
- *Why it's doubtful:* the rubric's US option also lists "FTC algorithmic fairness", which no item addresses. Item 23 shows CCPA *could* cover terminal data, but not whether the *company* is a covered "business" or a "service provider" to the operator, or whether it even ingests subscriber-level data.
- *Question a grader would ask:* "What does the FTC have to do with your product?"
- *What would resolve it:* add one line: fairness risk is low because the decisions concern machines, not people, but FTC Act §5 deception applies to AI capability claims in marketing (research the current FTC position on AI claims). State the company's CCPA role (service provider) and data-minimisation choice.

**R33 — Unlearning and data deletion on customer exit is unresearched [TB §9.3 Q18] [severity: low]**
- *Claim / assumption:* federated contributions are protected by DP and secure aggregation (TB:317).
- *Why it's doubtful:* once a departing operator's updates are averaged into the shared model, they can't be removed selectively. This is a governance question a privacy-literate grader may ask, and no item covers it.
- *Question a grader would ask:* "If a customer leaves and demands deletion, can you remove what the model learned from them?"
- *What would resolve it:* one honest line, e.g. periodic retraining from retained contributions or checkpoint rollback, with the limitation stated. Optionally research machine-unlearning feasibility.

---

## Cross-cutting

**R34 — The ~40% failure statistic isn't from the cited paper and covers a different population [Items 26, 29] [severity: medium]**
- *Claim / assumption:* "over 40% of CubeSats launched since 2000 have failed…", with Langer & Bouwmeester as key reference #3 (RF:146, 159).
- *Why it's doubtful:* Langer & Bouwmeester give 48–65% reliability at 2 years. The "40% since 2000" line was "cited via a broader… review… I did not directly pull the primary Swartwout paper" (raw/01:165), so the recommended wording has no retrieved source. The dataset is 178 CubeSats analysed in 2016 (a ten-year-old sample, and hardware-dominated failure causes are not shown to be software or cyber), yet it is used to size the anomaly-training layer for commercial constellation operators (TB:195).
- *Question a grader would ask:* "Where exactly does 40% come from, and are 2016 university CubeSats representative of Planet or Iridium?"
- *What would resolve it:* cite only what Langer & Bouwmeester actually say (the 2-year reliability range), or retrieve the Swartwout source. Note that the sample is CubeSats only and dated, and use it only to show that anomalies are common, not to size anything.

**R35 — Key references have unresolved verification flags and inconsistent source-type tags [Items 1, 6, 20, 29] [severity: medium]**
- *Claim / assumption:* the shortlist is "non-blog, verifiable, and directly load-bearing" (RF:156).
- *Why it's doubtful:* (1) NIST IR 8270 (reference #1) is tagged "[primary]" in item 6 (RF:34), and raw/05:62 claims its crosswalk was pulled "from the actual PDF text". Item 20 and raw/04:109 say the same PDF "failed to render" and the control bullets are secondary. Both can't be true, and open item 1 (RF:167) is still pending. The crosswalk also uses CSF 1.1 codes (ID.RA-1, PR.IP-12); raw/04:112 notes the CSF 2.0 renaming, so check whether 8270's mapping is current. (2) The SIA reference #2 links to the *press release* (RF:13), not the report. (3) Reference #3 has the R34 problem. (4) SPD-5 (#4) is a "close paraphrase" (RF:168). All four of the 3–4 key references carry an open flag.
- *Question a grader would ask:* "Did you read your own references?"
- *What would resolve it:* before drafting, open the four documents directly, pull one verbatim line from each, and cite the report or PDF rather than the press release or mirror. Fix the item 6 vs item 20 tag inconsistency.

---

## Top 5 to fix before drafting

1. **R20 + R19 — Revenue reality.** Count the real buyers and put one annual-contract-value assumption on the page. Without it, the Moat, Five Forces and "why customers pay" sections have no economic floor, and a grader can dismiss the company with arithmetic.
2. **R6 + R17 — What the AI can actually know.** Reframe the world model as post-uplink anomaly detection and risk scoring (not code-effect prediction) and name an evaluation metric. This is the most likely viva attack on the technical core.
3. **R26 + R25 — One first customer, one channel.** Reconcile the persona (commercial CISO), journey (SBIR) and beachhead (DoD contractors), and check SBIR status today. Items 10/15 and 17 currently contradict each other.
4. **R13 + R14 + R18 — The manufacturer dependency.** Redo supplier power from the company's side. SBOMs and simulators are high-power inputs held by consolidating primes that are also the top entrant threat. Either give manufacturers a reason to cooperate or remove them from the moat.
5. **R29 — Liability when an approved patch bricks a satellite.** It's the rubric's own A.5 headline question, and nothing in the findings answers it. Add a contractual and insurance position plus 3–5 stop rules (R30).
