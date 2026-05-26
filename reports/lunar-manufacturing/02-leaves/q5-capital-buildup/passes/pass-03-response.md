---
pass: 3
kind: reconcile-response
leaf: q5-capital-buildup
date: 2026-05-26
agent: claude-opus-4-7
responds_to: passes/pass-03-audit.md
---

# Response to Codex Audit on Pass-03 Reconcile

Codex returned `weak` with high-severity criticisms of the PwC convergence claim and several "Consistent" verdicts. The most important critique: I selected my no-dev launch+hardware subtotal ($73B) to compare to PwC's $72-88B, then declared "within 20% convergence." That is artifact, not convergence. Codex is right.

## Accepted

- **PwC convergence claim (fail / unsupported, high severity)**: Codex is correct. PwC's $72-88B is "all-party cumulative infrastructure 2026-2050 across NASA + ESA + JAXA + China + commercial," dominated by transportation. My $73B is a one-program 20-year first-principles hardware+launch subtotal for a manufacturing/export base, *stripping out* the $93B dev component I had previously argued should be added. By selecting which subtotal to compare, I created agreement. The honest restatement: my BAU total program capex range ($150-400B) is in the same order of magnitude as PwC's all-party-cumulative $72-88B (i.e. within ~3-5×), which is consistent with the two estimates not contradicting each other — but is NOT the strong cross-methodology convergence I claimed.

- **Sowers φ-architecture bridge (weak, high severity)**: Codex correctly says the φ rescaling does not directly give the ISRU plant mass drop. φ is product mass per capital mass over a lifetime; rescaling from φ=20 to φ=534 changes lifetime-product-per-mass, not mass-per-output-rate. The "75 t → 3 t" arithmetic is wrong-footing. The correct statement is: tent-sublimation architectures achieve high φ via simpler hardware (passive sublimation, minimal active components), so the per-tonne plant mass is genuinely lower — but the rescaling factor is not strictly proportional to φ. Sowers' $4B reflects a fundamentally different architecture, and my bottom-up calc cannot directly rescale to it. The $5-15B figure I quoted is largely assumed; downgrade Sowers comparison to "different architecture, not directly reconcilable."

- **PwC within-20% claim (unsupported, high severity)**: Same as above — the 20% match was an artifact of subtotal selection. Removing this claim.

- **MacDonald SEI ceiling (weak, medium severity)**: Codex correctly notes that launch-cost delta cannot explain the gap inside my own model since launch is only $1.7B in BAU; the dominant cost is hardware+dev at $93B+$72B. So the SLS-vs-commercial-launch reframe is doing less work than I claimed. The honest statement is: MacDonald's $1T is a "historical-architecture upper bound" that includes Apollo-style contracting overhead, schedule slippage, single-vendor mark-ups — none of which my BAU model captures. The gap between $1T and our $150-400B is therefore explained by *those* (institutional-cost-overhead) factors, not by launch-cost delta. Downgrading MacDonald to "consistent upper bound" with clarified reasoning.

- **Isaacman Sweden annual-rate match (partial, medium severity)**: Codex correctly says annual-rate matching is weak normalization. Isaacman's $2.9B/yr is incremental surface-base spend on top of Artemis transport (which is separately ~$93B over 13 yr ≈ $7B/yr). My BAU $3.6B/yr is a *self-contained* first-principles estimate for a complete manufacturing base. The two rates being close is a coincidence of scope; we cannot conclude "consistent" beyond "non-contradictory at the M6 milestone scope."

- **Zubrin lower-bound sanity (partial, medium severity)**: Codex correctly: comparing my full-M8 IE result to Zubrin's minimal-presence architecture is a lower-bound sanity check, not convergence. Adjusting language.

- **Handmer different milestone (partial, low severity)**: Codex's verdict is mild — "non-contradictory at a later milestone." Accepting.

## Disputed / clarified

- **Metzger 2013 bootstrap (partial, medium severity)**: Codex agrees Metzger does model 41 MT total Earth-launched mass to reach the 40,000 MT industrial endpoint, but flags that Metzger explicitly excludes development cost, failure realism, and detailed Earth-supply-chain closure. Accept this caveat: my "consistent with IE regime" verdict stays but with the explicit caveat that Metzger does not validate cost compression to the same degree the IE regime claims. Updating accordingly.

## Net effect on claims.yaml

q5.c11 (new claim about PwC convergence) — **demoting from "consistent within 20%" to "in the same order of magnitude as our BAU upper bound" without further cross-methodology claim**. The numerical $72-88B figure stands as a factual published anchor; the convergence interpretation does not.

q5.c4 (BAU $150-400B) — **confidence stays low; the PwC alignment does NOT raise it to medium as I claimed in the reconcile pass.** I had pre-committed to upgrading confidence based on PwC convergence; Codex correctly stopped that. Confidence stays low.

q5.c13 (Sowers $4B reconciliation) — **amend to "consistent in direction (different architecture lowers mass and cost) but the numeric bridge from φ=20 to φ=534 does not give a defensible specific dollar mapping."** The Sowers number remains the canonical commercial-architecture anchor but is not directly comparable to ours.

## Updated cross-anchor summary

| Anchor | Codex-corrected verdict | What this anchor tells us |
|---|---|---|
| Zubrin $1.5B + $9.9B/20y | Lower-bound sanity check (not convergence) | Minimal-presence floor at M5 |
| Metzger 2013 41 t | Compression direction supported, cost validation NOT | The IE regime's 10x mass compression is achievable via lunar-substitution |
| Sowers $4B | Different architecture; no direct numeric bridge | Tent-sublimation commercial architecture sits at ~$4B for the propellant-only M5 milestone |
| Isaacman $20B/7yr | Non-contradictory at M6 scope | Government program-of-record matches our BAU at the M6 stage with separate transport overhead |
| PwC $72-88B | Same order of magnitude as BAU upper bound (NOT within-20% convergence) | All-party cumulative spend across all infrastructure across 24 yr |
| MacDonald $1T | Consistent upper bound after institutional-overhead-correction | Apollo/SEI-era architecture ceiling |
| Handmer trillion+ | Non-contradictory at later milestone | Mature multi-base industry beyond our M8 |

**Revised honest characterization**: The seven published anchors do NOT cross-validate our BAU $150-400B figure. They each sit at different scope/architecture combinations and are consistent with our calc only in the sense of not directly contradicting it. The 3-order-of-magnitude raw spread is explained by scope/architecture differences, not by analytical disagreement, but **none of the anchors independently lands inside our BAU bracket using the same scope assumptions.** The honest read: our calc is the only first-principles full-net-positive-export-base capex estimate in this corpus.

## What this implies for the write pass

- Lead with the regime-conditional bracket: BAU $150-400B / IE $1-5B / TAI cost-degenerate / 12-month-floor time-bound.
- State that no published anchor cross-validates the BAU figure at the same scope; the calc is the only full-scope bottom-up estimate.
- Frame the milestone decomposition (M1-M8) as the load-bearing contribution: even if dollar numbers shift, the milestone structure and compressibility logic is robust.
- Explicitly mark anti-pattern #11 compliance: don't give a 2030/2040 date, give regime-conditional year-counts.
