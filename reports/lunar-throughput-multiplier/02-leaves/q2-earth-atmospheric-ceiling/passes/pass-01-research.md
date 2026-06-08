---
leaf: q2-earth-atmospheric-ceiling
pass: 01-research
started: 2026-06-09T02:30:00Z
ended: 2026-06-09T02:50:00Z
researcher: claude-opus-4-7
---

# Pass 01 — Research

Source gathering for q2 (Earth atmospheric ceiling). Five tier-S/A primary sources retrieved fresh; emission factors and current-cadence-impact baselines established.

## Tier-grouped source list

### Tier S — peer-reviewed primary
| Slug | Source | Bears on |
|---|---|---|
| `revell-2025-ozone` | Revell et al. 2025, *npj Climate Atmos. Sci.* | Launch-rate → ozone depletion scenarios (884 / 2,040 /yr → −0.17% / −0.29% global, −3.9% Antarctic spring) |
| `murphy-2023-pnas` | Murphy et al. 2023, *PNAS* 120(43) | 10% of stratospheric aerosol particles already contain spacecraft metals; projected to 50% within decades |
| `maloney-2025-alumina` | Maloney et al. 2025, *JGR Atmospheres* | 10 kt/yr alumina at 2040 60k-satellite cadence; +1.5°C polar mesospheric warming; polar vortex disruption |
| `ryan-2022-emissions` | Ryan et al. 2022, *Earth's Future* 10(6) | Canonical per-propellant emission factors (kerosene, hypergolic, LH2, solid); 500× BC potency in stratosphere |

### Tier A — peer-reviewed reviews / credentialed preprints
| Slug | Source | Bears on |
|---|---|---|
| `kukreja-2025-megaconstellation` | Kukreja/Oughton/Linares 2025 arXiv (MIT/GMU) | Megaconstellation LCA framework; 42% of 2030 space-sector climate impact from 2019+ launches |

### NOT YET FETCHED (flagged for re-pass)
- NASA TM-20240013276 *Impact of Spaceflight on Earth's Atmosphere* — PDF fetch returned binary streams; needs HTML alternative or alternative NTRS doc.
- Barker et al. 2026 *Earth's Future* on megaconstellation radiative forcing — paywalled (402).
- Direct fetch of Maloney 2025 JGR (only NOAA CSL secondary coverage retrieved).

## Topics surfaced (add to topics.yaml at report level)

- `rocket-ozone-depletion` — direct ozone destruction from chlorine (SRM), black carbon (kerosene), NOx (reentry)
- `stratospheric-water-vapor` — H2O from methalox/LH2 combustion at stratospheric altitudes; HOx-cycle ozone effects
- `reentry-alumina-mesosphere` — Al2O3 from spacecraft ablation 40-70 km; polar mesospheric heating; polar vortex effects
- `propellant-specific-emissions` — per-kg emission factors by propellant type (Ryan 2022 canonical)
- `polar-stratospheric-clouds` — alumina/metals nucleation effects on PSCs (Murphy 2023, Maloney 2025)

## Methalox-specific gap

**The peer-reviewed literature lacks dedicated atmospheric modeling for a pure-methalox future.** Revell 2025 explicitly notes methalox as a research gap. Ryan 2022's emission-factor table omits methalox (we can derive it from stoichiometry: 0.6 kg CO2 + 0.49 kg H2O + ~10 g NOx + minimal BC per kg propellant). At Starship-dominated cadence the ozone and aerosol picture should differ substantially from the Revell-2025 mixed-fuel projection — no chlorine, dramatically less BC, no alumina from combustion (alumina from reentry of payloads remains, however).

This is a real research gap. q2's calc pass must derive the methalox-specific atmospheric ceiling first-principles.

## Coverage assessment

- **Tier S is good:** 4 primary peer-reviewed papers covering the four main atmospheric impact pathways (direct ozone, stratospheric H2O, reentry alumina, propellant emission factors).
- **Tier A coverage thin:** Kukreja 2025 covers the LCA frame but not specific cadence-thresholds. Could add IPCC AR6 Chapter 8 (atmospheric composition) for general radiative-forcing context.
- **Tier B (public figures):** Casey Handmer, Eli Dourado, Eloise Marais (academic atmosphere specialist) all have public positions. None directly compiled here; could be a re-pass target.
- **Tier C/D:** Industry trade coverage (Space.com, Phys.org) consolidates the same primary findings — not separately reviewed in the current pass.

## Sub-pass deliverables

- 5 extract.md files in sources/ (all tier S/A)
- 1 pass-01-research.md (this file)
- 0 entries in claims.yaml — claims come from calc + reconcile

## Anti-pattern hygiene check

- No claim-bearing prose in this pass ✓
- No source borrowing across passes yet — calc-pass will be sources-sealed ✓
- All extracts have proper frontmatter (tier, type, peer_reviewed, venue, year, topics) ✓
- No hallucinated sources — every extract corresponds to a fetched WebFetch or PMC retrieval ✓

## Next sub-pass

Calc — derive Earth atmospheric ceiling first-principles, sources sealed. Apply lessons from q1: distinguish *fundamental* (atmospheric absorption capacity, ozone destruction rate per unit injection, irreversible thresholds) from *willingness-to-pollute* (current-cadence projections that scale linearly until they don't).
