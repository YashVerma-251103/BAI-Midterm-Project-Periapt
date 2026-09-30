# Periapt — Know Which Flaw Matters First

> **WARNING: this draft was written overnight from a plan the user had not yet reviewed** (`report/plans/2026-09-30-report-draft-plan.md`). Check it against the plan and spec before relying on it. Decisions made during the run: `logs/Overnight_Draft_Log_2026-09-30.md`.
>
> Draft for the author's rewrite. Tags: [RF n] = research/Research_Findings.md item · [Q n] = topic/Topic_Brainstorm_Report.md challenge · [R n] = research/Research_Findings_Review.md item. Strip all tags at the .docx step.

## Opening: 2 a.m.

*An illustrative scene.* It is 2 a.m. A security advisory lands: a flaw in the ground mission-control software could let an attacker send commands to the fleet. The vendor has no patch yet. The CISO of a mid-size satellite operator reads it and thinks of 200 satellites. Some are new. Some have flown for years on tired batteries. The security team, the flight-software team and mission operations each hold part of the answer, and each speaks a different language. One question has to be answered before morning: which satellites are most at risk tonight, and what can safely be done before the vendor's fix arrives? Tomorrow another advisory will arrive, and the same question starts again: **which flaw first, and why?**

## A.0 Overview: Periapt

**Brand.** A *periapt* is a protective amulet; the name also echoes *periapsis*, an orbit's closest point. Together: protection at the closest point of risk.
- **Mission:** "Tell every operator, within minutes of a new flaw, what it means for each satellite, with reasons they can check."
- **Vision:** "The trusted decision layer for every spacecraft operator." We start small and grow as trust is earned.

**Where it sits.** Gartner Layer 7, AI Security & Risk, where the course places CrowdStrike; the closest analogue is CrowdStrike's Charlotte AI, which helps analysts triage. Foundation Capital would call it domain-specific AI: the value is knowing satellites, not owning a model. B2B to operators; B2G through operators with US defence contracts.

**Market.** 14,266 satellites operated at end-2025; 4,434 were deployed in 2025 alone (+65%) [RF 1]. That growth is mostly mega-constellations, so Periapt targets the mid-size tier [R1, RF 11].

**Why now.**
- Advisories outgrow teams: 40,009 CVEs in 2024, 48,185 in 2025, 57,908 year to date to 31 August 2026 [RF 27].
- Tools already match known CVEs to software lists (Thales Alenia Space uses Black Duck [RF 12]); what stays manual is judging what a flaw means for *each satellite* [Q40].
- At Viasat in 2022, attackers entered through a misconfigured ground VPN appliance, then sent legitimate management commands; Viasat shipped nearly 30,000 modems [RF 4, RF 32].
- ML already forecasts which IT flaws will be exploited (EPSS [RF 32]); we found nothing that predicts what a flaw would do to a specific satellite.

**Topic fit.** Day zero is the day a flaw becomes known, often before a patch exists. Satellites are not one of the 16 US critical infrastructure sectors [RF 30], but critical sectors depend on them: Viasat's outage cut remote monitoring of ~5,800 wind turbines [RF 4], and the EU lists space as a high-criticality sector [RF 2].

So what does the AI actually do at 2 a.m.?

## A.1 Agentic AI and Value

## A.2 Architecture, Moat and Defensibility

## A.3 Porter's Five Forces

## A.4 Persona and Customer Journey

## A.5 Governance, Guardrails and US Compliance

## Close: Four Lenses, and 2 a.m. Again

## References

## Appendix: Thinking and AI Use
