# HIGH_GIRTH_LOCAL_WEIGHTING_BASE_B_CONDITIONAL

Status: CONDITIONAL

## Conditional Statement

Fix r >= 1 and m >= 1.

Let P_r(G) = (p_1(G), ..., p_m(G)) and P_r(H) = (p_1(H), ..., p_m(H))
be rooted radius-r profile count vectors.

Assume there exists M >= 0 such that for all i,

0 <= p_i(G) <= M,
0 <= p_i(H) <= M.

Let B := M + 1 and define

V_{r,B}(G) = \sum_{i=1}^{m} p_i(G) B^{i-1}.

Then

P_r(G) != P_r(H) => V_{r,B}(G) != V_{r,B}(H).

## Role

This gives an injective canonical weighting under an explicit bounded-coordinate hypothesis.

## Gap

Remove dependence on an a priori uniform bound M compatible with the admissible BEpTy regime.
