[codex cli ok]
```yaml
overall:
  verdict: weak
  summary: "The headline arithmetic reproduces, but the 20-year mass is fractional amortization, not a literal replacement schedule. Several sizing knobs are plausible lower bounds, while the TAI <1 yr milestone path is physically contradicted."

findings:
  - target: "headline arithmetic"
    target_kind: topic
    verdict: pass
    reason: "311.5 t = 25 + 125 + 75 + 31.5 + 40 + 15. The capex totals also reproduce: BAU $167.315B, IE $1.161B, TAI $0.00947B."
    severity: low

  - target: "721.8 t over 20 years"
    target_kind: claim
    verdict: partial
    reason: "721.8 t = sum(mass * 20 / lifetime), so it is a smooth amortized service-flow mass. A discrete replacement schedule over 20 years would be about 801 t if replacements at years 8, 12, 15, 16, etc. are counted."
    severity: medium

  - target: "25 t habitat for 4-person 12-mo independent ops"
    target_kind: claim
    verdict: partial
    reason: "It is plausible as a B330-class pressure-volume lower bound, but weak for true 12-month independent lunar surface operations. Gateway is 63 t fully assembled for 4 crew in non-permanent lunar orbit, and ISS scale is far larger; the calc under-specifies airlocks, radiation shielding deployment, ECLSS redundancy, medical/suit logistics, and spares."
    severity: medium

  - target: "125 t for 500 kWe FSP at 250 kg/kWe"
    target_kind: claim
    verdict: supports
    reason: "The arithmetic is exact, and 250 kg/kWe is defensible against NASA FSP targets: NASA specified under 6 t for 40 kWe, but later concept work also discusses roughly 10 t for 40 kWe. Scaling linearly to 500 kWe is still a simplification."
    severity: low

  - target: "75 t ISRU plant for 1000 t/yr output"
    target_kind: claim
    verdict: weak
    reason: "75 t implies 75 kg of plant per t/yr of annual output after redundancy, or 50 kg/(t/yr) before redundancy. That is aggressive versus published lunar propellant sizing around 109 kg/(t/yr) for plant alone and regolith metals/O2 studies near 140 kg/(t/yr); mixed propellant plus structural materials likely needs excavation, beneficiation, thermal, cryo, storage, and maintenance mass not fully counted."
    severity: high

  - target: "31.5 t mobility fleet"
    target_kind: claim
    verdict: weak
    reason: "The arithmetic is right: (20*500 + 10*100 + 5*2000)*1.5 = 31.5 t. The per-unit rover masses are plausible for scout-class vehicles, but low for a 1000 t/yr industrial excavation, hauling, construction, repair, and dust-survival fleet."
    severity: medium

  - target: "40 t manufacturing complement"
    target_kind: claim
    verdict: unsupported
    reason: "30 t of equipment plus 10 t seed stock is a plausible pilot-shop placeholder, not a derived manufacturing base. Electronics assembly, precision motors, bearings, QA/metrology, tooling, clean environments, and spare tooling are not sized."
    severity: medium

  - target: "15 t infrastructure"
    target_kind: claim
    verdict: weak
    reason: "Counting only comms, sensors, and landing-pad heads is optimistic. The mass budget appears to omit or bury power distribution, cryogenic storage, tanks, cables, thermal control, shelters, cranes/fixtures, and pad construction support."
    severity: medium

  - target: "hardware cost per kg knobs"
    target_kind: topic
    verdict: partial
    reason: "$100k/kg is plausible for BAU aerospace if interpreted as flight-hardware-ish cost, but historical $/kg figures often include development and integration, so the separate dev term risks double counting. $10k/kg is an optimistic mass-production regime; $1k/kg for human-rated lunar nuclear/habitat/ISRU hardware is unsupported."
    severity: high

  - target: "dev-cost = first-set hardware * 3 / sqrt(time_compression)"
    target_kind: claim
    verdict: weak
    reason: "The BAU math is clear: 311.5 t * $100k/kg * 3 = $93.45B. The 3x first-unit factor is a rough analogy; the square-root time-compression discount is arbitrary and may have the sign wrong unless automation, not schedule compression, is doing the work."
    severity: high

  - target: "25 yr BAU to 5 yr IE to <1 yr TAI"
    target_kind: claim
    verdict: contradicted
    reason: "The TAI schedule puts 'first crewed sustained occupation (12 mo)' at 0.4 years, which cannot mean completion of a 12-month occupation. Hardware fabrication, environmental qualification, nuclear handling, launch/transit, surface commissioning, and failure discovery impose physical lead-time floors even with perfect design automation."
    severity: high

  - target: "TAI degenerate case handling"
    target_kind: section
    verdict: partial
    reason: "The prose flags the degeneracy honestly, but the table still presents $0.01B and <1 yr as if the same model remains meaningful. A stronger treatment would stop the cost model or add irreducible physical/qualification lead-time floors."
    severity: medium

  - target: "sources sealed / first-principles claim"
    target_kind: topic
    verdict: partial
    reason: "Several inputs are not first-principles derivations: B330 mass, NASA FSP kg/kWe, Metzger/Pelech/Sowers phi anchors, q1 launch costs, hardware $/kg, and Shotwell/Metzger milestone anchors. That is acceptable if labeled as benchmark anchoring, but not as sealed first-principles derivation."
    severity: medium

notes:
  - issue: "Minor mismatch: the Python header says seven mass-budget components, but the actual capital list has six because cargo landing capability is excluded as transport cost."
    severity: low
  - issue: "External benchmark links used: NASA ISS facts https://www.nasa.gov/international-space-station/space-station-facts-and-figures/ ; NASA Gateway FAQ https://www.nasa.gov/gateway-frequently-asked-questions/ ; NASA FSP https://www.nasa.gov/centers-and-facilities/glenn/nasas-fission-surface-power-project-energizes-lunar-exploration/ ; B330 lunar-station NTRS https://ntrs.nasa.gov/citations/20150020448 ; ISRU sizing paper https://bigidea.nianet.org/wp-content/uploads/2019/10/Cost_Breakeven_Analysis_of_Cis-Lunar_ISRU-FINAL.pdf"
    severity: low
```