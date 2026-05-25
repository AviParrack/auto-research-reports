#!/usr/bin/env bash
# Commit current changes and push. Cloudflare Pages auto-rebuilds on push.
# Usage: scripts/commit-and-deploy.sh "commit message"

set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "usage: $0 \"commit message\"" >&2
  exit 1
fi

MSG="$1"
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

# Only commit if there's something to commit
if git diff-index --quiet HEAD --; then
  if ! git status --porcelain | grep -q .; then
    echo "no changes to commit" >&2
    exit 0
  fi
fi

git add -A
git -c user.email=avi@forethought.org -c user.name="Avi Parrack" commit -m "$MSG"

# Push, but don't fail catastrophically if remote is unreachable — local commit still useful
if git push 2>&1; then
  echo "✓ pushed; cloudflare will rebuild" >&2
else
  echo "⚠ push failed — local commit is safe, retry later" >&2
  exit 0
fi
