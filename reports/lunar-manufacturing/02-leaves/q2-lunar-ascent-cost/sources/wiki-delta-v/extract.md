---
slug: wiki-delta-v
title: "Delta-v budget (Wikipedia)"
url: https://en.wikipedia.org/wiki/Delta-v_budget
year: 2026
authors: ["Wikipedia contributors"]
fetched: 2026-05-25
fetcher: claude
type: reference
---

# Delta-V budget — Earth-Moon system

Reference for the canonical ΔV values used in q2 calc. Wikipedia delta-v tables follow standard high-thrust chemical-rocket conventions with Oberth assistance assumed.

## delta-v-values

- **Lunar surface to LLO (low lunar orbit):** **1.87 km/s** [direct quote from high-thrust Earth-Moon table]
- **Moon surface to LEO (combined via direct trajectory):** **5.93 km/s** [direct quote; assumes specific transfer architecture]
- **Earth surface to LEO:** "an increase of velocity from 0 to 7.8 km/s, but also typically 1.5–2 km/s for atmospheric drag and gravity drag" — total ≈ 9.3–9.8 km/s

## decomposition-for-our-calc

The Moon-to-LEO 5.93 km/s figure is the *total* propulsive ΔV needed if you use chemical maneuvers throughout. It decomposes approximately as:
- Lunar surface to LLO: 1.87 km/s
- LLO injection to trans-Earth: ~0.7 km/s
- Mid-course corrections + LEO insertion (with Oberth at perigee): ~3.36 km/s

If aerobraking is used at Earth for LEO insertion, this collapses by 3–3.5 km/s, leaving ~2.5 km/s of propulsive ΔV. This is a major architectural choice.

## architectural-comparison

- **Pure-chemical, no aerobraking:** 5.93 km/s. With Isp 360 s (methalox) → propellant mass fraction 0.82; with Isp 450 s (hydrolox) → 0.74.
- **Pure-chemical, aerobraking at Earth:** ~2.5 km/s propulsive. With Isp 450 s → 0.43.
- **SEP return (water propellant at Isp 2000 s):** still need ~1.87 km/s chemical from lunar surface to LLO, but the LLO-to-LEO leg uses SEP. Propellant mass fraction for chemical leg only: 0.39 at Isp 450 s.
- **Mass-driver launch + SEP transfer:** chemical leg eliminated entirely. Mass driver provides ~1.6 km/s departure (just below lunar escape ≈ 2.38 km/s), with SEP doing the remaining km/s as a slow spiral.

## relevance

These ΔV values are the load-bearing input for the calc pass. Combined with Isp assumptions they fix the propellant mass fraction, which dominates everything else.

## limitations

Wikipedia's tables use Hohmann-style transfers and high-thrust Oberth assumptions. Actual mission trajectories can be 5–15% different depending on patched-conic vs full-N-body computation. For BOTEC-level cost work this is acceptable.
