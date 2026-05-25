---
pass: 2
kind: response-to-audit
leaf: q4-gear-ratio
date: 2026-05-25
agent: claude-opus-4-7
audited_artifact: pass-02-calc.md
audit_file: pass-02-audit.md
---

# Response to Codex audit of pass-02-calc

Codex flagged 15 claims across the calc + interpretation. Net: `overall: needs-revision`. Walking through each verdict and accepting / disputing / deferring.

## Accepted (downgrade or remove)

- **c13 (CONTRADICTED): "PPP financing collapses LEO threshold by orders of magnitude"** — Codex is right. My own sweep at ξ=1 still gives LEO=∞. The claim is wrong as stated. Real conclusion: PPP financing helps closer destinations dramatically but LEO needs additional architectural change (aerobraking, mass driver, lower Γ_LEO architecture).
- **c14 (UNSUPPORTED): "GTO threshold ~50-200"** — also not supported by my own sweep at ξ≥1. The 50-200 range only emerges under (ω+ξ) ≈ 0.2, which I didn't include in the parameter sweep. Remove from interpretation; defer the GTO-specific threshold to reconcile.
- **c15 (PARTIAL): "I flag fragility"** — I do flag it, but Codex's point is right that I then keep making confident claims that the fragility undermines. Tightening.

## Disputed / clarified

- **Reusable Tsiolkovsky model**: Codex suggests "explicit mass accounting." My `G_round_trip = G_one_way × exp(Δv_return/(g·I_sp))` is a known simplification — it assumes empty-mass return without crossfeed propellant tracking. Metzger uses a more detailed model (his Eq. 2-3 with effective IMF including return Δv). My G_K = 14.97 is a *high-end* estimate; Metzger's baseline G = 6 with RLL-as-tug-from-LEO is a different (more efficient) architecture choice. Both are valid; my number bounds the conservative case.
- **ξ derivation**: Codex's recommended fix — derive ξ from WACC × buildup time × output amortization — is the right next step. Doing that in reconcile.

## Confirmed (no change)

- Tsiolkovsky math (c1-c5): supports
- Γ_X formula (c6): supports
- Necessary condition (ω+ξ)·Γ<1 derivation (c7): supports
- LEO is the hardest destination (c9, c10): supports
- The physics-only proof that Γ_LEO ≫ 1 with chemical reusable RT (c11): supports

## What this means for the leaf

The calc *does* produce defensible physics-only conclusions:
1. Γ_X structure: physics-driven, holds across architectures.
2. Destination ordering: LLO < EML1 ≈ GEO < GTO < LEO in difficulty for lunar product.
3. Necessary condition: structural — finance + ops costs alone must be small enough for any φ to work.

The calc *cannot* produce defensible threshold-φ point estimates without a proper cost model. That work moves to reconcile, where we compare my structural conclusions to Metzger 2023's full TEA and learn which of his cost parameters give realistic thresholds.

## Updated stance

Rewriting the calc interpretation section to:
- Keep the physics conclusions
- Remove the threshold point estimates
- Acknowledge that the cost-model assumptions made my sweep degenerate
- Flag the open question: under what realistic (x, ω, ξ) values does φ_threshold land in the 10-100 range that ISRU literature claims is achievable?

## What to carry to claims.yaml

From this pass, the proven claims are:
- q4.c1: Γ_LEO ≈ 14 under chemical reusable RT; this drives LEO being the hardest destination.
- q4.c2: For closer destinations (LLO, EML1, GEO), Γ_X is O(1); they should be easier markets.
- q4.c3: Lunar competitiveness at any destination requires (ω+ξ)·Γ_X < 1 — a finance/ops constraint that's binding for LEO.
- q4.c4: The threshold φ scales as ~(x+G)·Γ_X / [1−(ω+ξ)·Γ_X] in the launch-normalized framework.

What is NOT yet a defensible claim:
- Specific numerical threshold (need reconcile)
- Whether industrial-explosion-grade financing makes LEO competitive (need reconcile + the cost-model derivation Codex recommends)
