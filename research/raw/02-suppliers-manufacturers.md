# Research Thread 2 — Suppliers and Manufacturers

**Agent:** general-purpose subagent | **Run:** 2026-09-29 | **Item covered:** 12 (per `Research_Plan.md`)

## Prompt given

> You are researching for a fictitious-company business assignment (satellite-fleet vulnerability-prioritisation AI platform, B2B/B2G, Defence/Space/Cybersecurity segment). Use WebSearch/WebFetch.
>
> Research item 12 from the project's Research_Plan.md: **Supplier power analysis for a Porter's Five Forces section.**
>
> Specifically:
> - Identify the main satellite manufacturers relevant to mid-size constellation operators (e.g. Spire, Airbus Defence and Space, Thales Alenia Space, Terran Orbital, York Space Systems, Blue Canyon Technologies) — for each, note whether they publish anything about software/firmware update practices, SBOMs, or security patching for their satellite buses.
> - Identify ground-station-as-a-service providers (AWS Ground Station, KSAT — Kongsberg Satellite Services, Leaf Space, Atlas Space Operations) — pull pricing model info if public (e.g. AWS Ground Station's pricing page), and note how dependent an operator is on them (switching cost).
> - Assess: is any single supplier (manufacturer or ground-station provider) dominant enough to have high bargaining power over a mid-size operator? Or is the market fragmented (low supplier power)?
> - Note any evidence of manufacturers acting as resellers/channel partners for third-party software/security tools (relevant to a "manufacturers as partners" business model).
>
> Return a clean markdown section covering: Manufacturer landscape / Ground-station provider landscape / Supplier power verdict (with reasoning) — each claim with a source URL. If something can't be found publicly, say so explicitly rather than guessing. Do not write files — return markdown in your final message.

## Approach followed

Web search + fetch across each named manufacturer and ground-station-as-a-service provider individually, looking specifically for SBOM/patch-cadence disclosures, pricing pages, and reseller/partner-program evidence. Cross-checked market-structure claims (consolidation trend, hyperscaler competition) against trade press. Every claim tagged with a source URL; anything not found publicly (SBOM disclosures, numeric pricing, manufacturer-as-security-reseller evidence) was reported as an explicit gap.

## Sources visited

- https://spire.com/space-services/constellation-management-platform/
- https://cyber.airbus.com/en/newsroom/stories/2025-11-securing-our-space-future-our-commitment-to-satellite-security
- https://www.cyber.airbus.com/markets/space/
- https://www.blackduck.com/resources/case-studies/thales-alenia-space.html
- https://spacenews.com/terran-orbital-completes-delivery-of-satellite-bus-platforms-to-lockheed-martin-for-the-tranche-1-transport-layer/
- https://spacenews.com/york-space-systems-building-larger-lx-class-satellite-platform/
- https://www.bluecanyontech.com/technical-capabilities/
- https://www.futuremarketinsights.com/reports/small-satellite-market-share-analysis
- https://docs.aws.amazon.com/ground-station/latest/ug/contacts.billing.html
- https://aws.amazon.com/ground-station/pricing/
- https://www.satellitetoday.com/technology/2025/09/29/ksat-debuts-new-subscription-for-integrated-mission-services/
- https://www.kongsberg.com/ksat/services/ground-station-services/
- https://leaf.space/leaf-line/
- https://www.satellitetoday.com/technology/2023/02/01/atlas-space-operations-to-resell-aws-ground-station-through-partner-program/
- https://www.satelliteinsights.com/the-independent-and-regional-satellite-ground-segment-layer-a-2026-map/

## Full output

## Research Item 12 — Supplier Power Analysis (Porter's Five Forces)

### Manufacturer landscape (satellite bus suppliers for mid-size constellation operators)

| Manufacturer | Public info on SW/FW updates, SBOM, or patching |
|---|---|
| **Spire Global** | Publishes a "Constellation Management Platform" with an **On-Orbit Update Manager** described as automating satellite software deployment, automated rollbacks, and CI/testbed integration; also states ground-to-satellite links are end-to-end encrypted and Spire's own ground stations never decrypt customer data, with an optional double-encryption tier. No public SBOM or patch-cadence disclosure found. Notably, Spire markets this platform as a service to *other* operators, not just internal use. Source: [Spire Constellation Management Platform](https://spire.com/space-services/constellation-management-platform/) |
| **Airbus Defence and Space** | Has a dedicated "Airbus Cyber" business unit publishing general statements on satellite cybersecurity (zero-trust framework, COTS security testing, digital twins for verification) but **no specifics found on SBOM practices or patch/update cadence for satellite buses**. Sources: [Airbus Cyber — Securing Our Space Future](https://cyber.airbus.com/en/newsroom/stories/2025-11-securing-our-space-future-our-commitment-to-satellite-security), [Airbus Cyber Security for Space](https://www.cyber.airbus.com/markets/space/) |
| **Thales Alenia Space** | Confirmed to use **Black Duck SCA to generate and maintain an SBOM** of open-source components in its code, and states nearly 100% of its codebases contain open source; coding standards based on SEI CERT; physical/software domain segregation between payload and satellite control. This is the strongest concrete SBOM evidence found among manufacturers. Source: [Black Duck case study — Thales Alenia Space](https://www.blackduck.com/resources/case-studies/thales-alenia-space.html) |
| **Terran Orbital** (now part of Lockheed Martin, acquired Oct 2024) | No public information found on SBOM, firmware update practices, or patch cadence. Public materials focus on bus delivery milestones (e.g., SDA Tranche 1/3 contracts). Explicitly **could not find** security/patching disclosures. Sources: [Terran Orbital Tranche 1 delivery](https://spacenews.com/terran-orbital-completes-delivery-of-satellite-bus-platforms-to-lockheed-martin-for-the-tranche-1-transport-layer/) |
| **York Space Systems** | States its LX-CLASS bus "expands on cybersecurity protections developed for military customers" on its S-CLASS bus, reusing >90% of that design (implying shared, unpatched-in-place software lineage across products). No SBOM or patch-process detail disclosed. Source: [SpaceNews — York LX-CLASS](https://spacenews.com/york-space-systems-building-larger-lx-class-satellite-platform/) |
| **Blue Canyon Technologies** (RTX/Raytheon subsidiary) | Public materials mention Type-1 hardware encryption support for secure-comms missions and a new "FleXbus" modular subsystem line, but **no SBOM, patching or firmware-update disclosure found**. Source: [Blue Canyon Technical Capabilities](https://www.bluecanyontech.com/technical-capabilities/) |

**Consolidation trend relevant to supplier power:** Large primes are acquiring smallsat bus manufacturers — Lockheed Martin acquired Terran Orbital (Oct 2024, ~$450M), RTX owns Blue Canyon, Boeing owns Millennium Space Systems, Kongsberg owns NanoAvionics. This reduces the number of *independent* mid-size bus suppliers over time. Source: [Small Satellite Market Share Analysis](https://www.futuremarketinsights.com/reports/small-satellite-market-share-analysis)

### Ground-station-as-a-service (GSaaS) provider landscape

| Provider | Pricing model (public) | Switching-cost / dependency notes |
|---|---|---|
| **AWS Ground Station** | Usage-based, per-minute, metered by antenna contact duration (rounded up to nearest minute). Two axes: **On-Demand** (no commitment) vs **Reserved** (discounted, monthly commitment); **Narrowband** (<40MHz) vs **Wideband** (≥40MHz). Approximate published community-sourced rates: Narrowband ~$3/min reserved vs ~$10/min on-demand; Wideband ~$10/min reserved vs ~$22/min on-demand (discount tiers for ≥150 min/month annual commitments). AWS's own pricing page does not list numeric rates publicly and directs to sales contact. Sources: [AWS Ground Station billing docs](https://docs.aws.amazon.com/ground-station/latest/ug/contacts.billing.html), [AWS Ground Station pricing page](https://aws.amazon.com/ground-station/pricing/) |
| **KSAT (Kongsberg Satellite Services)** | No public per-minute pricing found. Recently (per Via Satellite, publishing around the query date) launched **Integrated Mission Services (IMS)** — a bundled subscription (ground network + satellite ops + mission monitoring) on a **"pay-as-you-grow"** model, explicitly marketed to reduce new-infrastructure burden as fleets scale. Operates 280+ antennas / 20+ sites globally including the uniquely valuable polar Svalbard site — a differentiator competitors can't easily replicate for polar-orbit coverage, which raises *KSAT-specific* switching cost for polar-heavy missions. Sources: [Via Satellite — KSAT IMS](https://www.satellitetoday.com/technology/2025/09/29/ksat-debuts-new-subscription-for-integrated-mission-services/), [KSAT Ground Network Services](https://www.kongsberg.com/ksat/services/ground-station-services/) |
| **Leaf Space** | Publishes tiered but not itemized pricing: "Leaf Line" (multi-mission GSaaS, all-inclusive per-minute pricing, access to one or all stations at fixed per-minute rate) and "Leaf Key" (dedicated GSaaS for medium-large constellations, monthly subscription scaled to performance need, positioned as a way to avoid the NRE/dedicated-staff cost of building a proprietary ground segment). Preferential pricing available with 1-year+ commitment. No specific dollar figures published. Source: [Leaf Space — Leaf Line](https://leaf.space/leaf-line/) |
| **Atlas Space Operations (Freedom)** | No public pricing found. Notably, **Atlas is a reseller of AWS Ground Station** under AWS's solution-provider partner program — Atlas customers get access to AWS's antenna sites through Atlas's own "Freedom" software with "zero software changes" required, growing Atlas's federated network from 18 to 29 sites. This is evidence of **aggregation reducing switching costs**: operators using Atlas's software layer can draw on multiple underlying networks (Atlas-owned + AWS + others) without re-integrating. Source: [Via Satellite — Atlas resells AWS Ground Station](https://www.satellitetoday.com/technology/2023/02/01/atlas-space-operations-to-resell-aws-ground-station-through-partner-program/) |

**Market structure context:** The GSaaS market is bifurcating into (a) hyperscaler-backed players (AWS Ground Station — Azure Orbital was shut down by Microsoft in 2024, reducing hyperscaler competition) and (b) independent/specialized operators (KSAT, Leaf Space, Atlas) plus aggregators that broker partner capacity (Infostellar, RBC Signals) rather than owning full networks themselves. Source: [Satellite Insights — 2026 ground-segment map](https://www.satelliteinsights.com/the-independent-and-regional-satellite-ground-segment-layer-a-2026-map/)

### Supplier power verdict

**Overall: moderate-low, trending toward moderate.** Reasoning:

1. **Satellite bus manufacturers — fragmented today, consolidating.** A mid-size operator can choose among Spire, Airbus, Thales Alenia, York, Blue Canyon, Terran Orbital (now Lockheed-owned), NanoAvionics, Rocket Lab, LeoStella, and others — enough independent options to keep any single manufacturer's bargaining power low *today*. However, the trend of prime contractors (Lockheed, RTX, Boeing, Kongsberg) absorbing independent bus makers is shrinking the pool of truly independent suppliers, which should push supplier power upward over the medium term — worth flagging as a forward-looking risk in the Five Forces writeup rather than a present-day high-power claim.

2. **Ground-station providers — fragmented, and actively de-fragmenting further via aggregation.** No single GSaaS provider is dominant enough to hold high bargaining power: AWS has scale but a competing hyperscaler already exited (Azure Orbital, 2024), independents (KSAT, Leaf Space) compete on price/coverage, and aggregator-resellers (Atlas reselling AWS, Infostellar, RBC Signals) exist specifically to let operators multi-home across networks through one software layer with minimal switching friction. The one partial exception is **KSAT's Svalbard polar site**, which is a geographically unique asset — an operator with heavy polar-LEO coverage needs could face elevated switching cost/bargaining power from KSAT specifically, even though the broader GSaaS market is not dominated by KSAT.

3. **No evidence of forced lock-in via proprietary/incompatible protocols** was found in public sources — ground segment communication generally uses interoperable standards (e.g., CCSDS-family protocols referenced across these providers' marketing, though this project's search did not verify CCSDS compliance claims per-vendor), and the Atlas/AWS reseller relationship explicitly markets "zero software changes" when adding capacity from a second network, which is direct evidence *against* high switching costs at the software-integration layer.

4. **"Manufacturers as channel partners" angle:** Concrete evidence found is on the ground-segment side, not the bus-manufacturer side: **Atlas Space Operations formally resells AWS Ground Station** under AWS's solution-provider partner program (confirmed, sourced above). On the manufacturer side, the only comparable reseller pattern found is unrelated to security tooling — e.g., **Telespazio reselling Starlink Business Services** in Europe, and **Globalsat Group reselling Amazon Leo** for enterprise customers — which shows satellite/ground infrastructure players do commonly act as resellers/channel partners for adjacent providers' connectivity products. **No direct public evidence was found of a satellite bus manufacturer (Spire, Airbus, Thales Alenia, York, Blue Canyon, Terran Orbital) formally reselling or channel-partnering for a *third-party cybersecurity/patching tool*.** Thales Alenia's use of Black Duck SCA is a *customer* relationship (buying an SCA tool), not evidence of Thales reselling it onward. This should be stated explicitly in the report as an unconfirmed/not-found item rather than assumed — if the business model needs a "manufacturer as reseller of our security product" precedent, the closest real-world analogue found is the Atlas–AWS or Telespazio–Starlink reseller structures, not a manufacturer-security-tool precedent.

**Bottom line for the Five Forces write-up:** Supplier power should be scored **low-to-moderate**, not high — fragmented manufacturer and ground-station markets currently give mid-size operators real choice and low switching costs (reinforced by aggregator/reseller models), with two caveats worth naming explicitly: (a) prime-contractor consolidation of bus manufacturers is an emerging upward pressure on manufacturer power, and (b) KSAT's polar ground-station asset (Svalbard) creates a narrow pocket of elevated supplier power for polar-coverage-dependent operators specifically.

---

### Items explicitly not found (state as gaps, not guesses)
- No public SBOM disclosure for Airbus D&S, Terran Orbital, York Space Systems, or Blue Canyon Technologies satellite buses.
- No public patch-cadence/patch-SLA figures for any of the six manufacturers.
- No numeric public pricing for KSAT, Leaf Space, or Atlas Space Operations (all require sales contact); only AWS Ground Station has semi-public per-minute rate figures (and those come from third-party/community sources, not AWS's own page, which withholds numbers).
- No evidence found of any satellite bus manufacturer formally reselling/channel-partnering a third-party cybersecurity or patch-management product.
