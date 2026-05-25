---
slug: wright-kuznetsov-kloesel-2011
title: "A Lunar Electromagnetic Launch System for In-Situ Resource Utilization"
url: "https://ntrs.nasa.gov/api/citations/20110007073/downloads/20110007073.pdf"
fetched: 2026-05-25
fetcher: claude
tier: S
type: paper
peer_reviewed: true
venue: "IEEE Electric Ship Technologies Symposium / NASA NTRS"
authors: ["Michael R. Wright", "Steven B. Kuznetsov", "Kurt J. Kloesel"]
year: 2011
date: 2011-04-01
topics: [em-launch-engineering, mass-driver-historical, lunar-power-budget, capital-cost-mass-driver, projectile-materials]
---

## Abstract

Wright, Kuznetsov, and Kloesel (NASA / IEEE, 2011) present a Lunar Electromagnetic Launch (LEML) reference concept tied to NASA's Constellation-era human exploration architecture. The system uses a Mark-III double-sided linear induction motor (DSLIM) family with state-of-the-art TRL parameters to launch 2 kg LOX commodity payloads at 2.53 km/s (direct injection to L2 from a 33.1° E equatorial launch site). Total energy per shot, including 33% net efficiency, is 19.2 MJ. Energy storage is supplied by flywheels (G3-class derived from NASA Glenn satellite work) charged in ~16 minutes from a 20 kW dedicated bus on the Advanced Fission Surface Power System (AFSPSS). The authors then perform a cost-versus-benefit comparison against Ares-V heavy lift and reach a conclusion at odds with O'Neill-era optimism: "the conclusion, however, is not as favorable for LEML as originally suggested." Key culprits are the construction-mass-from-Earth requirement (initial LEML construction does not depend on ISRU per Assumption 5), the thermal-energy management problem at the launch interface, and the relatively modest realistic cycle rate. The paper is one of the few peer-reviewed sources in the post-1980s era that does a head-to-head bottom-up sizing exercise for a lunar mass driver against a chemical-rocket alternative — and reports a negative verdict for LEML under the assumed near-term architecture.

## Key claims

- velocity-budget: "Velocity required to reach L2 is 2.53 km/sec from the equatorial site near 33.10° E longitude" (Section III-C).
- energy-per-shot: "E = ½(2 kg)(2.53 km/s)² = 6.40 MJ × 3 (33% efficiency) = 19.2 MJ" per 2 kg payload (Section III-F).
- efficiency-decomposition: "33% total efficiency, decomposed as ~50% motor + ~66% power conversion + remaining losses; SCR packaging mass dominates" — silicon-controlled rectifier "package masses from 50 to more than 1000 times heavier than the silicon wafer masses."
- flywheel-storage: "A flywheel energy storage system would be possible having the specs shown in Table II [33]. Assuming 20 kW of the AFSPSS were dedicated for LEML launch, it would take 16 minutes (19.2 MJ/20 kW) to store the energy."
- payload-and-throughput: 2 kg LOX commodity payloads at low cycle rate; "incremental shipments of commodities" to an L2 depot.
- earth-construction-dependency: "Initial LEML construction will not depend on ISRU, i.e., will require materials and equipment from earth" (Assumption 5).
- negative-verdict: "The conclusion, however, is not as favorable for LEML as originally suggested" (Abstract). Recommendation pivots toward "a shorter, lower-energy track for point-to-point surface transportation."

## Reviewer notes

Tier S because this is the only peer-reviewed post-O'Neill primary technical paper sizing a lunar mass driver against a contemporary heavy-lift alternative (Ares-V) using TRL-grounded subsystems (DSLIM motors, G3-class flywheels). Their result is striking: the 1979 NASA Phase II-era $1/lb optimism does not survive a 2011 bottom-up sizing exercise that takes Earth-launched construction mass and SCR-bottlenecked power electronics seriously. The 2 kg payload size is much smaller than the O'Neill or Handmer designs (200 kg) — but the per-kg energy (~3.2 MJ/kg with their efficiency) is broadly consistent with the 2.4 MJ/kg canonical Lunarpedia figure. The negative cost-benefit conclusion sits in tension with the popular advocacy literature (tier C: Handmer, Science Array). Load-bearing for our calc pass: if the 2011 Wright paper is right that even a modestly sized LEML loses to chemical rockets in the early era, then the q2.c5 "$50/kg late-era" headline depends crucially on (a) massive throughput scale-up to 10 Mt/yr (vs Wright's small-payload, low-cycle design) and (b) accepting Handmer's $2-4B reactor figure rather than Wright's much larger system mass.
