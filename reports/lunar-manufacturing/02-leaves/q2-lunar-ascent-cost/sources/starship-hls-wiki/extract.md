---
slug: starship-hls-wiki
title: "Starship HLS (Wikipedia)"
url: https://en.wikipedia.org/wiki/Starship_HLS
year: 2026
authors: ["Wikipedia contributors"]
fetched: 2026-05-25
fetcher: claude
type: reference
---

# Starship HLS — operational parameters

The current concrete reference architecture for chemical-rocket lunar delivery. Used here to anchor the "Earth-imports-only" and "partial-ISRU" scenarios.

## tanker-flight-counts

Numbers vary widely across sources:
- Elon Musk (2021): "between 'four and eight' tanker launches"
- GAO (2021): "16 launches overall"
- NASA official (2023): "in the high teens"
- SpaceX VP (2024): "10-ish"

Mid-range working assumption: 12–14 tanker flights per HLS mission to lunar surface and back.

## payload-and-vehicle

- **Payload to lunar surface:** "100,000 kg (220,000 lb)" — quoted for cargo variant
- **Vehicle volume:** "614 m³ (21,700 cu ft)"
- **Height:** ~52.3 m, **diameter:** 9 m
- **Crew (HLS variant):** 2–4 astronauts
- **Lunar loiter duration:** "100 days" in lunar orbit
- **Lunar surface stay:** ~7 days
- **Propulsion:** 3 Raptor sea-level + 3 Raptor vacuum + dedicated landing engines using gaseous methane + oxygen
- **Propellant:** CH₄/LOX (methalox)

## contract-cost

NASA HLS contract value: **$2.89 billion** initial award (development + first crewed mission demonstration).

## relevance-to-q2

If 14 tanker flights × 100 t payload each = 1,400 t of propellant in LEO per HLS mission, and the HLS carries 100 t to lunar surface, then the round-trip-equivalent gear ratio (LEO propellant per kg of lunar-surface payload delivered) is approximately:
- **14 tanker flights × 100 t / 100 t lunar payload = 14:1 propellant-to-payload ratio for one-way down**.

For a round trip (HLS returns to LEO), the ratio doubles or worse depending on whether ISRU propellant is available at the lunar surface for the ascent leg. This is the "Earth-imports-only" worst case.

If terrestrial LEO propellant costs $107/kg (q1's partial-mid scenario), and 14 tanker flights deliver 1,400 t of propellant per 100 t of lunar-surface payload, then the propellant-cost-only component of lunar-delivered payload is:
- (14 × 100,000 kg × $107/kg) / 100,000 kg payload = **$1,498/kg of payload delivered to lunar surface**, propellant alone.

Reversing the leg (lunar surface to LEO) under Earth-imports-only architecture is even worse: the lunar lander uses its own ascent propellant for return, which was itself launched from Earth. The effective Earth-imports-only lunar-to-LEO delivery cost is therefore not just q1's L_p but approximately Γ_chemical × L_p where Γ_chemical ≈ 14 for round trip — matching Metzger 2023's Γ_LEO figure.

## limitations

- Operational metrics from sources contemporaneous with Starship's pre-operational phase; subject to revision once Starship operates at scale
- Tanker-flight count is the most uncertain variable; doubling that number doubles the propellant cost component
- 100 t lunar-surface payload assumes mature Block 2 Starship; early Block 1 likely much less
