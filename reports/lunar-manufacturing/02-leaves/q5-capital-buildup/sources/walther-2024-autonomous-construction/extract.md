---
slug: walther-2024-autonomous-construction
title: "Autonomous construction of lunar infrastructure with in-situ boulders"
url: https://www.frontiersin.org/journals/space-technologies/articles/10.3389/frspt.2024.1345337/full
fetched: 2026-05-26
fetcher: claude
tier: S
type: paper
peer_reviewed: true
venue: "Frontiers in Space Technologies, Vol. 5"
authors: ["Jonas Walther", "Ryan Luke Johns", "Hendrik Kolvenbach", "Valentin Tertius Bickel", "Marco Hutter"]
year: 2024
date: 2024-04-01
topics: [autonomy-construction, lunar-base-architecture, robotic-assembly, staged-buildup-milestones]
public_figure: null
---

## Abstract

Verbatim: "Significant infrastructure is required to establish a long-term presence of humans on the lunar surface. In-situ resource utilization (ISRU) is a fundamental approach to ensure the viability of such construction. Here, we investigate the feasibility of constructing blast shields as one example of lunar infrastructure using unprocessed lunar boulders and an autonomous robotic excavator." The study models a 10 m³ payload-capacity excavator deploying in-situ boulders to construct quarter-ring blast shield segments. Construction throughput is ~174-193 m² per operational day; one quarter-ring (~314 m perimeter) requires 1,440-1,520 operational hours (~75-80 days at 20 hrs/day operation). The path-planning combines A* with greedy targeting under terrain-slope constraints. The paper does not provide a capital-cost estimate, an excavator-design TRL, or a system-level mass-to-surface number; it is a feasibility study at the planning-algorithm and throughput-arithmetic level.

## Key claims

- in-situ-boulders-construction: "An autonomous robotic excavator can use unprocessed lunar boulders to construct quarter-ring blast shield segments"
- throughput-174-193-m2-day: "Construction throughput approximately 174-193 m² per operational day"
- quarter-ring-1440-1520-hrs: "1,440-1,520 operational hours to build a quarter-ring blast shield segment"
- 10m3-payload-excavator: "10 m³ payload capacity for boulder collection"
- excavator-needs-development: "An excavator capable of operating in the lunar environment needs to be developed" — i.e. the hardware is not at deployment TRL today
- automation-stack: "Autonomous path planning using A* algorithm, greedy targeting, payload management, and terrain slope constraint enforcement"

## Reviewer notes

A purely demonstrational study — establishes that the autonomy-stack is solvable, but explicitly defers the hardware-development question. Load-bearing for q5 at a qualitative level: shows that in-situ-boulders-only construction (no regolith processing, no sintering) is achievable with one well-designed excavator, which is a much lower-mass / lower-capex path than processed-regolith methods (compare metzger-autry-2022-landing-pads' microwave sintering). Notably absent: cost in dollars, mass landed, TRL assessment, deployment timeline. Useful as evidence that the construction-throughput problem is bounded and tractable, not as a cost benchmark. Cross-leaf relevance: the lower-capex construction path matters for q5 buildup scenarios where Earth-launch mass dominates.
