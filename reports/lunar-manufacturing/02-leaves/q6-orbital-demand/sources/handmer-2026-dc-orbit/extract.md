---
slug: handmer-2026-dc-orbit
title: "Direct Current Data Centers"
url: "https://caseyhandmer.wordpress.com/2026/01/30/direct-current-data-centers/"
fetched: 2026-05-26
fetcher: claude
tier: C
type: blog
peer_reviewed: false
venue: "Casey Handmer's blog (Terraform)"
authors: ["Casey Handmer", "Matt Weickert"]
year: 2026
date: 2026-01-30
topics: [sdc-demand, ai-compute-orbit-coupling, sbsp-demand]
---

## Abstract

Handmer and Weickert argue that orbital deployment of GPU compute is
economically defensible at approximately 2× ground-based per-token
cost, particularly if SpaceX leverages Starlink hardware expertise.
Their thesis: GPUs are valuable enough per-gram that launching them
helps the economic utility of a watt of solar power. The unshaded
sun-synchronous orbital band (800-2500 km) provides 10^17 W of solar
flux available without battery storage. Their characterization of
orbital deployment as "essentially glorified Starlink satellites with
a bunch of GPUs attached" emphasizes the architectural similarity to
existing constellations. The post argues the bypass of terrestrial
permitting and grid congestion is the principal economic advantage,
not raw cost parity.

## Key claims

- 2x-cost-premium: SpaceX could ship gigawatts of inference compute
  to orbit at "~2× the per-token cost of ground-based AI" while
  remaining "quite profitable."
- sso-no-batteries: Sun-synchronous orbits 800-2500 km altitude are
  never in shade (except rare lunar eclipses), eliminating battery
  storage requirement.
- sso-band-capacity: The unshaded SSO band provides "10^17 W
  available" — i.e., 100 PW of solar flux.
- gpu-per-gram-value: GPUs are valuable enough per-gram that even
  launching them to orbit improves the economic utility of a watt of
  solar power.
- starlink-similarity: Orbital data centers are "essentially glorified
  Starlink satellites with a bunch of GPUs attached" — emphasizes the
  architectural inheritance from existing constellation operations.

## Reviewer notes

Tier C: credentialed-expert blog. Handmer is a former JPL engineer,
Terraform CEO, and one of the most influential public voices on
space-economics. The 2× cost premium claim is the most-cited Handmer
position on orbital compute viability. Tier C scalar verdict applies;
Handmer's specific quoted statements that bear on q6 are also
catalogued as a tier B public-figure quote review.
