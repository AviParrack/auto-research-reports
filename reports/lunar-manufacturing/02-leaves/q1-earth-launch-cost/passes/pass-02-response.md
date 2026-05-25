---
pass: 2
kind: response-to-audit
audited_artifact: pass-02-calc.md
audit_file: pass-02-audit.md
date: 2026-05-25
---

# Response to Codex audit (q1 pass-02-calc)

Codex audited propellant cost reasonableness, refurb scaling defensibility, scenario boundary choices, formula correctness, and conclusion strength. Net: mostly supports with two specific overclaims flagged.

## Accepted (will downgrade)

- **"Partial scenario as central 2030-2035 estimate" — UNSUPPORTED.** Codex right. I called it "most defensible" without an evidentiary argument. Reconcile pass needs to either supply that argument (probability weighting across operational outcomes) or just present scenarios without ranking them.

- **"Pessimistic = no improvement over Falcon 9" — WEAK.** Codex notes that even pessimistic Starship at $194-878/kg could undercut Falcon 9's current $2,720-7,000/kg list pricing depending on payload utilization. The "no improvement" framing conflates internal cost with list price.

## Notable Codex contribution: validated source URLs

Codex provided a curated list of real source URLs I should fetch in subsequent passes — these are higher-quality than my initial scoping search results:

- **FAA Starship PEA** — environmental assessment with operational data
- **NASA propellant costs report** (NTRS) — institutional propellant cost reference
- **EIA Henry Hub** — methane pricing index
- **Gwynne Shotwell 2017 statement** — official refurb cost commentary
- **SpaceX Capabilities & Services** PDF — current pricing
- **NewSpaceEconomy Feb 2026 rideshare pricing** — independent verification of SatBase numbers
- **Spaceflight Now 34th-reuse milestone** — operational reuse data

These move from speculation to concrete primary sources. The reconcile sub-pass should fetch these and cross-check my assumptions.

## Confirmed (no change)

- Propellant cost calc (3,400t methalox at industrial prices): supports
- Refurbishment scaling from Falcon 9 historical: supports
- Cost decomposition formula: supports
- Conclusion that Musk $10/kg requires near-margin or sub-2% refurb: supports

## What to carry forward

For the reconcile sub-pass:
1. Drop the "most defensible 2030-2035 central estimate" framing
2. Fetch the 7 Codex-provided primary sources
3. Cross-check refurb-rate assumption against Shotwell statement + recent reuse milestone data
4. Add explicit caveat distinguishing internal cost from list price throughout
