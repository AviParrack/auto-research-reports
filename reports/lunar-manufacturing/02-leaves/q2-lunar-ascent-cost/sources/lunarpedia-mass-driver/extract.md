---
slug: lunarpedia-mass-driver
title: "Mass Drivers (Lunarpedia)"
url: https://lunarpedia.org/w/Mass_Drivers
year: 2024
authors: ["Lunarpedia contributors"]
fetched: 2026-05-25
fetcher: claude
type: reference
---

# Lunarpedia — mass driver parameters

Community-maintained reference focused specifically on lunar applications.

## energy-and-dimensions

- **Energy per kg:** "2.4 MJ/kg" for lunar mass driver launches (including 20% energy losses)
- **Energy advantage vs chemical:** "rockets... require 45 times more energy" for aluminum-oxygen propulsion (compares aluminum-O2 ISRU rocket to electromagnetic launcher)
- **Linear track length for 2g passenger acceleration:** "100 km"
- **Cargo at 20g acceleration:** "10 km"
- **Cargo at 200g acceleration:** "0.5 km"
- **Circular design payload:** "about 200 kilograms"

## throughput

- **First lunar driver concept:** "10 kilogram loads launched once a minute or better"
- **Circular track:** "orbital rendezvous every 110 minutes"
- **Power requirements for circular design:** "43 kilowatts average power"

## structural-constraint

"Any item launched at lower than escape velocity will return to the launch point following orbital mechanics and hit the surface."

This is the critical architectural constraint: a lunar mass driver alone cannot put payload into a stable orbit. Either (a) the driver achieves escape velocity (2.38 km/s for the Moon) plus a small downstream correction, or (b) the projectile uses an attached propulsion stage for circularization, or (c) a downstream catcher (e.g., at L2) collects the projectiles.

## relevance-to-q2

The 2.4 MJ/kg energy figure is the canonical anchor. At $2.50/kWh assumed lunar power (Handmer 2026), this is 2.4 MJ × $2.50/kWh × (1/3.6 MJ/kWh) = **$1.67/kg in raw electricity cost**. The full delivered-to-LEO cost via mass driver is dominated by:
- Capital amortization of the driver track + reactor
- Propellant for circularization / LEO insertion
- Lunar-ops premium on everything

This source confirms the "energy is cheap, capital is expensive" framing.

## limitations

- Community wiki — vintage of specific numbers unclear
- Does not provide an integrated cost-per-kg estimate to LEO
- The 45× energy advantage figure compares to a specific aluminum-O2 ISRU rocket, not to imported hydrolox; the multiplier is different for other propellants
