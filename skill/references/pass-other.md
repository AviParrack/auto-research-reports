# Other Passes — source-review / consistency / audit

Tighter procedures for the supporting passes. Standalone invocations: `--pass source-review`, `--pass consistency`, `--pass audit`.

## Pass: source-review (standalone)

The leaf-pass sub-pass #4 reviews the sources cited *for that leaf*. The standalone `--pass source-review` is for **figures not yet cited but who should be** — the steelman trawl.

### Procedure
1. Identify the major public figures / sources who've publicly weighed in on the root question. Web search aggressively. Look for: substack posts, podcasts, papers, talks, tweets-with-substance, interviews.
2. For each figure not already represented under any leaf's `sources/`:
   - WebFetch their relevant work → `02-leaves/{nearest-leaf}/sources/{figure-slug}/extract.md`
   - Generate review.md with verdict taxonomy (see `schemas.md`)
3. Add each new source as evidence to any claim it bears on (update `claims.yaml`)
4. Run Claude+GPT tag team per source review

### Termination signal
Once every major figure has a review on file → set `meta.termination.all_figures_reviewed: true`.

How to know who's "major"? Practical heuristic: anyone whose name comes up in 2+ other reviewed sources, anyone who has 10k+ followers on the topic, anyone the user mentions in feedback. Don't be exhaustive — be representative.

---

## Pass: consistency

Cross-leaf adversarial check. Extracts every claim, groups by topic, flags contradictions.

### Procedure
1. Load every leaf's `claims.yaml`
2. Build a flat list: `[(leaf_id, claim_id, text, evidence_summary), ...]`
3. Group claims by topic — use semantic clustering (claims about "launch cost", "satellite lifetime", etc.)
4. For each cluster: do any two claims contradict?
5. Output `consistency-flags.yaml`:
   ```yaml
   flags:
     - id: cf-001
       claims: [q1.c3, q4.c2]
       contradiction: "q1 says ISRU is feasible by 2030; q4 says capital buildup takes 12+ years"
       severity: high | medium | low
       resolution_required_before_synthesis: true
       resolved_by: null    # filled when resolved
       resolution_note: null
   ```
6. Each high-severity flag is a required-resolution item before synthesis
7. Optionally: propose new tree nodes that would resolve specific contradictions (e.g., "does ISRU feasibility timeline match the capital buildup curve?")

### Claude+GPT tag team
GPT critique: "For each flag, judge whether this is a genuine contradiction or just framing difference. Rate severity."

---

## Pass: audit

Walks the whole report, verifies. Mandatory before declaring `status: done`.

### Procedure
1. **Claim integrity:** every claim in every claims.yaml has evidence array; every evidence.source maps to a folder with non-empty extract.md
2. **Link liveness:** every URL in every extract.md frontmatter still resolves (WebFetch with timeout)
3. **Calc re-derivation:** for every derived claim, re-execute the derivation code in `passes/pass-02-calc.md` (or equivalent) and verify the number still matches
4. **GPT adversarial pass:** invoke `ask-gpt.py` with the entire synthesis context and a prompt: "You are an adversarial reviewer of a research synthesis. List the three most likely errors, the three most underexplored assumptions, and three pieces of evidence that would shift the conclusion."
5. **Anti-pattern grep:** scan all prose for the forbidden transition words (However, Furthermore, ...) and weasel hedging
6. **Termination check:** recompute `meta.termination` predicates; update meta.yaml

### Output
`reports/{slug}/audits/audit-{N}.md` with:
- Pass/flag table per category
- Failed integrity items (broken links, missing extracts, calc drift)
- GPT adversarial findings
- Anti-pattern hits
- Updated termination state

### When to run
- Before declaring `status: done`
- After every 3-5 substantive passes (sanity check)
- On the user's explicit request
