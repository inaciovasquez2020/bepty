# BEpTy Roadmap

## Current release
- v0.2.0
- Topological specialization added
- Open Detection added
- Closed Shell Detection added
- URF-valued specialization added
- LocalExhaustion interface added

## Next theorem targets
1. Prove the high-girth target:
   \[
   \operatorname{girth}(G)>2R \Rightarrow Z_1(B_R(v))=0 \text{ for every } v\in V(G).
   \]

2. Derive the high-girth reduction:
   \[
   X_R(G)=Z_1(G).
   \]

3. Prove a monotonicity law for the dimension-valued refinement:
   \[
   \beta^{\dim}_R(G):=\dim_{\mathbf F_2} X_R(G).
   \]

4. Add one explicit graph example with nonzero local exhaustion.

## Integration threshold
- One proved URF-facing theorem
- One explicit URF invariant realized as a BEpTy valuation

5. Prove the BEpTy high-girth theorem in full detail.
6. Replace the zero-local-rank shortcut with an exact span computation.


## Next proof frontier
7. Prove that the profiled valuation is strictly finer than first Betti rank.
8. Fix an explicit sheaf-theoretic comparison class.
9. Construct a candidate equal-sheaf / distinct-profile witness pair.
10. Prove or refute sheaf nonrecoverability for the chosen class.


11. Replace the provisional sheaf comparison class by an exact categorical one.
12. Prove invariance of the profiled valuation under the intended BEpTy morphisms.
13. Search for an exact equal-sheaf / distinct-profile witness pair.
14. Prove or refute sheaf nonrecoverability for the exact class.


15. Formalize admissible BEpTy morphisms.
16. Prove the profiled valuation invariance lemma in exact form.
17. Replace note-level exact sheaf package by a fully specified categorical implementation.
18. Resolve the exact sheaf nonrecoverability problem.

## Colimit-kernel program
19. Compute \(C_R(K)\), \(\pi_K\), and \(\kappa_R(K)\) on the first explicit witness pair.
20. Determine whether \(\kappa_R\) is invariant under exact admissible morphisms.
21. If \(\kappa_R\) is not exact-package determined, promote \(\kappa_R\) to the new profiled obstruction.
22. If \(\kappa_R\) is exact-package determined, replace the profile by a finer higher-overlap kernel invariant.


## Verified reduction
23. Treat the toy-model colimit-kernel tests as verified reduction evidence that \(\kappa_R\) is the exact obstruction term at diagram level.
24. Replace toy diagrams by actual \(B_R(v;K)\) data from one explicit witness generator.
25. Search for \(K,L,R\) with isomorphic exact packages and distinct \(\kappa_R\).
