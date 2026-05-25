---
pass: 3
kind: reconcile
leaf: q6-orbital-demand
date: 2026-05-26
status: done
---

# Pass 3 — Reconcile (derived vs sources)

Reading every `sources/*/extract.md` and comparing the derived demand
figures (q6.c1-c8) against the literature. Updating evidence arrays
in `claims.yaml`. Disagreements documented below with resolutions.

## Agreement table

| Claim | Sources supporting | Sources contradicting | Resolution |
|---|---|---|---|
| q6.c1 (SDC ~40 t/MW) | peraspera-2025-orbital-compute (30-50 t/MW), luminix-2026-sdc (42 t/MW) | — | Strong agreement; mid-line confirmed |
| q6.c2 (regime-bracketed 20 kt → 2 Mt → 40 Mt) | introl-2026-orbital-dc (SpaceX 1M t/yr → 100 GW), marcy-2026-arxiv (100 GW US demand by 2035), nasa-otps-sbsp-2024 (conditional viability), metzger-2023-economics (exponential framework) | mccalip-quote-fomo (3× cost multiple suggests demand stays bounded), cote-2026-orbital-dc (bandwidth ceiling) | Held with explicit regime-conditional framing; skepticism captures stall + low-BAU |
| q6.c3 (SDC dominates) | marcy-2026-arxiv, introl-2026-orbital-dc, scientificamerican-2026-sdc | — | Strong agreement: orbital DC narrative dominates the 2026 industry literature |
| q6.c4 (SBSP 5 kg/kW, 0-100 GW regime range) | caltech-sspd-mankins-niac (1-6.7 kg/kW range), nasa-otps-sbsp-2024 (launch-cost conditional), orbysa-2026-sbsp (China 1 km array by 2028, Aetherflux Q1 2027) | spaceambition-2026-sbsp (notes ESA Frazer-Nash slightly higher mass) | Mid-line 5 kg/kW consistent with Mankins+SOA. Regime range defensible |
| q6.c5 (depot 800 t/yr/ship, 8-160 kt/yr BAU-TAI-C) | handmer-2025-propellant-stability (1,200 t/Starship × refuel ratio), wiki-propellant-depot (Griffin's 250 t × 2 missions/yr = 500 t/yr historical baseline), introl-2026 (SpaceX/xAI 1M t/yr satellite mass implies massive refueling) | — | Headline figures consistent. Sensitivity: NASA 16-tanker assumption doubles |
| q6.c6 (lunar-sourced bulk mass necessary-not-sufficient under TAI-C) | metzger-2023-economics (in-space industry framework supports), introl-2026-orbital-dc (industrial scale), handmer-2026-dc-orbit (2× cost premium tolerable) | mccalip-quote-fomo (3.2× cost multiple, "FOMO and aesthetic futurism") | Held with the necessary-but-not-sufficient framing per Codex audit |
| q6.c7 (stall fails for lack of demand) | nasa-otps-sbsp-2024 (no commercial viability without launch cost), peraspera-2025-orbital-compute (2030 "crawl phase" only) | — | Strong agreement: stall is a real regime, demand-led failure mode |
| q6.c8 (450 t/yr lunar-derived = ~5.6% of BAU LEO refueling) | kornuta-2019-clpa (450 t/yr near-term), metzger-2023-economics (same baseline), ida-demand-drivers (cites Kornuta as canonical) | — | The 5.6% interpretation is mine; sources support the 450 t/yr but don't make the all-source vs lunar-source comparison directly. Confidence held at medium |

## Disagreements

### McCalip vs Handmer on orbital DC cost multiple

McCalip's 3.2× cost multiple (Tom's Hardware / SpaceGPT calculator)
vs Handmer's 2× cost premium for inference compute. The 1.2× delta
sounds modest but matters: at 2× premium, Handmer's "still profitable"
case holds for inference economics; at 3.2× McCalip says the case
fails outside of FOMO.

**Resolution.** Both assessments are operating on slightly different
analyses. McCalip is computing total project cost (capex + opex) over
5 years for a 1 GW deployment under "extremely optimistic projections"
of launch cost reduction. Handmer is computing per-token cost for
inference compute under SpaceX-internal Starship + Starlink integration.
The gap is partly cost-decomposition methodology (whole-project vs
unit-economics) and partly architectural (3rd-party deployment vs
SpaceX-integrated). Both are defensible under their own framings.

For q6 demand decomposition, the implication is: the BAU regime
captures McCalip's range (SDC viable only at small scale), while
TAI-C captures Handmer + Metzger's range (viable at large scale
under compute-growth + Starlink-integration). The two positions
bracket the regime range usefully rather than contradicting.

Flag for synthesis: q6.c2 regime range is explicitly bracketed by
McCalip pessimist and Handmer optimist; q8 synthesis should treat
this as the canonical viability range.

### Cote's bandwidth ceiling

Cote (substack) argues orbital DC viability is structurally limited
by bandwidth: 500-800 Tbps total orbital comms capacity vs 5-20 Tbps
per single ground DC. Pickard corroborates: ground stations are the
binding constraint.

**Resolution.** Cote's bandwidth ceiling argument is potentially
foundational — if real, it puts a hard ceiling on orbital DC demand
that would invalidate the TAI-C 1,000 GW scenario regardless of
launch cost. Three responses:

1. **Optical inter-satellite links (OISL) bypass ground-station
   bottleneck.** Modern Starlink-class architectures use OISL to
   route compute internally. Pickard's "ground station" argument
   doesn't apply to AI training workloads served via OISL between
   compute nodes; only the final inference-output bytes need to
   return to ground, and those are very small per compute cycle.

2. **AI training is the killer app, not inference serving.**
   Handmer's "2× per-token cost" frames inference, where output
   bytes per token are large. AI *training* generates much higher
   compute-per-output-byte; the bandwidth-to-ground constraint
   is much looser.

3. **Even at 800 Tbps ceiling, orbital DC captures the high-
   intensity-compute workload subset.** Cote's "niche-only"
   conclusion is consistent with my BAU regime (50 GW = niche-scale
   compared to terrestrial total).

For q6, Cote's argument shifts the TAI-C ceiling slightly but doesn't
break the qualitative conclusion. Flag for synthesis: q6.c2 TAI-C
1,000 GW upper bound is sensitive to OISL bandwidth scaling
assumptions; if bandwidth scaling falls short, TAI-C compresses to
~200 GW. The factor-of-5 sensitivity is within the regime uncertainty
already declared.

### NASA OTPS vs my BAU SBSP 5 GW

NASA OTPS conclusion: SBSP not competitive vs terrestrial under
reference cost assumptions. My BAU regime posits 5 GW deployed by
2040. Tension: how does 5 GW deploy if not competitive?

**Resolution.** Two paths:
1. National-security / strategic-autonomy demand. China's 2028 1 km
   array is military-strategic, not commercial-LCOE. Aetherflux's
   Q1 2027 launch is venture-funded with strategic backing. State
   actors deploy at uncompetitive LCOE for strategic reasons.
2. Niche grid-value applications. Per spaceambition-2026-sbsp's
   VALCOE analysis, SBSP firm-output is competitive vs PV+storage
   for specific applications (remote sites, military forward bases,
   24/7-grid commit).

5 GW under BAU is consistent with strategic + niche deployment but
not with full commercial competitiveness. The 100 GW TAI-C scenario
requires NASA OTPS's "optimistic conditions" (launch < $200/kg +
mass-production scaling) to obtain. q6.c4 confidence held at high
because the regime conditionality is now explicit.

### Kornuta-Metzger 450 t/yr vs BAU 8,000 t/yr depot

q6.c8 reconciles this: 450 t/yr is the lunar-derived sub-market;
8,000 t/yr is total LEO refueling including Earth-launched
propellant. Sources cited (Kornuta 2019, Metzger 2023) are
specifically about the lunar-derived market.

**Resolution.** Confidence held at medium for q6.c8 because the
all-source vs lunar-source distinction is my framing, not directly
attributed to the sources. The 5.6% figure (450 / 8,000) is
calculation-derived from my own depot demand model.

## Updated claims.yaml evidence arrays

For each q6 claim, the source extracts listed in the agreement table
above are added to the evidence array with verdict tags. Updates to
follow in claims.yaml via separate edit.

## Acceleration regime — source corroboration

The three-regime framework (stall / BAU / TAI-C) is corroborated by:
- **Stall:** mccalip-quote-fomo + peraspera-2025-orbital-compute (2030 "crawl" only)
- **BAU:** luminix-2026-sdc (<15% viability 2029-31, 30-40% 2032-35); marketsandmarkets-2026-osam (modest growth)
- **TAI-C:** metzger-quote-orbital-dc (exponential-AI-conditional); introl-2026 (SpaceX 1M-sat filing); musk-mars-1m-tons (1,000-ship cadence)

Anti-pattern #11 compliance verified: the three-regime decomposition
is the deliverable; calendar dates are illustrative.

## Headline reconcile finding

The derived demand decomposition is broadly consistent with the
source literature at the regime-bracket level. The most
quantitatively robust point of agreement is the SDC mass intensity:
~40 t/MW (mine) ↔ 30-50 t/MW (peraspera) ↔ 42 t/MW (luminix). These
are three independent engineering analyses converging to within
±25%. The total LEO demand under BAU and TAI-C is dominated by SDC
in all three of mine + peraspera + luminix; SBSP and depots are
order-of-magnitude smaller in absolute mass.

The principal qualitative finding — **lunar-sourced bulk mass is
necessary-but-not-sufficient under TAI-C** — is supported by the
in-space industry framework literature (Metzger 2023, Kornuta 2019,
Crawford 2014) and is consistent with Handmer's mid-optimist position.
McCalip's skepticism applies to BAU, not TAI-C.

## Codex audit — pass 3

The reconcile reasoning above is audited in pass-03-audit.md.

## Next pass

Pass 4 (source-review): per-source review at depth matched to tier.
Tier S (full claim-by-claim) for the 7 tier S sources. Tier A
(medium) for Marcy + Mankins. Tier B (per-figure quote review) for
Musk, Bezos, Metzger, Handmer, McCalip. Tier C/D (scalar verdict).
