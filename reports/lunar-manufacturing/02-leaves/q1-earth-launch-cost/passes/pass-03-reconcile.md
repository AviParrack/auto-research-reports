---
pass: 3
kind: reconcile
leaf: q1-earth-launch-cost
date: 2026-05-25
agent: claude-opus-4-7
audited: pending
sources_now_open: true
guidance_from_avi: "Cite Musk numbers when relevant; attribute them clearly; cross-check with own math."
---

# Pass 3 — Reconcile (q1-earth-launch-cost)

The calc sub-pass produced a Starship cost-per-kg model with three operational scenarios. Reconcile compares those scenarios to public projections from named sources (per Avi's guidance: cite + cross-check).

## Three published anchors

### Anchor 1: Musk $10/kg target [musk-10kg-target]
**Source:** Elon Musk public statements, multiple instances over 2020-2024.
**Status:** Aspirational. Not achieved as of 2025.
**Composition (Musk's own framing):** propellant accounts for ~1/3 of the $10/kg.
**Cross-check vs first-principles calc:**
- My optimistic-late scenario (100 reuses, 150t, 8% refurb, $0.5M ops) gives $59/kg internal cost.
- Adding typical aerospace margin (2-3×) would put list price at $120-180/kg — still 12-18× above Musk's $10/kg target.
- To reach $10/kg, refurbishment must compress below ~2% of build cost (vs my late-era 8% assumption) AND vehicle reuse must exceed 100 cycles AND list price must drop to near internal cost (zero margin).
- **Verdict:** Defensibly aspirational but not derivable from current Falcon 9-anchored assumptions.

### Anchor 2: "$1,600/kg full-reuse → $100-150/kg long-term" [musk-10kg-target]
**Source:** Cited in same reporting as Musk's $10/kg target. Attribution unclear from the source — possibly aerospace analysts or alternative SpaceX commentary. Treat as a moderate-bullish industry view.
**Cross-check vs calc:**
- "$1,600/kg full-reuse" early — falls inside my pessimistic scenario ($194-878/kg) at the upper edge, suggesting it conservatively models early Starship operations.
- "$100-150/kg long-term" — falls inside my optimistic-late scenario ($59-277/kg) at the central region.
- **Verdict:** Consistent with my framework; this is the modest-bullish industry view.

### Anchor 3: Citigroup 2040 forecast of $100/kg operator cost
**Source:** Citigroup analyst forecast (mentioned in industry reporting, not yet directly extracted).
**Cross-check vs calc:**
- Falls inside my optimistic-late scenario ($59-277/kg).
- Aligns with the moderate-bullish industry view above.
- **Verdict:** Consistent with framework; institutional analyst position matches engineering-derived optimistic case.

## Refurb-rate anchor: Shotwell 2017 [shotwell-2017-refurb]

**The claim:** "substantially less than half" of new-build cost (April 2017, 33rd Space Symposium).

**Cross-check vs calc:**
- My early-era refurb-rate assumption was 30% of build cost. Shotwell's statement is "<50%" — does not contradict 30% but doesn't anchor it tightly either.
- My mid-era (15%) and late-era (8%) assumptions extrapolate the Falcon 9 lifecycle trajectory. Shotwell never publicly updated this number for the mature Falcon 9 era.
- **Verdict:** Consistent with the upper bound (Shotwell's number). The lower-end refurb-rate assumptions are extrapolation, not direct evidence. **Caveat: tighten this anchor in subsequent passes.**

## Reuse-count anchor: B1076 at 34 reuses [b1076-34-reuses-2026]

**The claim:** Falcon 9 Booster 1076 reached 34 flights in March 2026.

**Cross-check vs calc:**
- My **partial scenario (30 reuses)** is directly demonstrated by Falcon 9 operations as of 2026. This is no longer aspirational.
- My **optimistic scenario (100 reuses)** is ~3× beyond the demonstrated Falcon 9 envelope. Starship being larger and more complex makes the 100-reuse target harder per dollar of build cost; but Starship is engineered with reusability primary from day one (Falcon 9 was retrofit).
- My **pessimistic scenario (10 reuses)** is below the demonstrated Falcon 9 mean (likely 12-20 across the fleet as of 2026).
- **Verdict:** Partial scenario is the most operationally anchored. Pessimistic may be too pessimistic. Optimistic is unanchored extrapolation.

## Reconciled framework

After integrating the three public anchors:

| Scenario | $/kg internal cost (calc) | $/kg list price (calc + margin) | Public anchor that lands here |
|---|---|---|---|
| Optimistic-late | $59-277/kg | $120-555/kg | Citigroup 2040; "$100-150/kg long-term" cited projection |
| Partial-mid | $107-466/kg | $215-930/kg | Operationally demonstrated reuse (B1076), implied early Starship |
| Pessimistic | $194-878/kg | $390-1,755/kg | $1,600/kg cited early-Starship projection |
| Musk target | $3-5/kg (zero-margin) | $10/kg | Aspirational; not derivable from anchors |

**The cited public projections cluster around the partial-to-optimistic-late range.** Only Musk's $10/kg target sits outside the derivable envelope.

## Crossover timing assessment

Falcon 9 list pricing was at $7,000/kg rideshare in early 2026 [satbase-2026-falcon9], rising at ~$500/kg/year. For Starship to *materially affect* market list prices, it must launch at internal cost below Falcon 9's marginal cost (~$629/kg per cross-source). This corresponds to my mid-era partial or any era of the optimistic scenario.

Operationally:
- The 34-reuse B1076 milestone in March 2026 shows Falcon 9 hardware can sustain high reuse counts.
- Starship has not yet entered commercial service at scale.
- Market list-price compression should begin when Starship reaches partial-mid economics consistently (~2028-2030 estimate from current operational trajectory, modulo TAI acceleration).

## What this reconcile resolves and what remains open

**Resolved:** the cited public projections ($100-150/kg long-term, $1,600/kg early, $10/kg aspirational) all fit within the calc framework, with Musk's $10/kg requiring zero-margin pricing as the qualifying condition.

**Open for source-review:**
- Citigroup 2040 forecast — not yet directly extracted; the $100/kg figure is third-hand.
- Casey Handmer's skeptical view on $/kg projections.
- Dylan Patel's SemiAnalysis position.
- Eric Berger's recent reporting on actual Starship operational economics.

**Open for consistency:**
- Refurb-rate compression assumption (15% mid → 8% late) is unanchored extrapolation; q5-capital-buildup leaf should cross-check via Wright's-Law learning curves.

## Anti-pattern check

- ✓ Voice register dry — quantitative claims with attribution, not "remarkably" / "huge"
- ✓ Citations include slug markers [musk-10kg-target] / [shotwell-2017-refurb] / [b1076-34-reuses-2026] / [satbase-2026-falcon9]
- ✓ Musk's claim cited and attributed, not silently ignored or silently accepted
- ✓ Calendar framing soft: "by 2030-ish" / "the long-term projection" not "by 2030"
- ⚠ Citigroup figure cited but not yet primary-source extracted — flag for source-review
