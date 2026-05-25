---
pass: 1
kind: research
leaf: q5-capital-buildup
date: 2026-05-26
agent: claude-opus-4-7
audited: not-applicable
---

# Pass 1 — Research (q5-capital-buildup)

Sources gathered for the capital-buildup leaf under the new tier-hierarchy protocol. Research only; no claims written yet (claims come from the calc + reconcile sub-passes). Tier-B sources are one-card-per-public-figure; tier C/D are container-press for the public-figure quotes plus DARPA / NASA primary sources.

## Tier breakdown

| Tier | Count | Notes |
|---|---|---|
| S | 9 | Peer-reviewed academic + agency primary technical reports |
| A | 10 | Peer-reviewed surveys, FFRDC reports, agency OIG audits, integration studies |
| B | 9 | One per public figure (Metzger, Sowers, Musk, Shotwell, Bezos, Zubrin, Handmer, Isaacman, Nelson) |
| C | 6 | Trade press containers and credentialed-expert blogs (note: Handmer's blog content reviewed via the public-figure card not a separate Tier C entry, since the blog body is identical to his Tier B statements) |
| D | 2 | Mainstream press samples (ABC 2019 Bezos, CBS 2026 Isaacman) |
| **Total** | **36** | Tier-S sits at 9 because the lunar capex literature is concentrated on a small canonical core (Metzger / Sowers / Jones / Mueller / Walther + FSP + landing-pad). Tier-S target was 15-30; the topic is **saturated below that range** rather than under-sampled — additional Tier S would be diminishing-returns rephrases of the same primary anchors. |

The intent under the new protocol was to read all relevant peer-reviewed work in the topic area. The lunar capex / staged-buildup-milestone literature is **concentrated** rather than diffuse: roughly 8-12 primary credentialed sources carry most of the analytical content (Metzger 2013/2023, Sowers 2018/2021, Jones 2020, Mueller 2022, Walther 2024, plus the FSP / mass-driver / landing-pad papers). We do not believe there is a substantial corpus of additional tier-S work we have missed; topic-saturation appears to be effectively complete. The tier-A layer adds policy and integration studies (DARPA LunA-10, PwC, CSIS x3, IDA, NASA OIG). The tier-B layer covers all the major public figures whose statements shape current policy and capital-allocation decisions.

## Tier S — peer-reviewed primary and agency primary

Source files saved at `sources/{slug}/extract.md` with `## Abstract / ## Key claims / ## Reviewer notes` structure.

| Slug | Author(s) | Year | Venue | What it bears on |
|---|---|---|---|---|
| [metzger-2013-bootstrap](../sources/metzger-2013-bootstrap/extract.md) | Metzger, Muscatello, Mueller, Mantovani | 2013 | J. Aerospace Eng. | **Canonical:** 12 MT / 20-yr seed → 156-40,000 MT industrial endpoint via generation scheme |
| [metzger-2023-economics](../sources/metzger-2023-economics/extract.md) | Metzger | 2023 | Acta Astronautica | Gear-ratio + φ framework; capex decomposition substrate; SLS vs commercial-launch reframing |
| [jones-2020-breakeven](../sources/jones-2020-breakeven/extract.md) | Jones, Pensado, et al. | 2020 | NASA NTRS / AIAA ASCEND | 35-yr breakeven; 7 Mars missions; SLS-architecture pessimistic anchor |
| [sowers-2021-ice-mining](../sources/sowers-2021-ice-mining/extract.md) | Sowers | 2021 | New Space (SAGE) | $4B initial; $2.5B capture tent; 9% ROI; 15-year project life |
| [sowers-2018-clpa](../sources/sowers-2018-clpa/extract.md) | Sowers, ULA team, et al. | 2018 | CSM independent study | Staged architecture: prospecting → pilot → first plant → multiple plants → distribution |
| [metzger-autry-2022-landing-pads](../sources/metzger-autry-2022-landing-pads/extract.md) | Metzger, Autry | 2022/2023 | New Space (SAGE) | $229M-$47M landing pad cost as f($/kg launch); microwave sintering preferred |
| [walther-2024-autonomous-construction](../sources/walther-2024-autonomous-construction/extract.md) | Walther, Johns, Kolvenbach, Bickel, Hutter | 2024 | Frontiers in Space Tech | 174-193 m²/day boulder-construction throughput; autonomous excavator path planning |
| [nasa-fsp-2024-glenn](../sources/nasa-fsp-2024-glenn/extract.md) | NASA Glenn (Kortes) | 2024 | NASA primary | FSP 40 kWe / 6t / 10-yr / early-2030s deployment; $5M Phase 1 contracts |
| [mueller-2022-lunar-construction-planning](../sources/mueller-2022-lunar-construction-planning/extract.md) | Mueller | 2022 | NASA NTRS | Construction-method trades; staged sequence; equipment-design trades |

## Tier A — peer-reviewed surveys, FFRDC, agency policy

| Slug | Author(s) | Year | Venue | What it bears on |
|---|---|---|---|---|
| [duchek-2024-fsps-falcon-heavy](../sources/duchek-2024-fsps-falcon-heavy/extract.md) | Duchek et al. | 2024 | Nuclear Technology (Taylor & Francis) | 350-kWth conceptual microreactor under Falcon Heavy mass envelope |
| [aiaa-2025-mass-driver](../sources/aiaa-2025-mass-driver/extract.md) | AIAA 2025 authors | 2025 | AIAA Aviation 2025 | Mass-driver-as-HLS-alternative cost-benefit trade study |
| [shubov-2021-gsfr](../sources/shubov-2021-gsfr/extract.md) | Shubov | 2021 | arXiv (independent) | Speculative-upper-bound: GSFR 50-doubling → Dyson civilisation |
| [darpa-2024-luna-10](../sources/darpa-2024-luna-10/extract.md) | Nayak, DARPA LSIC | 2024 | DARPA primary | 14-company / 6-area integration study; mid-2030s target |
| [pwc-2026-lunar-market](../sources/pwc-2026-lunar-market/extract.md) | PwC France for ESA | 2026 | PwC commissioned by ESA | **$72.7-88.5B cumulative infrastructure spend 2026-2050;** transportation 70-80% of cost in early decade |
| [csis-miller-2026-cracking-code](../sources/csis-miller-2026-cracking-code/extract.md) | Miller | 2026 | CSIS | Lunar Development Authority concept; benchmarks (port authority $9.4B; Houston PW $3.5B) |
| [csis-macdonald-2026-economics](../sources/csis-macdonald-2026-economics/extract.md) | MacDonald | 2026 | CSIS | Apollo $250-300B today; SEI 1989 → $1T today; pessimistic on commercial revenue |
| [csis-swope-2024-cislunar](../sources/csis-swope-2024-cislunar/extract.md) | Swope, Gleason | 2024 | CSIS Aerospace Security | "No business case" structural-skeptic anchor |
| [ida-2024-demand-drivers](../sources/ida-2024-demand-drivers/extract.md) | IDA STPI | 2024 | IDA D-13219 | Demand drivers framework; **flagged as incomplete — PDF body not parsed** |
| [nasa-oig-2021-artemis-93b](../sources/nasa-oig-2021-artemis-93b/extract.md) | NASA OIG | 2021 | OIG audit IG-22-003 | $93B Artemis program-of-record through FY2025; $4.1B/launch SLS+Orion |

## Tier B — public figures (one card per figure)

Each figure card is `sources/figure-{name}/extract.md`. Sub-pass 4 will produce one `review.md` per figure with per-quote verdicts.

| Figure | Role | Anchored claims |
|---|---|---|
| [figure-metzger](../sources/figure-metzger/extract.md) | UCF planetary scientist, gear-ratio author | "1/3 or less of national space-program annual budgets"; 12 MT / 20 yr bootstrap |
| [figure-sowers](../sources/figure-sowers/extract.md) | CSM Space Resources, former ULA chief scientist | $4B initial ("luxury hotel in Las Vegas"); $2.5B tent ISRU; 9% ROI / $2B profit / 15 yr |
| [figure-musk](../sources/figure-musk/extract.md) | CEO SpaceX | 500-1000 TW/yr AI satellites; AI compute in space within 2-3 yr; TERAFAB |
| [figure-shotwell](../sources/figure-shotwell/extract.md) | President & COO SpaceX | Humans before 2030; lunar manufacturing within 5 yr ideally |
| [figure-bezos](../sources/figure-bezos/extract.md) | Founder Blue Origin | Heavy industry off Earth; 1 trillion people; Blue Moon 6.5 t cargo |
| [figure-zubrin](../sources/figure-zubrin/extract.md) | Mars Society president | **Lowest-anchor:** Moon Direct $1.5B initial + $420M/yr (minimal presence, no mfg) |
| [figure-handmer](../sources/figure-handmer/extract.md) | Terraform Industries CEO; ex-JPL | Trillion-dollar buildout; $100B/yr per mass driver; 450 MW reactor floor |
| [figure-isaacman](../sources/figure-isaacman/extract.md) | NASA Administrator (2026-) | **Current US program of record:** $20B / 7 yr surface base; 2 landings/yr cadence |
| [figure-nelson](../sources/figure-nelson/extract.md) | NASA Administrator (2021-2025) | $4.2B/launch; China-competition framing |

## Tier C — industry trade press, expert blogs, container press

| Slug | Container of |
|---|---|
| [spacenews-2023-luna-10-companies](../sources/spacenews-2023-luna-10-companies/extract.md) | DARPA LunA-10 announcement context |
| [payloadspace-2023-luna-10-awards](../sources/payloadspace-2023-luna-10-awards/extract.md) | Per-company LunA-10 focus assignments |
| [spaceflightnow-2026-20b-moonbase](../sources/spaceflightnow-2026-20b-moonbase/extract.md) | Isaacman $20B announcement coverage |
| [interestingengineering-2026-musk-mass-driver](../sources/interestingengineering-2026-musk-mass-driver/extract.md) | Musk mass-driver / TERAFAB quotes |
| [space-com-2026-musk-catapult](../sources/space-com-2026-musk-catapult/extract.md) | Musk Feb 2026 quote attribution |
| [breaking-defense-2024-csis-cislunar](../sources/breaking-defense-2024-csis-cislunar/extract.md) | CSIS skeptic analysis container |

## Tier D — mainstream press samples

| Slug | What it samples |
|---|---|
| [abc-2019-bezos-blue-moon](../sources/abc-2019-bezos-blue-moon/extract.md) | Bezos May 2019 Blue Moon event reach |
| [cbs-2026-moonbase](../sources/cbs-2026-moonbase/extract.md) | Mainstream reach of Isaacman $20B announcement |

## Tier E — orientation only (NOT saved under sources/)

Wikipedia (Artemis Program, ISS Program, Robert Zubrin, Gwynne Shotwell) used for date-checking and biographical orientation only. Not cited in claims. Lunarpedia / NSS articles (mostly derivative summaries of Metzger or Sowers) likewise.

## Topics added to topics.yaml

15 capex/buildup-specific topics created (plus 11 additions from q7-mass-driver-feasibility sibling). The set most load-bearing for q5 are: `capex-models`, `autonomy-construction`, `isru-plant-scaling`, `lunar-base-architecture`, `robotic-assembly`, `industrial-explosion-compression`, `tai-acceleration`, `depreciation-curves`, `learning-rate-wright`, `bootstrap-seed-mass`, `staged-buildup-milestones`, `fission-surface-power`, `artemis-program-cost`, `public-figure-projections`, `lunar-mass-driver`. See [topics.yaml](../../../topics.yaml).

## Pre-calc framing

The published anchors span ~3 orders of magnitude in total capex:

| Anchor | Total capex | Time horizon | Architectural assumption |
|---|---|---|---|
| Zubrin Moon Direct | $1.5B + $420M/yr | open-ended | Minimal sustained presence, no manufacturing |
| Metzger 2013 bootstrap | "low cost" (unspecified $) | 20 yr | Robotic seed + additive mfg + AI |
| Sowers 2021 commercial | $4B initial / $2.5B tent | 15 yr | Tent sublimation, fully robotic, commercial launch |
| Isaacman 2026 NASA | $20B (surface only) over 7 yr | 7 yr | Government program of record, habitat + nuclear |
| PwC 2026 cumulative | $72-88B | 2026-2050 | Cumulative across all parties, all infrastructure |
| MacDonald CSIS / SEI | ~$1T | open-ended | 1989-style architecture (pessimistic ceiling) |
| Handmer | "trillions" | open-ended | Full orbital-AI-compute trillion-dollar scenario |

The spread is **structural**, not just optimism vs pessimism: each anchor assumes a different product class (just-presence / propellant-only / habitat-only / commercial-export / AI-compute-export), a different transport architecture (SLS-class vs commercial-launch vs Starship+mass-driver), and a different automation regime. The calc pass will derive a bottom-up estimate **without consulting these anchors**, then the reconcile pass will compare back.

## Next sub-passes

- **calc**: derive bottom-up capex from physical mass budgets (cargo lander, habitat, ISRU plant, power, mobility, manufacturing) × launch cost ($/kg from q1) × replacement schedule (lifetime from q3+q4) under three automation regimes (BAU, industrial-explosion, TAI). Plus milestone-by-milestone decomposition under anti-pattern #11 framing.
- **reconcile**: compare derived numbers to the seven published anchors above.
- **source-review**: Tier S full claim-by-claim; Tier A medium; Tier B per-figure quote review; Tier C/D scalar verdict.
- **consistency**: cross-leaf check against q1 (reviewed), q2 (reviewed), q3 (reviewed), q4 (reviewed). q6/q7 in-flight and will be caught by post-batch cross-consistency.
- **write**: leaf report rendered from claims.yaml, anti-pattern #12 motivation-first structure.

## Anti-pattern check

- ✓ No claims yet — research is gather-only
- ✓ Tier-tagged sources with structured extracts (Abstract / Key claims / Reviewer notes)
- ✓ All quote-block content is verbatim or labelled as paraphrase
- ✓ Tier E orientation-only sources NOT saved to `sources/`
- ✓ Calendar-year framings noted in PwC (2050) and AIAA-2025 mass-driver work — flagged for re-framing in write-pass per anti-pattern #11
- ⚠ Some Tier S/A PDFs (Jones 2020, Mueller 2022, IDA 2024, CLPA 2018, FSPS 2024 paywall) could not be parsed at the body level; abstracts and key claims reconstructed from secondary coverage. Calc pass does not depend on these specifically; reconcile pass should re-attempt body-level parse if a specific claim depends on details.
- ✓ No tier-B figure cards lift quotes that don't appear in cited containers; quote attribution is via Tier C/D press containers where applicable.
- ✓ Public-figure cards include explicit `public_figure: "Name"` frontmatter per protocol.
