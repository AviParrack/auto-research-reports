---
slug: handmer-mass-driver-2026
title: "How to build a lunar mass driver"
url: "https://caseyhandmer.wordpress.com/2026/05/08/how-to-build-a-lunar-mass-driver/"
fetched: 2026-05-25
fetcher: claude
tier: C
type: blog
peer_reviewed: false
venue: "Casey Handmer's blog"
authors: ["Casey Handmer"]
year: 2026
date: 2026-05-08
topics: [em-launch-engineering, capacitor-bank-engineering, projectile-materials, lunar-power-budget, capital-cost-mass-driver, mass-driver-historical]
public_figure: "Casey Handmer"
---

## Abstract

Handmer presents a detailed engineering sketch of a lunar mass driver targeted at lunar low orbit (LLO) rather than escape. The headline design: 128 m main acceleration track, 1000 g, 1.6 km/s muzzle velocity, 200 kg payload per shot at 1 shot every 3 seconds, 10 Mt/yr nameplate throughput. Average kinetic power 450 MW, peak instantaneous power ~16 GW at midpoint of acceleration, requiring an active pulsed-power subsystem (capacitors and/or flywheels). The energy budget is dominated by the launch reactor, estimated at $2-4B if Earth-built. Handmer treats the rest of the system (track, magnets, sled, recovery, anchoring, projectile capture) at a sketch level. His framing is engineer-advocate rather than skeptic: the concept "does not violate the laws of physics" and can be Earth-tested at costs "reasonable in comparison to Starship development." The post lands at an aspirational $10/kg headline price for "rocks in lunar orbit," excluding the SEP transfer leg from LLO to LEO. Handmer is explicit that mass drivers do not become economically competitive against Starship at current launch costs (~$100/kg) until orbital deployment scales past ~100 TW/yr of capacity — a regime he expects only when the Earth launch supply curve binds.

## Key claims

- track-and-acceleration: "1,000 g acceleration, 128 m main track + 128 m sled recovery = 256 m total, launch velocity 1.6 km/s to lunar low orbit."
- throughput: "10 million tonnes per year nameplate, ~1 tonne every 3 seconds, 200 kg payload per shot, sled mass 1000 kg loaded / 800 kg empty, 0.64 s complete launch cycle."
- power-and-reactor: "Kinetic power 450 MW; peak instantaneous power 16 GW at midpoint of track; for reference, a reactor of this scale would typically cost $2-4B on Earth and weigh perhaps 1000 T."
- power-cost: "Assuming that 10% of this revenue pays for the power plant, this works out to $2.50/kWh, which is about 10x higher than a typical US rate payer in 2026."
- payload-material: "Raw lunar basalt (volcanic rock chemically similar to Earth basalts). Moon rocks are launched in their raw state because rocks tolerate 1,000 g acceleration without damage; processing occurs in orbit using abundant solar power."
- engineering-feasibility-stance: "Lunar mass drivers do not violate the laws of physics. Their tech can be developed and tested thoroughly in labs on Earth at prices that are reasonable in comparison to Starship development costs."
- economic-threshold: "Mass drivers become economically competitive against Starship only beyond ~100 TW/year of orbital deployment — a threshold decades away unless Earth launch becomes supply-constrained."
- unresolved-engineering: "Sintered magnet blocks 9 m long under 1000g shear and oscillating tension fatigue is not obviously feasible." Pulsed power infrastructure (capacitor banks / flywheels for 16 GW at 1.5 Hz) may dominate system mass and cost. Velocity dispersion >10^-4 makes projectiles orbital debris without an active catcher.

## Reviewer notes

This is the closest thing we have to a load-bearing modern engineering brief on a lunar mass driver — but it is a blog post, not a peer-reviewed paper, and Handmer himself states the design is a sketch. The reactor figure ($2-4B Earth-built, ~1000T) is the only enumerated capital number; total mass-driver capital is not stated. Our $10B aggregate figure in q2.c5 is an extrapolation, not Handmer's number. Several engineering issues (magnet fatigue under cyclic 1000g loading, GW-scale pulsed power at 1.5 Hz, projectile catching with 10^-4 velocity precision) are flagged but not resolved in the post. The $10/kg headline is for "rocks in lunar orbit" — not LEO — and assumes the system runs at 10 Mt/yr nameplate throughput. At a more realistic ramp-up, the per-kg figure rises substantially. Cross-reference to Casey-Handmer-public-figure tier-B review for stance on feasibility timeline.
