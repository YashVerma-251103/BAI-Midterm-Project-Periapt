# Research Thread 1 — Market, Customers, Pricing

**Agent:** general-purpose subagent | **Run:** 2026-09-29 | **Items covered:** 1, 4, 5, 11, 16, 17, 18, 26, 27, 28 (per `research/Research_Plan.md`)

## Prompt given

> You are researching for a fictitious-company business assignment (satellite-fleet vulnerability-prioritisation AI platform, B2B/B2G, Defence/Space/Cybersecurity segment). Use WebSearch/WebFetch. This is a research task, NOT company identification — do not worry about confidentiality, just gather public market data.
>
> Research and answer these specific items (numbers match the project's research/Research_Plan.md). For EACH item give: the finding, the source URL, and whether it's a primary source (official report/filing/standard) or secondary (news/blog). If you cannot find a real source, say so explicitly — do not fabricate numbers.
>
> 1. Current active-satellite count and LEO market growth trend/CAGR — find one credible industry report (Euroconsult, SIA "State of the Satellite Industry", NSR, or similar) in addition to any web trackers.
> 4. Cost of a patch-related satellite/network failure: Viasat KA-SAT (Feb 2022) attack — actual recovery/replacement cost if disclosed (Viasat statements, 10-K/annual report, insurance trade press), and any figure for what a "bricked" satellite is worth (typical smallsat/constellation satellite replacement cost).
> 5. Baseline cost of space-sector cybersecurity consulting or an internal security analyst: any published day-rate, salary range (space-sector job postings, Levels.fyi-style data, Glassdoor), so we can compute a savings claim.
> 11. How many "mid-size" satellite operators exist (roughly 50–300 satellites each)? Name them if possible. Use Orbital Radar "satellites by operator", SIA reports, or similar trackers.
> 16. Real job titles used at mid-size satellite operators (e.g. Spire, ICEYE, Planet, BlackSky) for whoever would own cybersecurity/mission-assurance decisions — search job postings/LinkedIn company pages (public listings only) to find actual title patterns, team size hints, reporting line.
> 17. Typical B2B/B2G security-tooling procurement pattern for a space company: budget cycle, security clearance requirements for defence customers, GSA schedule or Space Force SBIR-style contracting norms.
> 18. Any public reference for enterprise security-tool onboarding patterns (design partner → shadow mode → full automation → renewal) — doesn't need to be space-specific, an analogous SaaS security product's published customer journey is fine as a pattern reference.
> 26. The claim "~40% of small-satellite missions have had partial or total failure in the last 20 years" — find the actual underlying study/statistic (AIAA satellite reliability paper, or similar), confirm or correct the number.
> 27. Current annual CVE publication volume (~40,000/year claimed) — confirm with a current-year source (cve.org, NVD stats).
> 28. Any comparable B2B security-SaaS pricing model (per-asset, per-seat, tiered) that could inform a "per-satellite" or "per-fleet-tier" pricing structure — doesn't need to be space-specific.
>
> Return a clean markdown section, one subsection per item number, with Finding / Source (URL) / Source type (primary or secondary) / Confidence. Do not write any files — just return the markdown in your final message.

## Approach followed

Web search + fetch across each of the 10 assigned items, prioritizing primary sources (industry-association annual reports, SEC filings, live job postings, government program sites, vendor pricing pages) and falling back to secondary aggregators only where no primary source existed. Every finding was tagged with source type (primary/secondary) and a confidence level; anything not locatable was reported as an explicit gap rather than estimated or invented.

## Sources visited

- https://sia.org/affordability-productivity-drive-historic-satellite-industry-growth-satellite-industry-association-releases-29th-annual-state-of-the-satellite-industry-report/
- https://orbitalradar.com/satellites-by-operator
- https://orbitalradar.com/satellites/operator/oneweb
- https://keeptrack.space/satellites/owners/iceye
- https://www.viasat.com/perspectives/corporate/2022/ka-sat-network-cyber-attack-overview/
- https://www.sec.gov/Archives/edgar/data/797721/000095017022010881/vsat-20220331.htm
- https://en.wikipedia.org/wiki/Viasat_hack
- https://www.pv-magazine.com/2022/03/01/satellite-cyber-attack-paralyzes-11gw-of-german-wind-turbines/
- https://nanoavionics.com/blog/how-much-do-cubesats-and-smallsats-cost/
- https://en.wikipedia.org/wiki/Sky_and_Space_Global
- https://www.indeed.com/career/cybersecurity-consultant/salaries
- https://www.glassdoor.com/Salaries/cyber-security-consultant-salary-SRCH_KO0,25.htm
- https://www.contractrates.fyi/CyberSecurity-Consultant/hourly-rates
- https://www.itjobswatch.co.uk/contracts/uk/cyber%20security%20consultant.do
- https://job-boards.greenhouse.io/planetlabs/jobs/8014499
- https://spire.com/careers/job-openings/
- https://afwerx.com/get-funded/
- https://www.bwcoconsulting.com/fod/spacewerx-sbir-daf26bx06-dv512-cyberspace-warfare-for-space
- https://www.sda.mil/home/work-with-us/small-business/
- https://www.govconwire.com/articles/lmi-ssc-sbir-logistics-readiness-contract
- https://www.credo.ai/shadow-ai-discovery
- https://www.cloudflare.com/press/press-releases/2026/cloudflare-launches-design-partner-designation-to-accelerate-secure-ai-and-seamless-sase-adoption/
- https://www.akamai.com/blog/partners/2026/jul/partners-defend-network-ease-ai-anxiety
- https://digitalcommons.usu.edu/cgi/viewcontent.cgi?article=3397&context=smallsat
- https://www.semanticscholar.org/paper/Reliability-of-CubeSats-%E2%80%93-Statistical-Data,-Beliefs-Langer-Bouwmeester/03d4e3a8d745b028c44c299b17e5a92e344d5d8a
- https://jerrygamblin.com/2026/01/01/2025-cve-data-review/
- https://cve.icu/years.html
- https://cyberpress.org/over-40000-cves-published-in-2024/
- https://www.cve.org/Media/News/item/blog/2026/05/12/CVE-Program-Report-for-Q1-2026
- https://www.crowdstrike.com/en-us/pricing/
- https://www.crowdstrike.com/en-us/legal/crowdstrike-licensing/
- https://www.datadoghq.com/pricing/
- https://last9.io/blog/datadog-pricing-all-your-questions-answered/

## Full output

## Research Findings — Satellite-Fleet Vulnerability-Prioritisation Market Research

### 1. Active satellite count & LEO market growth

**Finding:** SIA's 29th Annual "State of the Satellite Industry Report" (2026 edition, covering 2025 data) reports **14,266 operational satellites** in orbit at end of 2025. A record 296 commercial launches deployed 4,434 satellites in 2025 — **65% more satellites deployed than in 2024**. Global space economy hit $429B (+3%); commercial satellite industry $303B (+4% YoY). Satellite broadband subscribers grew 62% to >10M, driven by LEO constellations. No single explicit "LEO CAGR" figure was published by SIA in the press release itself, but the 65% YoY deployment growth and 62% broadband-subscriber growth serve as the closest proxies.
Secondary confirmation: Orbital Radar (live tracker from Space-Track/CelesTrak data) shows SpaceX/Starlink alone ~9,900+ satellites, ~53% of all payloads in orbit — consistent with SIA's LEO-driven growth narrative.
**Source:** https://sia.org/affordability-productivity-drive-historic-satellite-industry-growth-satellite-industry-association-releases-29th-annual-state-of-the-satellite-industry-report/ ; https://orbitalradar.com/satellites-by-operator
**Source type:** SIA report = Primary (industry association official report). Orbital Radar = Secondary (web tracker).
**Confidence:** High for satellite count/revenue figures; Medium for "CAGR" framing since no single clean CAGR % was published — I did not fabricate one. A dedicated Euroconsult LEO CAGR report exists but is paywalled/not directly accessible; market-research aggregator sites (MarketsandMarkets, GMInsights, Fortune Business Insights) show LEO satellite market CAGR estimates ranging 11.9%–24.7% (2025–2030/2034) — wide variance, low confidence, secondary/syndicated market-research sources, treat as directional only.

---

### 4. Cost of a patch-related satellite/network failure — Viasat KA-SAT & smallsat replacement cost

**Finding (Viasat KA-SAT):** Viasat has **not publicly disclosed a specific dollar/euro cost figure** for the Feb 2022 KA-SAT attack recovery. Viasat's own corporate overview page describes operational scope (tens of thousands of customers affected, ~30,000 replacement modems shipped) but gives no cost. Viasat's 10-K filings state explicitly that **to date, no cybersecurity incidents (including KA-SAT) have had a "material impact" on the company's operations or financial results** — i.e., the company's own disclosure is that the cost was immaterial at the corporate financial-statement level, not a specific figure. Separately, the attack disabled remote monitoring for ~5,800 Enercon wind turbines in Germany (11 GW combined capacity) for weeks — no dollar damage estimate found for that either. **Recommend not asserting a specific KA-SAT dollar cost in the deck; instead cite "undisclosed / stated immaterial by Viasat, despite European-wide multi-sector disruption" as the finding.**

**Finding (smallsat/bricked-satellite replacement cost, typical figures found):**
- Student/hobbyist CubeSats: ~$3,500–$7,000 (e.g., PhoneSat)
- Commercial 3U CubeSats (e.g., Sky and Space Global): ~$500,000/unit build + ~$200,000–$250,000 launch
- Rideshare CubeSat launch alone: ~$90,000 (NanoRacks, 1U) to $150,000–$275,000 (SpaceX rideshare, per kg tiers)
- Traditional large GEO satellite: ~$300 million (for comparison/contrast)
These give a usable range for a "what a bricked satellite is worth" argument: roughly **$0.5M–$1M+ per smallsat unit (build+launch) for commercial constellation-class satellites**, scaling to hundreds of millions for GEO-class assets.
**Source:** https://www.viasat.com/perspectives/corporate/2022/ka-sat-network-cyber-attack-overview/ ; https://www.sec.gov/Archives/edgar/data/797721/000095017022010881/vsat-20220331.htm (and later 10-Ks) ; https://en.wikipedia.org/wiki/Viasat_hack ; https://www.pv-magazine.com/2022/03/01/satellite-cyber-attack-paralyzes-11gw-of-german-wind-turbines/ ; https://nanoavionics.com/blog/how-much-do-cubesats-and-smallsats-cost/ ; https://en.wikipedia.org/wiki/Sky_and_Space_Global
**Source type:** Viasat corporate page & 10-K = Primary. Wikipedia/pv-magazine/NanoAvionics = Secondary.
**Confidence:** High confidence that no cost figure is disclosed (verified via primary source). Medium confidence on smallsat cost ranges (industry figures, not audited financials).

---

### 5. Baseline cost of space-sector cybersecurity consulting / internal analyst salary

**Finding:** I could **not find space-sector-specific day-rate or salary data** despite targeted searching. General (industry-agnostic) cybersecurity consultant figures found:
- US salary: avg ~$115,579–$158,740/yr (ranges $71K–$264K depending on source/seniority)
- US freelance/contractor hourly: avg $143/hr (range $90–$178/hr; top 10% ≥$250/hr)
- UK day rate: median £675/day (contract postings, 6 months to May 2025)
No space-industry premium or discount could be confirmed from available sources — treat any "space cybersecurity consultant" rate as an extrapolation from these general figures, not a directly sourced number.
**Source:** https://www.indeed.com/career/cybersecurity-consultant/salaries ; https://www.glassdoor.com/Salaries/cyber-security-consultant-salary-SRCH_KO0,25.htm ; https://www.contractrates.fyi/CyberSecurity-Consultant/hourly-rates ; https://www.itjobswatch.co.uk/contracts/uk/cyber%20security%20consultant.do
**Source type:** All secondary (aggregator salary sites, not audited/primary).
**Confidence:** Medium for general cybersecurity rates; Low/no data for space-sector-specific premium — flag this gap explicitly if used in the deck.

---

### 11. Mid-size satellite operators (~50–300 satellites)

**Finding:** Per Orbital Radar's live operator tracker (Space-Track/CelesTrak-derived), operators in or near the 50–300 range:
- **Planet Labs** — ~200+ LEO satellites (Earth imaging)
- **Spire Global** — ~100+ LEO CubeSats (weather/maritime/aviation data)
- **Iridium Communications** — ~75 LEO satellites (voice/data/IoT)
- **SES** — ~50+ GEO/MEO satellites (video/connectivity)
- **Intelsat** — ~50 GEO satellites (media/government comms)
- **ICEYE** — borderline-low, ~52–72 satellites cataloged (SAR imaging) per KeepTrack.space
- Below range (not mid-size by this definition): Globalstar (~24), BlackSky (~18)
- Above range (mega-constellation, not "mid-size"): OneWeb/Eutelsat (648 satellites, targeting 1,300 by 2030), Starlink (~9,900+)
**Source:** https://orbitalradar.com/satellites-by-operator ; https://keeptrack.space/satellites/owners/iceye ; https://orbitalradar.com/satellites/operator/oneweb
**Source type:** Secondary (web trackers aggregating public catalog/Space-Track data, not an official SIA/Euroconsult census).
**Confidence:** Medium-High — figures are live-tracked but approximate ("~") and fleet sizes fluctuate with launches/deorbits.

---

### 16. Real job titles at mid-size satellite operators for cybersecurity/mission-assurance ownership

**Finding:** Confirmed via an actual live job posting: **Planet Labs — "Vice President & Chief Information Security Officer"** (Greenhouse job board, posted ~Aug 2026). Scope/reporting hints from the posting: oversees departmental budget and "a capable tier of front-line managers," leads a multi-year security strategy, owns ISO 27001/ISO 42001/CMMC certifications, physical security of manufacturing/R&D facilities, international industrial security/clearance reciprocity, and AI governance/secure ML pipeline oversight — i.e., a single VP/CISO owns cyber + mission assurance + compliance + physical security under one exec role. Explicit reporting line (to CEO vs. COO) was not stated in the posting text extracted.
Spire Global has a **"Security Operations Engineer"** role (per job-board search) responsible for "operating the security controls that protect the company's enterprise, cloud, and mission systems" — confirms a distinct "mission systems" security scope in the title/description, though a senior/director title and its reporting line could not be confirmed from search results alone (would need direct LinkedIn/Spire careers page crawl for full org chart).
ICEYE and BlackSky specific security titles were not found in this pass.
**Source:** https://job-boards.greenhouse.io/planetlabs/jobs/8014499 ; https://spire.com/careers/job-openings/
**Source type:** Primary (live company job postings).
**Confidence:** High for the Planet Labs title/scope (directly read from posting). Low/partial for Spire, ICEYE, BlackSky — only fragmentary evidence found; recommend a follow-up direct crawl of each company's careers page/LinkedIn if this item needs to be fully nailed down.

---

### 17. B2B/B2G security-tooling procurement pattern for a space company

**Finding:** No single consolidated public reference found, but concrete program-level evidence:
- **SpaceWERX / AFWERX** run the Space Force's SBIR/STTR small-business funding pipeline; AFWERX has awarded ~10,400 contracts worth $7.24B+ to startups/small businesses to date (2026). A live example: a SpaceWERX cyberspace-warfare SBIR topic (DAF26BX06-DV512) offering up to $2M/24 months, opened Sept 23 2026, covering software supply-chain vetting, on-orbit cyber defense, cyber range training, AI threat detection — directly analogous to this project's product category.
- Space Development Agency (SDA) also runs a dedicated small-business/procurement pathway (sda.mil).
- General pattern confirmed: SBIR Phase I (feasibility) → Phase II (development, e.g., the 19 contracts awarded in one Space Force pitch event) → Phase III (production/sole-source follow-on, e.g., LMI's $100M Space Force SBIR Phase III award) is the standard on-ramp for small vendors selling security/defense tech to Space Force — a "design partner → SBIR Phase I/II → Phase III production contract" pathway that maps well onto a GTM narrative.
- A specific GSA Schedule citation or personnel security-clearance-requirement threshold for a commercial (non-SBIR) sale was **not confirmed** in this pass.
**Source:** https://afwerx.com/get-funded/ ; https://www.bwcoconsulting.com/fod/spacewerx-sbir-daf26bx06-dv512-cyberspace-warfare-for-space ; https://www.sda.mil/home/work-with-us/small-business/ ; https://www.govconwire.com/articles/lmi-ssc-sbir-logistics-readiness-contract
**Source type:** Primary (AFWERX/SpaceWERX/SDA are official DoD program sites; GovConWire/ExecutiveBiz coverage of specific awards is secondary trade press).
**Confidence:** Medium-High for the SBIR Phase I→II→III procurement pattern; Low for GSA Schedule / clearance-threshold specifics (gap — not found).

---

### 18. Enterprise security-tool onboarding pattern (design partner → shadow mode → full automation → renewal)

**Finding:** No single canonical "official" published customer-journey document found, but the pattern is corroborated as an actual industry norm by multiple live examples:
- **Credo AI** runs a "Shadow AI Discovery" **Design Partner Program** (private-preview stage) explicitly as the entry point before general availability.
- **Cloudflare** launched a formal "Design Partner Designation" program (2026) with named partners to stage rollout of new secure-AI/SASE products.
- Security/network vendors commonly describe a **"monitor mode" (i.e., shadow/observe-only) deployment phase** as the explicit first production step specifically to "minimize customer concerns about introducing new networking/security tools" before moving to enforcement — cited generically in partner-channel guidance (Akamai partner blog).
- Combined, this supports the pattern: **private design-partner cohort → passive/shadow (monitor-only) mode in production → full enforcement/automation → renewal**, as a recognized SaaS security GTM motion, though I did not find one single named company publishing that exact 4-stage funnel end-to-end as a public case study.
**Source:** https://www.credo.ai/shadow-ai-discovery ; https://www.cloudflare.com/press/press-releases/2026/cloudflare-launches-design-partner-designation-to-accelerate-secure-ai-and-seamless-sase-adoption/ ; https://www.akamai.com/blog/partners/2026/jul/partners-defend-network-ease-ai-anxiety
**Source type:** Secondary (vendor blogs/press releases — legitimate as "an analogous SaaS security product's published pattern," per the task's own allowance, but not a formal industry-standard document).
**Confidence:** Medium — pattern is real and multiply-attested but not from one authoritative playbook.

---

### 26. "~40% of small-satellite missions have had partial or total failure in the last 20 years"

**Finding:** The claim is **broadly consistent with, and appears to derive from, real academic literature**, primarily:
- **Langer & Bouwmeester (TU Delft), "Reliability of CubeSats – Statistical Data, Developers' Beliefs and the Way Forward"** (AIAA/USU Small Satellite Conference, 2016) — analyzed 178 launched CubeSats. Kaplan-Meier reliability curves show reliability falling to 75–87% immediately post-deployment, 59–73% at 100 days, and only **48–65% at two years** — i.e., roughly a third to half of CubeSats show meaningful failure within 2 years, not 20.
- A separate, more directly matching figure was surfaced: **"more than 40 percent of CubeSats launched since 2000 failed to accomplish their objectives"** (cited via a broader small-satellite database review, consistent with the well-known Swartwout/Cal Poly CubeSat database analyses referenced in this literature, though I did not directly pull the primary Swartwout paper URL in this pass).
- **Correction/nuance:** the "40%" figure in the literature is typically framed as "since 2000" (i.e., ~25-year window) or as a 2-year post-launch reliability curve, not literally "in the last 20 years" as a rolling window — close enough to be defensible but should be footnoted as "CubeSats/smallsats since 2000" rather than a strict trailing-20-year stat.
**Source:** https://digitalcommons.usu.edu/cgi/viewcontent.cgi?article=3397&context=smallsat (Langer & Bouwmeester, AIAA/USU SmallSat Conference) ; https://www.semanticscholar.org/paper/Reliability-of-CubeSats-%E2%80%93-Statistical-Data,-Beliefs-Langer-Bouwmeester/03d4e3a8d745b028c44c299b17e5a92e344d5d8a
**Source type:** Primary (peer-reviewed/conference academic paper).
**Confidence:** Medium-High — the ~40% figure is real and traceable to credible academic sources, but exact wording ("20 years") should be softened to "since 2000" / "within first 2 years of operation" for accuracy.

---

### 27. Current annual CVE publication volume (~40,000/year claim)

**Finding:** Confirmed and updated with current-year data:
- **2023:** 28,818 CVEs published
- **2024:** 40,009 CVEs published (+38% YoY) — **this is the year that matches the "~40,000/year" claim exactly**
- **2025:** 48,185 CVEs published (+20.6% YoY, ~131/day avg)
- **2026 (YTD, as of Aug 31, 2026):** 57,908 CVEs published — trending well above 40,000 annualized, on pace for a record year.
**Correction:** the "~40,000/year" figure was accurate for **2024** specifically but is now **understated** — actual current-year run-rate is closer to **55,000–60,000+/year** in 2026. Recommend updating the deck's figure or explicitly dating it to "40K in 2024, now tracking ~58K in 2026."
**Source:** https://jerrygamblin.com/2026/01/01/2025-cve-data-review/ ; https://cve.icu/years.html ; https://cyberpress.org/over-40000-cves-published-in-2024/ ; https://www.cve.org/Media/News/item/blog/2026/05/12/CVE-Program-Report-for-Q1-2026
**Source type:** JerryGamblin.com and cve.icu are secondary (independent trackers/analysts using cve.org data feeds); CVE Program Q1 2026 report at cve.org is primary (official CVE.org blog).
**Confidence:** High — multiple independent trackers converge on the same year-over-year figures.

---

### 28. Comparable B2B security-SaaS pricing models (per-asset/per-seat/tiered)

**Finding:** Two solid, well-documented comparables for a "per-satellite" or "per-fleet-tier" pricing structure:
- **CrowdStrike Falcon:** priced **per-endpoint/per-year**, modular — customers buy a base tier (Falcon Pro/Enterprise/Elite/Complete) then add modules (EDR, Identity Protection, Cloud Security, Threat Intel) on top. No public list pricing; sold via direct sales/channel quote. This directly maps to a "per-satellite base + per-module add-on (e.g., per-constellation threat intel)" structure.
- **Datadog (DevSecOps/Cloud Security):** priced **per-host/per-month**, clearly tiered (Free → Pro $15/host/mo → Enterprise $23/host/mo for infra; DevSecOps Enterprise bundle $34/host/mo annual, $41 on-demand), with published list pricing and annual-commit discounts of 15–40%. This is the cleanest public analog for a transparent **"per-satellite/per-asset" unit-priced, tiered-by-feature** model.
**Source:** https://www.crowdstrike.com/en-us/pricing/ ; https://www.crowdstrike.com/en-us/legal/crowdstrike-licensing/ ; https://www.datadoghq.com/pricing/ ; https://last9.io/blog/datadog-pricing-all-your-questions-answered/
**Source type:** CrowdStrike/Datadog own pricing pages = Primary. Third-party pricing-breakdown blogs = Secondary (used to corroborate/summarize since vendor pages don't always list list-price tables cleanly).
**Confidence:** High — both are well-documented, current, and directly analogous (per-asset unit economics + feature tiers), a strong basis for a "per-satellite" or "per-fleet-tier" pricing narrative.

---

## Summary of gaps (do not fabricate — flagged instead of guessed)
- No space-sector-specific cybersecurity consulting day-rate found (item 5) — only general industry rates.
- No specific Viasat KA-SAT dollar cost disclosed anywhere public (item 4) — company states "not material," no figure exists to cite.
- No GSA Schedule / clearance-threshold specifics found for space-sector commercial security-tool sales (item 17) — only SBIR/SpaceWERX pathway confirmed.
- ICEYE/BlackSky-specific security job titles not confirmed (item 16) — only Planet Labs fully confirmed via live posting.
- No single named company publishes the full "design partner → shadow mode → full automation → renewal" funnel as one public case study (item 18) — pattern triangulated from multiple partial sources instead.
