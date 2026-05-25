[codex cli ok]
```yaml
overall:
  verdict: weak
  summary: "Useful sensitivity model, but not an audited estimate. The arithmetic in the Python output is coherent; the prose tables and several conclusions overclaim."

arithmetic_check:
  verdict: contradicted
  notes:
    - "Markdown results table does not match captured stdout or the formula."
    - "Correct stdout values are: optimistic 206/109/64, partial 330/185/117, pessimistic 780/490/354 $/kg for early/mid/late."
    - "Several prose interpretations use a third set of numbers, e.g. partial mid stated as ~$175/kg while stdout is $185/kg."

claims:
  propellant_numbers:
    verdict: weak
    notes:
      - "$1M/launch is plausible as a methalox order-of-magnitude."
      - "But 3,400t is not a full-stack propellant load in FAA-style specs; it is closer to booster-only. FAA draft specs list Super Heavy up to 3,700t and Starship up to 1,500t."
      - "At the model's own prices, 3,400t costs ~$620k; a ~4,800-5,200t full stack costs roughly ~$0.9-1.0M before handling/losses."
      - "Code variable names say KG but values are tonnes."

  falcon9_refurb_scaling_anchor:
    verdict: weak
    notes:
      - "Directionally defensible: public reporting supports early Falcon 9 refurb being far below new-build but still material, and later recovery/refurb claims below 10%."
      - "Exact '30% to 10% over 7 years' is not directly established by the cited public evidence."
      - "Applying Falcon 9 booster economics to the full Starship stack, especially the reentering ship/TPS, is an assumption, not a demonstrated historical anchor."

  reuse_counts_100_30_10:
    verdict: weak
    notes:
      - "Reasonable as a sensitivity sweep, not as proven upper/central/lower bounds."
      - "100 is aspirational; 30 has Falcon 9 booster precedent but not full-stack Starship precedent; 10 may be too high as a true lower bound for early Starship ship reuse."
      - "The model should label these as scenario knobs, not confidence bounds."

  amortization_formula:
    verdict: supports
    notes:
      - "C_hardware / N_reuse is the right basic amortization term."
      - "Strict lifetime-average refurbishment is closer to ((N-1)/N) * r * C_hardware unless r is treated as a per-flight accrual/reserve."
      - "The formula omits separate booster/ship lifetimes, spares, failures, financing, fixed infrastructure amortization, and development-cost recovery."

  musk_10kg_requires_near_zero_margin:
    verdict: contradicted
    notes:
      - "From the stdout model, best stated case is ~$64/kg internal cost. Zero margin gives ~$64/kg, not $10/kg."
      - "Even the speculative automation case at ~$15-25/kg would need either further cost reduction or negative-margin pricing to hit $10/kg."
      - "Defensible conclusion: $10/kg is not derivable from these assumptions. Not defensible: near-zero margin alone gets there."

  anti_pattern_check_passes:
    verdict: contradicted
    notes:
      - "The derivation overclaims in several places."
      - "'Most defensible 2030-2035 central estimate' is not proven by the model."
      - "'No improvement over Falcon 9' mixes Starship internal/list estimates with Falcon 9 list/internal comparisons."
      - "'Falcon 9 list prices rising $500/kg/year' should be narrowed to rideshare pricing, not Falcon 9 pricing generally."
      - "'Sources sealed' is only partly true: Musk/Citigroup targets may be sealed, but Musk-derived reuse/propellant anchors appear in the assumptions."

derived_conclusions:
  refurbishment_dominates_high_reuse:
    verdict: supports
    notes: "Within this model, yes. At 30+ reuses, refurbishment dominates hardware amortization unless r falls sharply."

  below_100kg_requires_refurb_under_5pct:
    verdict: weak
    notes: "True for the 30-reuse/100t central-style case. Not universally true: optimistic late is already below $100/kg at 8% refurb in stdout."

  partial_scenario_as_central_2030_2035:
    verdict: unsupported
    notes: "Plausible scenario, but no probability argument or operational evidence makes it 'most defensible'."

  pessimistic_no_improvement_over_falcon9:
    verdict: weak
    notes: "Could be near Falcon 9 internal economics, but likely below current Falcon 9 public list $/kg if payload is well utilized."

sources:
  faa_starship_pea: "https://www.faa.gov/sites/faa.gov/files/space/stakeholder_engagement/spacex_starship/Draft_PEA_for_SpaceX_Starship_Super_Heavy_at_Boca_Chica.pdf"
  nasa_propellant_costs: "https://ntrs.nasa.gov/api/citations/20205003646/downloads/NASA_TP_20205003646_interactive.pdf"
  eia_henry_hub: "https://www.eia.gov/dnav/ng/hist/rngwhhdD.htm"
  shotwell_2017_refurb: "https://www.airandspaceforces.com/refurbished-spacex-booster-less-than-half-the-cost-of-new-rocket/"
  musk_2020_refurb_reporting: "https://www.inverse.com/innovation/spacex-elon-musk-falcon-9-economics"
  falcon9_reuse_record_2026: "https://spaceflightnow.com/2026/03/30/falcon-9-booster-to-fly-for-record-34th-time-on-starlink-delivery-mission/"
  spacex_falcon9_price_2026: "https://www.spacex.com/assets/media/Capabilities%26Services.pdf"
  rideshare_price_2026: "https://newspaceeconomy.ca/2026/02/27/spacex-rideshare-pricing-as-of-february-2026-what-it-costs-what-s-included-and-how-buyers-budget-a-mission/?amp=1"
```