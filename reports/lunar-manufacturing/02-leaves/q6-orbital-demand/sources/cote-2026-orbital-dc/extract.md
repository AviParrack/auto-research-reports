---
slug: cote-2026-orbital-dc
title: "Do Orbital Data Centers Make Sense?"
url: "https://andercot.substack.com/p/do-orbital-data-centers-make-sense"
fetched: 2026-05-26
fetcher: claude
tier: C
type: blog
peer_reviewed: false
venue: "Andrew Cote's Substack"
authors: ["Andrew Cote"]
year: 2026
topics: [sdc-demand, ai-compute-orbit-coupling]
---

## Abstract

Andrew Cote's technical analysis of orbital data center economics
identifies bandwidth as the binding constraint rather than mass or
cost. For a 1 GW orbital DC, radiative cooling at 300 K requires
~2.6 km² radiator area, manageable within Starcloud's proposed 16 km²
envelope. Critical vulnerability: space-qualified chips lag commercial
H100 performance by 10-20×, neutralizing the cheap-orbital-energy
advantage. Global orbital comms capacity is "500-800 Tbps total"
while single ground DCs achieve 5-20 Tbps each — implying orbital
deployment is viable only for niche workloads served via in-space
laser cross-links, not for hyperscaler training workloads. Launch
costs at $1,000/kg currently, halving every few years per Cote.

## Key claims

- radiator-area-1gw: 1 GW system needs ~2.6 km² radiator at 300 K.
- starcloud-envelope: Starcloud's proposed deployment envelope is 16 km².
- space-qualified-perf-gap: Space-qualified chips "lag H100 perf by
  10-20×," erasing orbital energy economics.
- global-orbital-bandwidth-cap: 500-800 Tbps total orbital comms
  capacity vs 5-20 Tbps per single ground DC.
- niche-only-conclusion: Orbital DC viable only for specific niches
  (in-space processing via laser crosslinks), not hyperscaler
  replacement.
- launch-cost-current: $1,000/kg currently with reusable rockets;
  halving every few years.

## Reviewer notes

Tier C: credentialed-expert blog. Cote's bandwidth-constraint argument
is one of the most technically grounded skeptical positions in the
2026 literature. The 10-20× space-qualified-chip performance lag is
load-bearing — if true, the orbital DC market is fundamentally
niche-only at any launch cost. q6's source-review should explicitly
weigh Cote's bandwidth argument against the Handmer / Luminix
optimistic forecasts.
