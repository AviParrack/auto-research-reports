---
slug: ryan-2022-emissions
title: "Impact of Rocket Launch and Space Debris Air Pollutant Emissions on Stratospheric Ozone and Global Climate"
url: "https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2021EF002612"
fetched: 2026-06-09
fetcher: claude
tier: S
type: paper
peer_reviewed: true
venue: "Earth's Future 10(6)"
authors: ["Robert G. Ryan", "Eloise A. Marais", "Chloe J. Balhatchet", "Sebastian D. Eastham"]
year: 2022
date: 2022-06
topics: [rocket-emission-factors, propellant-specific-pollution, radiative-forcing-rockets]
---

## Abstract

Ryan et al. (2022) quantified per-fuel-type pollution emission factors and radiative forcing for the 2019 rocket launch fleet plus space-tourism extrapolations. The paper provides the canonical emission factors per kg propellant burned for kerosene/HTPB, hypergolic, liquid hydrogen, and solid fuels. Contemporary 2019 launches produced +3.9 mW/m² radiative forcing (predominantly from black carbon in the stratosphere). Space-tourism extrapolation over 3 years projects +7.9 mW/m². **Black carbon emitted into the stratosphere is approximately 500× more potent per unit mass than ground-source BC** (longer residence time + altitude-amplified radiative effect). Ozone depletion contributors at upper stratosphere (60-90°N, ~40 km): NOx from re-entry heating (51%) and chlorine from solid fuels (49%) — roughly evenly split.

## Key claims

| Propellant | NOx (g/kg) | H2O (g/kg) | BC (g/kg) | HCl (g/kg) | Al₂O₃ (g/kg) |
|---|---:|---:|---:|---:|---:|
| Kerosene / HTPB | 14 | 300 | 35 | — | — |
| Hypergolic | 20 | 550 | 4 | — | — |
| Liquid hydrogen | 33 | 1,000 | 0 | — | — |
| Solid | 3 | 370 | 0 | 4 | 380 |

- methalox-not-in-table: methalox emission factors not explicitly given. Stoichiometric methane combustion gives 0.6 kg CO2 + 0.49 kg H2O per kg propellant (mass balance from CH4 + 2O2 → CO2 + 2H2O).
- BC-500x-potency: stratospheric BC "approximately 500 times more" climate-potent than surface BC.
- ozone-loss-contributors: 51% from re-entry NOx, 49% from solid-fuel chlorine (at 60-90°N, ~40 km, upper stratosphere).
- contemporary-2019-RF: +3.9 mW/m² radiative forcing from 2019 launches.
- space-tourism-3yr-RF: +7.9 mW/m² after 3 years of space-tourism launch cadence.

## Reviewer notes

Tier S, peer-reviewed primary measurement. The emission-factor table is the most-cited canonical reference for propellant-specific atmospheric pollution. Critical for q2's calc: a Starship-dominated future is methalox (closer to LH2 in emission profile minus the higher H2O fraction). Per kg methalox propellant, primary stratospheric emissions are ~500 g H2O + ~600 g CO2 + ~10 g NOx (less than kerosene's NOx); essentially zero BC, zero Cl, zero alumina. **This makes methalox dramatically lower-impact per kg propellant than the current fuel mix Revell 2025 modelled.** Re-entry NOx contribution (51% of ozone loss per Ryan 2022) is propellant-independent — it comes from atmospheric N2 dissociation during reentry heating, not from the propellant itself. Even a fully-reusable methalox Starship still produces re-entry NOx during stage descent.
