# HIGH_GIRTH_LOCAL_COMPARISON_NORMALIZATION_GAP

Status: OPEN

## Statement

Construct a canonical pairwise normalization rule N_r(G,H) such that the valuation

\widetilde W_r(X;G,H) := \sum_{i=1}^{m} p_i(X) N_r(G,H)^{i-1}

satisfies

P_r(G) != P_r(H) => \widetilde W_r(G;G,H) != \widetilde W_r(H;G,H)

for all finite bounded-degree graphs G,H,

and N_r(G,H) is symmetric and canonical in the pair (G,H).

## Role

This isolates the exact normalization gap in
HIGH_GIRTH_LOCAL_BOUND_REMOVAL_STRATEGY.

## Reduction

pairwise_canonical_normalization => HIGH_GIRTH_LOCAL_BOUND_REMOVAL_GAP
