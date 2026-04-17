# HIGH_GIRTH_LOCAL_PAIR_BASE_ADMISSIBILITY_VERIFICATION

Status: CONDITIONAL

## Conditional Statement

Assume BEpTy admissibility permits pair-parameterized canonical valuation families.

For each fixed radius r and each canonical pair (G,H), define

N_r(G,H) := 1 + max\{S_r(G), S_r(H)\},

and

V_r(X;G,H) := \sum_{i=1}^{m} p_i(X) N_r(G,H)^{i-1}.

Then V_r(X;G,H) satisfies A1-A5 of
HIGH_GIRTH_LOCAL_BEPTY_ADMISSIBILITY_AXIOMS.

## Verified Checks Under the Assumption

### A1. Radius-r Locality

V_r(X;G,H) depends only on rooted radius-r profile data.

### A2. Canonicality

V_r(X;G,H) is determined by a fixed canonical rule.

### A3. Isomorphism Invariance

If X ≅ Y, then V_r(X;G,H) = V_r(Y;G,H).

### A4. Finite Evaluability

For every finite bounded-degree graph X, the value V_r(X;G,H) is finite.

### A5. Pair-Symmetry of Comparison Normalization

N_r(G,H) = N_r(H,G).

## Remaining Gap

Remove the pair-parameterized admissibility assumption or elevate it to an explicit BEpTy axiom.
