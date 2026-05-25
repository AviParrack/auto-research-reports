---
pass: 3
kind: response
leaf: q6-orbital-demand
date: 2026-05-26
status: done
audit_responded: passes/pass-03-audit.md
---

# Pass 3 — Response to Codex audit

Codex returned `partially_defensible` on the reconcile reasoning with
five findings (one high, two medium, two low) and three flat notes.

## Accepted

- **Cote bandwidth ceiling resolution under-supported (high)**: Codex caught that my OISL bypass, AI-training-not-inference, and 200 GW fallback ceiling arguments added uncited assumptions beyond what Cote's extract actually says. Cote-from-extract supports "niche-only" not "5× compression to 200 GW." Accepted: the reconcile prose was too confident. q6.c14 already states the bandwidth ceiling at medium confidence; clarifying that the 200 GW fallback estimate is my synthesis, not Cote-source-attributed.

- **NASA OTPS vs BAU SBSP 5 GW resolution (medium)**: Codex correctly noted that "strategic + niche" reconciliation isn't directly supported by the extracts at the 5 GW magnitude. Accepted: q6.c4 confidence downgraded from high to medium. The qualitative direction (BAU SBSP > 0 via strategic deployment) is defensible; the specific 5 GW figure is anchored to fewer sources than I claimed.

- **q6.c6 conditionality (medium)**: Codex correctly noted that the necessary-but-not-sufficient framing is conditional on the TAI-C demand scenario obtaining, not a source-settled resolution. McCalip's cost-critique does NOT inherently apply to BAU only. Accepted: claim text and evidence array updated with conditional framing and inclusion of mccalip-quote-fomo as `verdict: contradicts`.

- **q6.c6 evidence array missing source support (low)**: Codex noted the claim still listed only first-principles-calc evidence. Updated: added metzger-2023-economics (supports), handmer-2026-dc-orbit (partial), introl-2026 (supports), mccalip-quote-fomo (contradicts).

- **pass-03-audit.md missing (medium)**: Codex correctly noted the reconcile prose referenced an audit file that didn't exist yet. Created now (this audit run); the prose was forward-referencing the audit I was about to run.

- **High-tier extracts via secondary aggregators (medium)**: Codex correctly flagged that for source-review pass 4, NASA OTPS / NASA M2M / Metzger 2023 / Kornuta 2019 PDFs weren't directly parsed. The pass-01-research.md already flagged this. Pass 4 source-review will treat those as "secondary-cited primary" — tier S in terms of authority, but the depth of claim-by-claim review is constrained by what's reachable through the secondary aggregators. Acknowledging in pass 4.

## Disputed / clarified

- **McCalip vs Handmer BAU/TAI-C mapping (low)**: Codex notes this is the author's scenario framing, not source-settled. Agreed in characterization; the mapping is my reconciliation device, not a direct quote from either figure. Holding the framing because it produces a defensible bracket for q6.c2 regime range — McCalip is operating in a regime where compute demand does NOT scale enough to justify orbital deployment (his "FOMO" framing), while Handmer is operating in a regime where SpaceX-internal integration + scale produces favorable inference economics. The regime labels (BAU / TAI-C) are sensible if the regimes are defined by AI-compute-demand-growth-rate. Keeping the framing.

## Notes engaged

- **OISL scaling and training-vs-inference bandwidth (high-severity Cote finding)**: My reconcile prose claimed the 200 GW fallback ceiling but did not cite a specific source establishing OISL scaling beyond Starlink's current architecture. Acknowledged in q6.c14 audit notes that the 200 GW figure is my synthesis, not source-derived. Future iteration should add a tier S/A source on OISL bandwidth scaling.

## Updated stance

Codex's audit was substantively correct on the three highest-severity
findings (Cote, NASA OTPS, q6.c6 conditionality). The reconcile
prose was over-confident on the OISL argument and the 5 GW SBSP
"strategic + niche" floor. Both have been downgraded with
appropriate confidence levels.

Net effect on the headline answer: unchanged. The regime decomposition
(stall / BAU / TAI-C) still brackets demand across three orders of
magnitude; SDC still dominates under BAU+TAI-C; the q1-q6
demand-elasticity-cost coupling still drives the lunar-manufacturing
necessary-but-not-sufficient conclusion. The corrections sharpen
the conditional claims without changing the qualitative direction.

No findings rejected. q6.c4 and q6.c6 updated with explicit
conditional framing and revised confidence labels.
