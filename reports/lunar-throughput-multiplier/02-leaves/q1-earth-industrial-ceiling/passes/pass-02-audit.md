overall:
  verdict: weak
  summary: 'Near-term arithmetic is mostly internally consistent, but the pass is not genuinely first-principles and the high-scale ceiling claims contain major inconsistencies. The LOX-first ordering is plausible under the stated assumptions, while the 10^6-10^8 t/yr and Tt/yr conclusions are under-derived.'

findings:
  - target: 'method.first_principles'
    target_kind: method
    verdict: fail
    reason: 'Many key denominators are borrowed, not derived: US/global oxygen production, US gas consumption, stainless production, electricity generation, Raptor production target, pad count, and Baytown-class ASU capacity. That is acceptable as assumptions, but contradicts the pass framing.'
    severity: high

  - target: 'goal.5_50_100_ceiling_coverage'
    target_kind: completeness
    verdict: fail
    reason: 'The stated goal requires 5%, 50%, and 100% ceilings for each input. Several inputs omit 50% cases, and engines/pads are not expressed as fractions of a defined supply denominator.'
    severity: high

  - target: 'q1.c1'
    target_kind: claim
    verdict: partial
    reason: 'The LOX arithmetic is correct given 5,650 t propellant, O/F 3.6, and 10.3 Mt/yr oxygen supply. But the denominator is industrial oxygen, not necessarily merchant liquid oxygen capacity, storage, transport, or load-rate capacity, so the claimed LOX ceiling may be overstated.'
    severity: medium

  - target: 'assumption.3'
    target_kind: assumption
    verdict: partial
    reason: 'The 3.6:1 methalox mixture ratio is plausible for Raptor-like engines, but it is not stoichiometric; stoichiometric CH4/O2 is 4.0:1 by mass. The numerical impact is small, but the stated physical basis is wrong.'
    severity: low

  - target: 'step2.ng_conversion_comment'
    target_kind: calculation
    verdict: partial
    reason: 'The computed 50,000 scf/t methane is approximately right, but the comment gives garbled units: it should be about 1,400 m3 gas per tonne methane divided by 0.0283 m3/scf, not 1.4 m3/t times 1.42 m3/scf.'
    severity: low

  - target: 'q1.c2'
    target_kind: claim
    verdict: weak
    reason: 'The 2,564 launches/yr calculation follows from 1,000 engines/yr and 39 engines amortized over 100 flights. But both the 1,000-engine target and 100-flight life are borrowed/aspirational, and engine bill-of-material constraints are not analyzed.'
    severity: medium

  - target: 'q1.c3'
    target_kind: claim
    verdict: partial
    reason: 'The pad arithmetic is correct for 50-100 pads at 1-3 launches/day. The claim is still assumption-driven and omits pad refurbishment, deluge water, GSE, local range constraints, methane/LOX loading infrastructure, and site geography.'
    severity: medium

  - target: 'q1.c4'
    target_kind: claim
    verdict: partial
    reason: 'Natural-gas feedstock is correctly shown as non-binding relative to LOX under the stated assumptions. However, rocket-grade LCH4 purification, liquefaction capacity, storage, boiloff, and liquefaction electricity are not included.'
    severity: medium

  - target: 'q1.c5'
    target_kind: claim
    verdict: partial
    reason: 'The reusable steel arithmetic is internally correct if a 275 t stack lasts 100 flights. It omits fleet buildout, attrition, scrap/yield, specific stainless alloy availability, and steel in pads, tanks, ASUs, and GSE.'
    severity: low

  - target: 'q1.c6'
    target_kind: claim
    verdict: supports
    reason: 'The ASU electricity calculation is dimensionally correct: 300 kWh/t times 4,422 t LOX gives about 1.33 GWh/launch, making grid electricity non-binding before LOX capacity. Caveat: this excludes methane liquefaction and some liquid-product/storage losses.'
    severity: low

  - target: 'q1.c7'
    target_kind: claim
    verdict: contradicted
    reason: 'The high-end 100 Mt/yr case equals about 1,000,000 launches/yr. At 100-flight reuse that needs about 390,000 engines/yr, not 10^7, and at 1,000 launches/pad-yr it needs about 1,000 pads, not 10^5.'
    severity: high

  - target: 'q1.c8'
    target_kind: claim
    verdict: weak
    reason: 'The Tt/yr arithmetic is mostly correct, but the "4-5 OOM below" statement contradicts the stated 10^6-10^8 t/yr ceiling, which is only 1-3 OOM below 10^9 t/yr. The impossibility conclusion is plausible but not established by the presented derivation.'
    severity: high

notes:
  - issue: 'Helium is omitted. Starship may use autogenous pressurization, but purge, testing, leak-checking, pneumatic, and ground-system helium demand should be explicitly bounded because helium supply is small and strategically constrained.'
    severity: medium
  - issue: 'Hydrogen is out of scope for a pure methalox Starship analysis, but not for an "Earth chemical rockets" ceiling. Hydrolox alternatives require LH2 production, liquefaction electricity, insulation, boiloff, and large-volume tankage.'
    severity: medium
  - issue: 'Cryogenic insulation, vacuum-jacketed piping, perlite/MLI, tank farms, pumps, valves, and high-flow loading hardware are missing from the industrial-input list.'
    severity: medium
  - issue: 'Avionics, IMUs, flight computers, sensors, batteries, harnessing, and space-rated electronics are omitted. Probably not binding near term, but relevant at 10^5-10^7 launches/yr.'
    severity: low
  - issue: 'Copper and high-temperature alloys are omitted from the Raptor constraint. Combustion chambers, turbomachinery, wiring, power systems, and pad electrical infrastructure could become material at aircraft- or auto-scale engine production.'
    severity: medium
  - issue: 'The analysis mixes US and global denominators: US LOX/grid/gas are used for some ceilings, global oxygen for others, and cosmic-scale ASU power is compared to US electricity despite being framed as an Earth-scale limit.'
    severity: medium
  - issue: 'Ground tests, static fires, chilldown losses, boiloff, scrubbed launches, reserve propellant, and production rejects are excluded, so per-launch propellant and engine demand are optimistic.'
    severity: medium