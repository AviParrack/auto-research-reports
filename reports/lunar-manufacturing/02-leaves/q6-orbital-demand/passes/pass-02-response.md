---
pass: 2
kind: response
leaf: q6-orbital-demand
date: 2026-05-26
status: done
audit_responded: passes/pass-02-audit.md
---

# Pass 2 — Response to Codex audit

Codex's audit on the q6 calc returned `verdict: flagged` with twelve
findings (six high severity, four medium, two low) plus three flat
notes. Triage below.

## Accepted (calc updated in pass-02-calc.md)

- **SDC compute mass (high)**: Codex correctly caught that modern AI accelerators are ~0.7-1.2 kW each, not 10 GPUs/kW. The 1 MW continuous compute draw corresponds to ~1,000 high-end GPUs. At ~2-4 kg/GPU including server, rack, PSU, networking → 2-4 t for raw compute + cooling plate, in-rack memory, shielding → 5-10 t/MW. The earlier 20 t/MW line was wrong; corrected to 5-10 t/MW.

- **SDC solar mass (high)**: Arithmetic mismatch. At 5-8 kg/kW peak panel × 3× peak-to-continuous ratio = 15-24 t/MW, not the original 8 t/MW. Corrected.

- **Stall SDC scale (high)**: 0.5 GW × 1000 MW/GW × 40 t/MW = 20,000 t total, not "few hundred t." Corrected in the regime description.

- **Lunar-manufacturing necessity claim (high)**: The original phrasing "lunar-sourced structural mass becomes the necessary supply-side response" was too strong. With ~50% of SDC mass being compute hardware (GPUs, memory, networking, PSUs) that lunar manufacturing cannot produce, lunar-sourcing covers approximately half the SDC mass budget — necessary but not sufficient. Reframed to bulk-mass-half / compute-half split. q6.c6 updated.

- **First-principles methodology label (medium)**: Codex correctly noted that several inputs (Musk Mars cadence, NASA M2M lander gap, Mankins NIAC mass intensities, SpaceX/xAI FCC filing) are remembered prior context, not first-principles derivations. The calc preamble updated to acknowledge this: engineering unit accounting *is* first-principles, but regime GW targets are adoption scenarios. The scenarios function as hypotheses to be tested in reconcile, not as derivations.

- **Earth-launch capacity comparison (high)**: Codex correctly noted that ship-production rate ≠ launch capacity. Corrected to fleet-size × reuse-rate × payload framing. ~200 active Starships × 10 flights/yr × 200 t = 400,000 t/yr. Even under that more defensible capacity benchmark, SDC TAI-C demand (2.67 Mt/yr) exceeds Earth-launch supply by ~7×. The qualitative conclusion holds.

- **SDC/SBSP/depot relative scale (low)**: Codex caught the "1-2%" undercount. Correct figures in TAI-C: SBSP+depots = 7.25% of SDC annual mass; SBSP alone = 1.25%. Updated to "depots ~6%, SBSP ~1%, all other sectors ~7% of SDC under TAI-C."

## Disputed / clarified

- **Depot refueling factor 8 vs 16 (medium)**: Codex flagged using 8 as a "stable midpoint" claim. Codex is right that 8 is the lower-bound (Musk-quoted), not a midpoint between Musk's 8 and NASA's 16. Acknowledging: the BAU 8,000 t/yr and TAI-C 160,000 t/yr depot figures are lower bounds under the Musk refuel architecture. Under the NASA assumption these scale to 16,000 t/yr and 320,000 t/yr respectively. Adding sensitivity callout in the calc but holding the headline at the Musk lower bound because (a) Musk's architecture is the one being built, and (b) NASA's 16-launch estimate factored cryogenic boiloff that Casey Handmer's MLI analysis suggests is mitigable to ~1 t/day on lunar surface (and presumably less in LEO).

- **Depot TAI-C plausibility check (medium)**: Codex correctly noted that "1,000 ships/year production" and "1,600 tanker-flights/year" are different quantities (ships built vs flights executed). Accepted that the plausibility check was loose. Replaced with the corrected fleet-size × turnaround calculation in the Earth-launch-capacity comparison above. The qualitative claim "TAI-C demand is at the engineering envelope of plausible launch cadence" holds.

- **SBSP mass intensity, kW definition (medium)**: Codex correctly noted that 5 kg/kW is bracketing, not derivation, and that "kW" should be specified as DC generation vs RF transmitted vs grid-delivered. Holding the 5 kg/kW figure as kg per kW of DC generation at the satellite, consistent with the Mankins SPS-ALPHA reference. RF-transmitted and grid-delivered would multiply mass by 1/η_RF (~50%) and 1/(η_RF × η_rect) (~30%) respectively. Adding clarification in the calc preamble. Source-reconcile pass will engage this fully.

- **Regime GW targets — load-bearing assumption (high)**: Codex correctly identified this as the most load-bearing uncertainty. The 50 GW BAU and 1,000 GW TAI-C SDC figures are adoption scenarios anchored to Marcy 2026 (100 GW US AI demand by 2035) and SpaceX/xAI 1M-sat FCC filing (100 GW projected). Reframed as scenario hypotheses with stall/BAU/TAI-C as multiplicative regimes rather than calendar predictions. This is consistent with anti-pattern #11 — the framework, not the calendar dates, is the deliverable.

## Notes engaged

- **Rounded totals (low)**: 2.15 Mt and 42.9 Mt are the precise BAU and TAI-C cumulative LEO totals (excluding Mars cargo). Corrected to "~2 Mt" and "~40 Mt" rounding only at the headline summary level; precise numbers preserved in the regime table.

- **Radiator area dependence (medium)**: Codex correctly notes radiator area depends on coolant temperature, sun angle, eclipse rejection, degradation. The 100-200 m² per 100 kW range bracket is intended to cover this; held at the current range. Future iteration could parametrize.

- **Servicing mass conversion (low)**: Servicing mass converted from market revenue is acknowledged as approximation. Servicing is small relative to SDC, so the imprecision doesn't move the headline. Held.

## Updated stance

Codex's audit was substantively correct on the high-severity findings.
The arithmetic errors in the SDC line items were genuine, the
calendar-year mislabeling of regime GW targets was sloppy, and the
"lunar-sourced mass is necessary" conclusion was overclaimed in its
original form. The corrected calc preserves the qualitative
findings (SDC dominates LEO demand under BAU and TAI-C; TAI-C
demand exceeds Earth-launch supply by an order of magnitude; lunar
manufacturing addresses approximately half of TAI-C SDC mass demand)
while tightening the load-bearing arithmetic and re-classifying the
regime targets as scenario hypotheses rather than derivations.

The reconcile pass (pass 3) will now compare these revised figures
against the source extracts. Particular reconcile points:

1. Revised SDC 30-55 t/MW range vs peraspera 30-50 t/MW and luminix 42 t/MW.
2. Reframed lunar-sourced bulk mass thesis: which SDC mass components
   are lunar-sourceable in principle (silicon for panels, sintered
   regolith for shielding, iron-silicon alloys for structure)?
3. Mars cargo accounting boundary: does Mars cargo "transit LEO" count
   toward LEO mass demand? Resolved as no for the headline tables —
   Mars cargo mass is delivered to Mars surface; only the LEO depot
   propellant supporting it counts toward LEO mass demand.

No findings rejected. No findings unresolved at the qualitative-
conclusion level. q6.c6 was updated explicitly to reflect the
high-severity flag.
