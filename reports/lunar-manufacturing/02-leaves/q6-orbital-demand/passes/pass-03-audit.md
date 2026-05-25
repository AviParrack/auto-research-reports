[codex cli ok]
overall:
  verdict: partially_defensible
  summary: Most resolutions are acceptable as regime-bracket reconciliations, but the bandwidth-ceiling and BAU SBSP resolutions are under-supported relative to the confidence claimed.

findings:
  - target: McCalip vs Handmer cost multiple
    target_kind: disagreement_resolution
    verdict: defensible_with_caveats
    quote: "Both assessments are operating on slightly different analyses."
    reason: The source extracts support the distinction between McCalip's whole-project 1 GW / 5-year cost comparison and Handmer's SpaceX-integrated per-token inference framing. The caveat is that mapping McCalip to BAU and Handmer to TAI-C is the author's scenario framing, not directly established by the sources.
    severity: low

  - target: Cote bandwidth ceiling
    target_kind: disagreement_resolution
    verdict: partially_defensible
    quote: "OISL bypass ground-station bottleneck... AI training is the killer app, not inference serving."
    reason: The resolution correctly treats Cote as a serious constraint, but the rebuttal adds uncited assumptions. The extracts say Cote views orbital DC as niche-only and not hyperscaler training replacement; they do not substantiate OISL scaling, training-bandwidth sufficiency, or the derived 200 GW fallback ceiling.
    severity: high

  - target: NASA OTPS vs BAU SBSP 5 GW
    target_kind: disagreement_resolution
    verdict: partially_defensible
    quote: "5 GW under BAU is consistent with strategic + niche deployment but not with full commercial competitiveness."
    reason: Strategic and niche deployment is a plausible reconciliation with NASA OTPS, and Space Ambition's VALCOE framing helps. But the cited extracts do not directly support 5 GW by 2040, military-strategic status for China's array, or enough niche demand to justify high confidence. Medium confidence would be more defensible.
    severity: medium

  - target: Kornuta-Metzger 450 t/yr vs BAU 8,000 t/yr depot
    target_kind: disagreement_resolution
    verdict: defensible
    quote: "450 t/yr is the lunar-derived sub-market; 8,000 t/yr is total LEO refueling including Earth-launched propellant."
    reason: The extracts explicitly identify 450 t/yr as lunar-derived propellant demand. Treating 8,000 t/yr as the author's all-source depot model and holding q6.c8 at medium confidence is appropriately qualified.
    severity: low

  - target: q6.c6 lunar-sourced bulk mass necessary-not-sufficient
    target_kind: agreement_table_resolution
    verdict: partially_defensible
    quote: "McCalip's skepticism applies to BAU, not TAI-C."
    reason: The necessary-but-not-sufficient framing is defensible if the TAI-C mass-demand scenario is accepted, but McCalip's cost critique is not inherently limited to BAU. This should be framed as conditional on the author's TAI-C assumptions, not as a source-settled resolution.
    severity: medium

notes:
  - issue: pass-03-reconcile.md says the reasoning is audited in pass-03-audit.md, but no q6 pass-03-audit.md file is present in the passes directory.
    severity: medium

  - issue: Several high-tier extracts note that direct PDFs were not parsed and key numbers came from abstracts or secondary aggregators; pass 4 should not treat those as full primary-source reviews yet.
    severity: medium

  - issue: q6.c6's reconcile table names source support, but claims.yaml still lists only first-principles-calc evidence for q6.c6.
    severity: low