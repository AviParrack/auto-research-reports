---
slug: metzger-2023
title: "Economics of In-Space Industry and Competitiveness of Lunar-Derived Rocket Propellant"
url: https://arxiv.org/abs/2303.09011
year: 2023
authors: ["Philip T. Metzger"]
fetched: 2026-05-25
fetcher: claude
type: paper
---

# Metzger 2023 — gear-ratio framework and lunar-propellant competitiveness

The same paper q4 anchored on. Cited here for the q2-relevant pieces: gear-ratio G (cost of moving capital and finished propellant), propellant use ratio Γ (mass of propellant needed to move 1 kg of product to destination), and the architectural assumption about chemical vs SEP delivery on the lunar-product return leg.

## headline-claims-relevant-to-q2

- The propellant use ratio Γ for moving lunar product from lunar surface to **LEO** is approximately **14** under pure chemical reusable round-trip architecture. With SEP (solar-electric propulsion) using water as propellant at Isp ≈ 2000 s on the return leg, Γ_LEO drops to approximately 1.
- For closer cislunar destinations Γ is O(1): LLO ≈ 0.9, EML1 ≈ 1.3, GEO ≈ 1.4.
- The competitiveness inequality is (ω + ξ) · Γ_X < 1, where ω is launch-normalized labor + operations and ξ is launch-normalized finance cost. For LEO with Γ ≈ 14, this requires (ω + ξ) < 0.07 — very tight under realistic financing.
- φ ≥ 35 (production mass ratio) is the threshold for lunar absolute advantage at GTO under Metzger's mid-range cost parameters. Tent sublimation studies report φ = 442 (Kornuta) and 534 (Sowers), well above threshold.

## what-this-implies-for-lunar-to-LEO-cost

Metzger's framework treats the lunar-surface-to-LEO problem indirectly: the cost shows up as the Γ-factor multiplied by terrestrial launch cost L_p. So lunar-to-LEO delivery cost in this model is approximately Γ_LEO · L_p · (architectural overhead factor) — and the Γ_LEO factor itself is what kills pure-chemical LEO delivery in his model.

Under the SEP-return architecture (Γ_LEO ≈ 1), lunar product can be delivered to LEO at approximately the same per-kg cost as terrestrial launch cost — making the architecture choice the dominant variable, not the chemistry of the ascent vehicle.

## limitations-as-q2-input

- Metzger doesn't decompose lunar-ascent-only cost (surface → LLO) separately. The lunar-side ascent ΔV is embedded in his Γ values.
- The model assumes mature lunar industry — not the bootstrap problem of getting the ascent vehicle to the lunar surface in the first place.
- Doesn't model mass drivers explicitly. Mass drivers eliminate the Tsiolkovsky exponential cost by replacing chemistry with electricity, so Γ ≈ 0 for the ascent leg (still need a chemical maneuver to circularize at LLO or transfer to LEO).

## relevance-to-cross-leaf-consistency-with-q1-and-q4

This is the bridge source. q1 derived terrestrial Earth-to-LEO L_p at $59–878/kg over scenarios. q4 used Metzger's φ ≥ 35 threshold. q2 needs to multiply Γ_LEO by L_p in the chemical case, and contrast against the mass-driver case where Γ collapses.
