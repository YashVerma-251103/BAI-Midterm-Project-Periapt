#!/usr/bin/env python3
"""Clean a Claude Code /export file and append it to TRANSCRIPT_LOG.md, then commit.

Usage: transcript.py [export.txt]   (default: newest export in project root)
Re-running for the same session replaces its section (keyed by filename slug).
"""
import re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOG = ROOT / "TRANSCRIPT_LOG.md"
NAME = re.compile(r"(\d{4}-\d\d-\d\d)-(\d\d)(\d\d)\d\d-(.+)\.txt$")
HEAD = "# Conversation Transcript Log\n"


def redact(s):
    s = re.sub(r"[\w.+-]+@[\w-]+\.[\w.]+", "[email]", s)
    return re.sub(r"/home/[^/\s]+", "~", s)


def section(name, text):
    date, hh, mm, slug = NAME.match(name).groups()
    lines = text.splitlines()
    start = next((i for i, l in enumerate(lines) if l.startswith("❯")), 0)  # drop banner
    body = "\n".join(lines[start:]).strip()
    title = redact(lines[start][1:].strip())[:80] if lines else slug
    return (f"<!-- session: {slug} -->\n## {date} {hh}:{mm} — {title}\n\n"
            f"```text\n{redact(body)}\n```\n<!-- /session: {slug} -->\n")


def upsert(log, slug, sec):
    pat = re.compile(rf"<!-- session: {re.escape(slug)} -->.*?<!-- /session: {re.escape(slug)} -->\n", re.S)
    if pat.search(log):
        return pat.sub(lambda _: sec, log)
    return log.rstrip("\n") + "\n\n" + sec


def git(*a):
    subprocess.run(["git", "-C", str(ROOT), *a], check=True)


def main():
    if len(sys.argv) > 1:
        src = Path(sys.argv[1]).resolve()
    else:
        found = sorted(p for p in ROOT.glob("*.txt") if NAME.match(p.name))
        if not found:
            sys.exit("no export found; run /export first")
        src = found[-1]
    if not NAME.match(src.name):
        sys.exit(f"not an /export filename: {src.name}")
    slug = NAME.match(src.name).group(4)
    dest = ROOT / "exports" / src.name
    dest.parent.mkdir(exist_ok=True)
    if src != dest:
        src.rename(dest)
    log = LOG.read_text() if LOG.exists() else HEAD
    LOG.write_text(upsert(log, slug, section(dest.name, dest.read_text())))

    branch = "docs/transcript-" + NAME.match(dest.name).group(1)
    git("switch", "-q", "-c", branch) if subprocess.run(
        ["git", "-C", str(ROOT), "rev-parse", "--verify", "-q", branch],
        capture_output=True).returncode else git("switch", "-q", branch)
    git("add", str(dest), str(LOG))
    git("commit", "-qm", f"docs: log transcript {slug}")
    git("switch", "-q", "main")
    git("merge", "-q", "--no-ff", branch, "-m", f"Merge branch '{branch}'")
    print(f"logged {dest.name} -> {LOG.name}")


if __name__ == "__main__":
    main()
