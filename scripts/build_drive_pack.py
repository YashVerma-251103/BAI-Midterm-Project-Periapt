#!/usr/bin/env python3
"""Rebuild Periapt_Drive_Pack/ (gitignored, for Google Drive) from the repo.

Copies the documents, and cuts logs/TRANSCRIPT_LOG.md into one .txt per
conversation. Cuts fall only on user-turn lines; the check at the end joins the
parts back and compares with the log, so nothing is lost. Re-run any time;
add a row to PARTS when a new session is logged.
"""
import re, shutil, textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "Periapt_Drive_Pack"
LOG = (ROOT / "logs" / "TRANSCRIPT_LOG.md").read_text()

S1, S2, S3 = "command-intial-topic-brainstroming", "use-brainstorming-and-research-skills-to-plan-wha", "local-command-caveatcaveat-the-messages-below"
S4, S5, S6 = "discussion-on-the-world-model", "completed-v3-drafted-plan-report-draft-next", "i-have-not-read-the-draft-plan-but-i-think-after"

# (file name, session slug, first user line of the part (None = session start), when, goal, result)
PARTS = [
 ("T01_2026-09-17_Topic-Selection_Satellite-Idea-Locked", S1, None,
  "16 Sep (opened) - 17 Sep 2026",
  "Choose the industry and topic for the mid-sem project.",
  "Topic locked: Day-Zero Vulnerability Prioritisation, narrowed to satellite fleets. Competitors searched; moat, feasibility and the federated-learning idea attacked (a flaw in the AI's reasoning was caught and fixed). US recommended as jurisdiction. Topic report written (challenge log up to Q16). Mini-branch + micro-commit saving habit set."),
 ("T02_2026-09-26_Research-Plan_Seven-Research-Threads-Run", S2, None,
  "26 Sep (plan) - 29 Sep 2026 (research run)",
  "Turn the topic into a research plan, then run the research.",
  "Research_Plan.md written (items tied to the grading rubric). Seven research agents run in parallel; Research_Findings.md compiled and the 'verify before citing' list resolved. Each agent's prompt, approach, sources and output saved in research/raw. Prof_Materials symlink set up and git-ignored."),
 ("T03_2026-09-29_Challenging-Findings_US-Rules-and-In-House-Work", S3, None,
  "29 Sep 2026 (evening, running past midnight)",
  "Test the findings: does a legal duty keep us alive, and are operators really not doing this in-house?",
  "Item 30 added (binding US space-cyber rules). Item 7 corrected from 'moat' to a feasibility argument. In-house-work question sent to research and the discussion compiled (filed in T04 as Item 31 and Q17-Q22)."),
 ("T04_2026-09-30_Red-Team-Review_Economics-and-Liability-Doubts", S3, "Also, I think that research findings need a review",
  "30 Sep 2026 (after midnight)",
  "Red-team the research and test whether the business is feasible at all.",
  "Opus review of the findings saved (Research_Findings_Review.md, R1-R35 + top 5). Item 31 added, moat re-ranked, Q17-Q23 logged. The ~$90K per customer economics and liability doubts answered as Q24-Q25; drafting tasks added."),
 ("T05_2026-09-30_First-Report-Design_Spec-v2-and-Name-Change", S3, "/superpowers:brainstorming create an initial draft",
  "30 Sep 2026 (day)",
  "Design the first draft of the report using every finding, flaw and review.",
  "Draft spec written and revised to v2, covering every review item. Copilot positioning and value challenged (Q26-Q29). Viva_Prep.md started. Name clash found, company renamed Phylax -> Periapt (Q30)."),
 ("T06_2026-09-30_World-Model-Explained_Layered-Approach-Found", S4, None,
  "30 Sep 2026 (evening)",
  "Understand what a world model is and whether it fits the product.",
  "Concept explained in plain words; weaknesses of the JEPA idea found; a layered approach (learned model plus checks) worked out. No files changed in this part; the results were logged later as Q31-Q33."),
 ("T07_2026-09-30_Back-to-Original-Problem_Re-Centred-on-Prioritisation", S5, None,
  "30 Sep 2026 (evening)",
  "Review spec v2 properly, then check it against the original problem statement.",
  "Found the scope had drifted away from prioritisation. Re-centred: predictive prioritisation is the core, delivered as a copilot; autonomous up to the ranking, human approval before anything touches a satellite. Simple-language rule created. Q31-Q37 logged."),
 ("T08_2026-09-30_Hard-Scoring-Review_Concept-Approved", S5, "/effort",
  "30 Sep 2026 (evening)",
  "One last hard review of the whole concept against the grading components and course concepts.",
  "Concept scored against the rubric; verification pass (Item 32) run. World model moved from judging patches to judging threats. Decision list put to the user (concept, ranking rule, references, India/SBIR) - Q38."),
 ("T09_2026-09-30_Spec-v3-Approved_Drafting-Plan-and-Handoff", S5, "I approve the first three.",
  "30 Sep 2026 (night)",
  "Write and approve spec v3, then plan the drafting.",
  "Concept, ranking rule and references approved; India/SBIR on hold. Aerospace Corp treated as complement, not rival (FAR 35.017, Q39). Spec fixes (problem wording, fleet ageing, moat - Q40). Spec v3 approved; drafting plan written; HANDOFF.md and CLAUDE.md rewritten for the next session."),
 ("T10_2026-09-30_Overnight-Draft-Run_Full-Draft-Written", S6, None,
  "30 Sep 2026 (night)",
  "Run the drafting plan unattended while the user slept.",
  "Plan tasks 0-9 run: skeleton, opening and sections A.0-A.5, close, references, appendix, whole-draft checks and the overnight log. Ends with /export and a /transcript attempt (script branch-switch hiccup)."),
 ("T11_2026-10-01_Draft-Review-Part1_Opening-Value-and-Moat", S6, "Hey, I am back",
  "1 Oct 2026 (day)",
  "Review the draft section by section with the user (part 1 of 2).",
  "Opening and A.0 fixed (Layer 7 claim hedged, Q41). A.1 gets a value column, estimate wording and stage descriptions (Q42). A.2 rewritten around earned trust and data ownership (Q43)."),
 ("T12_2026-10-01_Draft-Review-Part2_Five-Forces-to-Appendix_Word-v1-Built", S6, "Yeah, a little more one out three is okay.",
  "1 Oct 2026 (afternoon)",
  "Review the rest of the draft (part 2 of 2) and build the submittable version.",
  "A.3 five forces (Q44), A.4 persona (Q45), A.5 model-poisoning test (Q46), close (Q47), pricing (Q48), appendix (Q49). Draft renamed Periapt_Report_Draft.md; no-repetition pass; handoff updated. Word and PDF v1 built with an S-shaped Figure 1."),
]
APPENDIX_PICKS = ("T01", "T07")

COPY = {  # pack folder -> repo sources
 "01_Submission": ["report/Periapt_Report_v1_FOR-REVIEW.docx", "report/Periapt_Report_v1_FOR-REVIEW.pdf"],
 "02_Brief": ["brief/"],
 "03_Topic_Decision": ["topic/Topic_Brainstorm_Report.md"],
 "04_Research": ["research/"],
 "05_Design_Plans_Viva": ["report/specs", "report/plans", "report/Viva_Prep.md"],
 "06_Drafts": ["report/Periapt_Report_Draft.md", "report/figures", "logs/Overnight_Draft_Log_2026-09-30.md"],
 "08_Project_Notes": ["CLAUDE.md", "HANDOFF.md", "README.md"],
}

W = lambda s, ind="": textwrap.fill(s, 78, initial_indent=ind, subsequent_indent=" " * len(ind))


def bodies():
    return {m.group(1): m.group(2).split("\n") for m in
            re.finditer(r"<!-- session: (.+?) -->.*?```text\n(.*?)\n```\n<!-- /session", LOG, re.S)}


def cut(lines, anchors):
    """Split lines at the user-turn line holding each anchor (searched in order)."""
    idx, pos = [0], 0
    for a in anchors:
        pos = next(i for i in range(pos + 1, len(lines)) if lines[i].startswith("❯") and a in lines[i])
        idx.append(pos)
    return [lines[a:b] for a, b in zip(idx, idx[1:] + [len(lines)])]


def transcripts():
    sess, chunks = bodies(), []
    for slug in dict.fromkeys(p[1] for p in PARTS):
        parts = [p for p in PARTS if p[1] == slug]
        pieces = cut(sess[slug], [p[2] for p in parts[1:]])
        assert "\n".join("\n".join(c) for c in pieces) == "\n".join(sess[slug]), slug  # lossless
        chunks += list(zip(parts, pieces))
    d = OUT / "07_Transcripts"
    d.mkdir(parents=True)
    names = [p[0] for p, _ in chunks]
    for n, ((name, slug, _, when, goal, result), body) in enumerate(chunks):
        multi = sum(1 for p in PARTS if p[1] == slug) > 1
        nav = []
        if n: nav.append("Continues from: " + names[n - 1] if multi and PARTS[n - 1][1] == slug else "Previous: " + names[n - 1])
        if n < len(names) - 1: nav.append("Next: " + names[n + 1])
        head = ["=" * 78, f"{name[:3]}  BAI Mid-Term Project (Periapt) - conversation transcript", "=" * 78,
                W(when, "WHEN:    "), W(goal, "GOAL:    "), W(result, "RESULT:  ")]
        head += [W(x) for x in nav] + [W("Source: logs/TRANSCRIPT_LOG.md, session " + slug + ". Text is cut only between "
                "user messages; nothing is edited. Emails and home paths are redacted. Timestamps inside the text are the "
                "real ones; a session can span several days.")]
        (d / (name + ".txt")).write_text("\n".join(head) + "\n" + "=" * 78 + "\n\n" + "\n".join(body) + "\n")
    rows = "\n".join(f"{p[0][:3]}  {p[0]}.txt\n     WHEN:   {p[3]}\n" + W(p[4], "     GOAL:   ") + "\n" + W(p[5], "     RESULT: ")
                     + "\n     LINK:   ________________\n" for p in PARTS)
    (d / "00_Transcript_Index.txt").write_text(
        "TRANSCRIPT INDEX - every AI conversation of the project, in order.\n"
        f"Suggested for the appendix links: {' and '.join(APPENDIX_PICKS)} (fill the LINK lines after upload).\n\n" + rows)


def main():
    shutil.rmtree(OUT, ignore_errors=True)
    for folder, srcs in COPY.items():
        (OUT / folder).mkdir(parents=True)
        for s in srcs:
            p = ROOT / s
            if s.endswith("/"):  # copy the folder's contents, not the folder
                shutil.copytree(p, OUT / folder, dirs_exist_ok=True)
            else:
                shutil.copytree(p, OUT / folder / p.name) if p.is_dir() else shutil.copy2(p, OUT / folder)
    transcripts()
    (OUT / "00_START_HERE.txt").write_text(
        "PERIAPT - BAI MID-TERM PROJECT: EVIDENCE PACK\n\n"
        "GitHub repo (full history):  ________________\n"
        "This Drive folder:           ________________\n\n"
        "01_Submission/          the report (Word + PDF)\n"
        "02_Brief/               assignment instructions, topic list, professor note\n"
        "03_Topic_Decision/      how the topic was chosen; every challenge and answer (Q1-Q49)\n"
        "04_Research/            plan -> findings -> plain-language version -> red-team review; raw/ = the 7 agents' full records\n"
        "05_Design_Plans_Viva/   report blueprint (spec v3), drafting plan, viva prep\n"
        "06_Drafts/              markdown draft with source tags, figures, overnight drafting log\n"
        "07_Transcripts/         all AI conversations, split by goal (start with 00_Transcript_Index.txt)\n"
        "08_Project_Notes/       CLAUDE.md, HANDOFF.md, README.md (working notes)\n\n"
        "Suggested reading order: 01 -> 07 index -> 05 spec -> 04 findings -> 03 topic report.\n"
        "Note: documents refer to each other by repo paths (e.g. research/Research_Findings.md); "
        "here the same file sits in the numbered folder above.\n")
    print("built", OUT, "-", sum(1 for _ in OUT.rglob("*") if _.is_file()), "files")


if __name__ == "__main__":
    main()
