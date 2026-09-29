# Research Thread 7 — Operators' In-House Vulnerability Management & Data-Sharing Willingness

**Agent:** general-purpose subagent (Sonnet) | **Run:** 2026-09-30 | **Items covered:** 31 (new, added after the original 29-item plan; see `research/Research_Findings.md` item 31)

## Prompt given

> Research question (for a university business-strategy report; today is 2026-09-30). We are designing a fictitious company: an AI platform that prioritises cybersecurity vulnerabilities across a satellite operator's whole mission system (ground stations → network → spacecraft → user terminals), validates candidate fixes in a digital twin, and schedules human-approved rollouts. Target customers are mid-size operators (roughly 50–300 satellites): Planet Labs, Spire Global, Iridium, SES, Intelsat (now part of SES), ICEYE, plus BlackSky and Globalstar as smaller comparators.
>
> We need hard evidence on HOW these operators handle vulnerability management TODAY, internally or via vendors, so we can judge whether they are real buyers or whether in-house work / existing vendors already cover the need. Use WebSearch/WebFetch. Prefer primary sources: SEC 10-K/20-F filings (especially Item 1C "Cybersecurity", required since FY2023 — quote it), company job postings (Greenhouse/Lever/LinkedIn/company careers pages), conference talks (e.g., CYSAT, Space Symposium, SmallSat, DEF CON Aerospace Village), company engineering blogs, official product pages.
>
> For each operator, find:
> 1. 10-K / 20-F / annual-report cybersecurity disclosure (Item 1C or equivalent for non-US filers like SES, ICEYE): what they say about risk management, vulnerability management, third-party assessors/tools, who owns it (CISO? reporting line?), team size if stated, any disclosed incidents.
> 2. Job postings (current or archived 2024–2026) mentioning vulnerability management, patching, flight software security, mission systems security, space segment security — and what tools/processes they name (e.g., Tenable, Qualys, Wiz, CrowdStrike, SBOM tools).
> 3. Any indication of security team size (headcount statements, LinkedIn-reported counts from secondary articles, talk statements). Mark approximate counts clearly.
> 4. Any evidence they do cross-domain (ground → spacecraft) vulnerability prioritisation, or digital-twin/testbed validation of patches before uplink, in-house.
>
> Separately:
> 5. Spire Global's "Constellation Management Platform" / On-Orbit Update Manager (https://spire.com/space-services/constellation-management-platform/): what exactly it does and does NOT do. Does it do security vulnerability prioritisation, or only software deployment/rollback? Who are its named external customers?
> 6. Any public evidence of satellite operators sharing security/telemetry data with each other or with a third party (e.g., Space ISAC membership and what members share, any consortium/federated data programs), and evidence of their reluctance to share (competitive/ITAR concerns).
> 7. Try to find ANY source for the claim "a 3-person team manages 300 satellites and 12 ground stations" or similar small-security-team-vs-large-fleet statistics for satellite operators. If not found, say NOT FOUND explicitly.
>
> Rules: cite a URL and date for every claim. Quote exact text where possible. Mark anything not confirmed from a primary source as UNVERIFIED. Say "not found" explicitly rather than filling gaps from memory. Do not edit any files.
>
> Return markdown with sections per operator, then sections 5–7, then a bottom line (max 8 lines) answering: (a) do mid-size operators already do this work internally, and how mature does it look; (b) is there evidence of the gap (cross-domain prioritisation + pre-uplink validation) we claim, or not; (c) does evidence support or undercut operators' willingness to share data with a third party.

## Approach followed

Read SEC 10-K Item 1C cybersecurity disclosures directly for the US filers (Planet, Spire, Iridium, BlackSky, Globalstar) and the SES Annual Report 2025 for SES/Intelsat, so those quotes are exact. Pulled live job postings from company boards (Greenhouse, iCIMS) and archived ones from aggregators. Aggregator and snippet dates are marked UNVERIFIED. Read the Spire CMP product page and a NASA-hosted Planet mission-ops deck directly. Checked data-sharing bodies (Space ISAC, Space Data Association, EU Space ISAC) and ran exact-phrase and paraphrase searches for the "3-person team" quote. Some pages returned 403/410 (s-isac.org, Via Satellite, expired postings) and are marked as such. Triggered by the user's challenge "why did we assume the companies are not doing the work internally?" (session of 2026-09-30).

## Sources visited

- https://www.sec.gov/Archives/edgar/data/1836833/000119312526119957/pl-20260131.htm
- https://job-boards.greenhouse.io/planetlabs/jobs/8014499
- https://job-boards.greenhouse.io/planetlabs/jobs/8160756
- https://embedded.jobs/job/Sr-Security-Engineer-Embedded-Software-with-Planet-689fc5
- https://jobs.luxcapital.com/companies/planet/jobs/20997019-flight-software-engineer-security
- https://www.nasa.gov/sites/default/files/atoms/files/how_to_effectively_operate_100s_of_satellites_-_lessons_learned_from_planet_mission_operations.pdf
- https://www.sec.gov/Archives/edgar/data/1816017/000119312526116169/spir-20251231.htm
- https://startup.jobs/secops-engineer-spire-company-8019001
- https://jobs.spacecapital.com/companies/spire-3/jobs/69451534-product-security-engineer
- https://www.sec.gov/Archives/edgar/data/1418819/000141881926000009/irdm-20251231.htm
- https://careers-iridium.icims.com/jobs/5124/senior-security-engineer-%28swoop%29/job
- https://www.ses.com/sites/default/files/2026-03/SES_AR25_2MAR26_vs21_web-LR.pdf
- https://www.ses.com/sites/default/files/2022-01/SES_and_Cybersecurity_FAQ.pdf
- https://satnews.com/2019/10/23/ses-joins-as-a-founding-member-of-the-space-information-sharing-and-analysis-center/
- https://builtin.com/job/manager-information-security-management-bucharest-ro/6829881
- https://builtin.com/job/senior-security-engineer-information-protection-and-cyber-security-iris2-betzdorf-lu/8013676
- https://iceye.com/hubfs/_DATA_AND_MISSIONS/ICEYE%20SAR%20Data%20Service%20Security.pdf
- https://jobs.trueventures.com/companies/iceye/jobs/42908174-senior-security-engineer-on-premise-infrastructure
- https://www.sec.gov/Archives/edgar/data/1753539/000175353926000032/bksy-20251231.htm
- https://boards.greenhouse.io/blacksky/jobs/8817028002
- https://www.sec.gov/Archives/edgar/data/1366868/000136686826000012/gsat-20251231.htm
- https://satnews.com/2026/04/18/amazonglobalstar-turbocharging-the-industry/
- https://spire.com/space-services/constellation-management-platform/
- https://www.airandspaceforces.com/satellite-operators-cybercrime-constant-threat/
- https://spacenews.com/space-industry-group-warns-of-escalating-cyber-threats-outmatched-defenses/
- https://www.space-data.org/sda/wp-content/uploads/2026/06/Who-are-the-SDA.pdf
- https://www.euspa.europa.eu/sites/default/files/documents/eu_space_isac_terms_of_reference.pdf
- https://www.satellitetoday.com/cybersecurity/2025/01/31/space-isac-brings-new-testing-capabilities-to-members/
- https://defenseone.com/business/2021/02/space-firms-put-aside-rivalries-share-threat-data/172285

## Full output

# Operator vulnerability-management evidence (research run 2026-09-30, no files edited)

**Sourcing notes.** The 10-K Item 1C texts, the SES Annual Report, the Spire product page, the Planet greenhouse feed and the Planet/NASA slide deck were fetched and read directly, so quotes from those are exact. Older job postings (Iridium 3695/4418/4620/4635, Spire product-security and SecOps, Intelsat, ICEYE) now return 410/403/expired. For those I rely on aggregator copies or search snippets, and their posting dates are UNVERIFIED. A few pages returned 403 (s-isac.org, Via Satellite). Anything I could not read is marked as such. Scratch downloads are in the session scratchpad only.

---

## 1. Planet Labs (~200+ operating sats; ground, network, spacecraft, terminals all in scope)

**Item 1C** (10-K FYE 31 Jan 2026, filed 2026-03-23): https://www.sec.gov/Archives/edgar/data/1836833/000119312526119957/pl-20260131.htm
- Scope: "We operate complex terrestrial and orbital computer networks and systems... comprising four interdependent security domains including: corporate security, space segment, data pipeline, and customer delivery."
- Process: "secure development lifecycle... formal security risk assessments, security design reviews, vulnerability management, security testing and verification of critical systems via in-house and third party penetration tests, proactive survivability planning, and third party risk management. Planet's secure development lifecycle leverages industry standard tools, guidelines and practices to identify and manage security vulnerabilities." No tool is named.
- Owner: "a dedicated security team... composed of professionals, each with deep cybersecurity expertise ranging from ten to twenty years, including our Chief Security Officer... Our Chief Security Officer regularly reports to our audit committee, risk management committee, and the board of directors." Internal auditors independently test IT and cyber controls. A management risk committee is led by the General Counsel and CFO.
- Team size: not stated (NOT FOUND).
- Incidents: "not been materially affected... including as a result of previously identified cybersecurity incidents". Prior incidents exist but are not detailed.

**Jobs**
- Current: "Vice President & Chief Information Security Officer" is posted twice, San Francisco (first published 2026-06-18, https://job-boards.greenhouse.io/planetlabs/jobs/8014499) and Arlington VA (2026-08-26, https://job-boards.greenhouse.io/planetlabs/jobs/8160756).
  - Scope: "Serve as the ultimate subject matter expert for security issues, including AI governance, secure machine learning pipelines, and space/ground-station asset protection." It also lists ISO 27001, ISO 42001, ISO 9001 and CMMC, plus ITAR/EAR/NDP-1 industrial security.
  - Two open CISO reqs against a 10-K that names a "Chief Security Officer" suggests a leadership change or restructure. That is my inference, not a stated fact.
- Archived, undated: "Sr. Security Engineer, Embedded Software" (greenhouse job 7099388, aggregator copy https://embedded.jobs/job/Sr-Security-Engineer-Embedded-Software-with-Planet-689fc5, now expired; $144.5k–$180.6k). Quote: "Planet's Satellite Security Team (SatSec)... mission is to secure Planet's space related systems." Duties include "Security focused code review of satellite and ground based software," "Running PEN tests," and "Maintaining systems... such as Hardware Security Modules". It names no vulnerability-management product (no Tenable, Qualys, etc.).
- Archived: "Flight Software Engineer, Security" (https://jobs.luxcapital.com/companies/planet/jobs/20997019-flight-software-engineer-security, "Posted 6+ months ago"): "Design and implement the processes and protocols to safeguard satellite communications, software updates, and data integrity."

**Cross-domain and pre-uplink validation (in-house, primary source).** Planet slide deck "How to Effectively Operate 100's of Satellites" (Lisa McGill, June 2022, hosted by NASA): https://www.nasa.gov/sites/default/files/atoms/files/how_to_effectively_operate_100s_of_satellites_-_lessons_learned_from_planet_mission_operations.pdf
- On-orbit software deploy workflow: "Prepare – Create ticket → In Progress → In Review: Impact is assessed, software is ground tested → Staging: On-orbit limited testing → Production: Rollout to production fleet → Done", with "Won't Fix: Software deemed un-spaceworthy".
- So Planet already runs ground test, then on-orbit canary, then fleet rollout, for software generally. The deck does not say this covers security patches specifically.
- No digital-twin claim found. "Nominal operations is 100% automated."

---

## 2. Spire Global (100+ sats, 55+ ground stations incl. partners; the 10-K says "over 30 ground stations")

**Item 1C** (10-K FY2025, filed 2026-03-19): https://www.sec.gov/Archives/edgar/data/1816017/000119312526116169/spir-20251231.htm
- ISMS: "We hold an ISO 27001:2013 certification related to our information security management system... encompasses... our corporate IT environment, as well as the satellite command and control systems, data uplink and downlink pipelines, and ground stations." Cross-domain scope, but as a certification scope rather than a prioritisation tool.
- Vendors and tools: "We also engage third-party penetration testers, assessors, vendors, and auditors to support external network vulnerability scanning, penetration testing, internal and external audits, threat intelligence, and employee training. In addition, we employ a range of self-hosted and SaaS-based tools to aid in vulnerability identification, mitigation, and remediation." No product is named.
- Prioritisation: "We rank and prioritize identified risks and vulnerabilities for mitigation based on the factors described above" (ISO 27005 likelihood/impact). Mitigation is "regular software patching and updates... prompt response to newly discovered exploitable vulnerabilities."
- Owner: overseen by the CTO. "Day-to-day... fall to the Director of Information Security and IT, who reports directly to the CTO, along with the cybersecurity professionals on that team." No CISO. No headcount (NOT FOUND).
- Incidents: none material.

**Jobs**
- Live Greenhouse board on 2026-09-30 (42 jobs): no dedicated security-titled role.
- Archived, via search snippets and aggregators (dates UNVERIFIED): "Security Operations Engineer" ($189–225k, startup.jobs/secops-engineer-spire-company-8019001). Text: "operating the vulnerability management lifecycle across endpoints, servers, containers, and cloud workloads, including scanning cadence, finding validation, prioritization, remediation tracking, and exception governance."
- Also archived: "Product Security Engineer" (Boulder, $171–202.5k, https://jobs.spacecapital.com/companies/spire-3/jobs/69451534-product-security-engineer, "no longer accepting applications"). Text: "SBOMs and vulnerability scanning into CI/CD pipelines" and "CMMC Level 2 requirements in AC, IA, SC, and SI families, building on their ISO 27001 foundation". A Principal Product Security role also exists on zerogtalent.
- Only the snippet text was retrievable. Neither names a commercial scanner. Neither mentions spacecraft.

---

## 3. Iridium (66 operational LEO sats, plus Aireon payloads)

**Item 1C** (10-K FY2025, filed 2026-02-12): https://www.sec.gov/Archives/edgar/data/1418819/000141881926000009/irdm-20251231.htm
- "Our most important information system is our satellite network and related ground systems that carry our customers' traffic."
- "Our management, led by our chief information officer, in conjunction with our internal management security committee and third-party service providers..." Methods include "manual and automated tools, internal and external threat assessments, and internal and external vulnerability assessments." Third parties are "threat intelligence service providers; cybersecurity consultants and software providers; penetration testing firms; monitoring services; forensic investigators."
- Controls list "vulnerability management, including of third parties". The committee meets monthly and the board gets quarterly reports. The CIO (20 years' experience) is supported by a "director of information security". The CIO "approv[es] budgets... approving cybersecurity processes". Reporting line is CIO to the CEO-level committee. No headcount (NOT FOUND). No incidents disclosed.

**Jobs**
- Live on 2026-09-30, Tempe AZ: "Senior Security Engineer (SWOOP)", https://careers-iridium.icims.com/jobs/5124/senior-security-engineer-%28swoop%29/job. Quote: "provide security support to Iridium's unique ground network... implementing new security technologies, upgrading and enhancing existing technologies, implementing security policies." Also "Principal Security Design Engineer" for a new service (job 5104), and "Senior Cloud DevSecOps Engineer" (5035/5053). No posting date is displayed.
- Archived, via search snippets (410 now): "Cyber Security Analyst" for an SDA project, "discovering vulnerabilities and risks on IT and OT equipment... ongoing vulnerability scans". The Principal Systems Security Administrator posting cites "DISA STIG and IAVA benchmarks" and "Space Force and DISA IAVA standards" (job 4635). No commercial tool names were found.
- The vulnerability work visible is ground and IT/OT (DoD compliance), not spacecraft.

---

## 4. SES (incl. Intelsat, consolidated from 2025-07-17)

**Annual Report 2025** (published 2026-03-03): https://www.ses.com/sites/default/files/2026-03/SES_AR25_2MAR26_vs21_web-LR.pdf (Cybersecurity section, p.131; risk table; p.154 IT controls)
- Team: "SES specialized Information and Cybersecurity team, numbering over 40 professionals, drives a multi-year Cybersecurity Strategy known as CORE." This is the only hard security-headcount figure found for any operator.
- Owner: "The Chief Engineering and Operations Officer, a member of the Senior Leadership Team, receives and reviews cybersecurity reporting and provides regular updates to both the Audit and Risk Committee and the Board." The report does not name a CISO.
- Scope: "embedded across the entire SES operational footprint, from customer interfaces through secure network and ground infrastructure, across satellite systems, and back to applications at remote sites... Regular external penetration testing and ongoing internal vulnerability assessments." It also cites a "dedicated Security Operations Centre" and zero trust.
- Integration: "the company is progressing toward a single, unified cybersecurity framework" across SES and legacy Intelsat.
- Risk table: "Persistent cyberattack threats targeting critical space and ground infrastructure pose a material risk of severe service disruptions."
- Older SES Cybersecurity FAQ (PDF metadata 2022-01): https://www.ses.com/sites/default/files/2022-01/SES_and_Cybersecurity_FAQ.pdf. Quote: "we operate an internally managed platform from a market-leading vendor that is complemented by a series of independently conducted external penetration tests. Our systems are continually scanned for vulnerabilities." The vendor is unnamed. It says "24/7/365" SIEM monitoring.
- Space ISAC: founding member (satnews, 2019-10-23). SES VP Group Information and Cyber Security Andre Adelsbach sits on the ISAC board. https://satnews.com/2019/10/23/ses-joins-as-a-founding-member-of-the-space-information-sharing-and-analysis-center/

**Jobs** (dates not displayed)
- "Manager, Information Security Management (Bucharest)" (https://builtin.com/job/manager-information-security-management-bucharest-ro/6829881): "Perform information security audits and vulnerability assessments and support the management of vulnerabilities"; "Vulnerability, compliance and patch management for complex networks, systems and applications". No product named.
- IRIS2 security engineer roles (Betzdorf): "space and ground architectural diagrams"; experience across "satellite control or data planes, IT & Datacentres, 5G systems, OSS/BSS, User Terminals, terrestrial fixed and mobile networks". This is cross-domain security architecture, but for design and accreditation, not vulnerability triage. https://builtin.com/job/senior-security-engineer-information-protection-and-cyber-security-iris2-betzdorf-lu/8013676
- Current SES careers search for "cyber" (2026-09-30) lists several information-security, cloud and system-security roles.

**Intelsat** (legacy jobs, spacetalent/builtin, dates UNVERIFIED): "Senior Security Operations Engineer" described as "threat & vulnerability management"; "Senior Network & Information Security Engineer" with "threat and vulnerability management". Intelsat no longer files separately, and the SES AR covers it.

---

## 5. ICEYE (private, Finland; 600+ employees per postings; SAR constellation)

No 10-K/20-F equivalent exists. Company documents only:
- "SAR Data Service Security" one-pager (dated 24/04/2024): https://iceye.com/hubfs/_DATA_AND_MISSIONS/ICEYE%20SAR%20Data%20Service%20Security.pdf. Quotes: "ISO/IEC 27001 ISMS certification"; controls include "security monitoring in satellite operations and service delivery... disaster recovery and vulnerability management"; "ICEYE manages security of its service and software supply chains and responds rapidly to vulnerabilities and incidents related to them." No owner, headcount or tools named.
- Jobs (aggregator copies, "Posted 6+ months ago", now closed):
  - "Senior Security Engineer (On-Premise Infrastructure)": securing "ICEYE's on-premise infrastructure and customer environments. This infrastructure is the heart of ICEYE's Mission Ground Segment product, used to operate satellite fleets." Part of a "Security Engineering team" (https://jobs.trueventures.com/companies/iceye/jobs/42908174-senior-security-engineer-on-premise-infrastructure).
  - "Product Security" role: "Embedding security into our DevOps pipelines... threat modelling, spotting vulnerabilities."
  - Warsaw "Senior Security Engineer": "Identify any publicly known vulnerabilities as well as new security issues that might arise from operational and functional risks."
  - There are also "Information Security Officer – GRC" and "Security Officer" postings (thehub.io), which I did not open.
- No cross-domain prioritisation or digital-twin evidence found. Notably ICEYE sells a Mission Ground Segment to sovereign customers, so it has its own security-for-customers problem.

---

## 6. BlackSky and Globalstar (smaller comparators)

**BlackSky** (10-K FY2025, filed 2026-03-17): https://www.sec.gov/Archives/edgar/data/1753539/000175353926000032/bksy-20251231.htm
- "We conduct at least quarterly assessments of risks from cybersecurity threats... evaluate the effectiveness of our safeguards at least semi-annually."
- "Our Chief Information Officer [who reports to the CEO] is primarily responsible for assessing and managing our material risks." The CIO reviews "weekly reports provided by our security team highlighting metrics that relate to potential threats and vulnerabilities". The Strategy Committee chair is a former Principal Deputy DNI.
- "We, like any technology company... have previously experienced cybersecurity incidents" (none deemed material). Third parties: "assessors, consultants, or other third parties for supplemental cyber monitoring." No tools or headcount.
- Live job (posted 2026-09-23): "Principal DevSecOps Architect" to "shape and drive the cybersecurity of BlackSky software systems and satellite ground segment deployments". It cites NIST 800-171/800-53/207 and FedRAMP; "assessing vulnerabilities and security risks through security and architectural reviews"; Terraform/Helm. It reports to the VP Product Architecture, alongside an "Information Security Office". https://boards.greenhouse.io/blacksky/jobs/8817028002

**Globalstar** (10-K FY2025, filed 2026-02-27; text identical to FY2024): https://www.sec.gov/Archives/edgar/data/1366868/000136686826000012/gsat-20251231.htm
- Program is "led by our Data Protection Officer", who is the VP of Network IT and Applications with 25+ years of experience. It is "on par with... NIST Cybersecurity Framework", "audited on an annual basis by independent third parties". "We also have a department dedicated to monitoring our systems." It does not mention vulnerability management at all.
- Jobs: only a cybersecurity intern posting found (wellfound), with "vulnerability assessments".
- Globalstar has about 24 satellites and Amazon is acquiring it for $11.6B, scheduled to close in 2027 (satnews 2026-04-18, https://satnews.com/2026/04/18/amazonglobalstar-turbocharging-the-industry/). It is below the 50–300 sat band and is about to be absorbed. It is a poor buyer.

---

## 5 (task item). Spire Constellation Management Platform (CMP) / On-Orbit Update Manager

Page fetched 2026-09-30: https://spire.com/space-services/constellation-management-platform/ (unversioned marketing page). Launched 2023-11-14, co-funded by ESA ARTES CC (€1.5M) and the Luxembourg Space Agency, per search-result copies of the satnews/SpaceNews articles (not opened).

**What it does** (page text):
- "a tool for streamlining satellite control for our customers; automating operations".
- Features: Smart Scheduling, File system manager, SLA monitoring, Configuration manager, Health monitoring and alerting, Telemetry Manager, and the 3S Console.
- "On-orbit update: The On-Orbit Update Manager automates satellite software deployment for quick updates and minimal downtime, offering automated rollbacks and CI/Testbed integration."
- "command and control for your constellation, satellite, virtual satellite, flatsat, and engineering model all from one dashboard."
- "Manage 100+ satellites single-handedly"; "All you ever need is one person and one laptop to control the entire operation."

**What it does NOT do (on the page).** The word "vulnerab", "patch" or "cyber" does not appear. The only "security" hits are "securing our position as the global leader" and "signals intelligence... early warnings and security". It has no vulnerability ingestion, CVE or advisory correlation, risk scoring or prioritisation, and no cross-domain (ground/network/terminal) view. It is deployment, rollback and testbed CI, so it is a possible integration point or partner for a pre-uplink validation step, not a competitor on prioritisation. That is my reading. Spire's roadmap could change.

**Named external customers on the page:** HiSky and Myriota (connectivity, "latest customers"), Northstar Earth & Space (space situational awareness/traffic vigilance), Adler (micro-debris monitoring). The page also names UK MoD, ESA and NASA as consumers of Spire's constellation data, which is not the same as CMP customers. Customer counts and any security-purchase detail: NOT FOUND.

---

## 6. Data sharing between operators / with third parties, and reluctance

**Evidence of sharing**
- Space ISAC (founded 2019, portal live Feb 2021, watch center 2023):
  - Members named: SES (founding member, board seat), Maxar/Vantor ("member of the Space ISAC and active contributor of threat intelligence", Air & Space Forces, 2025-10-21: https://www.airandspaceforces.com/satellite-operators-cybercrime-constant-threat/), Kratos, Booz Allen, MITRE, Parsons, Lockheed, Northrop, JHU APL, Aerospace Corp; plus Capella Space per a search snippet (UNVERIFIED).
  - Membership announcements: none found for Planet, Spire, Iridium, ICEYE, BlackSky or Globalstar. Absence of an announcement is not evidence of non-membership. The roster page was blocked (403).
  - Cost: "Companies pay anywhere from $2,500 to $50,000 a year" (SpaceNews, 2024-06-18: https://spacenews.com/space-industry-group-warns-of-escalating-cyber-threats-outmatched-defenses/).
  - What is shared: threat and vulnerability alerts, incident reports, indicators (via CSAP/TIX platforms per a search snippet), not fleet telemetry. The portal is "hosted by Cyware Labs", with "real-time alerting" on "mission impact, threat trending, operational hazards, and mitigation strategies" (Defense One, 2021-02-25).
- Space Data Association (2009): Intelsat, SES and Inmarsat founded it, with 21 members per the search snippet. Operators "pool" ephemeris and planned manoeuvre data in a neutral Space Data Center run by GMV. "Member information is never shared externally without consent, and in the event of an alert, only the minimum necessary data is disclosed." https://www.space-data.org/sda/wp-content/uploads/2026/06/Who-are-the-SDA.pdf. This is competitor-to-competitor, third-party-mediated sharing of operational data, but for collision safety, where the incentive is strong.
- EU Space ISAC: terms of reference v3.0 (2024-04-16) describe "sharing return of experience on security incidents on a voluntary basis". https://www.euspa.europa.eu/sites/default/files/documents/eu_space_isac_terms_of_reference.pdf
- Aerospace Corp's ASC-100 federated testbed access for Space ISAC members (Via Satellite, 2025-01-31): https://www.satellitetoday.com/cybersecurity/2025/01/31/space-isac-brings-new-testing-capabilities-to-members/. This is a competitor or adjacent offering to the digital-twin validation idea.

**Evidence of reluctance**
- Defense One (2021-02-25, Weisgerber): "It's rare for companies to openly share information about threats to their products or corporate infrastructure as it can reveal vulnerabilities and hand competitors an advantage." https://defenseone.com/business/2021/02/space-firms-put-aside-rivalries-share-threat-data/172285
- Space ISAC design responds to it: data "anonymized to ensure companies do not inadvertently reveal their own vulnerabilities" (SpacePolicyOnline, 2020-01-23); "non-attributable basis" (Air & Space Forces, 2018). Search-derived text, from an article I could not open (403): "Companies, worried about reputational damage or impacts to their share price, are generally unwilling to reveal if they've been attacked", so TLP (Clear/Green/Amber/Red) is used (Via Satellite, 2025-10-07, UNVERIFIED wording).
- ITAR/export-control explicit reluctance to share: NOT FOUND in these sources. Planet's CISO posting shows ITAR/EAR/NDP-1 are live compliance concerns, but that is not evidence about sharing.
- Federated or pooled security telemetry programs across operators: NOT FOUND. Everything found is human-mediated threat-intel sharing (ISAC) or ephemeris pooling (SDA).

---

## 7. "A 3-person team manages 300 satellites and 12 ground stations" (small security team vs large fleet)

**NOT FOUND** in any primary or secondary source, after several exact-phrase and paraphrase searches. Do not cite it.

Nearest verifiable data points, all different in kind:
- Planet (ops, not security): Dove fleet run on "One-week on-call rotations with one daily check-in (~1 hr)"; SkySat had "teams of 2" per contact in the past; "Nominal operations is 100% automated" (NASA-hosted Planet deck, June 2022).
- Spire marketing (ops, not security): "Manage 100+ satellites single-handedly."
- Hard security headcount: only SES ("over 40 professionals", AR 2025). No headcount stated by Planet, Spire, Iridium, BlackSky, Globalstar or ICEYE. LinkedIn-derived counts: NOT FOUND in citable secondary sources.
- Sector-wide: Space ISAC's executive director said the industry "lacks the resources and coordination to adequately defend itself" (SpaceNews, 2024-06-18). That is qualitative and gives no team sizes.

Other findings:
- No commercial vulnerability-tool names (Tenable, Qualys, Wiz, CrowdStrike, etc.) appear in any operator 10-K or in the postings I could read. The only tool-type hints are SBOM/CI-CD scanning (Spire product security), Terraform/Helm (BlackSky), HSMs (Planet), and STIG/IAVA (Iridium), plus SES's unnamed "market-leading vendor" scanner.
- SES has not published a CISO name in the 2025 AR. The older data point that the VP Group Information and Cyber Security was Andre Adelsbach comes from 2019 and secondary profile text.

---

## Bottom line

- **(a) In-house maturity:** Every operator claims a formal in-house program: ISO 27001 (Spire, SES, ICEYE, Planet), a named security leader, pen-testing, scanners and board reporting. SES has 40+ staff. Planet has a dedicated Satellite Security team (SatSec) and a staged ground-test to on-orbit-canary to fleet software-deploy pipeline. The programs look conventional (compliance and IT-centric) rather than novel. Small-tier operators (Spire, BlackSky, Globalstar) name single directors or a CIO/CTO with unstated team sizes.
- **(b) The gap:** Not evidenced directly. I found no operator claiming unified ground-to-spacecraft-to-terminal vulnerability prioritisation, and none claiming a digital-twin patch validation. Spire ranks vulnerabilities under an ISO 27005 risk method, and Planet and SES describe multi-domain scope. The gap is therefore an absence of public claims, not proof of absence. SES's IRIS2 hiring shows cross-domain security is being done as design and accreditation work, not as triage. The Planet and Spire deploy pipelines (ground test, staging, rollback, CI/testbed) show that pre-uplink validation exists for software generally, so "no one validates patches" would be wrong. Only "not tied to vulnerability prioritisation" can be argued.
- **(c) Data sharing:** Mixed. Operators do share via the Space ISAC (SES on its board) and the SDA (safety data through a neutral third party). But sharing is anonymised, TLP-gated and human-curated, and reluctance is documented ("hand competitors an advantage", with reputational and share-price concerns cited via a snippet). Nothing found supports a federated telemetry pool. A design that keeps each operator's data on-premise and shares only derived intelligence fits the evidence better than one that centralises raw fleet telemetry.
- **Buyer viability:** Real buyers (SES, Planet, Iridium) already staff this function and are consolidating or re-hiring leadership (Planet CISO reqs; SES-Intelsat integration). Globalstar is being acquired. Spire's CMP is a potential partner or integration point, not a rival.
