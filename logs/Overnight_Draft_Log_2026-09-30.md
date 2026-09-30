# Overnight Draft Session — Log and Decisions

**Started:** 2026-09-30, late evening. **Run:** unattended (user asleep; session in zellij).
**Goal:** write the report draft by running `report/plans/2026-09-30-report-draft-plan.md` against spec v3.
**Read this first in the morning.** Every decision I made on the user's behalf is listed under "Decisions (rulings)", with what it costs if wrong.

## User instructions for this run (verbatim summary)
- The user has **not read the drafting plan**. For safety, the draft's **file name must say so**, and this must be marked in the new handoff, `CLAUDE.md` and `README.md`.
- Read the handoff and start working without waiting.
- Log everything and every decision separately (this file).
- The user reviews the draft and the plan in detail in the morning.

## Decisions (rulings)
Format: *decision — why — cost if wrong.*

1. **Execution method: Native (one session writes everything).** — HANDOFF §2 says ask first; the user said "start working" and is asleep. Native is the recommended option and CLAUDE.md says no subagents unless asked. — Cost if wrong: none to the text; subagent-driven would only have changed who wrote each section.
2. **Draft file name: `report/Periapt_Report_Draft_PLAN-NOT-USER-REVIEWED.md`** instead of the plan's `report/Periapt_Report_Draft.md`. — The user asked for the "plan not reviewed" warning to be in the file name. — Cost if wrong: one rename (`git mv`) after the morning review.
3. **Branch: `docs/report-draft-v3`** instead of the plan's `docs/report-draft`. — `docs/report-draft` already exists (spec-phase branch, already merged into `main`; branches are never deleted in this project). — Cost if wrong: none.
4. **`scripts/draft_check.sh` default path points at the new file name.** Every plan command that hard-codes `report/Periapt_Report_Draft.md` is run against the new name. — Follows from ruling 2. — Cost if wrong: none.
5. **Final review is a self-review, not a fresh reviewer subagent.** — The executing-plans skill wants a fresh subagent reviewer; CLAUDE.md/HANDOFF say subagents only when the user asks. User instructions win. — Cost if wrong: a self-review shares the author's blind spots; the user's morning review is the real second pair of eyes.
6. **README.md is edited, but only my line is committed.** The user's own uncommitted lines (the `claude --resume` IDs) are left unstaged, as the handoff requires. — The user explicitly asked for a README mark. — Cost if wrong: none; the user's lines stay exactly as they were.
7. **No test-driven cycle in the code sense.** This is prose, so the plan's shell checks (required terms, banned words, word counts) are the "tests". Each section's check is run after writing it. — Cost if wrong: none.

(More rulings are appended below as tasks run.)

## Progress (one line per task)

- **Task 0: complete.** Skeleton (10 headings) + `scripts/draft_check.sh`. Checks: heading count 10 ✓; empty A.1 = 0 words ✓; missing term → `MISSING zzz`, exit 1 ✓. Added a warning banner at the top of the draft pointing to the unreviewed plan and this log.
