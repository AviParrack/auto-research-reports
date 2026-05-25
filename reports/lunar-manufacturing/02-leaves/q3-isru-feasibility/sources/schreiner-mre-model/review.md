---
source: schreiner-mre-model
reviewed_pass: 4
reviewed_by: claude+gpt
---

# Source Review: Schreiner-Sibille MRE Reactor Model

## Summary

| Verdict | Count |
|---|---|
| Consistent | 3 |
| Different conclusion | 0 |
| Novel supporting | 2 |
| Merits investigation | 0 |
| Not relevant | 0 |

## Claim 1 — Specific energy 21 kWh/kg O2

**Quote:** "An MRE reactor can produce on the order of 100 kg oxygen
annually per kilogram reactor mass with a specific energy around 21 kW-
hr per kilogram oxygen in an annual production range of 2000-3000 kg."

**Verdict:** Consistent (q3.c2, q3.c13)

**Why:** This is the *process-only* specific energy at the bath. My
thermodynamic floor (6.5 kWh/kg) is the pure-oxide lower bound; 21
kWh/kg includes Gibbs + heat-to-melt + electrochemical overpotentials —
consistent at ~3× floor.

## Claim 2 — Productivity per reactor mass (100 kg O2/yr/kg)

**Quote:** "100 kg O2 / yr / kg reactor mass"

**Verdict:** Consistent (q3.c13)

**Why:** This is the canonical MRE figure used downstream for plant
sizing (BIG Idea Challenge, Helios, Lunar Resources). Direct support
for the productivity argument that MRE clears q4's phi threshold over
multi-year integration.

## Claim 3 — Inert anode is the key advance

**Quote:** "Inert anode" (no consumable graphite or platinum) is the
key 21st-century advance over earlier MRE proposals.

**Verdict:** Novel supporting (q3.c6)

**Why:** Distinguishes Sadoway's MRE from FFC Cambridge (which uses
CaCl2 + sacrificial anode) and explains why MRE has the Earth-import
advantage. Strengthens the q3.c6 framing that MRE is preferred for
lunar economics over FFC.

## Claim 4 — Co-products

**Quote:** "Cathode products: iron alloy + silicon, with calcium and
aluminum recoverable depending on cell design."

**Verdict:** Consistent (q3.c9)

**Why:** Supports the materials-feasibility rollup that MRE produces
Fe + Si as default co-products (and Al + Ca with more sophisticated
cell design). This is the structural-metals route for lunar
manufacturing.

## Claim 5 — Plant mass-power-trade

**Quote:** "400 kg, 14 kW MRE-based ISRU system can produce 1,000 kg
O2/yr from lunar Highlands regolith"; "1,593 kg, 56.5 kW system can
produce 10,000 kg O2/yr."

**Verdict:** Novel supporting

**Why:** Two specific operating points constrain the wall-plug specific
energy: small system 140 kWh/kg O2, larger system 50 kWh/kg O2. The
larger system is more efficient (economies of scale in heat
management). Adds engineering credibility to the 40-150 kWh/kg O2
wall-plug range in my calc.
