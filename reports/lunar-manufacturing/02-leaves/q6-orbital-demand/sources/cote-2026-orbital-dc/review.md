---
source: cote-2026-orbital-dc
tier: C
reviewed_pass: 4
reviewed_by: claude+gpt
---

# Source Review: Andrew Cote — Do Orbital Data Centers Make Sense? (2026)

**Verdict:** Mixed
**Confidence:** medium-high

Cote's bandwidth-binding-constraint argument is one of the strongest
skeptical positions in the 2026 literature. The 500-800 Tbps total
orbital comms vs 5-20 Tbps per ground DC is a real constraint, but
Cote's "niche-only" conclusion assumes ground-station-routing rather
than OISL-interconnected compute clusters; this assumption is
contestable. The 10-20× space-qualified-chip performance lag is
the strongest single point — if true, orbital DC viability depends
on radiation-tolerant compute architecture or accepting the
performance penalty. Cote's piece is load-bearing for q6.c14 and
correctly tempers TAI-C optimism by factor-of-5 sensitivity.
