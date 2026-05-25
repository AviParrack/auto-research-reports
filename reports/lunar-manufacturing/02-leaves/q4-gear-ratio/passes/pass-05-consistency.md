---
pass: 5
kind: consistency
leaf: q4-gear-ratio
date: 2026-05-25
agent: claude-opus-4-7
---

# Pass 5 — Cross-leaf consistency check

Checking q4-gear-ratio claims against sibling leaves. Most siblings haven't run yet (only research stub), so this is a forward-looking compatibility check rather than a contradiction audit.

## Sibling leaves status

| Leaf | Status | Relevant intersection with q4 |
|---|---|---|
| q1-earth-launch-cost | research:pending | Provides L_p input (Starship cost curve) |
| q2-lunar-ascent-cost | research:pending | Provides G_LS-X gear ratios + Γ_X via SEP option |
| q3-isru-feasibility | research:pending | Provides φ achievability per technology (tent vs strip vs beneficiation) |
| q5-capital-buildup | research:pending | Provides M_K + buildup time + WACC inputs for ξ |
| q6-orbital-demand | research:pending | Provides D_30 market size sensitivity |
| q7-mass-driver-feasibility | research:pending | Alternative architecture that bypasses Tsiolkovsky-derived Γ_LEO |
| q8-synthesis-crossover | research:pending | Will integrate q4 threshold + q3 attainability + q1 launch curve |

## Claims requiring sibling consistency

### q4.c1 (Γ_LEO ≈ 14 chemical) — q4.c2 (closer destinations Γ ~1)
**Sibling:** q2-lunar-ascent-cost will derive the same Γ_X structure independently. They must agree.
**Status:** pending — will check when q2 runs

### q4.c5 (static-vs-amortized ξ) — q4.c10 (TAI-sensitivity)
**Sibling:** q5-capital-buildup will need to specify ξ time-evolution model.
**Status:** pending — q5 should not contradict the amortization story here

### q4.c6 (≥35 threshold contingent) — q4.c7 (tent φ=442-534)
**Sibling:** q3-isru-feasibility will assess what production mass ratios are actually achievable per technology by TRL stage.
**Status:** pending — must verify Kornuta/Sowers tent sublimation claims are at appropriate TRL for the timeline

### q4.c9 (LEO needs SEP) — q4.c10 (TAI compresses M_K not Γ)
**Sibling:** q7-mass-driver-feasibility offers an alternative path. Mass driver doesn't have Tsiolkovsky penalty — it's purely an energy cost. Could collapse Γ_LEO entirely.
**Status:** pending — q7 should explore mass driver as the LEO-viability alternative to SEP

### q4.c10 (TAI compresses φ via M_K) — sibling q5
**Sibling:** q5-capital-buildup will define how M_K decomposes. The compression hypothesis depends on whether M_K is dominated by structural mass (compressible via better materials) vs functional mass (compressible via automation).
**Status:** pending — TAI sensitivity claim should be revisited after q5 decomposes M_K

## Internal claim consistency

Checking q4 claims against each other:

- q4.c1 + q4.c3: Γ_LEO ≈ 14 → necessary condition (ω+ξ) < 0.07 at LEO. **Internally consistent.**
- q4.c4 (threshold formula) + q4.c6 (Metzger's MVP threshold 36.5): plug in (Γ_GTO ≈ 1.5 with SEP, x ≈ 10, G ≈ 6, ω+ξ ≈ 0.2) → φ ≈ 34. **Internally consistent within ~5%.**
- q4.c9 (LEO needs SEP) + q4.c1 (chemical Γ_LEO = 14): SEP I_sp = 2000 s drops effective Δv/(g·I_sp) by 4.4× → Γ collapses ~exponentially. **Internally consistent.**
- q4.c10 (TAI compresses φ) + q4.c6 (35 threshold contingent): if φ rises 10× via M_K compression, every existing TEA technology comfortably clears the threshold. **Internally consistent and reinforces the leaf's conclusion.**

No internal contradictions found.

## Flag for synthesis

When q8-synthesis-crossover runs, it must:
1. Pull Γ_X structure from q4 (and q2 once it runs)
2. Pull φ-by-technology from q3
3. Pull cost-curve dynamics from q1 + q5
4. Choose: which architecture (chemical only / chemical+SEP / mass driver from q7) shapes the LEO answer
5. Apply Metzger's time-evolving cost model to get crossover dates per destination
6. Crucially: carry q4.c10 — the industrial-explosion / TAI compression sensitivity — as a separate scenario, not buried as an asterisk

## Status

✓ No internal contradictions in q4.
⚠ 6 sibling intersections pending — synthesis pass must re-check when siblings have run.
