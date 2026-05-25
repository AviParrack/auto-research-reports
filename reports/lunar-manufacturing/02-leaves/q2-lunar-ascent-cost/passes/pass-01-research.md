---
pass: 1
kind: research
leaf: q2-lunar-ascent-cost
date: 2026-05-25
agent: claude-opus-4-7
audited: not-applicable
---

# Pass 1 — Research (q2-lunar-ascent-cost)

Initial scoping research. The leaf question demands a 2026–2040 trajectory of cost per kg from lunar surface to LEO, broken out by chemical rocket vs mass driver. This pass gathers candidate sources; no claims written yet.

## Sources captured

### Tier-1 (concrete engineering or pricing anchors)

- **[handmer-mass-driver-2026](sources/handmer-mass-driver-2026/extract.md)** — Casey Handmer's May 2026 first-principles lunar mass driver design exercise. Per-shot 200 kg, 1 t/3s cadence, 128 m track, $10/kg assumed product price. The cleanest near-contemporary mass driver engineering reference.
- **[metzger-2023](sources/metzger-2023/extract.md)** — The gear-ratio paper. Provides Γ_LEO ≈ 14 under chemical, Γ_LEO ≈ 1 under SEP return. Bridge to q4.
- **[coutts-sowers-2025](sources/coutts-sowers-2025/extract.md)** — VOI framework for lunar ice. Anchors lunar surface propellant price at $500/kg and Starship LEO cost at $30–300/kg.
- **[wiki-delta-v](sources/wiki-delta-v/extract.md)** — Canonical ΔV values. Lunar surface to LLO 1.87 km/s; full Moon-to-LEO chemical 5.93 km/s.
- **[starship-hls-wiki](sources/starship-hls-wiki/extract.md)** — Operational Starship HLS parameters. 100 t headline payload, 12–14 tanker flights per mission, $2.89B HLS contract.
- **[orbital-refueling-newspaceeconomy](sources/orbital-refueling-newspaceeconomy/extract.md)** — Dec 2025 trade-press analysis. 1,200 t propellant per HLS mission; ~$400M per mission estimate.

### Tier-2 (reference / corroboration)

- **[wiki-mass-driver](sources/wiki-mass-driver/extract.md)** — Mass driver physics envelope. 50–90% efficiency; theoretical 10.5 km/s at 5600 g; loose $47M / 10 kg projectile estimate.
- **[lunarpedia-mass-driver](sources/lunarpedia-mass-driver/extract.md)** — Lunar-specific reference. 2.4 MJ/kg energy. Track-length-vs-acceleration tradeoff.
- **[sciencearray-mass-drivers](sources/sciencearray-mass-drivers/extract.md)** — Secondary synthesis with $10/kg target and historical O'Neill $1/lb projection. Triangulation for Handmer.
- **[payload-cargo-landers](sources/payload-cargo-landers/extract.md)** — Operational cargo-variant payloads (12–15 t). Distinct from the 100 t crewed-HLS headline.

## Sources attempted but not fetched (worth chasing in source-review)

- **Kornuta et al. 2019 Commercial Lunar Propellant Architecture** — primary source for lunar propellant production cost. PDF behind paywall / OSTI binary; secondary citations only.
- **Lewis et al. NASA "Parametric Assessment of Lunar and Mars Ascent Vehicle Synergy"** — direct NASA ascent vehicle cost study. PDF binary; couldn't extract text via WebFetch.
- **AIAA 2025-4123 "Cost-Benefit Analysis of Lunar Mass Driver Technologies"** — recent peer-reviewed mass driver economic analysis. Paywalled (HTTP 403).
- **Ethan Miller 2023 thesis (SJSU)** — student deep-dive on lunar mass driver implementation. PDF binary.

These deferred sources are flagged for a future source-review pass; they would likely tighten the mass driver capital-cost estimates and the lunar ascent vehicle dry-mass numbers, but the headline conclusions of q2 don't depend on them.

## Key public figures for future Source Reviews

(For sub-pass 4 — applies to source-review or to a later cross-source pass)
- **Casey Handmer** — independent technical commentary, formerly JPL
- **Philip Metzger** — academic anchor for cislunar economics framework
- **George Sowers** — ULA's original lunar-propellant price-setter, now Colorado School of Mines
- **Dallas Bienhoff** — Boeing/private cislunar logistics consultant (referenced but not directly fetched)
- **Gerard O'Neill** — historical foundation of the mass driver concept (1974 work)

## Initial pattern of evidence

Two architectural families dominate the literature, and they don't compete in the same era:

**Chemical-rocket ascent (operational 2026–2035):**
- Earth-imports-only: ~$30,000–50,000/kg lunar surface to LEO, dominated by terrestrial-launch cost amplified by Γ_chemical ≈ 14
- Partial-ISRU: drops to ~$2,000–5,000/kg if lunar surface propellant available at Sowers's $500/kg target
- Full-ISRU mature operations (post-2035): potentially $500–1,500/kg, still dominated by ascent-vehicle hardware amortization

**Mass driver (post-2035–2040 at earliest):**
- Handmer's design closes at $10/kg "rocks in lunar orbit," but only at 10 million tonnes/year throughput
- Bootstrap problem: getting the mass driver to the Moon and operational is itself a multi-billion-dollar chemical-rocket project (q5 territory)
- For LEO delivery, additional propulsion needed after mass-driver launch; this adds back a chemical or SEP stage

## Engineering vs commercial decomposition

A critical distinction must be preserved in the calc pass: **lunar-ascent vehicle cost ≠ lunar-product LEO delivery cost ≠ effective $/kg for the comparison framework**.

- Ascent-only (lunar surface to LLO): drops out the Earth-to-LEO term but adds lunar ascent vehicle hardware + lunar ops + lunar-surface propellant
- Surface-to-LEO chemical: ascent + trans-Earth injection + LEO insertion (or aerobraking)
- Surface-to-LEO mass driver: kinetic launch + downstream chemical or SEP stage for LEO insertion (mass driver alone cannot circularize)

For the lunar-manufacturing competitiveness math (the root question of the report), the relevant comparator is **lunar product delivered to LEO** at full system cost, including the cost of getting the lunar infrastructure there in the first place. q2 will focus on **steady-state delivery cost** assuming the lunar infrastructure exists, and flag the bootstrap problem for q5 (capital buildup).

## What to chase in subsequent sub-passes

- **calc:** derive lunar-to-LEO cost from first principles. Three scenarios matching q1's structure:
  - **aggressive-ISRU**: lunar propellant available at Sowers price target; SEP return architecture; mass driver operational by late era
  - **partial-ISRU**: lunar propellant available but at higher price; chemical-only architecture
  - **Earth-imports-only**: no lunar propellant; HLS-style chemical round-trip with Earth-imported propellant
- **reconcile:** compare derived numbers to Coutts-Sowers, Metzger, Handmer. The disagreements ARE the data here.
- **source-review:** point-by-point Handmer + Metzger + Coutts-Sowers + others. Verify quote authenticity.
- **write:** produce trajectory with explicit scenario bands corresponding to architectural choice. Use TAI/industrial-explosion sensitivity as a separate axis (mass driver becomes feasible much earlier under TAI).

## Anti-pattern check

- ✓ Sources sealed for calc (this is research, no claims yet)
- ✓ No "by 2040" framing locked in — q2 intends to deliver a trajectory with conditional scenarios and acceleration sensitivity
- ✓ Voice register kept dry; no "real-but-contingent" / "the dominant lever" editorializing
- ⚠ Several primary sources (Kornuta, Lewis, AIAA-4123, Miller) gathered indirectly via secondary citations; flagged for source-review pass
- ⚠ Single contemporary mass-driver-engineering source (Handmer); should triangulate against AIAA-4123 if it can be obtained
