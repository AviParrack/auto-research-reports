---
slug: metzger-2023
title: "Economics of In-Space Industry and Competitiveness of Lunar-Derived Rocket Propellant"
url: https://arxiv.org/abs/2303.09011
pdf: https://arxiv.org/pdf/2303.09011
journal: Acta Astronautica
year: 2023
month: March
authors: ["Philip T. Metzger"]
affiliation: Florida Space Institute, University of Central Florida
fetched: 2026-05-25
fetcher: claude
type: paper
---

# Metzger 2023 — gear ratio & production mass ratio framework

The canonical economic treatment of lunar resource competitiveness. Develops the "spherical cow" model with two dominant variables: gear ratio on cost (G) and production mass ratio (φ). Concludes lunar propellant production will be commercially viable. Refutes the Charania-DePascuale and Jones et al. pessimistic conclusions by showing they made transportation architecture and capital-mass errors.

## abstract

> Economic parameters are identified for an in-space industry where the capital is made on one planet, it is transported to and teleoperated on a second planet, and the product is transported off the second planet for consumption. This framework is used to model the long-run cost of lunar propellant production to help answer whether it is commercially competitive against propellant launched from Earth. The prior techno-economic analyses (TEAs) of lunar propellant production had disagreed over this. The "gear ratio on cost" for capital transport, G, and the production mass ratio of the capital, φ, are identified as the most important factors determining competitiveness. The prior TEAs are examined for how they handled these two metrics. This identifies crucial mistakes in some of the TEAs: choosing transportation architectures with high G, and neglecting to make choices for the capital that could achieve adequate φ. The tent sublimation technology has a value of φ that is an order of magnitude better than the threshold for competitiveness even in low Earth orbit (LEO). The strip mining technology is closer to the threshold, but technological improvements plus several years of operating experience will improve its competitiveness, according to the model. Objections from members of the aerospace community are discussed, especially the question whether the technology can attain adequate reliability in the lunar environment. The results suggest that lunar propellant production will be commercially viable and that it should lower the cost of doing everything else in space.

## key concepts

### gear ratio on cost — Eq. 6

```
G = (L_K × G_{K,LEO-LS}) / L_p
```

- L_K = cost per kg of launching capital from Earth to LEO
- G_{K,LEO-LS} = mass gear ratio from LEO to lunar surface for the capital transport vehicle (from Tsiolkovsky)
- L_p = cost per kg of launching terrestrial propellant from Earth to LEO

Reduces to ordinary "gear ratio on mass" when L_K = L_p (same launch vehicle for both capital and competing propellant).

### production mass ratio — definition

```
φ = M_{p,LS} / M_K
```

- M_{p,LS} = total mass of propellant produced at lunar surface over the life of the capital
- M_K = mass of the capital

i.e. how many kg of product each kg of capital produces across its lifetime.

### the competitiveness condition — Eq. 8

```
[(x + G) φ^(-1) + ω + ξ] · Γ_X < 1
```

Where:
- x = launch-normalized equipment cost (ζ/L_p)
- ω = launch-normalized operations cost (λ/L_p)
- ξ = launch-normalized finance cost (f/L_p)
- Γ_X = G_{LS-X}/G_{LEO-X} = propellant use ratio for delivery to location X

When this inequality holds at destination X, lunar propellant has **absolute** advantage over Earth-launched propellant at X.

### launch-normalized capital cost — Eq. 9

```
χ = (x + G) φ^(-1)
```

### pre-delivery cost ratio — Eq. 10

```
ψ_X = (χ + ω + ξ) · Γ_X
```

Lunar wins at X when ψ_X < 1, i.e. ψ_0 < 1/Γ_X.

## numerical values — model baseline

| Parameter | Baseline value | Notes |
|---|---|---|
| L_0 (launch cost year 0) | $2,000/kg | Falcon 9 2022 |
| L_30 (target year 30) | $30/kg | Optimistic Starship with full reuse + cadence |
| τ_L (launch cost decay constant) | 4.67 years | exponential decay model |
| U_30 (year-30 annual up-mass) | 436,000 t/y | ~8 Starship launches/day at 150t |
| G baseline | 6 | RLL as tug LEO→LS, L_K = L_p |
| G alternative (full Starship arch) | 15 | 15 Starship flights to deliver 150t to LS |
| G alternative (Starship→EML1 + RLL) | 8.5 | Mixed architecture |
| G_p,LEO-LS (propellant delivery) | 10 | With refueled Starship |
| G_p,LEO-LS (with OTV) | 7 | OTV LEO-EML1 + RLL EML1-LS |
| I_sp baseline RLL | 450 s LOX/LH2 | |
| I_sp SEP option | 1000-4000 s (uses 2000) | molecular water |
| IMF baseline RLL | 0.10 | |
| Discount rate start | 21.7% | per Charania-DePascuale |
| Discount rate year 30 | 12% | Linear decline |
| Buildup period | 5 years | Baseline |
| R_0 (baseline reliability) | 0.78 | |
| E_R | 0.5 | Stanchliff et al. |
| Wright's Law b | 0.75 | Conservative for new industry |
| EOS exponent a | 0.66 | Haldi-Whitcombe |
| X_max | 10-20 t/day | Firm-level EOS limit |
| Metals industry start | Year 10 | Linear β ramp to 0.3 by year 15 |

## Table 2 — φ values per extant TEA studies

| Mining method | Study | φ |
|---|---|---|
| Tent sublimation | Kornuta et al. (K) | **442** |
| Tent sublimation | Sowers (S) | **534** |
| Borehole sublimation | Pelech (P) | 16.1 |
| Strip mining | Charania-DePascuale (CD) | 26.5 |
| Strip mining | Jones et al. (J) | 22.2 |
| Strip mining | Bennett et al. (B) | 43.4 |
| Strip mining | Pelech (P) | 3.7 |
| Beneficiation (Metzger MVP) | Metzger (M) | **36.5** |
| Baseline model (chosen mid-range) | — | 167 |

The "≳35× threshold" commonly cited as "the gear ratio threshold" is approximately Metzger's MVP value (36.5) — the φ at which his Minimum Viable Product technology achieves absolute advantage at GTO. It's not a universal threshold; the actual threshold for absolute advantage at location X depends on Γ_X (delta-v to X) and the other cost terms.

## Table 1 — years until lunar absolute advantage (baseline)

| Location | Optimistic (D_30 = 100%) | Moderate (10%) | Pessimistic (1%) |
|---|---|---|---|
| LS (lunar surface) | 1 | 1 | 1 |
| LLO | 1 | 1 | 1 |
| EML1 | 1 | 1 | 1 |
| GEO | 2 | 2 | 2 |
| DRO | 3 | 3 | 3 |
| GTO | 6 | 7 | 7 |
| LEO | 19 | 21 | 23 |

**Note:** market size has surprisingly weak effect on competitiveness — even a 100× smaller market only delays LEO crossover by ~4 years. The crossover times for everywhere except LEO are essentially market-insensitive.

## Table 3 — parameter elasticities (cost ratio ψ_0) as function of G/x

| G/x | M_{p,LS} | M_K | ζ | G | IMF | I_SP | L_0 |
|---|---|---|---|---|---|---|---|
| 0.02 | -0.990 | 0.983 | 0.973 | 0.011 | 0.005 | -0.023 | -0.947 |
| 1 | -0.990 | 0.710 | 0.432 | 0.277 | 0.120 | -0.614 | -0.692 |
| 50 | -0.990 | 0.982 | 0.024 | 0.958 | 0.437 | -2.116 | -0.040 |

**Crucial insight:** when G/x is large (capital transport dominates equipment cost), the lunar propellant cost becomes **insensitive to launch cost L_0**. This means Starship dropping launch prices doesn't undercut a properly-designed lunar mining operation — it actually helps lunar (because both terrestrial competitor AND lunar capital costs drop together, but lunar wins on physics).

Design implication: lunar mining firms should engineer to achieve **x < G** so their cost structure is dominated by capital transport, insulating them from terrestrial price wars.

## structural conclusions per TEA reassessment (§6)

| Study | G | φ | Conclusion (after Metzger's reassessment) |
|---|---|---|---|
| Charania-DePascuale (CD) | 64.9 (SLS) | 26.5 | "Two orders of magnitude too high" cost as-published; with commercial G + 5% ice + SEP + 12% PPP rate, gets GTO advantage by year 8 |
| Jones et al. (J) | 41.8 (SLS) | 22.2 | Pessimistic; SLS-based G + low φ + neglected finance/ops |
| Bennett et al. (B) | 5.4 (commercial) | 43.4 | Better than J; reaches DRO by year 16, GTO by year 20 if finance/ops included |
| Pelech (P) | 7.5 (Falcon Heavy) | 3.7 strip / 16.1 borehole | φ too low in both; borehole could reach economic with M_K overestimate corrected |
| Kornuta (K) tent | — | 442 | "Clearly economic and will outcompete other lunar mining methods" |
| Sowers (S) tent | — | 534 | "Clearly economic"; IRR 8.84% commercial; LEO advantage by year 5 |
| Metzger MVP (M) | — | 36.5 | "Still high enough to gain absolute advantage at least to GTO"; 4 satellites/year GTO→GEO from M_K an order of magnitude lower than other studies |

## headline economic claims (verbatim where possible)

- Section 3.1: *"the best payload mass fraction for conventional rocket technology launching off the Earth to GTO is about 2%. For launching off the Moon … the payload mass fraction can be about 48%, or 24 times higher. If this were the only difference between the Earth and the Moon, lunar propellant would be 24 times cheaper than Earth-launched propellant in GTO."*
- Section 3.1: The competitive question reduces to: *"can we (1) transport capital to the Moon, (2) tele-support its operation on the Moon, and (3) work with difficult raw materials in a harsh environment, with a total economic penalty that is less than a factor of 24 so it does not eat up the entire positive margin afforded by the physics?"*
- Section 3.2: *"lunar-derived propellant needs only a comparative advantage, not an absolute advantage"* — because Earth-launched propellant competes against the opportunity cost of launching more lucrative payloads instead.
- Section 5.3: *"Maximizing φ appears to be the dominant strategy for lowering the cost of lunar propellant"*
- Section 5.3: *"Lunar propellant can be insulated from decreasing launch costs by achieving x < G as a capital design goal."*
- Section 6.7: *"All models except J and B indicate that an absolute advantage is gained in GTO no later than year 12. Both tent sublimation studies predict economic viability in LEO from year 5."*
- Section 7: *"With 12% PPP discount rate, all studies except J and B predict absolute advantage in GTO by no later than year 10."*

## structural sensitivities

From the parameter sensitivity analysis (Fig. 10):
- Tripling φ has roughly the same effect as cutting M_K by 3× — both compress the cost curve down
- ζ (fabrication cost rate) is dominant in **year 1** but its importance fades over time as EOS/learning curve operate
- G remains dominant in long run because physics doesn't compress

## relevant for the gear-ratio leaf question

The leaf asks: *what gear ratio threshold must lunar capital achieve, and is it attainable?*

Metzger answers:
1. There's no single threshold; the threshold for absolute advantage depends on destination orbit (Γ_X) and other cost terms.
2. Tent sublimation (φ = 442-534) achieves the threshold at LEO from year 5 with conservative assumptions.
3. Strip mining (φ = 22-44) achieves GTO threshold but struggles for LEO.
4. Metzger's own MVP (φ = 36.5) gets to GTO by year 5 with optimistic market.
5. The threshold is ATTAINABLE with current technology choices, especially tent sublimation. The bottleneck is reliability and ground-truth on lunar ice deposits, not the gear ratio itself.

## what's missing / what to chase in subsequent passes

- Independent first-principles derivation (the calc sub-pass) — verify the φ ≥ 35-ish threshold from physics + capital cost first principles, without consulting Metzger's numbers
- Pelech, Charania-DePascuale, Sowers, Kornuta primary sources — to cross-check Metzger's reassessment quoted above
- Bennett et al. reassessment of Jones — primary source needed
- Post-2023 updates: anything from 2024-2026 that updates these numbers given Starship's actual progress (vs. assumed)
- Sensitivity to "modulo TAI" — Metzger explicitly assumes business-as-usual industrial scaling (Wright's Law b=0.75, EOS a=0.66). What happens if AI/automation collapses MK or compresses the buildup period?
