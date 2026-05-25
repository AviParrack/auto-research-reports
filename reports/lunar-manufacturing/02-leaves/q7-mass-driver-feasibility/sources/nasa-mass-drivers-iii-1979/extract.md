---
slug: nasa-mass-drivers-iii-1979
title: "Mass Drivers III: Engineering (1977 NASA Ames Summer Study)"
url: "https://nss.org/settlement/nasa/spaceres/III-3.html"
fetched: 2026-05-25
fetcher: claude
tier: S
type: report
peer_reviewed: true
venue: "NASA SP-428 Space Resources and Space Settlements"
authors: ["Henry H. Kolm", "Kevin Fine", "Peter Mongeau", "Fred Williams"]
year: 1979
date: 1979-01-01
topics: [mass-driver-historical, em-launch-engineering, capital-cost-mass-driver, lunar-power-budget]
---

## Abstract

The 1977 NASA Ames Summer Study Mass Drivers III chapter (NASA SP-428) presents the canonical Phase II lunar mass driver reference design. Authors are Henry Kolm and the MIT/Princeton mass driver group. The optimized lunar launcher: 10.5 kg payload at 4 Hz (42 kg/sec throughput, ~1.3 Mt/yr at 100% duty cycle), 2,400 m/s lunar escape velocity, 10,000 m/s² (~1000 g) acceleration, 488 m total length, 125 MW power, 96.4% claimed system efficiency. System mass: 3,130 t total (SCRs 50.3 t, drive windings 108 t, feeders 43.3 t, kinetic system 1.69 Mt). Capital cost projection: $3.137 billion (1979 dollars) for a baseline scenario projecting operational capability by mid-1985. The authors identify SCR (silicon-controlled rectifier) packaging as the dominant subsystem challenge and characterize the mass driver as one of three reaction-engine variants studied (the others being interplanetary reaction engines using mass driver thrust). The 96.4% efficiency claim depends on temperature optimization at 400 K rather than 300 K, projecting 32% mass reduction in power/radiator systems. The "$1/lb to L-5" headline from L5 News (Kolm 1980, derivative source) traces to this study's economics.

## Key claims

- design-target: "10.5 kg payloads at 4 Hz launch frequency, 2,400 m/sec velocity (lunar escape speed), and 10,000 m/sec² acceleration."
- length-and-power: "488-meter total length and required 125 megawatts of power."
- claimed-efficiency: "96.4% efficiency" — anomalously high relative to modern coilgun/railgun engineering (cf coilgun Wikipedia <22% for state-of-art).
- system-mass: "Total: 3,130,000 kg." Of which kinetic system (1,690 t) is the bulk, drive windings 108 t, SCRs 50.3 t, feeders 43.3 t.
- capital-cost: "Required $3.137 billion (1979 dollars)" for baseline operational scenario by mid-1985.
- scr-bottleneck: "Current devices carried 'package masses from 50 to more than 1000 times heavier than the silicon wafer masses,' representing a design bottleneck."
- temperature-optimization: "Potential 32% mass reduction in power and radiator systems by operating at 400 K instead of 300 K, though SCR pulse ratings would degrade at higher temperatures."
- operational-target: "Baseline scenario projected operational capability by mid-1985, requiring $3.137 billion and progressing through ground test models culminating in three operational reaction engines and one lunar launcher deployment."

## Reviewer notes

Tier S as a foundational NASA technical report and the canonical Phase II engineering reference. Two load-bearing notes for our calc pass: (1) the 96.4% efficiency claim is roughly 4× higher than what modern coilgun engineering has demonstrated (~22% for a DARPA 45-stage design per Wikipedia), and 2-3× higher than the 33% net efficiency Wright et al. 2011 use as a TRL-grounded estimate. Likely the 1979 efficiency is the drive-coil-to-projectile electromagnetic conversion before power-supply and pulsed-power overhead — useful as a theoretical ceiling but not the system-level efficiency. (2) The 1985 operational target was not met. The $3.137B figure was for a NASA programmatic scenario, not the steady-state amortization of a built system; the L5 News "$1/lb to L-5" derivative claim assumes 10-year operations and 600 kt/yr throughput, so $3.137B / (600 kt × 10 yr) ≈ $0.50/kg amortized, broadly consistent. But the negative-verdict 2011 Wright reanalysis using TRL-grounded subsystems should be the primary anchor over the 1979 optimism. The 1979 SP-428 figures are the lower-bound theoretical ceiling, not the realistic capital projection. Spawn tree-pass item: tension between 1979 and 2011 NASA conclusions on mass driver feasibility.
