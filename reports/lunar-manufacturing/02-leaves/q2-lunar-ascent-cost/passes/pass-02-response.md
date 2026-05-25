---
pass: 2
kind: response
leaf: q2-lunar-ascent-cost
date: 2026-05-25
agent: claude-opus-4-7
---

# Pass 2 — Response to Codex audit

Codex's audit ([pass-02-audit.md](pass-02-audit.md)) returned verdict **weak** with the headline: "The chemical Tsiolkovsky arithmetic and printed cost tables mostly check out from the stated inputs. But this is not a first-principles derivation: most load-bearing numbers are asserted, and several interpretation/calibration claims contradict the tables."

## What I fixed inline

1. **Arithmetic error in the calibration to q1** (Codex severity high). Original prose said aggressive-ISRU-late $994/kg is "~9× more expensive than q1's late-era $59/kg" — Codex caught this: $994/$59 = 16.8×, not 9×. The 9× figure does hold against q1's partial-late $107/kg. **Fixed in calc.md and claim q2.c8**: both ratios now stated explicitly ($994/$107 ≈ 9.3×, $994/$59 ≈ 16.8×).

2. **Bullet 1 contradiction** (Codex severity medium). Original prose said "all chemical scenarios except late-era aggressive-ISRU sit above $5,000/kg" in the no-aerobraking case — Codex correctly noted Earth-imports-only late ($3,339) is also below $5,000. **Fixed** in pass-02-calc.md interpretation block.

3. **Industrial-explosion arithmetic** (Codex severity medium). The bullet "$/kg by $4,500 in early-era to $4,500/100 ≈ $450" was arithmetically incoherent. **Fixed** to "early-era $5,000/kg → $500/kg, saving $4,500/kg in early-era chemical scenarios."

4. **Mass-driver early-era interpretation** (Codex severity medium). I had said "capital amortization is ~$500/kg, dominating energy" — Codex caught that the $500 figure is the SEP transfer cost, not the capital amortization (which is $25/kg). **Fixed** in pass-02-calc.md to attribute the cost components correctly.

## What I acknowledged but did not rebuild

Codex's structural critique (severity high): many load-bearing inputs are scenario priors, not first-principles derivations. Examples:

- ΔV component values (1.87, 0.7, 0.3, 3.0 km/s) are canonical/architectural, not derived
- Isp values (450, 360, 2000 s) are textbook vacuum engine performance
- Dry-mass-to-propellant ratio 0.12 is asserted
- Lunar surface propellant prices in the three scenarios are scenario priors
- Hardware $/kg/reuse, lunar ops cost, mass driver capital are asserted
- SEP transfer cost per kg is asserted, not derived from SEP Isp + ΔV + power

**Acknowledged** in calc.md anti-pattern block. Honest reframing: this is a scenario model with first-principles-justified priors (Tsiolkovsky algebra is correct from the inputs), not a from-axioms derivation. The decision: do not rebuild as a fully bottom-up derivation in this pass — many of those inputs (Isp, ΔV) would require an unmaintainably large appendix to "derive" further; others (lunar prop cost) ARE the scenario knobs the question is about. The reconcile pass will cross-check the priors against sources.

## What I flagged for reconcile pass

1. **Vehicle reusability assumption** (Codex severity high). The chemical ascent vehicle is amortized as if reusable, but its return-to-Moon leg is not separately modeled. The reconcile pass should check whether the source literature (Coutts-Sowers, Metzger) treats lunar ascent vehicles as reusable, and whether the return-leg propellant cost should be added to the calc. Carried forward as an explicit flag.

2. **SEP transfer cost** (Codex severity high). The $500/$150/$50 per kg figures for the post-mass-driver SEP transfer stage are asserted. Metzger 2023's SEP architecture (water at Isp 2000 s, lunar-product return leg with Γ_LEO ≈ 1) provides a partial anchor for reconcile. A v2 calc could derive SEP cost from first principles (power, propellant, vehicle dry mass, reuse count), but that's a significant additional model.

3. **Earth-imports gear-ratio amplification factor** (Codex severity medium). The 6× / 13× amplification factors used in the Earth-imports-only scenario are scenario assumptions. Reconcile should check against Metzger's Γ values and the trade-press tanker-flight figures.

## Net assessment

The headline numbers are arithmetically consistent with the stated priors. The priors themselves are defensible scenario assumptions, not first-principles derivations. Codex's "weak" verdict on the first-principles claim is fair; the calc is better described as a scenario sensitivity model than a from-axioms derivation. Headline claims (q2.c1 through q2.c8) survive with appropriate confidence labels.
