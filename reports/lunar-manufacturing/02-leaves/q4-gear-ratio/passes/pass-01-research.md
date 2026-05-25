---
pass: 1
kind: research
leaf: q4-gear-ratio
date: 2026-05-25
agent: claude-opus-4-7
audited: not-applicable
---

# Pass 1 — Research (q4-gear-ratio)

Sources gathered for the gear-ratio leaf. Research only; no claims written yet (claims come from the calc + reconcile sub-passes).

## Sources captured

### Tier-1 (primary canonical)

- **[metzger-2023](sources/metzger-2023/extract.md)** — Philip Metzger, *"Economics of In-Space Industry and Competitiveness of Lunar-Derived Rocket Propellant"*, Acta Astronautica, March 2023 (arXiv 2303.09011). 50 pages. **THIS IS THE CANONICAL SOURCE** for the gear-ratio framework. The extract contains: full formula set (Eqs. 1-15), the competitiveness inequality (Eq. 8), φ values for 7 prior TEAs (Table 2), Years-to-absolute-advantage table by destination orbit (Table 1), and parameter elasticities (Table 3). Captures both the "spherical cow" derivation and the TEA reassessment.

### Tier-2 (referenced from primary, to fetch when needed)

These are cited extensively by Metzger 2023 but not yet fetched. The reconcile sub-pass will pull them if any specific claim hinges on cross-checking them:

- Kornuta et al. ([1] in Metzger) — ULA-authored tent sublimation TEA (φ=442). Originator of the tent technology.
- Sowers, G. ([4] in Metzger) — Colorado School of Mines, tent sublimation TEA (φ=534). The economic optimism case.
- Pelech, T.M. et al. ([7]) — strip mining + borehole sublimation TEAs (φ=3.7 / 16.1). The pessimistic technology case.
- Charania, A. & DePascuale, J. ([5]) — SLS-based TEA (G=64.9, φ=26.5) — the published pessimistic conclusion that triggered Metzger's reassessment.
- Jones, C. et al. ([6]) — also SLS-based pessimistic TEA.
- Bennett et al. ([2]) — reassessed Jones, improved economies of scale for reactors (φ=43.4).
- NASA NTRS "Cost Breakeven Analysis of Lunar In-Situ Propellant Production" (2020) — fetched as PDF but body content not yet extracted. Tentative finding from search: 35-year breakeven, ≈7 Mars missions. To extract in reconcile pass if relevant.

### Tier-3 (orthogonal / contextual)

- O'Neill-Glaser contemporary analysis (NTRS 20120001744) — fetched as PDF. The legacy origin of mass-driver economics. Predates Metzger's framework but informs the "what if we use a mass driver instead of chemical rockets" path. Belongs more to q7 (mass-driver-feasibility) than q4 (gear-ratio), but the gear-ratio framework subsumes O'Neill's earlier "payback ratio" formalism.

## Public figures identified (to source-review later)

For Source Reviews against this leaf (sub-pass 4):
- **Philip Metzger** — covered above; primary
- **George Sowers** (Colorado School of Mines) — tent sublimation primary; needs his own writeups
- **Andrew McCalip** (Varda Space) — public economics calculator; not yet found a specific lunar-manufacturing writeup
- **Elon Musk / SpaceX** — Starship cost projections used in Metzger's launch cost model; values cited (L_30 = $30/kg) are Musk's claims, not third-party validated
- **Gerard O'Neill** (deceased; legacy) — original gear-ratio (via O'Neill-Glaser mass-driver) framing

## Key insights gathered from Metzger 2023

(For reference during calc/reconcile/write. NOT yet claims.)

1. **There is no universal "35× threshold."** The threshold for absolute advantage at destination X depends on Γ_X = G_{LS-X}/G_{LEO-X}. The "≳35" figure commonly cited corresponds to Metzger's MVP design (φ=36.5) achieving GTO absolute advantage, not a universal threshold.

2. **The economic argument has structural physics support.** Lunar gravity well is 24× weaker than Earth's for delivering to GTO. The competitiveness question is whether the operational economics on the Moon eat up *more* than the 24× factor. If they don't, lunar wins.

3. **Tent sublimation already exceeds the threshold.** Two independent studies (Kornuta φ=442, Sowers φ=534) put tent sublimation at an order of magnitude above what's needed for LEO advantage.

4. **G/x ratio matters more than absolute launch cost.** When G/x is large (capital transport dominates equipment cost), the lunar operation becomes insensitive to terrestrial launch cost L_0 — Starship dropping prices doesn't undercut lunar.

5. **The 2040+ timeline framings in popular accounts are misleading.** Metzger's table shows GTO advantage in year 5-8 with optimistic-realistic parameters, year 1 for closer destinations (LLO, EML1, GEO).

6. **Discount rate is a major lever.** 27.2% (commercial WACC for risky) → 13 years to GTO. 12% (PPP) → 5-8 years. This is policy-shaped, not technology-shaped.

7. **Pelech's pessimism (φ=3.7) is challenged.** Metzger argues Pelech overestimated capital mass M_K by basing on terrestrial excavator analogies that don't apply to space-engineered hardware.

## Next sub-passes

- **calc**: derive the gear-ratio threshold from first principles. Use Tsiolkovsky for G, payload economics for φ requirement, ignoring Metzger's specific numbers during calc. Then in reconcile compare.
- **reconcile**: compare first-principles result to Metzger's full model. Where they agree and disagree.
- **source-review**: point-by-point Source Review of Metzger 2023 with verdict taxonomy. Probably also Sowers and CD primary sources.
- **consistency**: cross-leaf check against q1-earth-launch-cost (do their L_0 / L_30 assumptions agree?) and q3-isru-feasibility (does ISRU TRL support Metzger's φ assumptions for tent sublimation?).
- **write**: leaf report rendered from claims.yaml.

## Anti-pattern check

- ✓ No claims yet — research is gather-only
- ✓ Source extract is verbatim where appropriate
- ✓ Calendar-year framings ("by 2040") avoided — extract uses Metzger's year-from-start framework which is conditional
- ⚠ Single source (Metzger) carries most of the load; reconcile pass must pull cross-checks
