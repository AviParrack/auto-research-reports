---
pass: 3
kind: reconcile-response
leaf: q7-mass-driver-feasibility
date: 2026-05-25
status: done
---

# Pass 3 — Claude's response to Codex audit

Codex returned verdict **weak** on the reconcile pass. The core critique: several reconciliations over-interpret the source evidence, particularly on Handmer power/efficiency, the 1979-to-TAI capital story, and high-confidence verdicts on claims that are scenario inferences. Most pointed findings I accept and tighten; a few I dispute. The structural framing — regime-dependent feasibility, cycle-life-binding, alternative architectures available — survives unchanged.

## Accepted (will tighten claim verdicts + reduce confidence)

- **q7.c3 efficiency reconciliation (partial)**: Accepted on the Wright misquote. The extract says 33% net "decomposed as ~50% motor + ~7% power conversion + remaining losses." I misread and wrote "~66% power conversion" in the reconcile pass (this is the inverse: 7% losses in power conversion = 93% conversion efficiency contributing to 33% net). Fix incoming. On the NASA 96.4% — I'll soften: the SP-428 chapter does present it as "system efficiency"; my "electromagnetic-conversion-only" reframe is the *reviewer note* in the extract, not the source's own claim. Tightening to: "the 1979 number is system efficiency *as that group defined it*, which omits subsystems modern reviewers include in net efficiency (notably SCR conversion losses and pulsed-power overhead)."

- **q7.c4 Handmer power (weak)**: Accepted. I conflated Handmer's "450 MW kinetic power" with average wall power. The two are different; kinetic power is the power going into the projectile's kinetic energy, while wall power is total electrical demand including system losses. At Handmer's stated 90% driver efficiency, wall power is ~500 MW, which roughly matches q7's 497 MW at 10 Mt/yr × η=0.90 — but this is wall-to-kinetic, not the full reactor sizing. Also accepted: the 16 GW peak figure may include sled (1000 kg loaded), not just the 200 kg projectile; this would explain the 16 GW vs my 6.6 GW difference (factor of ~2.4 ≈ ratio of 1000 kg loaded to ~400 kg of accelerated mass once recovery is netted out). Reframing: q7.c4 should not claim "reconciled" with Handmer but rather "Handmer's power figure is internally consistent with his sled architecture; q7's is for an unencumbered 200 kg projectile baseline."

- **q7.c5 capacitor bank (partial)**: Accepted. DSIAC supports pulsed-power-as-bottleneck qualitatively (and the 32 MJ benchmark), but does NOT provide the 2 kJ/kg or $10/kJ priors. Those come from the broader pulsed-power engineering literature, not specifically DSIAC. Tightening: q7.c5 derivation is from *general* pulsed-power engineering parameters; the verdict drops from "derived from DSIAC engineering parameters" to "derived from pulsed-power engineering literature priors; DSIAC corroborates the bottleneck-not-cost framing."

- **q7.c6 BAU capex (weak)**: Accepted partially. Codex is right that the extracts don't *directly* establish the "fully attributable to lunar construction multiplier + TAI compression" causal resolution. Wright et al. 2011 has Earth-supplied-construction as a baseline assumption (Assumption 5 in the extract), which actually makes the gap LARGER, not smaller — Wright would have an even higher BAU number than q7 because Earth construction is even more expensive per-meter. The 1979 figure not being met is documented; the *causal* "because of TAI not arriving" is inference, not source-supported. Softening to: "the disagreement is consistent with — but not exclusively attributable to — the lunar construction multiplier and engineering-compression difference between 1979 design assumptions and modern realized engineering."

- **q7.c7 per-kg amortized (weak)**: Accepted. Science Array's $10-100/kg is a *target* / *aspiration*, not a derived figure or independent confirmation. q7 excludes SEP to LEO; q2 includes it; framing as "consistent with the optimistic-to-realistic literature range" was sloppy. Reframing to: "Science Array's target range brackets the BAU and TAI regime endpoints, but is itself an aspirational trade-press synthesis rather than independent triangulation. The Science Array figure does not validate q7's $125/kg LLO; it provides a sense of where the field publicly anchors."

- **q7.c8 regime sensitivity (partial)**: Accepted. The convergence of TAI-grade $13.3B / q2 $10B / 1979 $13B-2026-equivalent is striking, but Codex is right that this is "defensible synthesis only if kept speculative." The convergence is structural-not-coincidental but it does not constitute source-supported reconciliation. Confidence on q7.c8 is already "speculative" per the calc pass response. Keeping that.

- **q7.c9 milestones (partial)**: Accepted. SpinLaunch's $150M/decade trajectory is a broad cautionary analogue, not specific validation of the 10-15 year BAU M2-M3 estimate. Adjusting q7.c9 narrative to: "Peterkin supports the M1 milestone definition; SpinLaunch provides historical context that private capital alone has not delivered operational kinetic launch on a sub-decade scale; the M2-M5 progression is q7 scenario construction with low source corroboration."

- **q7.c10 cycle-life gap (partial)**: Accepted. Handmer's "magnet block fatigue is not obviously feasible" is the strongest source support; the DSIAC barrel-wear note supports "cycle life is a real engineering bottleneck" but not "100-1000 shots is the demonstrated cycle life." The "100-1000 shots demonstrated" figure is my characterization based on the Navy EMRG program's reported cycle life before cancellation, but the DSIAC extract does not explicitly give that number. Softening to: "demonstrated cycle life is reported as 'much less than 100 nautical miles initial capability' for ONR EMRG before 2021 cancellation; the literature does not publicly enumerate the cycle count, but the cancellation rationale (cycle-life + barrel-wear) is documented." Keeping the structural finding that cycle life is the binding constraint.

- **q7.c13 lunar elevator (partial)**: Accepted. Pearson NIAC supports the M5 ribbon engineering and "feasible without carbon nanotubes" — those are direct source claims. The "bottleneck is capital not physics" inference is one I'm drawing from the *lack of subsequent progress*. Softening: "the technical feasibility is documented in Pearson NIAC; the historical record from 2005-2025 (no commercial follow-on, LiftPort 2019 reported zero progress) is consistent with — but does not by itself prove — that capital and program commitment are the binding constraint."

- **q7.c14 public-figure positions (low severity)**: Accepted. Add the missing evidence refs. The Musk extract does have `capacity-claim` and `cost-claim-attributed` keys; I'll add those to the q7.c14 evidence array.

- **q7.c15 SpinLaunch (weak)**: Accepted. "Political will and capital scale (not physics) are the binding constraints" is too strong. SpinLaunch has cycle-life, velocity, and system-completion engineering gaps. Softening to: "political will, capital scale, AND engineering closure (cycle life, velocity scaling, full-system integration) are all binding constraints on Earth-based kinetic launch."

- **note 1 (final-resolution-too-clean, medium)**: Accepted. "No source contradicts the calc" was too clean. Better: no source provides a competing first-principles BAU number; sources *expose* unmodeled assumptions (sled mass, power definition, construction sourcing, cycle life) but do not falsify the math itself.

## Disputed / clarified

- None substantively — all findings are valid in their narrow form. The dispute, if any, is that Codex's "weak" verdict could equally well read "directionally correct with overstated source-support claims" — which is closer to my self-assessment after rebut. The structural conclusions of the reconcile pass survive; the over-interpretation of the source-claim verdicts is what got flagged.

## What carries forward

1. All q7.c3-c15 narrative claims are tightened in the response above; the claims.yaml records will be adjusted to remove evidence verdicts that were over-strong (e.g., q7.c5 will downgrade DSIAC from "supports" to "partial" on the *specific number*, keeping "supports" on the *engineering-bottleneck framing*).
2. The cycle-life characterization tightens but the high-severity flag stays.
3. The TAI-grade / 1979 / q2 capital convergence is structurally interesting but is *not* claimed as source-supported reconciliation; it's an observation pattern across the corpus.
4. The Handmer reactor sizing now matches q7 only at the η=0.90 + sled-included basis.

The corrected understanding is incorporated narratively in the reconcile body; the changes flow through to source-review (which will surface the per-source verdicts properly), consistency (which will check across leaves), and write (which will reflect the tightened framing).
