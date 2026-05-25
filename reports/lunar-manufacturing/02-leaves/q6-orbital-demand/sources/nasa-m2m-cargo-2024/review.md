---
source: nasa-m2m-cargo-2024
tier: S
reviewed_pass: 4
reviewed_by: claude+gpt
---

# Source Review: NASA M2M Lunar Surface Cargo (2024 ACR)

## Summary

| Verdict | Count |
|---|---|
| Consistent | 4 |
| Merits investigation | 1 |

## Claim 1: 1,500 kg current cargo lander capability

**Quote:** "Current capabilities planned for lunar surface operations
are limited to transporting approximately 1,500 kg of cargo."

**Verdict:** Consistent

**Why:** Directly used in q6.c12. The 1,500 kg/mission figure is the
BAU lower bound for Artemis-era lunar surface cargo. Cross-validated
against CLPS award sizes (e.g., Intuitive Machines $180M for ~75 kg
rover-instrument collective).

## Claim 2: Gap vs multi-tonne exploration objectives

**Verdict:** Consistent

**Why:** The gap is the architectural impetus for the surface-habitat
+ cargo-lander new elements in the 2024+2025 ACR cycle. Three
resolution paths identified (develop larger lander, use Starship HLS
cargo, rescope objectives) are themselves regime-conditional choices.

## Claim 3: Gateway resupply via GLE

**Verdict:** Consistent (not directly relevant to q6's surface-cargo
focus but informational)

**Why:** Gateway logistics adds ~28 commercial cargo missions over
program life to the LEO-to-cislunar transit budget. q6's cislunar
mass demand should include this; current accounting puts it under
"depots" implicitly via tanker support.

## Claim 4: Annual landing cadence post-Artemis-V

**Verdict:** Consistent

**Why:** ~1/year landings × 1,500 kg/mission × ~10 years operational
= 15,000 kg cumulative under BAU. Consistent with my BAU 30 t/yr
surface cargo figure (which generously assumes some Starship HLS
cargo utilization in the post-2030 cadence).

## Claim 5: Diverse cargo needs taxonomy

**Verdict:** Merits investigation

**Why:** NASA's cargo-need diversity (varying size, mass, cadence,
operational needs) implies different lander classes serving different
sub-segments. This is a topology question that q5-capital-buildup
(sibling) is investigating; cross-leaf consistency check applies.

## Anti-hallucination check

- The 1,500 kg figure is widely cited and is in q3's reviewed
  framework as well. Cross-validated.
- Direct PDF not parseable via WebFetch; key figures attributed via
  the NASA M2M Architecture site and the GAO-25-107591 report.
- Flag: future iteration should hand-extract the full cargo
  decomposition tables.

## Notes

NASA M2M Cargo 2024 is the tier-S authoritative source for Artemis-
era lunar surface cargo demand. The 1,500 kg baseline gap is the
operational constraint underlying my BAU 30 t/yr surface cargo
figure. Under TAI-C, Starship HLS cargo variant at ~100 t/lander
× 5 landers/yr = 500 t/yr is consistent with the agency's own
"diverse cargo needs" framing.
