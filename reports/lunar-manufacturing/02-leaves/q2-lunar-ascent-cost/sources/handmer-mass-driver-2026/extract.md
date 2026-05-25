---
slug: handmer-mass-driver-2026
title: "How to build a lunar mass driver"
url: https://caseyhandmer.wordpress.com/2026/05/08/how-to-build-a-lunar-mass-driver/
year: 2026
authors: ["Casey Handmer"]
fetched: 2026-05-25
fetcher: claude
type: blog
---

# Casey Handmer — lunar mass driver design and economics, May 2026

Recent first-principles design exercise from a former JPL engineer. Best near-contemporary public source on the engineering envelope for a lunar mass driver. The author has previously published on Starship economics and is technically credible on cislunar logistics math.

## headline-numbers

- **Per-shot payload:** ~200 kg of moon rocks per launch
- **Cadence:** "1 tonne every 3 seconds"
- **Annual throughput target:** ~10 million tonnes per year
- **Track length:** 128 m main acceleration (256 m including deceleration section)
- **Launch speed:** 1.6 km/s (just below lunar escape, ~2.38 km/s; trajectory uses lunar gravity assist + downstream maneuver)
- **Acceleration tolerance:** ~1000 g for monolithic rock projectiles
- **Kinetic power:** 450 MW (assuming 90% driver efficiency)
- **Peak instantaneous power:** 16 GW at track midpoint during launch
- **Average power consumption:** 1.75 MW per meter of track
- **Reactor cost:** $2–4B on Earth; lunar-built ~10× Earth ops cost
- **Power rate assumed:** $2.50/kWh (10× typical US 2026 grid rate)
- **Annual revenue (assumed):** $100B/year per mass driver

## assumed-product-price

Direct quote: "$10/kg is the assumed price for 'rocks in lunar orbit' delivered to customers." This is the **product price** at which the throughput economics close, not a derived breakeven. Handmer frames it as the price below which lunar bulk material isn't a commodity worth bothering with for satellite/space-economy customers.

## relevance-to-q2

The Handmer piece is the cleanest first-principles lunar-mass-driver design exercise in the recent literature. It does NOT directly model lunar-surface-to-LEO cost-per-kg. The output state is "rocks in lunar orbit" (specifically, projectiles on a trajectory that catches at some downstream collection point, typically near EML2 or in low lunar orbit). Lunar-to-LEO conversion requires an additional propellant-using maneuver and a separate cost stack.

Key quote on commercial limits: "At even $500/kg, launch cost is only 5% of the total satellite deployment cost, so a lunar mass driver is unlikely to drastically improve the economics of space-based AI."

## anchors-for-our-calc

- 200 kg per shot, 1 t/3 s → ~30,000 t/year of throughput per single track at full duty cycle. Handmer pushes to 10M t/yr via multiple parallel tracks or higher cadence — large scale.
- 450 MW kinetic power → ~12.5 MJ/kg kinetic per shot (at 1.6 km/s, KE = 0.5·v² = 1.28 MJ/kg, so ~2.4 MJ/kg with driver losses matches the conventional Lunarpedia figure).
- Capital structure: nuclear reactor + track. Per-kg cost dominated by capital amortization and lunar-construction premium, not energy.

## limitations

- Single-blog source, not peer-reviewed
- Product price $10/kg is **assumed**, not derived from a cost stack
- The 10× Earth-ops-cost lunar premium is a thumb-in-the-air estimate
- Doesn't address LEO delivery — only "rocks in lunar orbit"
