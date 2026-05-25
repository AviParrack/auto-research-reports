---
slug: janhunen-2024-gravity-anomalies
title: "Launching mass from the Moon helped by lunar gravity anomalies"
url: "https://arxiv.org/abs/2410.09616"
fetched: 2026-05-25
fetcher: claude
tier: A
type: preprint
peer_reviewed: false
venue: "arXiv"
authors: ["Pekka Janhunen"]
year: 2024
date: 2024-10-12
topics: [em-launch-engineering, mass-driver-historical, alternative-architectures-tether]
---

## Abstract

Pekka Janhunen (arXiv:2410.09616, October 2024) shows that lunar mass-concentration ("mascon") gravity anomalies on the equatorial nearside can keep a projectile launched at sub-escape velocity (~1.7 km/s rather than 2.4 km/s) in lunar orbit for up to 9 Earth days before reimpacting. The 9-day window dramatically eases the projectile-catching problem that has dogged mass-driver concepts since the 1970s: instead of needing a precisely positioned active catcher synchronized to a projectile arriving on a hyperbolic trajectory within seconds, a tug spacecraft has days to rendezvous. The paper identifies at least three viable equatorial launch sites. Practically, this lowers the muzzle-velocity requirement by ~30% (1.7 km/s vs 2.4 km/s), which translates to roughly half the kinetic energy per kg (1.45 MJ/kg vs 2.88 MJ/kg) and corresponding reductions in track length or peak acceleration for a given payload mass. The author notes "passive projectiles can be made entirely from lunar material," eliminating the need for kick-motor circularization stages. The paper is a credentialed preprint (Janhunen is at FMI / Aurora Propulsion Technologies, a long-established space-physics figure) rather than a peer-reviewed paper, but the underlying celestial-mechanics analysis is straightforward enough that the result is likely robust.

## Key claims

- velocity-reduction: "Approximately 1.7 km/s (orbital speed)" rather than 2.4 km/s escape — ~29% reduction in launch velocity, ~50% reduction in kinetic energy per kg.
- orbital-duration: "A passive projectile can remain in lunar orbit for up to 9 Earth days" at specific equatorial nearside sites.
- viable-sites: "At least three locations identified on the lunar equator and nearside."
- catching-relaxation: "Extended orbital window provides prolonged opportunities for an active spacecraft to catch the projectile."
- material-self-sufficiency: "Passive projectiles can be made entirely from lunar material" — supports a closed-loop ISRU + mass-driver architecture.
- launcher-agnostic: "Suits multiple launcher architectures — coilgun, railgun, quenchgun, sling, or similar."

## Reviewer notes

Tier A (credentialed preprint, not yet peer-reviewed). The central celestial-mechanics result is the kind of finding that should hold up in review — mascon-induced orbital stability is well-documented in the lunar gravity literature (GRAIL mission etc.). For our q7 calc, this changes the energy-per-kg budget by ~50% in the favorable case and substantially relaxes one of the historically problematic engineering subsystems (catching). Cross-reference: the Handmer 2026 design uses 1.6 km/s muzzle velocity to LLO, in the same ballpark as Janhunen's anomaly-assisted 1.7 km/s. Combined, these two results suggest the modern engineering envelope has moved toward sub-escape launch + orbital tug, away from the O'Neill / NASA SP-428 escape-velocity-to-L5 architecture. Load-bearing if true: any q7 capital estimate built on a 2.4 km/s baseline is over-stating the energy budget by ~2×.
