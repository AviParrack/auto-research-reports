---
slug: coilgun-wiki-engineering
title: "Coilgun engineering reference (Wikipedia)"
url: "https://en.wikipedia.org/wiki/Coilgun"
fetched: 2026-05-25
fetcher: claude
tier: E
type: reference
peer_reviewed: false
venue: "Wikipedia"
authors: ["Wikipedia community"]
year: 2025
date: 2025-01-01
topics: [em-launch-engineering, capacitor-bank-engineering]
---

## Abstract

Coilgun reference. Sequential coil activation accelerates ferromagnetic or conducting projectiles without sliding contact (vs railgun). Inherent low-speed efficiency limitations due to coil heating; efficiency improves at higher velocities as mechanical power scales v² while resistive losses stay constant. Demonstrated peak: 1978 Soviet record, 2-gram ring reaching 5,000 m/s over 1 cm. Modern DARPA 45-stage coilgun mortar achieves only ~22% efficiency despite sophisticated engineering. Hobbyist designs typically <1% to several percent efficiency.

## Key claims

- velocity-record-historical: "1978 Soviet record: a 2-gram ring reaching 5,000 m/s over just 1 centimeter."
- darpa-coilgun-efficiency: "Modern military research, including DARPA's 45-stage mortar design, achieves only 22% efficiency despite sophisticated engineering."
- hobbyist-efficiency: "Modern hobbyist designs operate at under one percent to several percent efficiency."
- saturation-limit: "Magnetic saturation in ferromagnetic projectiles reduces efficiency gains beyond saturation point, despite increased current."
- ringing-loss: "Uncoupled magnetic flux creates 'ringing' effects that can damage capacitors, requiring protective diodes that dissipate remaining energy as heat."
- railgun-comparison: "Coilguns avoid hypervelocity physical contact and erosion by keeping projectiles centered within coils rather than sliding against bore walls."

## Reviewer notes

Tier E (Wikipedia reference, orientation only). Captured for the engineering ceiling claim: state-of-the-art demonstrated multi-stage coilgun efficiency (DARPA, 45 stages) is ~22%, significantly lower than the 96.4% claimed in the 1979 NASA SP-428 chapter or the 33% Wright et al. 2011 use. This is the load-bearing data point for re-thinking the q7 energy budget: if a lunar mass driver achieves ~25% net efficiency (between 22% terrestrial demonstrated and 33% Wright's NASA-flow estimate), the required input energy per kg is ~4× the kinetic energy (i.e. ~9.6 MJ/kg for 1.7 km/s launches, not 2.4 MJ/kg). This 4× factor matters for the lunar power budget — at 10 Mt/yr nameplate throughput, kinetic power 540 MW vs Handmer's 450 MW figure (which assumes ~90% driver efficiency).
