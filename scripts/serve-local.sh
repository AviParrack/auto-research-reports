#!/usr/bin/env bash
# Local-mode deploy: build the Astro site and serve it on http://localhost:4321/.
#
# Idempotent — safe to call after every pass. Reuses an existing server if one
# is already running on the configured port (the rebuilt dist/ is picked up on
# the next browser load).
#
# Env:
#   AUTO_RESEARCH_PORT  — override port (default 4321)
#   AUTO_RESEARCH_OPEN  — set to "1" to open browser after first start; the
#                         skill should set this only during intake.
#   AUTO_RESEARCH_URL_PATH — path to open relative to root (e.g. "/my-report/")

set -euo pipefail

PORT="${AUTO_RESEARCH_PORT:-4321}"
URL_PATH="${AUTO_RESEARCH_URL_PATH:-/}"
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SITE_DIR="$REPO_ROOT/site"
DIST_DIR="$SITE_DIR/dist"
PID_FILE="$REPO_ROOT/.auto-research-server.pid"

if [[ ! -d "$SITE_DIR" ]]; then
  echo "site/ not found at $SITE_DIR" >&2
  exit 1
fi

# 1. Install deps if needed (first run only).
if [[ ! -d "$SITE_DIR/node_modules" ]]; then
  echo "installing site dependencies (first run)..." >&2
  (cd "$SITE_DIR" && npm install) >&2
fi

# 2. Build.
echo "building site..." >&2
(cd "$SITE_DIR" && npm run build) >&2

# 3. Check if server is already running on PORT (via PID file).
SERVER_RUNNING=0
if [[ -f "$PID_FILE" ]]; then
  EXISTING_PID="$(cat "$PID_FILE" 2>/dev/null || echo "")"
  if [[ -n "$EXISTING_PID" ]] && kill -0 "$EXISTING_PID" 2>/dev/null; then
    SERVER_RUNNING=1
    echo "✓ server already running (pid $EXISTING_PID); rebuilt dist/ visible on next page load" >&2
  else
    rm -f "$PID_FILE"
  fi
fi

# 4. Start server if not running.
if [[ "$SERVER_RUNNING" -eq 0 ]]; then
  if ! command -v python3 >/dev/null 2>&1; then
    echo "python3 not found — required for local serving" >&2
    exit 1
  fi
  # Background python http.server. Logs to /tmp so the foreground stays clean.
  LOG_FILE="$REPO_ROOT/.auto-research-server.log"
  (
    cd "$DIST_DIR"
    nohup python3 -m http.server "$PORT" --bind 127.0.0.1 >"$LOG_FILE" 2>&1 &
    echo $! >"$PID_FILE"
  )
  sleep 0.5
  if [[ -f "$PID_FILE" ]] && kill -0 "$(cat "$PID_FILE")" 2>/dev/null; then
    echo "✓ server started on http://localhost:$PORT/ (pid $(cat "$PID_FILE"))" >&2
    echo "  logs: $LOG_FILE" >&2
    echo "  stop: kill \$(cat $PID_FILE)" >&2
  else
    echo "⚠ failed to start server; see $LOG_FILE" >&2
    exit 1
  fi
fi

# 5. Open browser on first start or when explicitly requested.
if [[ "${AUTO_RESEARCH_OPEN:-0}" == "1" ]]; then
  URL="http://localhost:$PORT$URL_PATH"
  echo "opening $URL ..." >&2
  python3 -c "import webbrowser; webbrowser.open('$URL')" 2>/dev/null || true
fi
