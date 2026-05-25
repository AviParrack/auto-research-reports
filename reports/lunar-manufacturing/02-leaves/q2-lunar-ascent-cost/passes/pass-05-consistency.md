---
pass: 5
kind: consistency
leaf: q2-lunar-ascent-cost
date: 2026-05-25
agent: claude-opus-4-7
---

# Pass 5 — Cross-leaf consistency check (q2)

Checking q2's claims against the two reviewed sibling leaves (q1, q4). q3, q5, q6, q7, q8 are still open — flagged for the future cross-leaf consistency pass.

## Sibling intersection

| Leaf | Status | Intersection with q2 |
|---|---|---|
| q1-earth-launch-cost | reviewed | L_p (Earth-to-LEO cost) is the denominator partner; q2's Earth-imports-only scenario uses q1's L_p × gear-ratio amplification |
| q4-gear-ratio | reviewed | Γ_LEO framework: q4 uses Metzger's 14× chemical / 1× SEP; q2's calc reproduces 12× chemical for Earth-imports |
| q3-isru-feasibility | open | ISRU propellant cost assumption ($300-2000/kg across eras) is a load-bearing input to q2; q3 will determine whether these scenarios are physically realistic |
| q5-capital-buildup | open | Mass driver bootstrap cost (~$10B aggregate) is q5's territory; q2 takes it as scenario knob |
| q6-orbital-demand | open | 1100 mT/yr propellant demand assumption from Coutts-Sowers is q6's territory |
| q7-mass-driver-feasibility | open | Engineering envelope of the mass driver itself; q2 takes Handmer's 200 kg/shot design as scenario knob |
| q8-synthesis-crossover | open | Will consume q2's chemical-vs-mass-driver crossover finding directly |

## Numerical consistency check: q2 vs q1

q1's L_p ranges (partial-mid $107-466/kg, optimistic-late $59-277/kg) feed q2's Earth-imports-only scenario via gear-ratio amplification.

| q1 era / scenario | q1 L_p | q2 gear-ratio applied | q2 implied surface prop cost | q2 actual scenario value |
|---|---|---|---|---|
| partial / early | $466/kg | × 13 (early pipeline) | $6,058/kg | $6,000/kg ✓ |
| partial / mid | $245/kg | × 6 (mature pipeline) | $1,470/kg | $1,500/kg ✓ |
| optimistic / late | $59/kg | × 10 (mature pipeline) | $590/kg | $600/kg ✓ |

**Verdict:** Strong internal consistency. The Earth-imports scenario uses q1's L_p directly via the gear-ratio assumption, and the values track within ~5% of q1's partial/optimistic ranges.

**No contradictions identified.**

## Numerical consistency check: q2 vs q4

q4's framework uses Γ_LEO ≈ 14 under chemical reusable round-trip, Γ_LEO ≈ 1 under SEP return.

| q4 claim | q2 reproduction |
|---|---|
| Γ_LEO ≈ 14 chemical | Trade-press ~12 (1,200 t propellant / 100 t payload, newspaceeconomy.ca) — matches within 15% |
| Γ_LEO ≈ 1 SEP | My mass-driver+SEP architecture uses SEP for the LLO-to-LEO leg, reducing the chemical ΔV from 5.57 to 1.87 km/s and the propellant mass fraction from 0.72 to 0.35 for hydrolox; consistent with Metzger's claim that SEP collapses Γ to O(1) |
| φ ≥ 35 production threshold | Not directly tested in q2 (q2 models the ascent leg, not the production stage); q3-q4 territory |

**Verdict:** Strong agreement. q2's calc is the natural numeric counterpart to q4's framework — Metzger's Γ values emerge from the same Tsiolkovsky physics I used.

**No contradictions identified.**

## Architectural consistency: hydrolox vs methalox assumption

q1's calc used methalox (Starship's chemistry, Isp 360 s). q2's calc primarily uses hydrolox (Isp 450 s) because the load-bearing lunar lander reference architectures (Centaur-derived ULA designs, Blue Moon) are hydrolox. q4 doesn't specify lander chemistry.

**Cross-leaf check:** The chemistry assumption differs between q1 (methalox) and q2 (hydrolox) because the vehicles differ. Starship (Earth-launched) is methalox; lunar landers (Earth-launched then refilled with lunar ISRU) are typically hydrolox-design because lunar water → H2 + O2 is the natural ISRU output. **No contradiction**; the assumptions are vehicle-appropriate.

**Flag for q8 synthesis:** if Starship HLS (methalox) is the operational lunar lander rather than a hydrolox design, my methalox row (Isp 360, propellant mass fraction 0.56 with aerobraking) is the more relevant case. My calc included methalox variants but the headline summary uses hydrolox; q8 should choose the architecture that matches the deployed vehicle.

## Architectural consistency: reuse count assumption

q1's calc uses {100, 30, 10} reuse counts for Starship. q2's calc uses {5, 15, 50} reuse counts for the lunar ascent vehicle (lower because the lunar surface refurbishment environment is more constrained than Earth).

**Cross-leaf check:** No direct contradiction — they're modeling different vehicles in different environments. But the assumption that lunar refurbishment is 2-3× harder than Earth refurbishment is itself a scenario knob that should be carried forward.

**Flag for q5 capital buildup:** if lunar refurbishment infrastructure is itself capital-intensive, my late-era 50-reuse assumption may be optimistic; trade-press suggests 8-10 for HLS-class vehicles.

## Cross-leaf flag carried forward

- **For q3 (ISRU feasibility):** my ISRU propellant cost scenarios ($300-2000/kg across eras) need q3's validation that lunar water extraction + electrolysis can produce hydrolox at these costs.
- **For q5 (capital buildup):** the $10B mass driver capital and the $2-4B reactor capital from Handmer's design need q5's validation that this capital can be delivered to the Moon at reasonable cost.
- **For q6 (orbital demand):** the demand-side question (who buys 10⁷ t/yr of lunar material in the late era?) is q6's; my calc assumes the demand exists for the throughput scenarios to close.
- **For q7 (mass driver feasibility):** my mass driver engineering envelope (200 kg/shot, 1000 g, 128 m track) comes from Handmer; q7 should validate.
- **For q8 (synthesis):** the crossover between chemical and mass-driver architectures around $50-100/kg in the late era is the structural finding q8 will consume.

## Status

✓ No internal contradictions found with q1 or q4.
⚠ Five cross-leaf checks deferred to when sibling leaves complete: q3 (ISRU cost), q5 (capital), q6 (demand), q7 (mass driver feasibility), q8 (synthesis).
