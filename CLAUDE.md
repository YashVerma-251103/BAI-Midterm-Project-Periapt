# CLAUDE.md

Context for every session working on this project.

## What this is

The Business of AI — Mid-Semester Assignment (20 marks). **Not code.** The deliverable is a 4-page + 1-page-appendix story of a fictitious AI company, submitted as a doc/slides/video (or a mix), due **1 Oct 2026, 23:59**. See `brief/Instructions.md` for the graded rubric (§A: Overview, Agentic AI & Value, Moat, Porter's Five Forces, Persona & Journey, Governance) and `brief/GC_instructions.txt` for the professor's framing note. `brief/Project Topics.md` is the source topic list — read-only, never edit.

## Locked decisions

- **Company:** **Periapt** (protective amulet; echoes *periapsis*): an AI platform that predicts and prioritises which known security flaws matter most for each satellite in an operator's fleet (ground systems count as the way in), inside the listed topic "Day-Zero Vulnerability Prioritisation" (Defence, Space & Cybersecurity segment). Renamed from Phylax on 2026-09-30 (name clash; topic report Q30).
- **Positioning (re-centred 2026-09-30, Q31–Q39):** **predictive prioritisation** is the core: scan advisories → score → rank flaws per satellite, with reasons. It's delivered as a copilot to the security, flight-software and ops teams, and each team keeps its decision. It runs on its own up to the ranking; a human approves anything that touches a satellite or a ground system. It complements Aerospace Corp (builds on SPARTA; under FAR 35.017 an FFRDC shouldn't use privileged access to compete with industry). Growth is staged: fixing, validation and rollout come later, once trust is earned.
- **Architecture:** LLM agent (self-hosted, citation-required; ReAct orchestrator) + reused scores (CVSS, EPSS, SPARTA) + reach map + **world model** (learned per fleet from telemetry and command history; predicts what an attacker's commands would do to each satellite, and forecasts battery/thermal margin; JEPA-style as the candidate). Ranking rule: the AI can raise a priority, lowering needs a human, and outside its data means high. The RL planner, patch testing, rollout/rollback and monitoring are **cut** from Stage 1. Evolution: topic report Q26 and Q31–Q39.
- **Jurisdiction:** **United States** (confirmed 2026-09-30). India line and SBIR: on hold (user decision pending).
- **Format:** Word/PDF doc, 4 pages + 1-page appendix, 3 visuals. Draft in markdown with source tags; the user rewrites it in their own voice.
- **Current state:** see `HANDOFF.md` (read it first in a new session). Spec v3 is approved; the drafting plan (`report/plans/2026-09-30-report-draft-plan.md`) was run overnight (Native); the draft `report/Periapt_Report_Draft.md` was reviewed with the user on 1 Oct (Q41–Q49), and the user confirmed it holds all the material. Next: the submittable Word version for the user's review (`report/Periapt_Report_v1_FOR-REVIEW.docx`), then their rewrite and submission. Overnight decisions: `logs/Overnight_Draft_Log_2026-09-30.md`.

## File map

| Folder | Holds |
|---|---|
| `brief/` | Assignment inputs (Instructions, Project Topics, professor note). Read-only. |
| `topic/` | `Topic_Brainstorm_Report.md` — topic decision history, every challenge raised and answered, §10.1 verification log. |
| `research/` | `Research_Plan.md` (29 numbered research tasks, tagged to rubric markers) → `Research_Findings.md` (sourced answers) → `Research_Findings_Explained.md` (same, plain-language). `Research_Findings_Review.md` (red-team list of weak claims, R1–R35 + top 5). `research/raw/` = the 7 subagents' full prompts/approach/sources/output — never edit, historical record. |
| `report/` | `specs/2026-09-30-report-draft-design.md` (report blueprint, **spec v3, approved**), `plans/2026-09-30-report-draft-plan.md` (drafting tasks + checks), `Viva_Prep.md` (defend-ready answers; §9 is current). The draft (`Periapt_Report_Draft.md`) and final submission go here. |
| `logs/` | `TRANSCRIPT_LOG.md` (committed, redacted, feeds the mandatory GenAI appendix) + `exports/` (raw `/export` dumps, source material for the log). `Overnight_Draft_Log_2026-09-30.md`: rulings and checks from the unattended drafting run. |
| `scripts/` | `transcript.py` + its test, `build_drive_pack.py` (Drive pack builder) — do not hand-edit `TRANSCRIPT_LOG.md`. `draft_check.sh` (created by plan Task 0) — checking tool for the draft only (required terms, word counts per section); not part of the report. |
| `Periapt_Drive_Pack/` | Generated, **gitignored** upload folder for Google Drive: numbered folders (brief, topic, research, specs/plans/viva, drafts, transcripts T01–T12, notes) + `00_START_HERE.txt`. Rebuild with `python3 scripts/build_drive_pack.py`; never hand-edit. |
| `Prof_Materials` | Symlink to the professor's lecture/student-PPT materials — gitignored (external, not project content), but its course concepts must be applied when drafting. |

Flow: `research/raw` → `research/Research_Findings*` → `topic/` → `report/`. `HANDOFF.md` (root) = current work state for a fresh session.

## Constraints that shape every decision

- **Must not be an existing company's work** — this is why the satellite niche exists inside the generic "Day-Zero Vulnerability Prioritisation" topic. Before asserting originality, check `research/raw/03-competitors-rivalry.md` — Aerospace Corp's SPARTA and CT Cubed's IRON GALAXY are the two closest adjacents and must be named/differentiated explicitly in the report, never omitted.
- **4 pages + 1-page appendix.** Appendix needs: working evidence, AI tools used + ≥2 transcript links, hardest-concept discussion, what was accepted/modified/rejected/independently developed.
- **3–4 key references, non-blog.** Final list approved in spec v3 §1 (SIA 2026 report, NIST SP 800-171, NIST AI RMF 1.0, Hundman et al. 2018); it replaces the item 29 shortlist.
- Grading: Content 8 · Presentation 4 · Storytelling 4 · Creativity 4. Plagiarism must stay under 10%.

## Working habits (do these without being asked)

- **Source facts, don't recall them.** Before stating a market number, competitor claim, or regulatory fact in the report, check `research/Research_Findings.md` first. If it's not there, either research it or flag it explicitly as unverified — never assert from model memory (see `topic/Topic_Brainstorm_Report.md` §10.1 for what happened last time unverified numbers were used).
- **Save work in mini-branches.** Every meaningful change: short-lived `docs/<topic>` branch, small commits with conventional prefixes, `git merge --no-ff` back into `main`, never push (no remote), leave branches undeleted. Don't wait to be asked.
- **Transcripts.** After `/export`, run `/transcript` (wraps `scripts/transcript.py`) to file it into `logs/TRANSCRIPT_LOG.md`. A later export that continues an earlier one replaces that section — don't hand-append. For a new session, add a row to `PARTS` in `scripts/build_drive_pack.py` (goal, result; cut only on user-turn lines) and rebuild the pack. The build checks the split is lossless.
- **User challenges reasoning hard** and wants honest pushback, not agreement — see the full challenge/answer log in `topic/Topic_Brainstorm_Report.md` §4 for the standard this project holds itself to. Log each new challenge as the next Q-entry (Q41+) there and in `report/Viva_Prep.md` §9.
- **Plain language.** Answers are short, simple and to the point, with no jargon (user rule, 2026-09-30).
