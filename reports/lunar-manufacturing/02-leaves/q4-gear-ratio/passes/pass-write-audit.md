[codex cli ok]
orphan_numerical_claims:
  - "Lead says 35-50 kg/kg at GTO; claims support φ≈35/36.5, not the 50 upper bound."
  - "Γ_X≈0.3-1.4 for closer destinations; claims support chemical Γ≈0.9/1.3/1.4 only, not 0.3 or SEP/OTV variants."
  - "Γ_LEO≈6-14 under chemical-only delivery; claims support ≈14, not 6."
  - "LOX/LH2 I_sp 450 s and 10% inert mass fraction are not in claims.yaml."
  - "Capital-transport gear ratio 6-15, including Metzger G=6 and Starship-class G=15, is not claimed."
  - "Table values for GTO Γ≈2.1 and Γ≈0.4 are not in claims.yaml."
  - "SEP collapses Γ_LEO from 14 to ~1; claims support SEP qualitatively and Γ≈14 chemically, not Γ≈1."
  - "5-year buildup and 22% WACC are not claimed."
  - "Finance costs exceed the LEO threshold by an order of magnitude in early years is not claimed."
  - "LEO crossover after roughly two decades is not claimed."
  - "Metzger reviews seven TEAs and disagreement traces to two parameters is not claimed."
  - "Charania-DePascuale G=64.9 and Jones G=41.8 are not claimed."
  - "Metzger parameterization G=6, ω+ξ≈0.2, x≈10, derived φ≈34, and within 5% of 36.5 are not claimed except for 36.5."
  - "Wright's Law b=0.75 and economies-of-scale exponent a=0.66 are not claimed."
  - "Automation making LEO breakeven reachable in early operating years is not claimed."
  - "Discount rates below double-digit territory is not claimed."
  - "Year-1 viability requiring the full time-evolving model is not claimed."

lead_quality: "Strong: the first 200 words give the headline answer and contingency, but the lead includes unsupported numeric range/detail."

anti_patterns_found:
  - "No mechanical However/Furthermore/Moreover pattern found."
  - "No naive calendar target like 'by 2040' found; the 'two decades' duration is unsupported but not a calendar anti-pattern."
  - "No obvious safety-speak or heavy over-hedging."

confidence_concerns:
  - "Γ_X physics confidence is supportable for the claimed chemical values, but the prose table adds unclaimed SEP/OTV/crossfeed Γ values."
  - "LEO via SEP at medium-high relies on unclaimed Γ≈1 and q3 readiness context not present in this claims file."
  - "TAI/industrial-explosion section is marked low confidence, which is honest, but the prose makes stronger unclaimed timing and exponent claims."
  - "The 'two parameters' TEA explanation is less supportable than q4.c8, which explicitly says multiple factors drive disagreement."

overall: needs-revision

notes: "Main issue is claim hygiene, not narrative structure. Add claims for the extra physics/table/finance/timing numbers or remove/soften them."