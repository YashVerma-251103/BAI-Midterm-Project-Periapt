#!/usr/bin/env python3
"""Clean a Claude Code /export file and append it to logs/TRANSCRIPT_LOG.md, then commit.

Usage: transcript.py [export.txt ...]   (default: newest export in project root)
Re-running for the same slug replaces its section. An export that continues an
already-logged one (its cleaned text starts with the logged text) supersedes it:
the old section is replaced by the fuller one, so each session appears once.
Several files are processed oldest-first; a leading "@" is stripped; args that
are not /export filenames are skipped with a warning.
"""
import re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOG = ROOT / "logs" / "TRANSCRIPT_LOG.md"
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


def body_of(sec):
    return re.search(r"```text\n(.*)\n```\n<!-- /session", sec, re.S).group(1)


def supersedes(log, sec):
    """Slug of a logged section whose text is a proper prefix of sec's, else None."""
    new = body_of(sec)
    for m in re.finditer(r"<!-- session: (.+?) -->.*?<!-- /session: \1 -->\n", log, re.S):
        old = body_of(m.group(0))
        if old != new and new.startswith(old):
            return m.group(1)


def upsert(log, slug, sec):
    old = supersedes(log, sec)
    if old and old != slug:  # continuation under a new filename: drop the old section
        log = re.sub(rf"<!-- session: {re.escape(old)} -->.*?<!-- /session: {re.escape(old)} -->\n\n?",
                     "", log, flags=re.S)
    pat = re.compile(rf"<!-- session: {re.escape(slug)} -->.*?<!-- /session: {re.escape(slug)} -->\n", re.S)
    if pat.search(log):
        return pat.sub(lambda _: sec, log)
    return log.rstrip("\n") + "\n\n" + sec


def git(*a):
    subprocess.run(["git", "-C", str(ROOT), *a], check=True)


def log_one(src):
    slug = NAME.match(src.name).group(4)
    dest = ROOT / "logs" / "exports" / src.name
    dest.parent.mkdir(parents=True, exist_ok=True)
    if src != dest:
        src.rename(dest)
    log = LOG.read_text() if LOG.exists() else HEAD
    LOG.write_text(upsert(log, slug, section(dest.name, dest.read_text())))

    branch = "docs/transcript-" + NAME.match(dest.name).group(1)
    git("switch", "-q", "-c", branch) if subprocess.run(
        ["git", "-C", str(ROOT), "rev-parse", "--verify", "-q", branch],
        capture_output=True).returncode else git("switch", "-q", branch)
    git("add", str(dest), str(LOG))
    if subprocess.run(["git", "-C", str(ROOT), "diff", "--cached", "--quiet"]).returncode:
        git("commit", "-qm", f"docs: log transcript {slug}")
    git("switch", "-q", "main")
    git("merge", "-q", "--no-ff", branch, "-m", f"Merge branch '{branch}'")
    print(f"logged {dest.name} -> {LOG.name}")


def main():
    args = [a.lstrip("@") for a in sys.argv[1:]]
    if args:
        srcs = []
        for a in args:
            if NAME.match(Path(a).name) and Path(a).exists():
                srcs.append(Path(a).resolve())
            else:
                print(f"skipping {a!r}: not an existing /export file", file=sys.stderr)
        if not srcs:
            sys.exit("no valid export given")
    else:
        found = sorted(p for p in ROOT.glob("*.txt") if NAME.match(p.name))
        if not found:
            sys.exit("no export found; run /export first")
        srcs = [found[-1]]
    for src in sorted(srcs, key=lambda p: p.name):
        log_one(src)


if __name__ == "__main__":
    main()
