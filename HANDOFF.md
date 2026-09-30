# Session Handoff

> **⚠ Partly superseded (2026-09-30 evening).** The scope was cut back to the original problem, with AI at the centre: **predictive prioritisation** (scan → score → rank with reasons) delivered as a copilot. The world model now predicts what a flaw would do to each satellite, plus battery/thermal margin. The RL planner, rollout/rollback building and monitoring are cut. See topic report **Q31–Q39**, RF **item 32** and Viva_Prep **§9**. **Spec v2 is NOT to be drafted from.** **Spec v3 is written** (same path) and awaits the user's review. Next: approval → writing-plans → draft. India and SBIR are on hold. §1–§4 below describe the older v2 state; where they differ, trust v3.

**Written:** 2026-09-30, end of the research-validation + report-design session.
**Deadline:** 1 Oct 2026, 23:59. That's about a day, so bias toward drafting, not more research.
**Purpose:** give a fresh session everything it needs to continue without re-deriving decisions. `CLAUDE.md` (auto-loaded) has the stable facts; this file has the *state of work* and the *why* behind recent decisions.

---

## 1. Where we are

The design is finished; the report prose has not been started.

- **Spec v2 written, awaiting the user's approval:** `report/specs/2026-09-30-report-draft-design.md`. The user has **not** approved it yet (last answer before the rename: "Discuss more first", then v2 was written from that discussion).
- **Next steps, in order** (the superpowers:brainstorming → writing-plans flow was in use; respect its gates):
  1. Get explicit approval of spec v2 (or apply requested changes).
  2. Invoke `superpowers:writing-plans` for an implementation plan for the draft; the user picks the execution method.
  3. Write `report/Periapt_Report_Draft.md`: full prose, every fact tagged `[RF n]`/`[Q n]`. **The user will rewrite it in their own voice** (brief §F forbids unrevised AI text; a viva is possible).
  4. Later: visuals (loop diagram + Five Forces table), then `.docx` conversion (docx skill), then strip the tags.
- **Parallel tasks still to launch once the spec is approved** (spec §7):
  - India research (Sonnet subagent) → RF item 32 + `research/raw/08-*.md`. It feeds **one vision line only**: India as next market / engineering base.
  - SBIR/STTR current status check (review R25: items 10/15 say lapsed, item 17 cites a live Sept 2026 topic).
  - *(The name check is done; see §3.)*

## 2. Read order for a new session

1. `CLAUDE.md` (auto-loaded): stable decisions and working habits.
2. **This file.**
3. `report/specs/2026-09-30-report-draft-design.md`: **the blueprint.** Section design, numbers to use or avoid (§4), coverage matrix of every review item (§4a), v2 changes (§8).
4. `report/Viva_Prep.md`: every challenge compressed into defend-ready answers. The fastest way to absorb the reasoning.
5. `research/Research_Findings.md`: the sourced facts (items 1–31). **Check here before stating any number.**
6. `research/Research_Findings_Review.md`: red-team list R1–R35 (why many claims were reframed).
7. `topic/Topic_Brainstorm_Report.md` §4 **Q17–Q30** (this session's challenges), §7 concept (§7.5 moat is marked superseded), §9.6 drafting tasks T1–T8.
8. Only if needed: `research/raw/0N-*.md` (full subagent outputs; never edit), `brief/Instructions.md` (rubric), `Prof_Materials/` course decks (text extracts can be regenerated with `pdftotext`).

## 3. Decisions made this session (and why)

| Decision | Outcome | Why / where logged |
|---|---|---|
| **Company name** | **Periapt**: a protective amulet; echoes *periapsis*, "protection at the closest point of risk" | "Phylax" clashed with Phylax Intelligence (EU AI security firm, different product). Amyntor failed a *deep* check (two Indian cybersecurity firms). Periapt has no security/space use. [Q30] |
| Format | Word/PDF doc, 4 pages + 1-page appendix, 2 visuals | user choice |
| Jurisdiction | **United States** (main); India as next-market line pending research | user choice |
| Draft depth | Full prose with source tags; user rewrites | academic-integrity rule |
| Structure | Design-Thinking frame: empathy opening → one course concept anchoring each rubric section → four-lens close (Feasibility/Usability/Desirability/Viability). Each section also targets a named grading component. | user asked for "course concepts in harmony" + "mix grading components" |
| Positioning | **A domain copilot that owns the workflow**: makes security, flight-software and ops teams more productive; the team decides | [Q26, Q27] |
| Product core | The agentic flow **known flaw → safe, scheduled fix across the whole mission** (reachability → ranked plan → validation → human approval → watch/halt), not scoring or monitoring | [Q26] |
| World model role | **Judge** of manufacturer-emulator runs and the canary satellite vs "how this satellite normally behaves"; fleet-wide watch during rollout. It does **not** predict unseen code. | [Q26, R6] |
| Planner | Constraint solver (passes/power) + learned rollout *ordering*. **Differs from the CLAUDE.md "constrained RL" lock; user confirmation is pending.** | [R8] |
| Moat order | (1) context graph / patch-outcome record → (2) switching costs → (3) efficient scale → network effect *conditional* only. Public data and manufacturer partnerships removed. | [Q18, Q22, RF 7] |
| Value | **No revenue/ACV figure.** Three-layer value case: value table (efficiency / risk / innovation) → before/after of the opening scene → renewal on pilot metrics. Pricing *structure* only: per-fleet subscription + onboarding fee. | [Q29] |
| First customer | One actor: a US mid-size operator that also holds DoD contracts. Persona "the Stretched Sentinel" (CISO) + buying committee (mission-ops approver, SecOps champion). User approved. | [Q28, R26, R27] |
| Liability | "Decision support with evidence and stated residual risk", never "certified safe"; command/boot/auth-path changes never automated; missing approval → hold | [Q25, R29, R30] |

## 4. The discussion arc, compressed (so the next session doesn't re-open settled points)

Each line is a user challenge and what it changed. Full entries are in the topic report §4.
- **Q17:** regulation is a double edge → there is **no binding US vulnerability-management mandate** (RF 30); regulation is only a tailwind.
- **Q18:** public data proves feasibility for everyone → not a moat.
- **Q19:** "static vs live" is the wrong SPARTA axis → reference vs decision-and-execution; build *on* SPARTA.
- **Q20–Q21:** operators already do this in-house, formally (SES 40+ staff, Planet SatSec, Spire ISO 27005 ranking; RF 31) → "connect and speed up", not "you lack a team". The "3-person team" quote **has no source; never cite it.**
- **Q22:** operators won't feed competitors → network effect conditional; SDA-style sharing is the only precedent.
- **Q23:** "worst topic?" → everything that died was an overclaim, not the core. Stop researching, draft.
- **Q24:** unit economics don't close at SaaS per-asset rates; the cost is **people**, not compute.
- **Q25:** "needing undo means unreliable" → reliability = rare, contained, recoverable failures; unrecoverable classes are prevented.
- **Q26–Q27:** detection and monitoring already exist → the product is the flaw→fix flow; a copilot for researchers.
- **Q28:** the persona was a decision, not a task; transcripts go out as Google Drive links.
- **Q29:** drop revenue/ACV; show customer value in three layers.
- **Q30:** name clash → Periapt.

## 5. Hard rules for drafting

- **Source every fact** from `research/Research_Findings.md` (CLAUDE.md rule; §10.1 in the topic report shows why).
- **Never say:** "~16k satellites", "58k CVEs/yr" (57,908 is **YTD to 31 Aug 2026**), any Starlink %, "3-person team", "40% of CubeSats since 2000", "fully tested", "legally required to patch", "nobody validates patches", any revenue/ACV number. (Spec §4.)
- **Name SPARTA/SPARTEND and CT Cubed IRON GALAXY** explicitly (originality rule).
- Keep **Spire** as the co-opetition case, not a buyer; **Globalstar** is out (Amazon acquisition).
- Every review item R1–R35 has a planned handling in spec §4a. Don't silently drop any.
- The user **challenges hard and wants honest pushback, not agreement.** When a challenge lands, log it as the next Q-entry (Q31+) in the topic report §4 *and* add the defend-ready answer to `report/Viva_Prep.md`.

## 6. User-owned tasks (Claude can't do these)

- Approve spec v2 (and confirm the planner change).
- Final rewrite of the draft in their own voice.
- Transcript links: split the **redacted** `logs/TRANSCRIPT_LOG.md` into per-session chunks (Claude can do the split), upload to Google Drive with "anyone with the link can view", and paste ≥2 links into the appendix.
- Before claiming references were read: check NIST IR 8270's control text in the PDF, and cite the SIA *report*, not its press release (R35).

## 7. Practical gotchas

- **Git:** mini-branch per change (`docs/<topic>`), conventional commits, `merge --no-ff` into `main`, never push. `README.md` has an **uncommitted user edit (resume IDs)**: leave it alone and never stage it.
- **`/transcript` does its own git work.** `scripts/transcript.py` branches from the *current* HEAD, commits and merges into `main`. Run from a feature branch, it also merges that branch's unmerged work. That is harmless, but tell the user.
- **Bash's auto-mode safety check can fail transiently.** Fall back to the Read tool for reading.
- **Name checks:** a quick web search isn't enough (Amyntor passed quick, failed deep). Use the extended search mode.
- The session style used subagents only when the user asked (Sonnet for research, Opus for review). Don't spawn unprompted.
