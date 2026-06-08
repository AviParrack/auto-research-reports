# Claude+GPT Tag Team Protocol

Every writing step in this engine is a tag team. The structural commitment is what defeats single-model echo chamber bias and Newman's narrative-over-logic failure mode.

## The four steps

### 1. Claude proposes
Claude writes the artifact (a pass file: research notes, calc derivation, source review, leaf write, synthesis draft, etc.). Save to its canonical location.

### 2. GPT critiques (claim-keyed)
Immediately after Claude saves the artifact, invoke `scripts/ask-gpt.py`:

```bash
python3 scripts/ask-gpt.py \
  --system "You are an adversarial reviewer. Read the attached artifact, then list every factual claim, derivation, or conclusion. For each, give a verdict (supports / weak / unsupported / contradicted by general knowledge) and a one-line reason. Format as YAML matching the audit-file schema below." \
  --input path/to/artifact.md \
  --output path/to/artifact-audit.md
```

The script tries two paths internally:
1. **Codex CLI** (`codex exec`) — preferred. Bills against the user's ChatGPT subscription. Requires `npm install -g @openai/codex` + `codex login`.
2. **OpenAI API direct** (`OPENAI_API_KEY`) — fallback. Bills against API.

If both fail, the script exits 2 — caller marks `audit.gpt.status: unaudited` and continues.

The audit file lives alongside the artifact: `pass-02-calc.md` → `pass-02-audit.md`.

**Audit file format:**

```yaml
---
audited: 2026-05-26T03:14:00Z
auditor: gpt-5-pro
artifact: pass-02-calc.md
---

claims:
  - id: derived-claim-1
    quote: "..."
    verdict: supports | weak | unsupported | contradicted
    reason: "..."
  - id: derived-claim-2
    quote: "..."
    verdict: ...
    reason: ...
overall: pass | needs-revision | reject
notes: ""
```

### 3. Claude responds (point-by-point)
Read the audit file. For each verdict:

- **supports** → no action
- **weak** → update artifact with stronger evidence or downgrade the claim's confidence
- **unsupported** → either find evidence (run more web search), or remove the claim
- **contradicted** → run a mini-research pass; if GPT is right, fix; if Claude is right, leave + record rebuttal

Update `claims.yaml` to reflect any changes. Update each claim's `audit.gpt.status` to `passed` (if no change needed), `flagged` (if disagreement remains), or revise the claim.

Write a brief `pass-NN-response.md` summarizing what changed and what stays disputed.

### 4. Unresolved disagreements → flag for the user
If after Claude's response any item remains contested (Claude and GPT disagree on substance, neither has decisive evidence), add to `meta.yaml.flagged_for_user[]` with the audit file path. The user resolves in the next pass via the `--message` argument or by editing `notes/`.

## When GPT is unreachable

`scripts/ask-gpt.py` tries Codex CLI first, then OpenAI API. If both fail (CLI not installed AND no API key, or both error out):

1. Continue the pass — never block.
2. Set `audit.gpt.status: unaudited` for any claim written this pass.
3. Add a line to `meta.yaml.gpt_outages[]` with timestamp + reason.
4. Surface in the post-pass report to the user.

A later `--pass audit --leaf {slug}` invocation can re-audit unaudited claims once GPT is available.

A subsequent pass can re-run audits on unaudited claims: `auto-research --pass audit --leaf <slug>`.

## When to do the tag team (and when to skip)

**Always tag-team:**
- Calc passes (P2) — math errors are exactly what Newman flagged
- Source review passes — verdicts matter
- Leaf write passes — claims must be substantiated
- Synthesis passes — substantive disagreement triggers debate phase
- Audit passes — these *are* the GPT-side check, so Claude reviews them in reverse

**Skip the tag team:**
- Pure schema/format edits (no claims involved)
- Tree pass when only deleting nodes (user's call, agent just executes)
- Intake pass (only the initial framing — leaves go through full tag-team in subsequent passes)

## The synthesis-pass variant

Synthesis is special: instead of Claude→GPT critique, both write independently first, then a diff agent triages style vs substance. See `pass-synthesis.md` for details. The structure is:

```
Claude writes claude-v1.md  ←  isolated, no GPT context
GPT writes gpt-v1.md         ←  isolated, no Claude context
diff agent reads both → diff.md  (style differences vs substantive disagreements)
  if only style:    → publish both, no debate
  if substance:     → invoke debate flow → debate.md → consensus.md
                  → Claude writes claude-v2.md from consensus
                  → GPT writes gpt-v2.md from consensus
```

Four final reports tab-switchable on the site. The debate transcript is its own tab.
