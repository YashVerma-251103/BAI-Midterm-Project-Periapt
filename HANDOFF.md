# Session Handoff

**Written:** 2026-09-30, end of the overnight drafting run (the earlier version, written after spec v3 + the plan, is in git history).
**Deadline:** 1 Oct 2026, 23:59. No new research.

> The draft was written overnight from a plan the user had not read. **On 1 Oct the user reviewed the whole draft section by section with Claude (Q41–Q49)** and approved renaming it to `report/Periapt_Report_Draft.md`.

---

## 1. Where we are

- **Spec v3 is approved:** `report/specs/2026-09-30-report-draft-design.md`.
- **The drafting plan was run in full overnight (Tasks 0–9), unattended.** The user had not read the plan.
- **Draft written and reviewed:** `report/Periapt_Report_Draft.md` (with source tags). Reviewed with the user on 1 Oct (Q41–Q49). Body ≈ 3,700 words without tags; it must shrink to ≈ 2,100 for 4 pages.
- **Every decision made on the user's behalf** is in `logs/Overnight_Draft_Log_2026-09-30.md` ("Rulings", "Deferred minors"). Read it first.

## 2. What the next session does, in order

1. Read `logs/Overnight_Draft_Log_2026-09-30.md`, then the draft.
2. The user reviews the plan and the draft (morning of 1 Oct). Act on their changes; log new challenges as Q41+.
3. Done 1 Oct: draft renamed after the review. Next: the no-repetition pass (Claude), then the user's rewrite and cut.
4. Then: the user's voice rewrite and cut to 4 pages + 1-page appendix → visuals (Visual 1 mermaid, Visual 2 Five Forces table, Visual 3 persona + journey) → .docx (docx skill) → strip tags. User tasks are in §6.
5. `scripts/draft_check.sh` points at the current draft name by default (`DRAFT=<path>` overrides it). Re-run the checks after edits.

## 3. Read order

1. `CLAUDE.md` (auto-loaded): locked decisions and working habits.
2. **This file.**
3. `report/specs/2026-09-30-report-draft-design.md`: **the blueprint.** Read all of it: the product (§2), threads (§3), each section (§4), the use/avoid list (§5), and the coverage matrix (§6).
4. `report/plans/2026-09-30-report-draft-plan.md`: the tasks and their checks (all tasks run; checkboxes ticked; deviations are in the overnight log).
5. `report/Viva_Prep.md` **§9**: the current reasoning in plain words. §1–§8 are older; where they differ, §9 wins.
6. `research/Research_Findings.md`: check here **before writing any number**. Item 32 holds the newest verified facts.
7. Only if needed: `topic/Topic_Brainstorm_Report.md` §4 **Q31–Q40** (why the scope changed), `research/Research_Findings_Review.md` (R1–R35), and `Prof_Materials/` (course decks; regenerate text with `pdftotext` if needed).

## 4. The concept in one paragraph

Periapt watches new security advisories around the clock. For every flaw it works out which satellites are affected, whether an attacker could reach them, how likely an attack is, and **what the attack would actually do to each satellite**. It then ranks the flaws with reasons and briefs each team (security, flight software, mission ops) in its own terms.
- **AI parts:** an LLM agent (reads, matches, briefs) and a **world model** learned per fleet from telemetry and command history. The world model predicts attack impact per satellite and forecasts battery/thermal margin.
- **Reused, not rebuilt:** existing tools cover CVSS, EPSS and SPARTA.
- **Autonomy:** it runs on its own up to the ranking. Humans can override at any time. A human approves anything that touches a satellite or a ground system.
- **Ranking rule:** the AI can raise a priority; lowering it needs a human; outside the model's data, impact counts as high.
- **Scope:** Stage 1 is prioritisation only. Fixing, validation and rollout are later stages, once trust is earned.

## 5. Decisions made in this session (and why)

| Decision | Outcome | Where logged |
|---|---|---|
| Scope | Cut back to the original problem: **predictive prioritisation**, not the whole flaw → fix flow | Q34, Q36 |
| Positioning | A copilot for the three teams; it plugs into their own ranking method (e.g. ISO 27005) | Q35 |
| World model | Predicts **flaw impact** per satellite, plus margin forecast. It does **not** predict what a patch does, and it is **not** a monitoring product | Q31, Q33, Q36 |
| Planner | RL dropped; a plain scheduler fed by the forecast | Q32 |
| Autonomy | Autonomous up to the ranking; on-the-loop override; in-the-loop approval | Q37 |
| Aerospace Corp | **Complement, not rival** (builds on SPARTA; FAR 35.017, softened wording) | Q39, Q40 |
| Value over time | Grows with time in orbit; how fast is a pilot metric, not a promise | Q39, Q40 |
| Moat | The record + earned trust. The telemetry archive belongs to the customer | Q40 |
| People-heavy | Deliberate, to earn trust; viability stays the weakest point | Q39 |
| References | SIA 2026 report · NIST SP 800-171 · NIST AI RMF 1.0 · Hundman et al. 2018 | spec §1 |
| Visuals | 3: loop diagram (mermaid in the draft), Five Forces table, persona + journey strip | spec §4 |
| India, SBIR | **On hold.** Keep them out of the draft | spec §9 |

## 6. User-owned tasks (Claude can't do these)

- The final rewrite of the draft in their own voice, and cutting it to 4 pages + a 1-page appendix.
- Choosing the appendix's hardest concept (default: *what the AI should predict*).
- Transcript links: run `/export` then `/transcript` for this session; split the **redacted** `logs/TRANSCRIPT_LOG.md` into chunks; upload to Google Drive with "anyone with the link can view"; paste ≥2 links into the appendix.
- Before submitting: check the NIST AI RMF PDF text, and cite the SIA *report*, not its press release.
- The India decision.
- Whether to move `Discussion on the World model.txt` into `logs/` as appendix evidence (it's the user's own study session).

## 7. Practical gotchas

- **Git:** mini-branch per change (`docs/<topic>`), conventional commits, `merge --no-ff` into `main`, never push. **Never stage** `README.md` (the user's uncommitted edit) or `Discussion on the World model.txt` (the user's file).
- **`/transcript` does its own git work:** it branches from the current HEAD and merges into `main`. Run from a feature branch, it also merges that branch. Harmless, but tell the user.
- **The Bash safety check can fail transiently.** Retry once. If it fails again, use the Read/Edit/Write tools, which worked every time this session.
- **Plain language is a user rule:** short, simple, to the point, no jargon.
- The user challenges hard and wants honest pushback. Log each new challenge as the next Q-entry (**Q41+**) in the topic report §4 *and* in Viva_Prep §9.
- Subagents only when the user asks.
