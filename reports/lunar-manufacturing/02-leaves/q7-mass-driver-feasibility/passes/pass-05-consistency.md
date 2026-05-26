---
pass: 5
kind: consistency
leaf: q7-mass-driver-feasibility
date: 2026-05-25
status: done
---

# Pass 5 — Consistency: q7 vs reviewed siblings

Cross-leaf claim comparison. Per the parallel-execution caveat: I check q7 against the four leaves `reviewed` at run start (q1, q2, q3, q4). Siblings q5 and q6 are running concurrently and will be caught by the post-batch `--pass cross-consistency`.

## Topic-aligned comparison

### Topic: capital-cost-mass-driver — q2 vs q7 (THE LOAD-BEARING ROW)

| Source | Claim | Number |
|---|---|---|
| **q2.c5** | "Mass driver + SEP transfer lunar-surface-to-LEO cost per kg, under a $10B capital assumption and 20-year amortization, scales from $528/kg (early era, 100k t/yr nameplate, 20% availability) to $152/kg (mid, 1M t/yr nameplate, 60%) to $50/kg (late, 10M t/yr nameplate, 85%)" | $10B capital |
| **q2.c11** | "Casey Handmer's May 2026 lunar mass driver design specifies 200 kg per shot... reactor alone estimated at $2-4B Earth-built; total mass-driver capital is not enumerated in the extract — my calc's $10B aggregate is an extrapolation" | $10B (extrapolated, not Handmer-stated) |
| **q7.c6** | First-principles BAU capex: ~$1,242B (1 Mt/yr architecture); track + drive coils dominate at $1,200B with sourced-prior 200× lunar construction multiplier | $1,242B BAU |
| **q7.c8** | Regime sensitivity: BAU $1,242B / IE $127B / TAI $13.3B | $13.3B under TAI compression |

**Verdict:** **Major contradiction at BAU; reconciled at TAI-grade.**

q2.c5's $10B is roughly 100× lower than q7.c6's BAU. The convergence at TAI-grade ($13.3B) suggests that q2.c5 implicitly assumes TAI-grade economics for the mass-driver capital line — but q2.c5's prose frames the $10B as a "late-era" figure without explicit TAI conditioning. This is the load-bearing inter-leaf contradiction the report's headline crossover hinges on.

**Action:** Add to q7's `contradictions_with: [q2]`. The cross-consistency / synthesis pass should explicitly bridge this — either q2.c5 needs to relabel as TAI-conditional, or q2's late-era headline needs an alternative scenario at BAU compression (which would give $300-500/kg-class numbers, not $50/kg).

### Topic: TAI-compression-em-launch — q2 vs q7

| Source | Claim |
|---|---|
| **q2.c7** | "Under industrial-explosion / TAI-grade automation pressure, lunar surface operations could compress 10×, ISRU propellant cost 5×, hardware amortization 3×, and mass driver throughput 10×. The combined effect drops chemical-aggressive-ISRU-late from $994/kg to roughly $150-250/kg, and mass-driver mid-era from $152/kg to roughly $30/kg." |
| **q7.c8** | Regime sensitivity: BAU 1× / IE ~10× / TAI ~100× capex compression |

**Verdict:** **Consistent.** Both leaves use similar regime-compression framing. q2's 10× compression matches q7's IE regime; q2 does not enumerate TAI separately, but q2.c7's "decade earlier" framing is structurally consistent with q7's TAI-grade ~$13B / 1.5-yr-to-operational.

### Topic: em-launch-engineering — q2 vs q7

| Source | Claim |
|---|---|
| **q2.c11** | Handmer's design: 200 kg/shot, 1 t per 3 s cadence, 128 m track, 10 Mt/yr nameplate, $2-4B reactor, 2.4 MJ/kg energy. The $10/kg price is for "rocks in lunar orbit" — output state is at LLO not LEO. |
| **q7.c1, c2, c4, c5** | Kinematics, energy budget, power requirements at matched parameters. |

**Verdict:** **Consistent.** q7's kinematic derivation reproduces Handmer's specifications. The reactor figure ($2-4B Handmer-stated, $3B q7-derived for 200 MW class including shipping) is within range. q7 is more conservative on power (894 MW vs Handmer's 450 MW) only because of efficiency assumption (η=0.50 vs Handmer η=0.90); at matched efficiency the numbers agree.

### Topic: gear-ratio-framework — q4 vs q7

| Source | Claim |
|---|---|
| **q4.c1** | "Propellant use ratio Γ_LEO ≈ 14 under chemical LOX/LH2 reusable round-trip from lunar surface. This makes LEO the hardest cislunar destination." |
| **q4.c9** | "Lunar propellant achieving absolute advantage at LEO in Metzger's model requires non-chemical delivery architecture — specifically SEP (solar electric propulsion) with molecular water propellant at I_sp ≈ 2000 s." |
| **q4.c12** | "Solar electric propulsion (SEP) with molecular water propellant at I_sp ≈ 2000 s used on the lunar-product return leg can drop Γ_LEO from approximately 14 to approximately 1." |
| **q7.c1, c8, c11** | Mass driver at v_LLO + SEP transfer is the q2-q4-q7 architecture that makes LEO economically reachable. |

**Verdict:** **Strongly consistent and load-bearing.** q4's gear-ratio framework establishes that LEO is structurally unreachable from the Moon under chemical-only delivery (Γ_LEO ≈ 14). q4 identifies mass driver + SEP as the architectural fix. q7 provides the engineering feasibility analysis of that architectural choice. **The chain q4 → q7 → q2 → q8 is the central architectural argument of the report.**

### Topic: industrial-explosion-compression / tai-acceleration — q1 / q3 / q7

| Source | Claim |
|---|---|
| **q1.c7** | "Under industrial-explosion / TAI-grade automation pressure, refurbishment labor could compress ~10×, launch cadence rise ~10×, ground-operations cost compress ~5×." |
| **q3.c8** | "TRL trajectory for every ISRU process is acceleration-regime dependent, not calendar-year dependent. Under TAI-compression... carbothermal and MRE plausibly reach TRL 8 within a few years of present. Under business-as-usual, the same milestones land roughly a decade later. Under a 50-year-Apollo-drought stall, processes remain at their 2024-2026 baselines indefinitely." |
| **q7.c8** | BAU $1,242B / IE $127B / TAI $13.3B; time-to-operational 20-30 yr / 6 yr / 1.5 yr; Stall never. |

**Verdict:** **Consistent regime framing across leaves.** q1, q3, q7 all use the same four-regime structure (BAU / IE / TAI / Stall) with similar compression-factor magnitudes (~10× per regime step). The framework is the canonical structural treatment of anti-pattern #11.

### Topic: projectile-materials — q3 vs q7

| Source | Claim |
|---|---|
| **q3.c9** | "Materials feasibility by 2030 under BAU: O2 high, Fe + Si high, Al medium, Ti medium, glass and structural blocks high. LOX as propellant is high feasibility." |
| **q3.c5** | "Lunar methane (LCH4) propellant has no native carbon source at bulk scale... is therefore not a BULK lunar-native ISRU product." |
| **q7 (extracted from Handmer)** | Projectile material: raw lunar basalt; "Moon rocks tolerate 1,000 g acceleration without damage" |

**Verdict:** **Consistent.** Handmer's design uses raw basalt as projectile, avoiding the ISRU refinement bottlenecks q3 identifies (Al via FFC Cambridge chlorine import; LH2 prospecting gate; LCH4 no carbon route). The mass driver decouples projectile material from refined-products economics. **This is a load-bearing observation for the q3-q7 architectural compatibility:** projectile launch does not depend on ISRU refinement maturity; only the post-launch products do.

## Architecture-level consistency

The report's central architectural argument lines up cleanly across the four reviewed leaves and q7:

1. **q4 (gear-ratio)** establishes that LEO is structurally unreachable under chemical-only lunar delivery (Γ_LEO ≈ 14).
2. **q4** identifies mass driver + SEP transfer as the architectural fix (drops Γ_LEO to ~1).
3. **q3 (ISRU feasibility)** confirms that O₂/Fe/Si/structural-block production is high-TRL; the projectile material (raw basalt for a mass driver) does not require refined-ISRU maturity.
4. **q2 (lunar-ascent-cost)** derives the chemical-rocket vs mass-driver lunar-to-LEO cost spectrum.
5. **q7 (mass-driver-feasibility)** provides the engineering envelope and capital cost of the mass-driver line in q2's spectrum.
6. **q1 (Earth-launch-cost)** sets the comparator: terrestrial launch cost evolution determines when the crossover becomes economically meaningful.

The architecture story is internally consistent. The single load-bearing inter-leaf contradiction is the q2.c5 / q7.c6 capital figure (q2 $10B vs q7 BAU $1,242B; reconciled only at q7 TAI-grade $13.3B).

## What goes into `leaf.yaml.contradictions_with`

- `q2`: q2.c5 $10B capital vs q7.c6 BAU $1,242B (reconciled at TAI). The single most load-bearing inter-leaf contradiction in the report.

The contradiction is not a falsification of either leaf — it is a *scenario-conditioning* gap. q2.c5 implicitly assumes the q7 TAI-grade capex; q7.c6 explicitly enumerates the BAU baseline that q2 does not address. The cross-consistency / synthesis pass should explicitly bridge.

## Consistency conclusions

q7 is structurally compatible with q1, q3, q4 across all topic clusters. The one contradiction with q2 is fully attributable to the implicit-TAI-conditioning of q2.c5 and explicit-BAU enumeration in q7.c6; this is a load-bearing item for synthesis but not a falsification.

The four-regime framework (BAU / IE / TAI / Stall) is the canonical structural treatment across all five leaves examined, and the report's headline crossover analysis depends on the regime assumption — this is the substantive contribution of the consistency check.

## Next pass

Pass 6 (write) — render the leaf report from claims.yaml. Headline: mass driver lands in the report's headline architecture *only* under IE or TAI-grade compression; under BAU the late-era cost line is chemical-aggressive-ISRU and the report's "$50/kg crossover" framing is conditional on the q7 capital-compression assumption.
