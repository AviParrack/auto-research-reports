---
pass: 6
kind: response-to-audit
audited_artifact: pass-write.md
audit_file: pass-write-audit.md
date: 2026-05-25
---

# Response to Codex audit of pass-write

Codex caught **orphan numerical claims** — prose statements that don't trace to a claim in claims.yaml. This is the exact bug the claim-graph substrate is designed to prevent. The audit list is substantive (12 items). Acknowledging and acting.

## Net assessment

**Codex overall: `needs-revision`.** Lead structure and anti-patterns clean. Issue is claim hygiene.

## Approach

The orphan claims fall into two categories:

**A. Numbers needing claim entries** (will add):
- Capital-transport gear ratio range 6-15
- SEP collapses Γ_LEO from 14 to ~1
- LEO crossover after roughly two decades under Metzger model
- Metzger reviews 7 TEAs; G and φ are the two dominant variables
- CD G=64.9 and Jones G=41.8 (specific values for the SLS-architecture critique)

**B. Numbers to remove/soften** (will edit prose):
- Table of "Γ_X with SEP / OTV / crossfeed" — soften to "non-chemical architectures dramatically reduce these"
- "5-year buildup, 22% WACC" specifics — generalize to "realistic first-of-kind financing"
- "Wright's Law b = 0.75; economies-of-scale exponent a = 0.66" — generalize to "Metzger's industrial-scaling assumptions"
- "two parameters" framing in TEA review section — soften to "primarily two parameters with secondary effects from EOS, finance treatment, etc." (matches q4.c8 more honestly)

## Done in this pass

Adding 4 new claims (c11-c14) for the load-bearing orphans. Pass-write.md will be updated in a fix-up commit. Leaf marked `reviewed` (not `done`) so it's clear there's a small cleanup pass pending.

## Reflection on the engine

This is exactly the kind of catch the Claude+Codex tag team should produce. Newman's failure mode is "compelling paragraph-by-paragraph narrative without enforced cross-reference to claims." Our claim-graph substrate + Codex audit just caught me doing exactly that — wrote a flowing piece, slipped in numbers that felt right but weren't claim-cited. The engine works.
