#!/usr/bin/env python3
"""
Bridge to OpenAI GPT for the Claude+GPT tag team.

Usage:
  ask-gpt.py --system "system prompt" --input path/to/artifact.md --output path/to/audit.md
  ask-gpt.py --system "..." --prompt "user prompt text" --output out.md
  echo "prompt" | ask-gpt.py --system "..."          # stdin → stdout

Requires OPENAI_API_KEY in env. Defaults to gpt-5-pro; override with --model.

Exit codes:
  0  ok
  2  unreachable (no key, network, rate limit, etc.) — caller should mark unaudited and continue
  3  bad arguments
"""

import argparse
import json
import os
import sys
import urllib.request
import urllib.error

DEFAULT_MODEL = "gpt-5-pro"
API_URL = "https://api.openai.com/v1/responses"

def call_openai(system_prompt: str, user_content: str, model: str) -> str:
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
        raise RuntimeError(f"HTTP {e.code}: {err_body}")
    except urllib.error.URLError as e:
        raise RuntimeError(f"network error: {e.reason}")

    # GPT-5 Responses API returns output as a list of items; extract text from message items
    if "output_text" in body and body["output_text"]:
        return body["output_text"]
    for item in body.get("output", []):
        if item.get("type") == "message":
            parts = item.get("content", [])
            chunks = [p.get("text", "") for p in parts if p.get("type") in ("output_text", "text")]
            if chunks:
                return "\n".join(chunks)
    raise RuntimeError(f"could not extract text from response: {json.dumps(body)[:300]}")


def main():
    ap = argparse.ArgumentParser(description="GPT bridge for auto-research tag team")
    ap.add_argument("--system", required=True, help="System prompt")
    src = ap.add_mutually_exclusive_group()
    src.add_argument("--input", help="Path to file whose contents become the user prompt")
    src.add_argument("--prompt", help="User prompt text inline")
    ap.add_argument("--output", help="Path to write response (default: stdout)")
    ap.add_argument("--model", default=DEFAULT_MODEL)
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

    try:
        response = call_openai(args.system, user_content, args.model)
    except RuntimeError as e:
        sys.stderr.write(f"gpt unreachable: {e}\n")
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
