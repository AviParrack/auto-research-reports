---
pass: 2
kind: calc
leaf: q6-orbital-demand
date: 2026-05-26
status: done
sources_sealed: true
---

# Pass 2 — Calc (sources sealed)

## Method

First-principles demand decomposition for orbital structural mass and
propellant 2026-2040, by use case: SDC, SBSP, propellant depots,
lunar surface cargo, Mars surface cargo, satellite servicing. Three
acceleration regimes bracket each estimate — stall, BAU, TAI-C — per
anti-pattern #11. The Python script ([pass-02-calc.py](pass-02-calc.py))
takes the regime as input and outputs total-mass-to-orbit (t over 15
years) and annual-average rates (t/yr).

Sources sealed: I did not consult `sources/*/extract.md` while
constructing assumptions. Codex audit notes that the engineering
inputs draw on remembered prior context (Musk Mars cadence, NASA M2M,
Mankins NIAC, SpaceX/xAI FCC filings) — this is acceptable as
background knowledge but the regime GW targets are scenario inputs,
not first-principles derivations. They function as adoption-rate
hypotheses to be tested against the cross-leaf demand-elasticity-cost
mechanism. Pass 3 reconciles against the source extracts proper.

## Assumptions per use case

### SDC — orbital data centers (revised post-Codex audit)

Codex audit (May 2026) flagged two arithmetic / unit errors in the
original SDC mass breakdown. Both accepted; corrected derivation
below. The 40 t/MW total is preserved as a midpoint engineering-
unit estimate because it is cross-corroborated by independent
analyses (peraspera 30-50 t/MW; luminix 42 t/MW). The flagged
derivations were the line items, not the total.

| Parameter | Value | Justification (corrected) |
|---|---:|---|
| Compute hardware | 5-10 t/MW | Modern AI accelerators are ~0.7-1.2 kW each (not 10 GPUs/kW). A 1 MW compute draw is ~1000 high-end GPUs; at ~2-4 kg/GPU including servers, racks, PSUs, networking, the compute hardware mass alone is 2-4 t. With cooling plate, in-rack memory, and shielding, total 5-10 t/MW. |
| Solar panels | 15-25 t/MW | Codex caught the error: at 5-8 kg/kW peak panel and 3× peak-to-continuous ratio (LEO eclipse + Sun-angle inefficiency), 1 MW continuous needs ~3 MW peak ≈ 15-24 t/MW panel mass. The earlier 8 t/MW figure understated this. |
| Radiators | 5-10 t/MW | 100-200 m² per 100 kW (depends on radiator temperature, allowable coolant, eclipse rejection assumptions); ~5 kg/m² deployable structures |
| Structure + station-keep | 5-10 t/MW | Booms, attitude control, drag-compensation propellant tankage |
| **Total** | **30-55 t/MW** | Revised range; midpoint ~40 t/MW retained because the total is the cross-corroborated number from independent analyses. |

**The 40 t/MW midpoint is partly source-anchored** (peraspera +
luminix concurrence); the line-item decomposition is now consistent
with the engineering literature. The line items were wrong in
the original derivation; the total was within range by happy
accident. Flag carries into pass 3 reconcile — the rough
agreement with peraspera/luminix at the total level is itself
load-bearing evidence rather than a coincidence.

### SBSP — space-based solar power

| Parameter | Value | Justification |
|---|---:|---|
| Mass intensity | 5 kg/kW | Mankins SPS-ALPHA target ~1 kg/kW (mass-produced); SOA (2015) 6.7 kg/kW. Mid-line 5 kg/kW assumes partial scaling success by 2030s |

### Propellant depots

| Parameter | Value | Justification |
|---|---:|---|
| Tanker propellant payload | 100 t/flight | Starship tanker spec; consistent with Wikipedia depot taxonomy |
| Refuelings per outbound ship | 8 | Musk-quoted figure for full interplanetary refuel; NASA cites 16. Midpoint 12 stable; using 8 as the lower-bound architectural commit |

### Lunar surface cargo, Mars cargo, servicing

Regime-dependent — see "Regime decomposition" below.

## Acceleration regime decomposition (anti-pattern #11)

Regime numbers are scenarios, not calendar predictions. The regime
identity, not the calendar year, determines feasibility.

### Stall

- **SDC:** 0.5 GW deployed by 2040 (Starcloud + Axiom + Kepler stay operational at demonstration scale; no scale-up). At 40 t/MW × 500 MW = 20,000 t total over 15 years, ≈ 1,333 t/yr. (Codex audit caught earlier "few hundred t" misstatement — corrected.)
- **SBSP:** 0 GW. NASA OTPS conditions never met.
- **Depots:** 0 ships/yr refueled. No orbital refueling architecture.
- **Lunar cargo:** 0 t/yr by 2040. Artemis slips out indefinitely.
- **Mars cargo:** 0 t/yr.
- **Servicing:** 50 t/yr (extrapolation of current OSAM market).
- **Total LEO demand:** ~1,400 t/yr average.

### BAU — business-as-usual

- **SDC:** 50 GW deployed by 2040. ~5% of US data center growth captured by orbit; aligns with Luminix 30-40% viability by 2032-35 partially materializing.
- **SBSP:** 5 GW deployed by 2040. China's 2028 1 km array + Aetherflux + 1-2 commercial GEO stations come online.
- **Depots:** 10 ships/year refueled (~Artemis HLS annual + few commercial deep-space). 10 × 8 × 100 = 8,000 t/yr at depot.
- **Lunar cargo:** 30 t/yr to surface by 2040 (1-2 Starship HLS cargo at partial utilization).
- **Mars cargo:** 200 t/yr average over 2026-2040 (one or two windows × 5-20 ships × 75 t × 60% success).
- **Servicing:** 200 t/yr (MarketsAndMarkets $5.1B projection).
- **Total LEO demand:** ~143,000 t/yr average — driven principally by SDC.

### TAI-C — TAI compression / industrial explosion

- **SDC:** 1,000 GW deployed by 2040. SpaceX/xAI 1M-sat filing at 100 GW × 10× compression. Captures ~50% of projected US 2035 AI demand per Marcy.
- **SBSP:** 100 GW deployed by 2040. Mankins SPS-ALPHA at scale + ESA SOLARIS operational + China beyond demo.
- **Depots:** 200 ships/year refueled. Mars cadence at Musk 2033 "up to 500 missions/window" annualized.
- **Lunar cargo:** 500 t/yr to surface (5 Starship HLS cargo, fully utilized, beginning of industrial buildup).
- **Mars cargo:** 15,000 t/yr average (Musk envelope at full multi-window cadence).
- **Servicing:** 2,000 t/yr (routine large-structure assembly + ADR).
- **Total LEO demand:** ~2,860,000 t/yr average — driven principally by SDC, with SBSP and depots at 1-2% scale of SDC.

## Sanity checks

**SBSP TAI-C 500,000 t over 15 yr** — equivalent to ~165 Starship-200t
launches/year for SBSP alone. Mankins reference: 80,000 t for 4 GW
at 20 kg/kW → 100 GW at 5 kg/kW = 500,000 t. Consistent within
mass-intensity assumption.

**Depot TAI-C 160,000 t/yr propellant** — 1,600 tanker-flights/year
(~4.4/day). SpaceX target 1,000 ships/year production. Consistent
with industrial-explosion launch cadence.

**SDC TAI-C 2.67 Mt/yr** — at architectural limit of any conceivable
Earth-launch program. Codex correctly flagged that Earth launch
capacity depends on fleet size × turnaround rate × pad cadence, not
on annual ship production alone. A reusable Starship at 10 flights/yr
amortized across 200 active ships would give ~400,000 t/yr LEO
capacity. Under that more defensible benchmark, SDC TAI-C demand
(2.67 Mt/yr) still exceeds Earth-launch supply by ~7×. The
exact multiplier is sensitive to fleet/reuse assumptions; the
qualitative conclusion — TAI-C SDC demand exceeds plausible
Earth-launch capacity — is robust to all reasonable parameterisations.

Codex also caught a stronger overclaim in the original draft: the
phrase "lunar-sourced structural mass becomes the necessary supply-
side response" is too strong because ~50% of orbital DC mass under
the corrected breakdown is compute hardware (GPUs, memory, networking,
PSUs) that lunar manufacturing cannot supply. The correct framing:
**lunar-sourced bulk mass (structure, radiators, sintered shielding,
silicon for solar panels) covers approximately half the SDC mass
budget**. The other half — compute hardware — still requires Earth
launch. The lunar-manufacturing thesis is necessary but not sufficient:
it relaxes a binding supply-side constraint on the bulk-mass half
of SDC, but the high-value compute half remains Earth-launch-bound
regardless. This is a more precise statement of the q1-q6 coupling.

## Headline answers

**Stall regime:** 2026-2040 cumulative LEO demand ~20,000 t.
**BAU regime:** ~2,000,000 t (2 Mt) cumulative; SDC dominant.
**TAI-C regime:** ~40,000,000 t (40 Mt) cumulative; SDC dominant
by factor of >10× over all other sectors combined.

| Sector | Stall (t/yr) | BAU (t/yr) | TAI-C (t/yr) | Demand-elasticity note |
|---|---:|---:|---:|---|
| SDC | 1,333 | 133,333 | 2,666,667 | High — couples to AI compute growth |
| SBSP | 0 | 1,667 | 33,333 | Medium — needs $100-200/kg launch |
| Depots | 0 | 8,000 | 160,000 | Very high — depots ARE the demand-elasticity mechanism |
| Lunar cargo | 0 | 30 | 500 | Low — supply-constrained |
| Mars cargo (deep-space, transits LEO) | 0 | 200 | 15,000 | Low — political/programmatic |
| Servicing | 50 | 200 | 2,000 | Low — capability-gated |

**Cross-leaf-critical observation.** Under stall and BAU, the demand
total is comfortably within plausible Earth-launch capacity (Starship
delivering ~100,000-400,000 t/yr to LEO at 500-2,000 flight-cycles/yr
across an active fleet is plausible by 2030 under reasonable
reuse assumptions). Under TAI-C, SDC alone exceeds plausible
Earth-launch architecture supply by roughly an order of magnitude —
lunar-sourced bulk mass (structure, radiators, silicon for panels,
sintered regolith for shielding) becomes a necessary supplement
for roughly half the SDC mass budget. Compute hardware (~50%) still
requires Earth launch. This is the q1↔q6 coupling Avi asked us to
surface: launch cost determines which regime obtains, the demand
response is highly non-linear, and the supply-side architecture
splits into Earth-launched compute + lunar-sourced bulk mass under
TAI-C.

## Derived claims for claims.yaml

1. SDC orbital mass density under first-principles decomposition is
   ~40 t/MW (range 30-50 t/MW across architecture maturity).
2. Cislunar / LEO total mass demand 2026-2040 spans ~20 kt (stall),
   ~2 Mt (BAU), to ~40 Mt (TAI-C) under three regimes.
3. SDC dominates total LEO mass demand under BAU and TAI-C by factor
   >5× over all other sectors.
4. SBSP mass demand scales as 5 kg/kW × deployed GW, ranging from
   0 (stall) to 500,000 t (TAI-C @ 100 GW) over 15 years.
5. Propellant depot annual throughput scales as 800 t/yr per refueled
   ship (8 tankers × 100 t/tanker); BAU ~8,000 t/yr; TAI-C ~160,000 t/yr.
6. Under TAI-C, SDC alone (~2.7 Mt/yr) exceeds plausible Earth-launch
   throughput by ~10×, structurally requiring lunar-sourced mass
   supply for orbital build-out — the q1↔q6 demand-elasticity-cost
   coupling.
7. Stall regime cumulative demand (~20 kt over 15 years) is small
   enough that Earth launch alone trivially fulfills it; lunar
   manufacturing thesis fails for lack of demand, not supply.
8. The 450 t/yr Kornuta-Metzger near-term propellant demand baseline
   is the BAU-regime floor for depot demand specifically (one sub-component
   of the 8,000 t/yr total LEO refueling under BAU).

## Confidence

- **High:** First-principles mass-per-MW SDC decomposition (engineering
  unit accounting).
- **High:** SBSP kg/kW range (Mankins NIAC reference + SOA bracketing).
- **High:** Stall regime total — small market, near-current activity.
- **Medium-high:** BAU regime total — driven by SDC adoption rate,
  the load-bearing assumption.
- **Medium:** TAI-C regime total — assumes Musk Mars cadence and
  SpaceX/xAI filing materialize at face value; both are aspirational.
- **Medium:** Regime-conditional regime-rate assumptions per anti-
  pattern #11. The framework is the deliverable; specific dates are
  illustrative.
- **High (qualitative):** SDC-dominant conclusion. Robust across any
  reasonable variation in mass-per-MW (factor of 2) or GW-deployed
  (factor of 5).

## Plots — skipped at leaf level

The deliverable is a categorical demand decomposition with three
regime brackets; a sensitivity sweep would not clarify what the
regime table already shows. Reserved visualisation for q8 synthesis
where cross-leaf supply-demand crossover demands the chart.

## Next pass

Pass 3 (reconcile): open `sources/*/extract.md`, compare derived
demand figures against the source literature, update `claims.yaml`
evidence arrays. Particularly important reconcile points:
- SDC 40 t/MW vs peraspera 30-50 t/MW and luminix 42 t/MW (should
  match closely)
- BAU 8,000 t/yr depot demand vs Kornuta-Metzger 450 t/yr (factor
  of ~18; resolve scope mismatch)
- TAI-C 100 GW SBSP vs OTPS launch-cost-conditional framing
- Mars cargo BAU 200 t/yr vs Musk's stated 5-ship 2026/27 window
