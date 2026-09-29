# CLAUDE.md

Context for every session working on this project.

## What this is

The Business of AI — Mid-Semester Assignment (20 marks). **Not code.** The deliverable is a 4-page + 1-page-appendix story of a fictitious AI company, submitted as a doc/slides/video (or a mix), due **1 Oct 2026, 23:59**. See `brief/Instructions.md` for the graded rubric (§A: Overview, Agentic AI & Value, Moat, Porter's Five Forces, Persona & Journey, Governance) and `brief/GC_instructions.txt` for the professor's framing note. `brief/Project Topics.md` is the source topic list — read-only, never edit.

## Locked decisions

- **Company:** an AI platform that prioritises and safely resolves cybersecurity vulnerabilities across satellite missions (ground → network → spacecraft → terminals), inside the listed topic "Day-Zero Vulnerability Prioritisation" (Defence, Space & Cybersecurity segment).
- **Architecture:** JEPA-style world model (fleet telemetry) + constrained RL rollout planner + LLM agent (advisory ingestion) + human-approved uplinks only. Full detail and its evolution: `topic/Topic_Brainstorm_Report.md` §7.
- **Jurisdiction:** United States recommended (NIST AI RMF + IR 8270/8401 + SPD-5 + ITAR/EAR) — see `topic/Topic_Brainstorm_Report.md` §4 Q16. **Final confirmation still pending.**
- **Still open:** company name/mission/vision, submission format, final jurisdiction sign-off.

## File map

| Folder | Holds |
|---|---|
| `brief/` | Assignment inputs (Instructions, Project Topics, professor note). Read-only. |
| `topic/` | `Topic_Brainstorm_Report.md` — topic decision history, every challenge raised and answered, §10.1 verification log. |
| `research/` | `Research_Plan.md` (29 numbered research tasks, tagged to rubric markers) → `Research_Findings.md` (sourced answers) → `Research_Findings_Explained.md` (same, plain-language). `Research_Findings_Review.md` (red-team list of weak claims, R1–R35 + top 5). `research/raw/` = the 7 subagents' full prompts/approach/sources/output — never edit, historical record. |
| `report/` | Final submission goes here. Currently empty. |
| `logs/` | `TRANSCRIPT_LOG.md` (committed, redacted, feeds the mandatory GenAI appendix) + `exports/` (raw `/export` dumps, source material for the log). |
| `scripts/` | `transcript.py` + its test — do not hand-edit `TRANSCRIPT_LOG.md`. |
| `Prof_Materials` | Symlink to the professor's lecture/student-PPT materials — gitignored (external, not project content), but its course concepts must be applied when drafting. |

Flow: `research/raw` → `research/Research_Findings*` → `topic/` → `report/`.

## Constraints that shape every decision

- **Must not be an existing company's work** — this is why the satellite niche exists inside the generic "Day-Zero Vulnerability Prioritisation" topic. Before asserting originality, check `research/raw/03-competitors-rivalry.md` — Aerospace Corp's SPARTA and CT Cubed's IRON GALAXY are the two closest adjacents and must be named/differentiated explicitly in the report, never omitted.
- **4 pages + 1-page appendix.** Appendix needs: working evidence, AI tools used + ≥2 transcript links, hardest-concept discussion, what was accepted/modified/rejected/independently developed.
- **3–4 key references, non-blog.** Shortlist already narrowed in `research/Research_Findings.md` item 29.
- Grading: Content 8 · Presentation 4 · Storytelling 4 · Creativity 4. Plagiarism must stay under 10%.

## Working habits (do these without being asked)

- **Source facts, don't recall them.** Before stating a market number, competitor claim, or regulatory fact in the report, check `research/Research_Findings.md` first. If it's not there, either research it or flag it explicitly as unverified — never assert from model memory (see `topic/Topic_Brainstorm_Report.md` §10.1 for what happened last time unverified numbers were used).
- **Save work in mini-branches.** Every meaningful change: short-lived `docs/<topic>` branch, small commits with conventional prefixes, `git merge --no-ff` back into `main`, never push (no remote), leave branches undeleted. Don't wait to be asked.
- **Transcripts.** After `/export`, run `/transcript` (wraps `scripts/transcript.py`) to file it into `logs/TRANSCRIPT_LOG.md`. A later export that continues an earlier one replaces that section — don't hand-append.
- **User challenges reasoning hard** and wants honest pushback, not agreement — see the full challenge/answer log in `topic/Topic_Brainstorm_Report.md` §4 for the standard this project holds itself to.
