# HIGH_GIRTH_LOCAL_PAIR_BASE_CANDIDATE

Status: CONDITIONAL

## Candidate

For finite bounded-degree graphs G,H, define

S_r(X) := \sum_{i=1}^{m} p_i(X),

and set the symmetric canonical pair-base

N_r(G,H) := 1 + max\{S_r(G), S_r(H)\}.

Define

\widetilde W_r(X;G,H) := \sum_{i=1}^{m} p_i(X) N_r(G,H)^{i-1}.

## Conditional Claim

If P_r(G), P_r(H) have coordinates in \{0,\dots,N_r(G,H)-1\} and
P_r(G) != P_r(H), then

\widetilde W_r(G;G,H) != \widetilde W_r(H;G,H).

## Role

This is the first explicit candidate for
HIGH_GIRTH_LOCAL_COMPARISON_NORMALIZATION_GAP.

## Remaining Gap

Prove the coordinate bound
p_i(X) < N_r(G,H)
holds canonically for all profile coordinates.
