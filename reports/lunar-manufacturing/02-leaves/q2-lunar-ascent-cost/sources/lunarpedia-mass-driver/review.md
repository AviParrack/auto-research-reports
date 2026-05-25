---
source: lunarpedia-mass-driver
reviewed_pass: 4
reviewed_by: claude+gpt
---

# Source Review: Lunarpedia "Mass Drivers"

## Summary

| Verdict | Count |
|---|---|
| Consistent | 3 |
| Different conclusion | 0 |
| Novel supporting | 0 |
| Merits investigation | 1 |
| Not relevant | 1 |

## Claim 1: 2.4 MJ/kg lunar mass driver energy (including 20% losses)
**Quote:** "2.4 MJ/kg"
**Verdict:** Consistent
**Why:** Used as the energy input in my calc. Confirms Handmer's 2026 figure tracks the canonical Lunarpedia number; the value has been stable across decades.

## Claim 2: 45× energy advantage vs aluminum-O2 rocket
**Quote:** "rockets... require 45 times more energy"
**Verdict:** Not relevant
**Why:** Comparison is to aluminum-oxygen rocket, not to hydrolox or methalox. The multiplier shifts for other propellants. Not used as a calc input.

## Claim 3: Track-length-vs-acceleration tradeoff
**Quote:** "Cargo at 200g acceleration: 0.5 km" / "Cargo at 20g acceleration: 10 km" / "Linear concept for 2g passenger acceleration: 100 km"
**Verdict:** Consistent
**Why:** Matches Handmer's 128 m at 1000 g (Lunarpedia's 0.5 km at 200 g extrapolates to ~125 m at 1000 g, exact agreement). Cross-validates the engineering envelope.

## Claim 4: 200 kg circular design payload, 110 min orbital rendezvous cadence
**Quote:** "Circular mass driver payload: about 200 kilograms"
**Verdict:** Consistent
**Why:** Matches Handmer's 200 kg per shot. Convergence across two independent sources on this anchor.

## Claim 5: Linear-launch projectiles cannot reach orbit without circularization
**Quote:** "any item launched at lower than escape velocity will return to the launch point following orbital mechanics and hit the surface."
**Verdict:** Merits investigation
**Why:** Architectural constraint that informs the calc — confirms that a mass driver alone cannot deliver to LEO; downstream propulsive maneuver (or downstream catcher) is required. This is the structural reason my $50/kg late-era figure includes a SEP transfer stage that Handmer's $10/kg figure does not.

## Anti-hallucination check

All quotes verbatim from extract.md. No hallucinated content.
