# Research Findings, Explained Simply

Plain-language version of `Research_Findings.md`. Same headings and item numbers. Each item says what was found, what it means, and any catch.

---

## A.0 Company Overview

**Item 1 — Satellite count & market growth**
About 14,266 working satellites were in orbit at the end of 2025, according to the industry association (SIA). Nearly 4,434 were launched in 2025 alone, 65% more than in 2024. The space business is worth about $429B, and satellite internet users grew 62%. *What it means:* the number we used earlier (16,000–17,000) was too high, so we replace it with 14,266. *Catch:* no trustworthy growth-rate forecast exists. The market-research sites disagree widely (12%–25%), so only mention them loosely.

**Item 2 — Regulatory pressure trend**
Europe is moving toward making space cybersecurity a legal duty. An existing law (NIS2) already lists space as an important sector, but only for the ground equipment, not the satellites. A proposed law (the EU Space Act) would require hacking-style security tests before launch and every 3 years. *Catch:* it isn't law yet and probably won't apply before 2030. We're focusing on the US, so use it only as "where regulation is heading."

**Item 3 — Company name/mission/vision**
Nothing researched. This is a creative choice you still have to make.

---

## A.1 Agentic AI & Value Proposition

**Item 4 — Cost of a patch-related failure**
We can't put a dollar cost on the 2022 Viasat satellite hack, because Viasat itself said it didn't hurt its finances materially. So don't invent a number. What we can say: the hack cut off remote control of about 5,800 wind turbines for weeks, and roughly 30,000 modems had to be replaced. For value, a small satellite costs roughly $0.5–1M or more to build and launch. *What it means:* use "scale of disruption" and "value of a lost satellite," not "cost of the attack."

**Item 5 — Consulting/analyst cost baseline**
We found no price for space-specific security consultants. The best stand-in is general cybersecurity consultants: about $115K–$159K a year in salary, around $143 an hour as a contractor in the US, or about £675 a day in the UK. *Catch:* say clearly this is a general estimate, not a space-industry number.

**Item 6 — Operational pipeline analogue**
Our 8-step process (collect → match → score → test → schedule → send to satellite → watch → undo) isn't one existing official process. It's a combination of two real ones. A US standard (NIST IR 8270) covers finding, scoring, and fixing flaws. The European Space Agency's software-update method (used on real missions) covers testing on simulators, building small patches, sending them up, and tracking the configuration. *Catch:* nobody documents an automatic "undo" step. Real teams rely on records and human judgment. Admit that as a limitation.

---

## A.2 Moat & Defensibility

**Item 7 — Public data sufficiency for JEPA cold-start**
Public satellite datasets exist (ESA: 17.5 years of data from 3 missions; OPS-SAT: one small satellite), but they're small compared to what this type of AI usually learns from. *What it means:* public data shows the approach can work, but the real product needs private data from customers who partner with us. That's an honest way to explain why we're hard to copy.

**Item 8 — Federated learning under heterogeneous fleets**
Federated learning means training an AI across many operators without pooling their raw data. It goes wrong when each operator's data looks very different, because the shared model gets pulled in different directions. Known fixes exist: a method that keeps local updates from straying too far (FedProx), a shared core with a small custom part per satellite type, and grouping similar operators. *Catch:* none of this is space-specific or our invention. Present it as known techniques we apply.

**Item 9 — DP/secure aggregation overhead**
Two privacy tools are affordable at our scale. Differential privacy (adding noise so individual data can't be recovered) costs about 1.5–3× the computing. Secure aggregation (combining updates so nobody sees individual ones) roughly doubles the network traffic. *Real risk:* the noise can make the AI less accurate when each operator has little data, which is our situation. It's an accuracy risk, not a cost risk.

**Item 10/13 — Competitor "whole loop" refresh**
Nobody offers the complete package: prioritize by orbit, schedule patches, test on a twin, roll out. Two competitors must be named in the report:
- **Aerospace Corp's SPARTA:** a published, government-backed way of ranking security fixes. It's the closest overlap, but it's a reference guide, not a live product with testing and automatic rollout.
- **CT Cubed:** sells training/practice environments and AI risk assessment, not day-to-day fixing.

Others do only parts (detection only, consulting-delivered, generic IT, or access control), and some don't overlap at all. *Also:* the government small-business funding program (SBIR/STTR) expired in Sept 2025 and wasn't renewed, so our "government funding" argument needs updating.

**Moat/defensibility bottom line**
The strongest moat is the shared pool of "which patches worked or failed" data. Items 7–9 show it's technically realistic to build.

---

## A.3 Porter's Five Forces

**Item 11 — Buyer concentration / mid-size operators named**
Target customers (50–300 satellites) include Planet Labs, Spire, Iridium, SES, Intelsat, and possibly ICEYE. Globalstar and BlackSky are too small. Starlink and OneWeb are too big to be our target. *What it means:* the customer pool is small, so each buyer has some bargaining power.

**Item 12 — Supplier power**
Suppliers (satellite makers, ground stations) have low-to-moderate power, rising. Satellite makers are being bought up by big defense firms (e.g., Lockheed bought Terran Orbital). Ground stations are becoming easy to switch between, except KSAT's polar site. *Catch:* we found no case of a satellite maker reselling someone else's security software. For a "sell through partners" idea, use the ground-station example (Atlas reselling AWS) instead. Only one concrete fact on manufacturer security: Thales Alenia Space uses a tool to track its software ingredients (SBOM).

**Item 14 — Substitutes evidence**
The main alternative to our product is doing nothing, and that's documented: many older satellites just accept the risk. The White House said in 2025 that space cybersecurity practices are underdeveloped. SpaceX built its own update system for Starlink rather than buying one. *Catch:* we couldn't find real prices for consultants' space security work, so we can't prove alternatives cost more. Say it's unquantified.

**Item 15 — Entry barriers**
Reasons it's hard for a new company to enter: (1) security clearances need a sponsor; (2) foreign-ownership limits affect fundraising; (3) export laws restrict sharing spacecraft data with foreigners; (4) customers hesitate to give sensitive data to an unproven vendor; (5) building a good simulator needs real spacecraft expertise; (6) the small-business funding program has lapsed. *New:* a bill called the Satellite Cybersecurity Act of 2025 (S.3404) is pending. It could help us if it passes.

---

## A.4 Persona & Customer Journey

**Item 16 — Real persona**
A real job ad at Planet Labs for a "VP & Chief Information Security Officer" shows one person owning cybersecurity, mission safety, compliance, and AI governance, with their own budget. That's a solid, citable customer to describe. Spire has a separate mission-systems security engineer role too.

**Item 17 — Procurement pattern**
Small companies normally sell to the US Space Force in three stages: a small feasibility grant, a bigger development grant, then a production contract. A live topic on space cyber defense (up to $2M) is very close to our product. *Catch:* new awards are paused because the funding program lapsed (see Item 10). We found nothing on how to sell without the grant route.

**Item 18 — Onboarding journey pattern**
No company publishes the exact steps "pilot partner → watch-only mode → automation → renewal." But the pattern shows up across several companies (Credo AI, Cloudflare, security vendors' "monitor mode"). Use it as a common pattern, not one named case.

---

## A.5 Governance, Guardrails & Regional Compliance (US)

**Item 19 — NIST AI RMF four functions mapped**
NIST's AI risk framework has four jobs, and each maps to our design:
- **Govern:** who's accountable → a human must approve each upload to a satellite.
- **Map:** what the AI is allowed to do → it recommends, and never sends commands itself.
- **Measure:** track how well and how reliably it performs → checks for wrong answers and ongoing monitoring.
- **Manage:** what to do when things go wrong → stop rules and incident response.

*Catch:* wording came from NIST's website, not the PDF. Check the PDF before citing.

**Item 20 — NIST IR 8270 / IR 8401 control specifics**
These two NIST documents list security controls for satellites. 8270 points to flaw-fixing rules and notes satellite software can be patched from the ground. 8401 covers ground systems, including keeping test and live environments separate, which supports testing patches before sending them up. *Catch:* weakest sourcing. The details came from summaries, so read the actual PDFs before citing.

**Item 21 — SPD-5 primary text**
This 2020 US space policy sets the basic rules: build security in before launch, block unauthorized access and spoofing, protect command links with strong encryption, follow NIST practices on the ground (patching, separation), check the supply chain, and share threat info. It applies to both government and commercial satellites.

**Item 15/22 — ITAR/EAR**
Export laws are confirmed to apply. US arms rules (ITAR) cover spacecraft technical data. Giving that data to a foreign person, even inside the US, counts as an export. Most commercial satellites fall under a lighter rule (EAR, category 9A515). *What it means:* our claim that federated learning helps by not moving data across borders is legally well-grounded.

**Item 23 — CCPA/CPRA applicability**
California's privacy law likely applies if satellite internet subscribers include Californians, because it counts precise location and device data as personal information. Government and military terminals are probably excluded, and anonymized data is exempt.

**Item 24 — Escalation thresholds & audit trail**
NIST's audit rules give a ready template: log every upload command, AI escalation, and human override (AU-2); record what/when/who/result for each (AU-3); review the logs at least weekly, and daily for privileged access (AU-6). A commercial standard (SOC 2) adds alert rules with a named owner. Logs are typically kept 12–15 months.

**Item 25 — India fallback**
If we need an India option: the DPDP Act 2023 requires consent to process personal data, with some exceptions. India's space regulator (IN-SPACe) authorizes space activity, and foreign firms must work through an Indian subsidiary or joint venture. India's CERT-In requires reporting security incidents within 6 hours. *Catch:* the 6-hour rule was confirmed only via secondary sources. Re-check it.

---

## Cross-cutting

**Item 26 — Smallsat failure-rate stat**
The "about 40% fail" figure is roughly right but was worded wrongly. A 2016 study of 178 CubeSats found reliability drops to 48–65% after two years. Another source says over 40% of CubeSats launched since 2000 failed their goals. *Fix:* say "over 40% of CubeSats launched since 2000 have failed to fully meet their objectives," not "in the last 20 years."

**Item 27 — CVE volume**
The "~40,000 vulnerabilities per year" figure is outdated. That was 2024. 2025 had 48,185, and 2026 is already at 57,908 through August. *Fix:* use "~58,000 per year (2026 pace), up from ~40,000 in 2024."

**Item 28 — Pricing comparables**
CrowdStrike charges per device per year, with add-on modules. Datadog charges per server per month ($15–$41 depending on tier). Both are good models for our own pricing: a base price per satellite plus paid add-ons, or tiers by features.

**Item 29 — Reference shortlist**
The four strongest sources to cite: (1) NIST IR 8270 (satellite security standard), (2) SIA 2026 report (market numbers), (3) Langer & Bouwmeester 2016 (CubeSat failure rate), (4) SPD-5 (US policy). Backups: NIST IR 8401 and the Bonawitz paper on secure aggregation.

---

## Open items still needing action before drafting

1. **Re-read NIST IR 8270/8401 PDFs.** They didn't load as text, so exact wording is still unchecked.
2. **Re-read the SPD-5 text.** Current quotes are close paraphrases.
3. **Choose company name, mission, and vision.** It's a creative decision, not research.
4. **Confirm the US as the jurisdiction.** All the research assumed it.
