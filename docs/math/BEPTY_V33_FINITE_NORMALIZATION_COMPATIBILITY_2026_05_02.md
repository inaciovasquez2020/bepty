# BEpTy v33 Finite-Normalization Compatibility

Status: CONDITIONAL LEMMA PACKET

## Target lemma

Let

\[
v_{33}(X)=\#\{\{u,w\}\in E(X):\deg_X(u)=3,\deg_X(w)=3\}.
\]

Let \(N\) be the declared BEpTy finite-normalization map.

The needed compatibility statement is:

\[
\forall X,\qquad v_{33}(N(X))=v_{33}(X).
\]

## Weakest sufficient structural assumption

It is enough that \(N\) preserves the degree-labeled edge-incidence multiset:

\[
\mathcal E_{\deg}(X)=
\{\!\{\{\deg_X(u),\deg_X(w)\}:\{u,w\}\in E(X)\}\!\}.
\]

That is, if

\[
\mathcal E_{\deg}(N(X))=\mathcal E_{\deg}(X),
\]

then

\[
v_{33}(N(X))=v_{33}(X).
\]

## Proof

The valuation \(v_{33}\) is the multiplicity of the unordered label pair
\(\{3,3\}\) inside \(\mathcal E_{\deg}(X)\).

Therefore preservation of \(\mathcal E_{\deg}\) preserves that multiplicity.

Hence

\[
v_{33}(N(X))=v_{33}(X).
\]

## Boundary

This packet proves only the reduction:

\[
\mathcal E_{\deg}(N(X))=\mathcal E_{\deg}(X)
\Rightarrow
v_{33}(N(X))=v_{33}(X).
\]

It does not assert that the repository already defines a finite-normalization map \(N\) satisfying this condition.

The remaining unconditional obligation is exactly:

\[
\forall X,\qquad
\mathcal E_{\deg}(N(X))=\mathcal E_{\deg}(X).
\]
