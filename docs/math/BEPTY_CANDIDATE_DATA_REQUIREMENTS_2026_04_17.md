# BEpTy Candidate Data Requirements

To instantiate the high-girth separation template, provide:

1. Family data:
- explicit pair family F = {G_n,H_n}_{n \ge 1}

2. Compared-class equalities:
- #V(G_n) = #V(H_n)
- #E(G_n) = #E(H_n)
- L_deg(G_n) = L_deg(H_n)
- I_cc(G_n) = I_cc(H_n)

3. Local exhaustion witness:
- explicit statement verifying the local exhaustion condition from theory/HighGirthLocalExhaustion.md

4. Valuation data:
- explicit BEpTy valuation v
- normalization-invariance statement for v

5. Separation witness:
- explicit n with v(G_n) \neq v(H_n)

Status:
- this file records the exact missing input package
- no existence claim is made here
