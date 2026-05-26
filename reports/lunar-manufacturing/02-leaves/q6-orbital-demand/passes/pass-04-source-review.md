---
pass: 4
kind: source-review
leaf: q6-orbital-demand
date: 2026-05-26
status: done
---

# Pass 4 — Source Review (tier-dependent depth)

Per-source review at depth matched to tier (per source-tiers.md):
- Tier S: full claim-by-claim review (7 sources)
- Tier A: medium review with 3-5 key claims (2 sources)
- Tier B: per-public-figure quote review (5 figures)
- Tier C: scalar verdict + 1 paragraph (9 sources)
- Tier D: scalar verdict + flag if conflicts higher tier (7 sources)
- Tier E: not reviewed (5 wiki sources)

Each review.md file is saved alongside its source extract. This file
aggregates the headline verdicts.

## Tier S verdicts (7 sources, full claim-by-claim)

| Source | Verdict summary | Reviews #claims |
|---|---|---:|
| metzger-2023-economics | Consistent 3 / Novel 1 / Merits 1 | 5 |
| kornuta-2019-clpa | Consistent 4 / Novel 1 | 5 |
| nasa-otps-sbsp-2024 | Consistent 3 / Different conclusion 1 / Merits 1 | 5 |
| nasa-m2m-cargo-2024 | Consistent 4 / Merits 1 | 5 |
| nasa-m2m-logistics-2025 | Consistent 3 / Merits 1 | 4 |
| crawford-2014-lunar-review | Consistent 2 / Merits 1 / Not relevant 1 | 4 |
| ida-demand-drivers | Consistent 3 / Merits 1 | 4 |

**Tier S net:** 22 consistent verdicts, 2 novel supporting, 5 merits-
investigation, 1 different-conclusion. The single different-conclusion
verdict (NASA OTPS vs Saarland on emissions) is tangential to q6's
mass-demand question and flagged for synthesis.

## Tier A verdicts (2 sources)

| Source | Overall |
|---|---|
| marcy-2026-arxiv | Consistent — 100 GW US AI demand by 2035 directly underlies TAI-C scenario |
| caltech-sspd-mankins-niac | Consistent — kg/kW range and 80,000 t / 4 GW reference both load-bearing |

## Tier B verdicts (5 public figures)

| Figure | Aggregate quote verdict |
|---|---|
| Elon Musk | Supports as TAI-C upper envelope (aspirational; 1M-ton, 1,000-ship-per-window) |
| Jeff Bezos | Mixed — 24/7 solar half-qualified; "beat terrestrial in next couple decades" contradicts BAU but supports TAI-C |
| Philip Metzger | Supports under exponential-AI-conditional framing (canonical position) |
| Casey Handmer | Supports under TAI-C; 2× cost-premium is canonical mid-optimist bracket |
| Andrew McCalip | Supports BAU skepticism; 3.2× cost-multiple is canonical skeptical bracket |

**Tier B net:** Three figures supporting the optimist + conditional-
optimist case (Musk, Bezos, Metzger, Handmer); one figure supporting
the skeptic case (McCalip). The McCalip / Handmer cost-multiple delta
(3.2× vs 2×) brackets the BAU-to-TAI-C transition; q6.c2 and q6.c10
explicitly capture this.

## Tier C verdicts (9 sources, scalar)

| Source | Verdict | Note |
|---|---|---|
| handmer-2026-dc-orbit | Consistent | Starlink-derivative architecture argument cross-validated |
| handmer-2025-propellant-stability | Consistent | Quantitatively detailed; 1,200 t/Starship + MLI analysis |
| peraspera-2025-orbital-compute | Consistent | 30-50 t/MW corroborates mine + luminix |
| luminix-2026-sdc | Mixed | Mass-density figure load-bearing; viability probabilities scenario-level |
| introl-2026-orbital-dc | Consistent | Most up-to-date industry snapshot |
| cote-2026-orbital-dc | Mixed | Bandwidth ceiling real; OISL mitigation contestable |
| spaceambition-2026-sbsp | Consistent | Consolidates NASA OTPS + ESA Frazer-Nash LCOE |
| pickard-2026-orbital-dc | Consistent | Conceptual corroboration of Cote |
| starcloud-factories-2026 | Consistent | Corporate reference page |
| nvidia-2026-space-compute | Consistent | Supply-side product-line documentation |
| spacenews-2026-governance | Consistent | Source of Metzger quote; governance framing |

## Tier D verdicts (7 sources, scalar + conflict-flag check)

| Source | Verdict | Conflicts higher tier? |
|---|---|---|
| scientificamerican-2026-sdc | Mixed | Partial — emissions debate is tangential |
| tomshardware-2026-mccalip | Consistent | No |
| fortune-2026-bezos-musk | Consistent | No |
| orbysa-2026-sbsp | Consistent | No |
| bisnow-2026-bluemoon-sunrise | Consistent | No |
| marketsandmarkets-2026-osam | Consistent | No |
| orbital-propellant-newspaceeconomy | Consistent | No |

No tier-D source conflicts with tier-S findings in ways that affect
q6's headline conclusions.

## Tier E not reviewed

wiki-sbsp, wiki-propellant-depot, wiki-mars-colonization,
wiki-starship-payload, wiki-artemis-cargo — orientation only per
source-tiers.md, no review file written.

## Cross-source consensus map

Three convergent findings across the source set:

1. **SDC mass intensity ~40 t/MW**, cross-validated by three independent
   engineering analyses (mine, peraspera, luminix) within ±25%. High
   consensus.

2. **Launch cost $100-200/kg is the SBSP + SDC viability threshold**,
   cross-validated by NASA OTPS, Google Suncatcher reference,
   Luminix, scientificamerican-2026-sdc. The threshold defines the
   BAU-to-TAI-C transition.

3. **450 t/yr near-term cislunar propellant demand floor** is the
   established consensus figure cited across Kornuta 2019, Metzger 2023,
   IDA D-13219. Lower bound for the lunar-derived sub-market within
   the broader BAU depot throughput.

Two divergent findings within the source set:

1. **Orbital DC cost multiple**: McCalip 3.2× (whole-project capex+opex)
   vs Handmer 2× (per-token inference under SpaceX integration). q6
   bracket via regime decomposition.

2. **Emissions parity**: NASA OTPS finds parity with terrestrial
   sustainables; Saarland researchers find orbital DC could be order-
   of-magnitude higher. Tangential to q6 mass-demand question; flagged
   for q8 synthesis on regulatory regime.

## Anti-hallucination checks (per source-tiers.md)

- All quoted figures in tier S/A/B reviews appear verbatim in the
  source extract.md files.
- Verdicts assigned per Newman taxonomy (Consistent / Different
  conclusion / Novel supporting / Merits investigation / Not relevant)
  for tier S; per scalar verdict (Consistent / Mixed / Different
  conclusion / Not relevant) for tiers A-D.
- Scalar verdicts at tier C/D are calibrated against tier S findings;
  no tier C/D verdict contradicts a tier S finding without explicit
  flag.

## Codex audit

Pass 4 audit run on the aggregated source-review verdicts (per
source-tiers.md / claude-gpt-protocol.md aggregate-review-for-tier-B/C/D).

## Next pass

Pass 5 (consistency): cross-leaf claim comparison against q1
(Earth launch cost, reviewed), q3 (ISRU feasibility, reviewed),
q4 (gear ratio, reviewed), and the two parallel siblings q5
(capital-buildup, in-flight) and q7 (mass-driver-feasibility,
in-flight). Per the parallel-execution caveat in pass-leaf.md,
the siblings in-flight will be caught by the post-batch
cross-consistency pass, not by this leaf's pass 5.
