# HIGH_GIRTH_LOCAL_BOUND_REMOVAL_STRATEGY

Status: OPEN

## Strategy

Replace dependence on an a priori bound M by a graph-dependent canonical base.

For a finite bounded-degree graph X, let

S_r(X) := \sum_{i=1}^{m} p_i(X),

and define

B_r(X) := S_r(X) + 1.

Then define the candidate valuation

W_r(X) := \sum_{i=1}^{m} p_i(X) B_r(X)^{i-1}.

## Role

This is a candidate bound-removal construction for
HIGH_GIRTH_LOCAL_BOUND_REMOVAL_GAP.

## Remaining Gap

Prove that a comparison-normalized canonicalization of the base yields
separation for all pairs G,H while remaining admissible.
