---
description: Clean /export file(s) and append them to logs/TRANSCRIPT_LOG.md (committed to git)
---
Run `python3 scripts/transcript.py $ARGUMENTS` from the project root and report its output. Run /export first and save to a file in the project root; with no argument the newest export there is used.

Pass only export filenames as arguments (a leading `@` is fine); leave any prose out of the command. Multiple exports may be given.

Several exports of the same session (a later /export that continues an earlier one, so its text begins with the earlier text) are handled by the script: the fuller, newer export replaces the earlier section, so the session is logged once under the newest export. Exports that do not continue a logged one get their own section. If the user says files are versions of one session, pass them together, oldest first or in any order; the script sorts by name. After running, check the output has one `logged ...` line per valid file, and mention any `skipping` warnings.
