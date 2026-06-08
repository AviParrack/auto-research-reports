#!/usr/bin/env python3
"""
Bridge to OpenAI GPT for the Claude+GPT tag team.

Claude (the orchestrator) calls this when it needs a GPT critique. Two paths
tried in order:
  1. Codex CLI  (`codex exec`) — preferred. Bills against Avi's ChatGPT
     subscription. Requires: npm install -g @openai/codex && codex login
  2. OpenAI API direct        — fallback. Requires OPENAI_API_KEY env var.

Usage:
  ask-gpt.py --system "system prompt" --input artifact.md --output audit.md
  ask-gpt.py --system "..." --prompt "user prompt text"
  echo "prompt" | ask-gpt.py --system "..."

Override path:
  --path codex   (force Codex CLI, fail if missing)
  --path api     (force OpenAI API, fail if no key)

Exit codes:
  0  ok
  2  unreachable (no CLI AND no key, or both errored)
  3  bad arguments
"""

import argparse
import json
import os
import shutil
import subprocess
import sys
import urllib.request
import urllib.error

DEFAULT_API_MODEL = "gpt-5-pro"
API_URL = "https://api.openai.com/v1/responses"


def call_codex_cli(system_prompt: str, user_content: str) -> str:
    """Run via OpenAI Codex CLI. Subscription-billed."""
    if shutil.which("codex") is None:
        raise RuntimeError("codex CLI not on PATH")

    # codex exec writes its full agent transcript to stdout. To get only the
    # final reply, use --output-last-message <file>. System prompt goes in the
    # body since codex exec doesn't take a separate system flag.
    combined = f"[SYSTEM]\n{system_prompt}\n\n[USER]\n{user_content}"
    import tempfile
    with tempfile.NamedTemporaryFile("w+", suffix=".txt", delete=False) as tmp:
        out_path = tmp.name
    try:
        codex_model = os.environ.get("CODEX_MODEL", "gpt-5.5")
        result = subprocess.run(
            ["codex", "exec", "--skip-git-repo-check", "-c", f"model={codex_model}", "-o", out_path, "-"],
            input=combined,
            text=True,
            capture_output=True,
            timeout=600,
            check=False,
        )
        if result.returncode != 0:
            raise RuntimeError(f"codex exec exit {result.returncode}: {result.stderr[:400]}")
        with open(out_path, "r") as f:
            out = f.read().strip()
        if not out:
            raise RuntimeError(f"codex returned empty; stderr={result.stderr[:200]}")
        return out
    except subprocess.TimeoutExpired:
        raise RuntimeError("codex exec timed out (10 min)")
    except FileNotFoundError:
        raise RuntimeError("codex CLI not installed")
    finally:
        try:
            os.unlink(out_path)
        except OSError:
            pass


def call_openai_api(system_prompt: str, user_content: str, model: str) -> str:
    """Direct OpenAI Responses API. API-billed."""
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY not set")

    payload = {
        "model": model,
        "input": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content},
        ],
    }

    req = urllib.request.Request(
        API_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=300) as resp:
            body = json.loads(resp.read())
    except urllib.error.HTTPError as e:
        try:
            err_body = e.read().decode("utf-8", errors="replace")
        except Exception:
            err_body = str(e)
        raise RuntimeError(f"HTTP {e.code}: {err_body[:400]}")
    except urllib.error.URLError as e:
        raise RuntimeError(f"network error: {e.reason}")

    if "output_text" in body and body["output_text"]:
        return body["output_text"]
    for item in body.get("output", []):
        if item.get("type") == "message":
            parts = item.get("content", [])
            chunks = [p.get("text", "") for p in parts if p.get("type") in ("output_text", "text")]
            if chunks:
                return "\n".join(chunks)
    raise RuntimeError(f"could not extract text from API response: {json.dumps(body)[:300]}")


def main():
    ap = argparse.ArgumentParser(description="GPT bridge for auto-research tag team")
    ap.add_argument("--system", required=True, help="System prompt")
    src = ap.add_mutually_exclusive_group()
    src.add_argument("--input", help="Path to file whose contents become the user prompt")
    src.add_argument("--prompt", help="User prompt text inline")
    ap.add_argument("--output", help="Path to write response (default: stdout)")
    ap.add_argument("--model", default=DEFAULT_API_MODEL, help="API model (when path=api)")
    ap.add_argument(
        "--path",
        choices=["auto", "codex", "api"],
        default="auto",
        help="Force a specific path. 'auto' tries codex CLI then API.",
    )
    args = ap.parse_args()

    if args.input:
        with open(args.input, "r") as f:
            user_content = f.read()
    elif args.prompt:
        user_content = args.prompt
    else:
        user_content = sys.stdin.read()

    if not user_content.strip():
        sys.stderr.write("empty user content\n")
        sys.exit(3)

    errors = []
    response = None

    if args.path in ("auto", "codex"):
        try:
            response = call_codex_cli(args.system, user_content)
            sys.stderr.write("[codex cli ok]\n")
        except RuntimeError as e:
            errors.append(f"codex cli: {e}")
            if args.path == "codex":
                sys.stderr.write(f"gpt unreachable: {errors[-1]}\n")
                sys.exit(2)

    if response is None and args.path in ("auto", "api"):
        try:
            response = call_openai_api(args.system, user_content, args.model)
            sys.stderr.write("[openai api ok]\n")
        except RuntimeError as e:
            errors.append(f"openai api: {e}")

    if response is None:
        sys.stderr.write("gpt unreachable:\n  " + "\n  ".join(errors) + "\n")
        sys.exit(2)

    if args.output:
        os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)
        with open(args.output, "w") as f:
            f.write(response)
        sys.stderr.write(f"wrote {args.output}\n")
    else:
        sys.stdout.write(response)


if __name__ == "__main__":
    main()
