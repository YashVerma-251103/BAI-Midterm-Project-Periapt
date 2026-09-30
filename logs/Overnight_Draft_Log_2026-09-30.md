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
- **Task 1: complete.** Opening (121 words, target 90–140) + A.0 (320, target 220–320; first pass was 396, trimmed twice). All required terms ok (6/6, 12/12).
  - *Ruling:* Viasat modems worded as "Viasat shipped nearly 30,000 modems" (RF 32 wording), not "replaced" — RF 32 says modems were restorable by factory reset, so "had to be replaced" overstated. Cost if wrong: none.
  - *Ruling:* the opening does not say "dozens of advisories a week" (my first idea) — no source for that rate. It says "tomorrow another advisory will arrive". Cost if wrong: slightly weaker scene.
  - *Ruling:* the fictional CISO gets no gendered pronoun (neutral wording throughout).
  - *Note:* the "we found nothing that predicts…" line in A.0 is an absence-of-claims statement; the streetlight caveat (R23) is stated in A.3.
- **Task 2: complete.** A.1 with the three-layer table, value table, before/after, five tests and the Visual 1 mermaid block. Required terms 16/16 ok. Hedge check: 3 lines flagged, all describe the design (table row, tool list, mermaid node), none claims a result — accepted as the plan allows.
  - *Ruling:* raw word count 615 vs target 420–560 (first pass 713, rewritten). Prose alone, without the mermaid block and tags, is 528, inside the range. The plan says the mermaid block "counts a little", so I stopped cutting there. Cost if wrong: ~55 more words for the user to cut; A.1 is the densest rubric section.
  - *Ruling:* the tool list in "Why it is agentic" is shortened to six named tools ("scores" covers the CVSS/EPSS feed). Cost if wrong: none.
  - *Ruling:* before/after says a ranked list "arrives in minutes" (matches the mission line), marked illustrative; no measured time is claimed.
- **Task 3: complete.** A.2: seven-feature architecture list, "changed tomorrow" answer, five ranked Morningstar moats, value-over-time, not-moats, honest limit. Required terms 9/9 ok; banned moat-claim grep: no output ✓. Words 380 (target 280–380; first pass 397).
  - *Ruling:* spec §2.5 says time in orbit is a moat "because a later rival starts with less history". That clashes with "the telemetry archive belongs to the customer" (a rival could train on the same archive). I wrote "a later rival must retrain on that history and re-earn trust" instead, which is consistent with moat #2. Cost if wrong: a slightly weaker moat claim; flag for the user's morning review.
- **Task 4: complete.** A.3: strategic point first, Visual 2 table (force · rating · evidence · what Periapt does), Spire as co-opetition, named neighbours (SPARTA/SPARTEND, Aerospace + Google, IRON GALAXY, Silent Shield, Spire CMP), streetlight caveat, Aerospace as partner (FAR 35.017, ASC-100), regulation both ways (3.14.1 beachhead). Required terms 15/15 ok; FAR wording grep: no output ✓. Words 420 (target 300–420; first pass 439).
  - *Ruling:* Tenable and Qualys are not in Research_Findings. The topic report's §10.1 log marks them "general industry knowledge — fine to keep", so they stay, tagged `[RF 10; TB §10.1]`. I removed my first-pass claim that they rank "with EPSS", because nothing in the research verifies it. Cost if wrong: none.
  - *Ruling:* "Spire ranks by ISO 27005" was dropped from the Buyers row to save words; it is already stated in A.1. Cost if wrong: none.
- **Task 5: complete.** A.4: persona card (pains, goals, decision criteria, psychographic), buying committee, Diffusion + product lifecycle, journey table (Lemon & Verhoef stages × Puntoni experiences, pilot trap), S11 satisfaction/emotion line, labelled timeline. Required terms 17/17 ok. Words 424 (target 350–470).
  - *Checked in the course decks:* Sanchez et al. (2011) "Subject Matter experts will rely less on automation" and the satisfaction definition (Kumar et al. 2019) are in the Session 11 trust deck; "Over 80% of enterprise AI initiatives stall in the pilot" is in the Session 1 & 2 notes; CrowdStrike "8.5M Windows devices" and Charlotte AI are in the student moats deck. So these course numbers are sourced, even though they aren't in Research_Findings.
  - *Ruling:* the journey is a markdown table (six rows) rather than a strip; the table is the content for Visual 3 and gets drawn as a strip at the .docx step. Cost if wrong: none.
