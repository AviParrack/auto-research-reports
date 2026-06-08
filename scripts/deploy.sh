#!/usr/bin/env bash
# Mode-aware commit + deploy step. Reads the mode from the argument; the caller
# (the skill or new-report) is responsible for sourcing it from meta.yaml.
#
# Usage:
#   scripts/deploy.sh --mode cloudflare "commit message"
#   scripts/deploy.sh --mode local "commit message"
#
# Both modes always commit. Only cloudflare pushes. Only local rebuilds + serves.

set -euo pipefail

MODE=""
MSG=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --mode)
      MODE="$2"
      shift 2
      ;;
    -h|--help)
      cat <<EOF
Usage: $0 --mode {cloudflare|local} "commit message"

Both modes always commit. Cloudflare pushes; local rebuilds + serves at
http://localhost:4321/ via scripts/serve-local.sh.
EOF
      exit 0
      ;;
    *)
      if [[ -z "$MSG" ]]; then
        MSG="$1"
      else
        echo "unexpected argument: $1" >&2
        exit 3
      fi
      shift
      ;;
  esac
done

if [[ -z "$MODE" || -z "$MSG" ]]; then
  echo "usage: $0 --mode {cloudflare|local} \"commit message\"" >&2
  exit 3
fi

if [[ "$MODE" != "cloudflare" && "$MODE" != "local" ]]; then
  echo "mode must be 'cloudflare' or 'local', got: $MODE" >&2
  exit 3
fi

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

# Commit only if there's something to commit (same logic as legacy script).
if git diff-index --quiet HEAD --; then
  if ! git status --porcelain | grep -q .; then
    echo "no changes to commit" >&2
    if [[ "$MODE" == "local" ]]; then
      # Still rebuild + serve so the browser stays current even on no-op passes.
      exec "$REPO_ROOT/scripts/serve-local.sh"
    fi
    exit 0
  fi
fi

git add -A
git commit -m "$MSG"

case "$MODE" in
  cloudflare)
    if git push 2>&1; then
      echo "✓ pushed; cloudflare will rebuild" >&2
    else
      echo "⚠ push failed — local commit is safe, retry later" >&2
      exit 0
    fi
    ;;
  local)
    "$REPO_ROOT/scripts/serve-local.sh"
    ;;
esac
