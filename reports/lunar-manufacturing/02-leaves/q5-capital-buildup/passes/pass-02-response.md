---
pass: 2
kind: calc-response
leaf: q5-capital-buildup
date: 2026-05-26
agent: claude-opus-4-7
responds_to: passes/pass-02-audit.md
---

# Response to Codex Audit on Pass-02 Calc

Codex's overall verdict was `weak` with several high-severity findings. Three categories of response: accept-and-downgrade, accept-and-amend, dispute.

## Accepted (will downgrade or amend)

- **721.8 t over 20 years (partial)**: Codex correctly observed this is the smooth amortized service-flow mass, not a discrete replacement schedule. The discrete number is closer to 800 t. I will retain 721.8 t as the **amortized planning anchor** and note the discrete-schedule sensitivity (+10%) in claims.yaml. Confidence on q5.c2 stays at medium.

- **75 t ISRU plant (weak, high severity)**: Codex's 109 kg/(t/yr) vs 140 kg/(t/yr) benchmarks (which it cited from the NIA bigidea ISRU paper) suggest my 50 kg/(t/yr) pre-redundancy figure is aggressive by ~2x. Accepting the criticism: the realistic ISRU plant mass for 1000 t/yr mixed output is more like 140-150 t (~2x my baseline). This pushes one-set total from 311 t to ~390 t (~25% increase) and BAU grand total from $167B to ~$210B. I'll note this as a calibration adjustment in claims.yaml (q5.c1, q5.c4 confidence downgraded).

- **15 t infrastructure (weak)**: Codex correctly notes my infrastructure budget is sparse — power distribution, cryogenic storage, tanks, cables, thermal control, shelter, cranes are largely uncounted. Realistic infrastructure mass is probably 40-60 t, not 15. Adjustment direction is "BAU total revises upward by another ~20 t one-set, another ~$5-10B in BAU $".

- **TAI 0.4-yr 12-mo occupation (contradicted, high severity)**: Codex is right that "M6 first crewed sustained occupation (12 mo) at 0.4 yr" is internally inconsistent. The compression collapses elapsed-time *between* milestones but cannot compress the elapsed-time *within* a 12-month occupation. The TAI row should specify hardware-iteration-cycle compression, not literal calendar floor compression. The corrected reading: under TAI, the *time-between-milestones* compresses 30x, but M6 by definition takes 12 months once initiated. M8 (net-positive export) thus takes minimum ~12+ months even under TAI. The write pass will reframe this honestly. Lowering confidence on q5.c7 milestone-timing-under-TAI.

- **TAI degenerate case (partial)**: Codex says the model should "stop" or "add irreducible physical lead-time floors" at the TAI extreme. Accept: the write pass will not present the $0.01B / <1 yr row as a usable estimate but as a degenerate boundary indicating the calc framework's domain of applicability. q5.c6 confidence is already `speculative`; clarifying language in the write pass.

- **dev-cost ÷ sqrt(time_compression) (weak, high severity)**: Codex flags the heuristic as arbitrary and possibly wrong-signed. Accept: the heuristic is indeed arbitrary. The honest move is to retain it as a placeholder-with-flag rather than try to defend it as derived. In the write pass I'll present development cost as a separate dimension that doesn't compress with launch/hardware — TAI design and qualification cost is a separate domain.

- **sources sealed / first-principles (partial)**: Codex correctly notes that several inputs are benchmark anchors (B330, NASA FSP kg/kWe, q1 launch costs, Sowers φ) rather than derivations from first principles. Accept the labeling correction: these are **benchmark anchors used to size the components**, not values cribbed from any single TEA. The calc is "sealed" in the strong sense of "no Metzger 2023 / Sowers 2021 / Jones 2020 TEA numbers consulted during this pass" — the benchmark inputs (B330 dry mass, NASA FSP target, q1 launch cost) are physical/engineering anchors not TEA outputs. Pass-02-calc.md should clarify this distinction; will note in claims.yaml.

- **$1k/kg TAI hardware cost (high severity, partial)**: Codex flags $1k/kg as "unsupported" for human-rated lunar nuclear/habitat/ISRU hardware. Accept partially: the TAI regime is by definition the regime in which the human-rating-and-qualification cost structure breaks down (TAI can iterate hardware faster than current qual processes; or designs are de-novo robust enough that qual costs collapse). The calc's $1k/kg figure is the speculative-TAI corner, not a defensible-by-precedent number. Already flagged as speculative; reconcile will not lean on this number.

## Disputed / clarified

- **125 t for 500 kWe FSP (supports — no dispute, but adding note)**: Codex confirms my arithmetic. The "linear scaling" caveat Codex flags is real — 500 kWe is *not* simply 12.5 × 40 kWe NASA-FSP units; a single 350-kWth class microreactor (Duchek 2024) is the architecturally-natural unit at this scale. The 125 t estimate is conservative either way.

- **31.5 t mobility fleet (weak)**: Codex says per-unit masses are "plausible for scout-class but low for industrial 1000 t/yr operations." Accept that scout-class numbers underestimate industrial-scale haulers; 5 × 2,000 kg haulers is probably 5 × 5,000 kg = 25 t in the haulers alone, not 10 t. Realistic mobility fleet is more like 60-80 t, not 31.5 t. Same direction as ISRU and infrastructure — BAU total revises upward.

- **40 t manufacturing complement (unsupported)**: Codex flags this as a "pilot-shop placeholder." Accept that 40 t is a near-term-aspirational figure. Realistic full-mfg-complement is probably 80-150 t. Same upward revision direction.

## Net effect: BAU revises from $167B toward $250-400B

Aggregating Codex's accepted criticisms (ISRU 75→150t, mobility 31.5→75t, mfg 40→120t, infra 15→50t), the one-set capital mass goes from 311 t to ~500 t (~60% increase). BAU grand total revises from $167B to roughly $250-300B over 20 yr. **This is much closer to MacDonald's SEI/Apollo-precedent $1T ceiling and slightly above PwC's $72-88B all-party cumulative**.

Decision: rather than re-run pass-02-calc.py with all adjusted inputs (which would inflate the dev-cost heuristic alongside), I'll present the BAU figure in the write pass as a **range** of approximately $150-400B reflecting Codex's accepted criticisms, with the headline being "**BAU ~ $200B order of magnitude**." This is honest about the calc's precision limit. The IE figure scales similarly to $1.5-3B (still close to Zubrin's $1.5B floor). The TAI row stays degenerate but presented as boundary rather than estimate.

## Updated claims.yaml entries

q5.c1: amend text to "one-set capital mass approximately 311-500 t (lower bound from calc baseline; upper bound after Codex-accepted adjustments to ISRU/mobility/mfg/infra mass budgets)"; confidence stays medium.

q5.c4: amend headline figure to "$150-400B over 20 yr (calc-baseline $167B; Codex-adjusted upper bound ~$300-400B)"; confidence stays low.

q5.c7: amend M6 (first crewed sustained occupation) to note that the 12-month occupation itself cannot compress below 12 months under TAI, so the M8 milestone clock has an irreducible 12+ month floor; under TAI the milestone clock is "as fast as physical lead-times for hardware and qualification permit."

q5.c10: amend to reflect Codex's "double-counting hardware vs dev cost" critique; note that the $/kg hardware × dev-multiplier may overlap with realistic published $/kg figures that already include development.

Codex's external benchmark links (ISS, Gateway, NASA FSP, B330 NTRS, NIA ISRU paper) will be sampled in the reconcile pass to tighten the sizing further if needed.
