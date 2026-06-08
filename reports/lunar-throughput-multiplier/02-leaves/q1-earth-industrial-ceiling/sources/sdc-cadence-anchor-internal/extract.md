---
slug: sdc-cadence-anchor-internal
title: "Starship Launch Cadence Constraints: Hard Numbers for Scaling Models (workspace anchor)"
url: "file:///Users/aviparrack/Avi-Claude/Workshop/Space/sdc/starship-launch-cadence-constraints.md"
fetched: 2026-06-08
fetcher: claude
tier: C
type: report
peer_reviewed: false
venue: "internal workspace compilation"
authors: ["Avi + Claude (workspace synthesis)"]
year: 2026
date: 2026-03-25
topics: [starship-cadence, lox-bottleneck, methane-supply, raptor-production, pad-cadence, atmospheric-impact, reuse-targets]
---

## Abstract

The SDC project's internal compilation aggregates and cross-references the primary industrial-input constraints for Starship-cadence scaling. As a workspace-internal source it is treated tier-C: a synthesis layer over primary tier-S/A/C citations, useful as a starting roadmap but not citable as primary evidence. Its key compiled figures are: per-stack propellant ~4,900 t (3,870 t LOX + 1,030 t LCH4; Block 2 baseline); total US O2 production ~10.3 Mt/yr (per EPA); LOX constraint thresholds at 100 / 500 / 1,000 / 1,200 / 10,000 launches/yr giving fractions 3.8% / 18.8% / 37.5% / 44.9% / 375% of US O2 production; Linde Starbase ASU at ~2,000 t/d ($100M); current Raptor production ~1/day; FAA-approved Boca Chica cadence 25 launches/yr (as of May 2025 FONSI). Each compiled number is keyed to a public primary URL in the SDC doc's source list.

## Key claims

- starship-block2-propellant: "Block 2 ~4,900 t propellant per stack (3,870 t LOX + 1,030 t LCH4)" — per SDC compilation, citing Wikipedia + Mobius.
- lox-binding-thresholds: At 2,660 launches/yr Starship LOX demand equals current US O2 production; soft ceiling ~130-270 launches/yr from existing supply before causing industrial disruption (5-10% of US output).
- linde-starbase-asu: "SpaceX's own on-site ASU at Starbase: approved July 2025, reportedly capable of 2,000 t LOX/day" — adds ~189 launches/yr of capacity.
- asu-capex-scaling: "3,000 t/d ASUs at ~$125M each, ~365 operating days/year, ~300 kWh/t average" — derived per-launch costs and power demand.
- raptor-production-2025: "Raptor 3 engines observed up to serial number 68 by November 2025, with regular truckloads of 3-4 engines leaving McGregor test site" — current production ~1/day, target 2-4/day.
- starship-pads-planned: ~5 pads by 2027 (Pad A + Pad B Starbase; LC-39A KSC; SLC-37 Cape Canaveral two pads).
- faa-boca-chica-25: "Boca Chica approved for 25 launches/year (up from 5), as of May 2025 FONSI."
- stainless-steel-anchor: At 10,000 new stacks/yr, steel demand is 3 Mt = 143% of US stainless production; for reusable fleet (500 vehicles × 20 flights = 10,000 launches), steel need is ~150 kt one-time, not binding.

## Reviewer notes

This is our own workspace synthesis. Use only as a roadmap to primary URLs and as cross-reference for derived numbers. **Do not cite SDC compilation as primary evidence** — instead cite its underlying URLs (Mobius, EPA, Wikipedia, FAA FONSI, NASASpaceFlight, etc.) from their own extract.md files where they are fetched separately. The summary's "single most important number" — ~2,660 Starship launches/yr is the hard LOX ceiling at current US O2 capacity — should be re-derived in the calc sub-pass first-principles, not borrowed.
