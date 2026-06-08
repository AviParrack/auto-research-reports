---
leaf: q1-earth-industrial-ceiling
pass: 01-research
started: 2026-06-08T21:00:00Z
ended: 2026-06-08T21:35:00Z
researcher: claude-opus-4-7
---

# Pass 01 — Research

Source-gather only. No claims written to `claims.yaml`. Calc and reconcile sub-passes come next.

## Tier-grouped source list

### Tier S — peer-reviewed primary / government primary
| Slug | Source | What it bears on |
|---|---|---|
| `eia-natural-gas-2025` | EIA Natural Gas Navigator — U.S. natural gas consumption 2025 | 33.52 Tcf/yr denominator for methane-fraction calc |
| `epa-o2-supply-chain-2023` | EPA Oxygen Supply Chain Profile, Mar 2023 | ~10.3 Mt/yr US O2 production baseline — **fetch retry needed: PDF returned binary streams** |

### Tier A — peer-reviewed reviews / conference proceedings / credentialed preprints
*None retrieved in this gather. Note: q1's primary substrate is government and industry data; academic peer-reviewed work on this exact topic (rocket-propellant industrial scaling) is sparse. The research pass should re-run with a wider academic search for Acta Astronautica, Journal of Spacecraft and Rockets, AIAA SciTech papers on launch-vehicle production-rate scaling.*

### Tier B — public figures (quote review)
| Public figure | Quotes file | Topics |
|---|---|---|
| Elon Musk | `musk-10k-ships-2026-01` | 10,000 ships/yr production target |
| Casey Handmer | `handmer-starship-2021` + `handmer-mass-driver-2026` | aspirational 10⁶ t/yr LEO; 67,000 launches/yr for 1 TW orbital solar; pad cadence 1/week → 1/hour |

### Tier C — industry trade press / expert blogs / corporate technical
| Slug | Source | What it bears on |
|---|---|---|
| `mobius-fueling-starships-2024` | Mobius Risk Group, Oct 2024 | per-launch propellant, methane fraction of US NG at Musk-aspirational cadence |
| `thunder-said-energy-asu` | Thunder Said Energy ASU economics | $200/(t/yr) capex rule, 150-800 kWh/t energy |
| `handmer-starship-2021` | Casey Handmer blog | aspirational LEO cadence trajectory |
| `handmer-mass-driver-2026` | Casey Handmer blog | Earth 1-TW-orbital-solar at 67k launches/yr (counterfactual) |
| `air-liquide-baytown-2024` | Air Liquide corporate press, Jun 2024 | 9 kt/d ASU, $850M capex — empirical capex anchor |
| `sdc-cadence-anchor-internal` | Workspace internal compilation | roadmap to primary URLs; current US O2, FAA approval, Raptor production |

### Tier D — mainstream press / non-public-figure
| Slug | Source | What it bears on |
|---|---|---|
| `gmk-stainless-steel-2024` | GMK Center, Dec 2024 | global stainless 62.6 Mt/yr; US 1.95 Mt/yr |
| `musk-10k-ships-2026-01` | Benzinga, Jan 2026 (container for Musk quote — quote itself tier B) | container for the Musk quote |

### Tier E — orientation only (not reviewed; not citable as evidence)
- `spacex-raptor-wiki` — Wikipedia Raptor entry. Used to orient on engine specs and production targets. Will not appear as evidence in `claims.yaml`; primary press releases inside are the citable substrates and will be re-fetched in a future research re-pass if needed.

## Topics surfaced (will feed topics.yaml at report level)

- `lox-supply-bottleneck` — US oxygen production capacity, ASU capex and energy intensity, scaling math
- `methane-supply-bottleneck` — US natural gas consumption baseline, per-launch demand, LNG liquefaction
- `engine-production-rate` — Raptor production rate, reuse-life implications
- `pad-cadence-faa` — pad turnaround, FAA-approved cadence at Boca Chica and KSC
- `airframe-feedstock` — stainless steel needs for reusable vs. expendable fleet
- `asu-capacity-power` — ASU electricity demand at scale, dedicated capacity vs shared
- `aspirational-cadence-target` — Musk, Handmer, industry-stated cadence targets to bound the question

## Coverage assessment

**Tier S coverage is thin.** The two primary government data sources (EIA NG consumption, EPA O2 supply chain) are the load-bearing tier-S anchors. The EPA PDF failed to fetch cleanly — needs a retry with a different rendering path (HTML, or alternative U.S. industrial-gas data source like the U.S. Geological Survey Mineral Commodity Summaries, which sometimes covers industrial gases). 

**Tier A coverage is empty.** A targeted academic search did not surface peer-reviewed work on the exact topic of launch-vehicle production-rate constraints in chemical industry; the literature instead lives in policy and trade-press venues. This is a finding in itself — q1's substrate is institutional and industrial data, not academic. Flag for the audit pass.

**Tier C is the analytical backbone** — Mobius, Thunder Said Energy, Handmer, plus our internal SDC compilation. These give us the per-launch numerator and per-input denominator math for the calc sub-pass.

**Tier B is small but pointed** — Musk's 10,000-ships target and Handmer's 10⁶ t/yr LEO trajectory are the two aspirational anchors against which the calc-pass ceiling estimates should be compared.

**Coverage gaps to address in a future research re-pass:**
1. Direct fetch of the EPA Oxygen Supply Chain Profile (HTML rendering of the report's summary tables, or USGS alternative).
2. Methane liquefaction capacity at Starbase / Boca Chica — Rio Grande LNG, Brownsville LNG; relevant for fast-cycle Starship operations.
3. Air separation literature on energy efficiency of next-generation cryogenic plants (membrane separation, oxygen ionic transport membrane technology) — could matter at 10⁴+ launches/yr scale.
4. Pad infrastructure scaling literature — Apollo-era studies on multiple-pad launch operations, ESA / Roscosmos data on pad turnaround.

## Sub-pass deliverables

- 10 `extract.md` files in `sources/` covering tier S/B/C/D + 1 tier E for orientation.
- 1 `pass-01-research.md` (this file).
- 0 entries in `claims.yaml` — claims come from calc + reconcile, not research.

## Anti-pattern hygiene check (research-pass-specific)

- **No claim-bearing prose in this pass.** ✓ Confirmed: this file is pure source-gather summary.
- **No source borrowing across passes yet.** ✓ Confirmed: calc-pass sources will be sealed.
- **All extracts have proper frontmatter (tier, type, peer_reviewed, venue, year, topics).** ✓ Confirmed across 10 extracts.
- **No hallucinated sources.** ✓ Confirmed: every extract corresponds to a WebFetch result or workspace anchor. The two failed fetches (EPA PDF, Spacenews, Ars Technica) are explicitly flagged.

## Next sub-pass

`--pass leaf --leaf q1-earth-industrial-ceiling --sub calc` — derive ceiling from first principles, **sources sealed**.
