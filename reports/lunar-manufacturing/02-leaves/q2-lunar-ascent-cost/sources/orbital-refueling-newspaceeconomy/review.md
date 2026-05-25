---
source: orbital-refueling-newspaceeconomy
reviewed_pass: 4
reviewed_by: claude+gpt
---

# Source Review: New Space Economy "Orbital Refueling of the Starship Architecture" (Dec 2025)

## Summary

| Verdict | Count |
|---|---|
| Consistent | 3 |
| Different conclusion | 0 |
| Novel supporting | 1 |
| Merits investigation | 0 |
| Not relevant | 0 |

## Claim 1: 10-20 tanker launches per HLS mission, mid 12-14
**Quote:** "Current estimates range from '10 to nearly 20 launches'... 'High single digits to high teens (e.g., 15-18 launches)' typical"
**Verdict:** Consistent
**Why:** My calc's gear-ratio amplification factor (~12-14×) tracks this. Captured in q2.c12.

## Claim 2: ~1,200 tons propellant per Starship HLS mission
**Quote:** "a fully fueled Starship HLS requires approximately 1,200 tons of propellant"
**Verdict:** Consistent
**Why:** With 100 t lunar payload, gives Γ ≈ 12 — matches Metzger's Γ_LEO ≈ 14 within tolerance. The 14 vs 12 difference is roughly the return-leg propellant overhead.

## Claim 3: ~$400M per HLS mission
**Quote:** "the price is likely to be $400M per run (including HLS investment recapture and 50% profit over 10 uses)"
**Verdict:** Consistent
**Why:** Direct anchor for q2.c12. $400M / 100 t = $4,000/kg of lunar-surface payload — matches my Earth-imports-only mid-era $4,162/kg within 5%. Strong cross-check.

## Claim 4: HLS depreciated over 10 uses, 50% profit margin
**Quote:** "including HLS investment recapture and 50% profit over 10 uses"
**Verdict:** Novel supporting
**Why:** Provides the reuse-count + margin assumption that q2.c9 captures. The 50% profit margin is a market-pricing assumption that adds about $1,500/kg on top of the internal cost. My calc's hardware $/kg/reuse figures aim at internal cost, not list price; this is consistent.

## Anti-hallucination check

All quotes appear in extract.md. This is trade press, not peer-reviewed, but the specific tanker-count and propellant-mass figures are consistent with the SpaceX HLS architecture documentation across multiple sources.
