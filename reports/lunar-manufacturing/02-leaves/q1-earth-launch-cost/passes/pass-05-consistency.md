---
pass: 5
kind: consistency
leaf: q1-earth-launch-cost
date: 2026-05-25
agent: claude-opus-4-7
---

# Pass 5 — Cross-leaf consistency check (q1)

## Sibling intersection

| Leaf | Status | Intersection with q1 |
|---|---|---|
| q4-gear-ratio | reviewed | Uses L_p (terrestrial propellant launch cost) as denominator in competitiveness inequality |
| q2-lunar-ascent-cost | open | Provides numerator (lunar surface to LEO cost) for direct comparison |
| q5-capital-buildup | open | Discount rate / WACC inputs interact with q1's amortization timeline |
| q6-orbital-demand | open | Demand for LEO mass interacts with q1's launch-cadence assumptions |
| q8-synthesis-crossover | open | Will consume q1 + q4 to compute crossover dates |

## Numerical consistency check: q1 vs q4's L_p assumptions

Metzger 2023 used L_p = \$30-\$2,000/kg trajectory across 2026-2040 (his Eq. 17-18). My q1 calc partial-scenario gives \$107-466/kg by mature operations — comfortably inside Metzger's modelled L_p range.

**Verdict:** consistent. q4's framework parameters are compatible with q1's bottom-up cost projections.

## Architectural consistency: refurb rate assumption

My q1 calc uses refurb rate {30% early, 15% mid, 8% late}. Metzger 2023 doesn't model refurb explicitly — he uses the abstracted L_p directly. So this is an internal-to-q1 assumption with no cross-leaf check available.

**Flag for q5-capital-buildup:** when q5 runs, its Wright's-Law learning-curve assumption (Metzger used b = 0.75) should be checked against the implicit learning rate in my refurb-rate compression.

## Architectural consistency: reuse-count assumption

My q1 calc uses {100, 30, 10} reuse-count scenarios. The b1076-34-reuses-2026 anchor demonstrates 30 is achievable for Falcon 9 first-stage. Cross-system extrapolation to Starship not directly evidenced.

**No contradiction with sibling leaves** — q1 is the only leaf making vehicle-reuse assumptions in this report so far.

## Claim-level cross-check

Q1's claims (to be written in claims.yaml during the write pass) about Starship $/kg trajectory will be referenced by:
- q4.c4 (threshold formula) — uses L_p implicitly
- q8 synthesis — will use q1's headline trajectory directly

No contradictions identified in this pass. Flag for synthesis pass:
- Whether q1's pessimistic scenario (Starship-doesn't-arrive) is compatible with q6's orbital-demand projections, which usually assume Starship economics.

## Status

✓ No internal contradictions found.
⚠ Two cross-leaf checks deferred to when siblings run: q5 (refurb-vs-Wright's-Law) and q6 (demand-vs-cost-scenario coupling).
