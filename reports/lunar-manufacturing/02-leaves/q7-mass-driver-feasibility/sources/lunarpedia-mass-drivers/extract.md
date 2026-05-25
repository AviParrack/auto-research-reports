---
slug: lunarpedia-mass-drivers
title: "Mass Drivers — Lunarpedia"
url: "https://lunarpedia.org/w/Mass_Drivers"
fetched: 2026-05-25
fetcher: claude
tier: E
type: reference
peer_reviewed: false
venue: "Lunarpedia wiki"
authors: ["Lunarpedia community"]
year: 2024
date: 2024-01-01
topics: [em-launch-engineering, mass-driver-historical, lunar-power-budget]
---

## Abstract

Lunarpedia's Mass Drivers page is a community-curated technical summary of the canonical mass-driver design space. The article establishes 2.4 MJ/kg (including 20% energy losses) as the baseline energy needed to launch material from the Moon at orbital velocity of ~2,000 m/s. It outlines three acceleration profiles (passenger 2g / cargo 20g / high-acceleration 200g) with corresponding track length and power-density requirements that span two orders of magnitude. The page notes that mass drivers below escape velocity require additional propulsion or a downstream catcher because launched objects will return to the surface — a constraint the 2024 Janhunen paper substantially relaxes via mascon-assisted orbits. Lunarpedia is tier E (community wiki, orientation only) but is cross-referenced here because the 2.4 MJ/kg figure is the de facto canonical energy reference in the field, including in the q2-lunar-ascent-cost claims.

## Key claims

- canonical-energy: "2.4 MJ/kg (including 20% energy losses) represents the baseline energy needed to launch material from the Moon at orbital velocity of 2,000 m/s."
- acceleration-profiles: "Passenger transport (2g): 100 km track, 24 kW/kg power. Cargo (20g): 10 km track, 240 kW/kg power. High-acceleration cargo (200g): 0.5 km track, 2,400 kW/kg power."
- aluminum-comparison: "For aluminum-oxygen propulsion achieving 2,000 m/s, the energy required to produce this aluminum is 110 MJ, or about 28 times the exhaust energy when accounting for embodied manufacturing energy" — energy advantage of mass driver vs propellant production.
- sub-escape-constraint: "Mass drivers cannot independently achieve orbit — launched objects below escape velocity will return to the surface" unless an active catcher or mascon-orbit assist is used.
- first-system-concept: "First system launches 10-kilogram payloads containing small circularization rockets, using magnetic capture nets on orbital platforms for retrieval."

## Reviewer notes

Tier E (community wiki) and not citable as primary evidence per the source-tiers rule. Captured here only to anchor the 2.4 MJ/kg canonical energy figure used in q2.c5. The acceleration-vs-track-length trade scaling (linear inverse: 100 km for 2g, 10 km for 20g, 0.5 km for 200g) is straightforward kinematics — v² = 2as, so for v=2 km/s, a track of length s requires acceleration a = v²/2s, and the Lunarpedia numbers check out (2 km/s requires 200 m/s² over 10 km, ~20 g). This kinematic ceiling is load-bearing for q7's calc pass.
