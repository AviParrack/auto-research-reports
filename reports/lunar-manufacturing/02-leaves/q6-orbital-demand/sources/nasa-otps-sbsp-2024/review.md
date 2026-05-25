---
source: nasa-otps-sbsp-2024
tier: S
reviewed_pass: 4
reviewed_by: claude+gpt
---

# Source Review: NASA OTPS — Space-Based Solar Power (Jan 2024)

## Summary

| Verdict | Count |
|---|---|
| Consistent | 3 |
| Different conclusion | 1 |
| Merits investigation | 1 |
| Not relevant | 0 |

## Claim 1: SBSP not competitive vs terrestrial under reference assumptions

**Quote:** Baseline LCOE $610-1,590/MWh vs terrestrial PV ~$84/MWh;
optimistic-scenario $40-80/MWh.

**Verdict:** Consistent

**Why:** This is the authoritative skeptical position on SBSP
commercial viability under current launch-cost regime. q6.c4 BAU
5 GW deployment is conditional on strategic-autonomy demand
(non-LCOE) rather than commercial competitiveness, consistent with
NASA's finding. The TAI-C 100 GW deployment requires the "optimistic
scenario" of $40-80/MWh + sub-$200/kg launch + mass-production
scaling — explicitly NASA's optimistic-corner case.

## Claim 2: $100-200/kg launch threshold for SBSP viability

**Verdict:** Consistent

**Why:** This couples directly to q1's Starship cost-curve
projection. Per q1's reviewed answer, $100-200/kg LEO is in the
optimistic-late-2030s corner under partial-reuse, and is fully
attainable only under TAI-grade compression. The launch-cost
threshold IS the BAU-vs-TAI-C regime distinction for SBSP.

## Claim 3: Capability-gap inventory (on-orbit assembly, autonomous
operation, beam-power hardware, GEO operations)

**Verdict:** Consistent

**Why:** These are the engineering bottlenecks that
spaceambition-2026-sbsp also identifies (km-scale phased arrays as
"hardest unsolved engineering risk"). Cross-corroborated.

## Claim 4: Lifecycle emissions parity with terrestrial sustainable

**Verdict:** Different conclusion

**Why:** Where NASA OTPS finds emissions parity with terrestrial
sustainables, scientificamerican-2026-sdc cites Saarland University
researchers finding orbital DC could be "order of magnitude greater
emissions" once launch and reentry are factored. The discrepancy is
SBSP-vs-SDC scope (NASA is SBSP specifically; Saarland is broader
orbital infrastructure including SDC). For q6 the emissions question
is tangential to the mass-demand question, but flag for synthesis:
emissions-driven regulatory regimes could cap orbital deployment
volume regardless of launch cost.

## Claim 5: Capability-gap closure path

**Verdict:** Merits investigation

**Why:** NASA OTPS identifies the gaps but does not endorse a closure
path. Where does TAI-grade automation enter the closure? q3-isru
already establishes a framework for acceleration-regime-dependent
TRL progression; q6 should adopt the same framework for SBSP TRL.
Cross-leaf consistency: q3's TAI-C / BAU / stall regimes map
directly onto q6's SBSP deployment scenarios. Flag for synthesis.

## Anti-hallucination check

- The LCOE ranges and $100-200/kg threshold are widely cited NASA OTPS
  figures, cross-validated via the spaceambition-2026-sbsp extract.
- Direct PDF not parseable via WebFetch; figures attributed via
  multiple secondary aggregators citing the report.
- Flag: future iteration should hand-extract the LCOE sensitivity
  tables for direct primary-source review.

## Notes

NASA OTPS is the tier-S authoritative source on SBSP economic
viability under reference assumptions. The skeptical finding is
itself load-bearing for q6.c4's BAU-vs-TAI-C regime distinction.
The optimistic-scenario LCOE $40-80/MWh creates the conditional
under which 100 GW TAI-C deployment becomes commercially viable.
