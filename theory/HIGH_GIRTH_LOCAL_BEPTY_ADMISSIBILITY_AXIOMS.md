# HIGH_GIRTH_LOCAL_BEPTY_ADMISSIBILITY_AXIOMS

Status: OPEN

## Axioms

A valuation V_r is BEpTy-admissible if the following hold.

### A1. Radius-r Locality

V_r(X) depends only on rooted radius-r profile data.

### A2. Canonicality

V_r is determined by a fixed canonical rule from the profile data, with no non-canonical choices.

### A3. Isomorphism Invariance

If X ≅ Y, then V_r(X) = V_r(Y).

### A4. Finite Evaluability

For every finite bounded-degree graph X, the value V_r(X) is a finite well-defined quantity.

### A5. Pair-Symmetry of Comparison Normalization

If V_r is built from a pair-normalized base, the normalization rule is symmetric in the ordered data of the comparison pair.

## Role

This specifies the exact BEpTy admissibility axioms needed for
HIGH_GIRTH_LOCAL_ADMISSIBILITY_CRITERION.

## Next Check

Verify A1-A5 for the pair-normalized valuation
V_r(X) := \widetilde W_r(X;G,H).
