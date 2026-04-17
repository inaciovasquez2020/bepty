# BEpTy High-Girth Separation Template

Objects to instantiate:
- explicit family F = {G_n,H_n}_{n \ge 1}
- explicit BEpTy valuation v

Required clauses:
1. Invariance:
   - v is invariant under the declared finite normalization layer.

2. Compared-class agreement:
   - for each n,
     - #V(G_n) = #V(H_n)
     - #E(G_n) = #E(H_n)
     - L_deg(G_n) = L_deg(H_n)
     - I_cc(G_n) = I_cc(H_n)

3. Separation:
   - there exists n such that v(G_n) \neq v(H_n)

4. High-girth local exhaustion:
   - F satisfies the local exhaustion condition required by theory/HighGirthLocalExhaustion.md

This file is a theorem-instantiation template only.
It does not claim existence of F or v.
