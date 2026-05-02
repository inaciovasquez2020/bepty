# BEpTy Final Status Index

Status: FINAL STATUS INDEX

## Repository status

\[
\boxed{
N_{\deg E}\text{-NORMALIZED CLOSURE ONLY}
}
\]

This is the maximal unconditional closure status currently certified in the repository.

## Locked chain

1. High-girth local \(v_{33}\) separating packet.
2. Finite-normalization compatibility reduction.
3. Explicit degree-edge normalizer \(N_{\deg E}\).
4. \(N_{\deg E}\)-normalized closure lock.
5. Normalizer-independence frontier lock.
6. Normalizer Dichotomy / Maximality lock.

## Core objects

\[
N_{\deg E}(X)=\mathcal E_{\deg}(X)
\]

\[
v_{33}(X)=\#\{\{u,w\}\in E(X):\deg_X(u)=3,\deg_X(w)=3\}
\]

\[
v_{33}(N_{\deg E}(X))=v_{33}(X)
\]

## Separating family

For \(m\ge4\), \(G_m\) and \(H_m\) satisfy

\[
#V(G_m)=#V(H_m),
\]

\[
#E(G_m)=#E(H_m),
\]

\[
L_{\deg}(G_m)=L_{\deg}(H_m),
\]

\[
I_{cc}(G_m)=I_{cc}(H_m),
\]

but

\[
v_{33}(G_m)=1,\qquad v_{33}(H_m)=0.
\]

## Maximality theorem

For any proposed finite-normalizer class \(\mathcal N\), either

\[
\forall N\in\mathcal N,\ \forall X,\quad
\mathcal E_{\deg}(N(X))=\mathcal E_{\deg}(X),
\]

in which case \(v_{33}\)-closure is certified over \(\mathcal N\), or the current packets do not certify \(\mathcal N\)-uniform closure.

If a normalizer changes the \((3,3)\)-edge multiplicity, then \(v_{33}\)-closure fails for that normalizer.

## Future promotion criterion

Any future unrestricted promotion requires a foundational admissible-normalizer class satisfying

\[
\mathsf{AdmNorm}_{\mathrm{BEpTy}}\subseteq\mathsf{AdmNorm}_{v33}.
\]

Equivalently,

\[
\forall N\in\mathsf{AdmNorm}_{\mathrm{BEpTy}},\ \forall X,\quad
\mathcal E_{\deg}(N(X))=\mathcal E_{\deg}(X).
\]

## Boundary

This does not assert unrestricted BEpTy closure.

This does not assert normalizer-independence.

This does not declare \(\mathsf{AdmNorm}_{v33}\) as a foundational BEpTy axiom.

This does not promote beyond \(N_{\deg E}\)-normalized closure.

This index records the current certified repository status only.
