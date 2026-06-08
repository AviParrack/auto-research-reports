# Pass: Synthesis

The dual-model synthesis pass. Claude and GPT independently write reports from the current state of the question tree + leaves. If they agree on substance, both publish. If they disagree, they debate and produce v2s from consensus.

This pass is what makes the engine a **tag team at the report level**, not just at the claim level.

## Prerequisites
- Every leaf has at least `passes_status.write: done`
- Every leaf in `tree.nodes` with `type: leaf` has `status: answered` (or explicitly deprecated)
- Consistency pass has run; no unresolved contradictions in `consistency-flags.yaml`

If any prereq fails, refuse the pass and tell the user what's missing.

## Outputs
- `03-synthesis/v{N}/claude-v1.md`
- `03-synthesis/v{N}/gpt-v1.md`
- `03-synthesis/v{N}/diff.md`
- Conditional: `debate.md`, `consensus.md`, `claude-v2.md`, `gpt-v2.md`
- Updated `tree.root.answer` (set from consensus or claude-v1 if no debate needed)
- Updated `meta.yaml.termination.root_answered` if appropriate

## Procedure

### 1. Build the synthesis context
Generate a single context file that both writers will read:
- Root question
- Tree structure with each leaf's headline answer + confidence
- For each leaf: the leaf write-up (`passes/pass-06-write.md`)
- Source review verdict counts (not individual reviews, just the meta-summary)
- Any unresolved consistency flags (these are uncertainties the synthesis must acknowledge)

Save to `03-synthesis/v{N}/context.md`. Both writers read ONLY this. Neither sees the other's draft.

### 2. Claude writes v1
- Read `context.md` and any project-specific style guide present at the repo root (e.g. `STYLE.md`)
- Lead with the take (first 200 words = headline answer)
- Subsequent sections derived from the tree
- Bolded topic sentences, visual variety, confidence labels, no mechanical transitions
- Save to `claude-v1.md`

### 3. GPT writes v1 (isolated)
- Invoke `scripts/ask-gpt.py` with system prompt: "You are an independent researcher writing a synthesis report. Read the attached context (question tree + leaf findings). Write a publication-ready synthesis: 800-1500 words, lead with the headline answer, justify with the evidence from leaves, acknowledge uncertainties. Do NOT see anyone else's draft. Format: markdown."
- Pipe `context.md` as input
- Save to `gpt-v1.md`

If GPT unreachable: skip GPT-v1, mark synthesis as `single-model`, continue with Claude-v1 as final. Note in `meta.yaml.synthesis_outage`.

### 4. Diff agent (style vs substance triage)
Read both v1s. Produce `diff.md` with three sections:

**Substantive agreements:** claims/conclusions both versions make the same way.
**Style differences:** same conclusion, different framing or emphasis.
**Substantive disagreements:** different conclusions on numbered claims.

The triage rule: a difference is **substantive** if it changes what the user would do with the answer. Otherwise it's style.

### 5. Branch on triage result

**No substantive disagreements:**
- Publish both v1s. Both go in `03-synthesis/v{N}/`.
- Skip to step 8.

**Substantive disagreements exist:**
- Proceed to debate phase.

### 6. Debate phase
- If a `/debate` skill is available, invoke it with topic "{root_question}, given the evidence in 03-synthesis/v{N}/context.md, where Claude argues {claude position summary} and GPT argues {gpt position summary}"
- Or manual: run 2-3 rounds of cross-rebuttal. Claude rebuts GPT-v1; GPT rebuts Claude-v1; second-round responses via `ask-gpt.py`.
- Save transcript to `debate.md`

### 7. Consensus extraction
- A neutral pass reads the debate transcript and extracts:
  - **Resolved:** positions both agree on after debate
  - **Conceded by Claude:** Claude moved toward GPT
  - **Conceded by GPT:** GPT moved toward Claude
  - **Unresolved:** still disputed (these become uncertainty acknowledgments in v2)
- Save to `consensus.md`

### 8. V2 writes (if debated)
- Claude reads `consensus.md` → writes `claude-v2.md` in Claude's voice but with consensus content
- GPT reads `consensus.md` → writes `gpt-v2.md` in GPT's voice but with consensus content
- The v2s should be SUBSTANTIVELY identical but STYLISTICALLY distinct

### 9. Update tree + meta
- Set `tree.root.answer` to a one-sentence distillation of the synthesis headline
- Set `tree.root.status: answered`
- If consistency flags + termination predicates pass, set `meta.termination.root_answered: true`

### 10. Tab-switching on the site
The synthesis page renders all available versions in tabs. The site code reads files in `03-synthesis/v{N}/` and shows whatever exists:
- v2 versions if debated (default tab)
- v1 versions (older tab)
- diff.md as its own tab
- debate.md as its own tab
- consensus.md as its own tab

### 11. Report to the user
- Headline answer (one sentence)
- Debate triggered? Yes/No. If yes, what was the disagreement?
- Termination: which predicates pass, which still open
- Suggested next: audit pass if everything looks good, more leaf passes if anything's stale
