---
pass: 1
kind: research
leaf: q1-earth-launch-cost
date: 2026-05-25
agent: claude-opus-4-7
audited: not-applicable
---

# Pass 1 — Research (q1-earth-launch-cost)

Initial scoping research. The leaf question demands a 2026-2040 trajectory of $/kg to LEO with realistic uncertainty bands. Gathering candidate sources; no claims written yet.

## Sources captured

### Tier-1 (concrete pricing data)

- **[satbase-2026-falcon9](sources/satbase-2026-falcon9/extract.md)** — SatBase Feb 2026 pricing analysis. Confirms 2026 Falcon 9 rideshare at $7,000/kg, $5,000/kg→$7,000/kg between 2021 and 2026 (rising, not falling). SpaceX's stated $500/kg annual structural increase. Internal cost ≈$629/kg per cross-source. Critical baseline for the "Starship dropping list prices" thesis.

### Tier-2 (to fetch in subsequent passes)

- **Netizen "Cost per Kilogram to LEO Over Time"** — has full historical $/kg trajectory plus Citigroup 2040 forecasts. ECONNREFUSED on initial fetch attempt; retry.
- **Citigroup 2040 forecast** — $100/kg operator cost projection by 2040.
- **NextBigFuture "Starship Roadmap 100x"** — Musk's claimed $10/kg targets with full reuse + cadence assumptions.
- **OrbitalRadar 2026 launch cost comparison** — multi-rocket dollar-per-kg table.
- **Eric Berger / Ars Technica** — typically the best-sourced Starship technical/commercial reporting. Worth grabbing recent pieces.

## Key public figures for future Source Reviews

(For sub-pass 4)
- **Elon Musk** — Starship cost claims (the optimistic anchor)
- **Casey Handmer** — technical commentary on launch economics
- **Dylan Patel (SemiAnalysis)** — skeptic on $/kg projections; useful counter-anchor
- **Eric Berger (Ars Technica)** — neutral reporting on real-world progress
- **Andrew McCalip (Varda)** — public economics calculator
- **Citigroup analysts** — institutional forecast viewpoint

## Initial pattern of evidence

**The crossover question**: there's a stark gap between Musk's claimed Starship costs ($10/kg with full reuse + 1000 launches/year) and Falcon 9 list prices that are *rising* at $500/kg/year. Three scenarios emerge:

1. **Starship achieves operational targets** → list prices drop to ~$30-100/kg by 2030-2035, ~$10-30/kg by 2040. Lunar manufacturing question is much harder because terrestrial competitor is cheap.
2. **Starship partially achieves** → list prices stabilize at ~$200-500/kg through 2035, ~$100-300/kg by 2040. Lunar manufacturing competitiveness depends on architecture.
3. **Starship hits operational ceiling** (low cadence, reliability issues, regulatory) → list prices stay at $1,000-2,000/kg through 2040, never reach Musk's targets. Lunar manufacturing comparatively easy to compete.

The 2026 trade-press evidence (SatBase) doesn't yet show Starship pulling list prices down. Falcon 9 rideshare is at $7,000/kg and rising. The Starship cost claims are speculative until Starship achieves operational cadence at scale.

## Engineering vs commercial decomposition

A critical distinction: **internal SpaceX cost ≠ list price ≠ effective $/kg for lunar comparison**.

- Internal cost (what it actually costs SpaceX to build + launch): ~$629/kg Falcon 9 today
- List price (what customers pay): $2,720-7,000/kg depending on tier
- Margin: ~75% in current Falcon 9 economics

For lunar manufacturing competitiveness math, the relevant comparator is whichever value SpaceX uses internally for their own logistics (closer to internal cost) — or the published list price if lunar product is sold to *other* customers.

## What to chase in subsequent sub-passes

- **calc**: derive Starship costs from first principles — payload mass, dry mass, propellant cost, vehicle amortization across N reuse cycles. NOT from Musk's claims. Compare to historical learning curves (Wright's Law applied to launch vehicles).
- **reconcile**: compare first-principles result to Musk projections, Citigroup forecast, Patel's skeptic critique. Identify which scenario above the calc lands in.
- **source-review**: point-by-point Musk + Patel + Handmer claims. The disagreement IS the data here — there's no consensus answer.
- **write**: produce trajectory with explicit scenario bands (optimistic / central / pessimistic) corresponding to the three operational outcomes above. Use TAI/industrial-explosion sensitivity as a separate axis.

## Anti-pattern check

- ✓ Sources sealed for calc (this is research, no claims yet)
- ✓ No "by 2040" framing locked in — the leaf intends to deliver a trajectory with conditional scenarios
- ✓ Voice register kept dry; "real-world progress", "structured pricing strategy", not "Musk's bold vision"
- ⚠ Single source so far (SatBase); subsequent fetches needed for breadth
