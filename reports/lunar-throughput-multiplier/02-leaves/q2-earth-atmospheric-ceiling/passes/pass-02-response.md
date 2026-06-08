---
leaf: q2-earth-atmospheric-ceiling
pass: 02-response
responding_to: pass-02-audit.md
auditor: codex / gpt-5.5
responder: claude-opus-4-7
---

# Response to Codex audit on q2 pass-02-calc

Codex caught four high-severity issues plus four medium. Most are accepted. The qualitative conclusion (atmospheric chemistry binds well before solar-PV area) holds, but the quantitative ceiling moves up by ~1-2 orders of magnitude.

## Accepted — substantive corrections

- **Reentry NOx 5 kg/kg-reentered (HIGH, contradicted):** Codex cites Larson 2017, Vliex et al. 2024, Ryan 2022 all using **~17.5% of reentered mass** as NOx (0.175 kg/kg) for reusable spacecraft, with 40% for discarded objects. My 5 kg/kg was ~30× too high. Per Block-3 Starship launch at 100 t reentered: **17.5 t NOx** (not 500 t).

- **Catastrophic ozone scaling (HIGH, contradicted):** Larson 2017 modeled 10⁵-10⁶ launches/yr with hydrogen propellant and found **~0.5% global ozone loss at 10⁵ and ~11 DU (~3-4%) at 10⁶ launches/yr** — not the "30-50% ozone loss" I extrapolated. NOx and HOx-cycle catalytic destruction saturates at high concentrations rather than scaling linearly with emissions. My linear extrapolation of Revell 2025 was wrong.

- **Revell 2025 extrapolation (HIGH, unsupported):** Revell's depletion is driven by Cl (from SRMs) and BC (from kerosene), NOT by NOx. Revell explicitly notes rocket-emitted NOx is insignificant in their setup AND they omit reentry NOx. Linear scaling from Revell to a methalox-only future at 10⁵-10⁶ launches/yr is unjustified.

- **NOx perturbation table internal inconsistency (HIGH):** my table said "5% NOx perturbation at ~90 launches/yr" but if 250 launches → 140%, then 5% binds at ~9 launches/yr. Math error in my output.

- **NOx 20 g/kg propellant (MEDIUM):** newer altitude-resolved inventories show NOx EI is altitude-dependent: 33 g/kg at ground falling to <1 g/kg above 14 km. The bulk-stratospheric methalox NOx contribution is much smaller than I claimed.

- **NOx residence-time model (MEDIUM):** NOx is short-lived in the lower stratosphere (days-weeks), not 5 years. My 5-year box-model accumulation is dimensionally wrong for NOx.

- **Stratospheric injection fraction (MEDIUM):** Vliex et al. 2024 splits propellant burn ~20-29% in stratosphere, ~10-19% in mesosphere, balance higher up — not the 50% I assumed.

- **Combustion model (MEDIUM):** fuel-rich methalox produces CO + H₂ intermediates with afterburning, not "5% CO2 deficit + 5% unburned CH4." H₂O figure stays close; CO2 figure may be lower.

## Recomputed q2 ceiling

Anchoring on Larson 2017 (high-cadence H2-propellant scenarios, the closest analog to a methalox-dominant future since both lack chlorine and produce dominant H2O + NOx perturbations):

| Cadence (launches/yr) | Larson 2017 ozone loss | Methalox correction | Operational tier |
|---|---|---|---|
| 10⁵ (~10 Mt/yr LEO) | ~0.5% global | ~similar (H2O dominates both) | **Detectable** |
| 10⁶ (~100 Mt/yr LEO) | ~11 DU = ~3-4% global | ~3-5% global | **Disruptive** (substantial biosphere UV stress) |
| 10⁷ (~1 Gt/yr LEO) | not directly modeled | extrapolating with saturation effects: ~10-30% global | **Catastrophic** (UV catastrophe at high latitudes) |
| 10⁸ (~10 Gt/yr LEO) | far beyond model regime | atmospheric chemistry fundamentally altered | **Beyond ceiling** |

**Recomputed atmospheric ceiling: ~10⁶-10⁷ launches/yr (100 Mt/yr to 1 Gt/yr LEO)** — about 1-2 OOM higher than my original Mt/yr estimate, but still **10-100× lower than q1's solar-PV ceiling at ~100 Gt/yr LEO**.

**The qualitative conclusion holds:** atmospheric chemistry is the load-bearing Earth-side constraint at *any* post-current cadence. Cosmic Tt/yr (10¹² t/yr = 10¹⁰ launches/yr) is *still* unreachable from Earth chemical — atmospheric chemistry binds by 3-4 OOM at cosmic scale.

**Reentry alumina ceiling (Murphy 2023 / Maloney 2025) stays at ~10⁵-10⁶ launches/yr** — but largely driven by aluminum-skinned payloads, not vehicle propellant. With non-Al satellite materials and reusable vehicles, this ceiling is partly architecture-dependent.

## Disputed / clarified

- **Methalox vs fossil/synthetic methane (MED, partial):** my original claim was specifically about synthetic-vs-fossil **methane** combustion being chemically identical. Codex right that it could be misread as methalox-vs-current-fuel-mix (which is dramatically different — methalox eliminates Cl, alumina, and most BC). CLARIFY: synthetic-vs-fossil-methane is identical combustion; methalox-vs-kerosene-SRM is much cleaner. Both true; readers need both.

## What changes in claims.yaml

- q2.c1 — per-launch emissions: reentry NOx corrected from 500 t → 17.5 t (factor 30 lower). H2O figure ~1,400 t stays. NOx propellant figure adjusted with altitude dependence.
- q2.c2 — atmospheric ceiling: shift "disruptive" from 10⁵ launches/yr to 10⁶, "catastrophic" from 10⁶-10⁷ to 10⁷-10⁸.
- q2.c3 — reentry NOx dominant: still load-bearing but with corrected magnitude. At Larson 17.5%, reentry NOx ≈ propellant NOx for methalox at typical reentry mass.
- q2.c5 — Tt/yr still unreachable: holds with corrected numbers. Tt/yr cadence = 10¹⁰ launches/yr, ~3-4 OOM above corrected catastrophic ceiling.
- q2.c6 — atmospheric ceiling vs PV ceiling: q2 still 10-100× lower than q1 (not 1,000-10,000× as I originally claimed). Atmospheric chemistry remains the binding constraint, but by a smaller margin.

## What does NOT change qualitatively

- Earth chemical-rocket throughput is atmospheric-chemistry-bound below the solar-PV-area ceiling.
- Cosmic Tt/yr LEO is unreachable from Earth chemical, primarily on atmospheric grounds (with PV-area as secondary constraint).
- Methalox is dramatically lower per-launch atmospheric impact than the current mixed fuel mix (no Cl from SRMs, much less BC, no alumina from combustion).
- Reentry NOx and reentry alumina are propellant-independent — they come from atmospheric N₂ dissociation and spacecraft material ablation during reentry heating.
- The Moon's architectural necessity for cosmic-scale throughput is established by q2 (atmospheric) + q1 (solar-PV) jointly.

## Next action

Patch pass-02-calc.md with the corrected reentry NOx factor + Larson 2017 anchor + revised ceiling. Then reconcile (now needs Larson 2017 fetched as a source).
