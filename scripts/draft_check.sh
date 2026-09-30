#!/usr/bin/env bash
# Checks for the report draft, scoped to one "## " section.
#   draft_check.sh words "<heading>"        -> word count of that section
#   draft_check.sh has "<heading>" term...  -> ok/MISSING per term (case-insensitive); exit 1 if any missing
set -euo pipefail
f="${DRAFT:-report/Periapt_Report_Draft_PLAN-NOT-USER-REVIEWED.md}"
sec() { awk -v h="$1" '$0=="## " h {f=1; next} /^## /{f=0} f' "$f"; }
cmd="$1"; h="$2"; shift 2
case "$cmd" in
  words) sec "$h" | wc -w ;;
  has) miss=0
       for t in "$@"; do
         if sec "$h" | grep -qiF -- "$t"; then echo "ok  $t"; else echo "MISSING $t"; miss=1; fi
       done
       exit $miss ;;
  *) echo "usage: $0 words|has <heading> [terms...]" >&2; exit 2 ;;
esac
