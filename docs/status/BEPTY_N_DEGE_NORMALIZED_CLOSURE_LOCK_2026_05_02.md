# BEpTy \(N_{\deg E}\)-Normalized Closure Lock

Status: N_DEGE_NORMALIZED CLOSURE LOCK

## Locked result

The repository now contains an explicit normalized BEpTy closure packet for the high-girth local \(v_{33}\) separation.

The normalizer is

\[
N_{\deg E}(X)=\mathcal E_{\deg}(X).
\]

The valuation is

\[
v_{33}(X)=\#\{\{u,w\}\in E(X):\deg_X(u)=3,\deg_X(w)=3\}.
\]

The normalized extraction identity is

\[
v_{33}(N_{\deg E}(X))=v_{33}(X).
\]

## Separating family

For \(m\ge4\), let \(G_m\) be the \(m\)-cycle with two leaves attached to adjacent cycle vertices \(0,1\).

Let \(H_m\) be the \(m\)-cycle with two leaves attached to nonadjacent cycle vertices \(0,2\).

Then

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

## Local condition

The induced-ball acyclicity condition is locked as

\[
\operatorname{girth}(G)>2R+1.
\]

For \(R=1\), the witness family satisfies this condition for \(m\ge4\).

## Dependency chain

The closure chain is:

\[
\text{explicit pair family}
\Rightarrow
\text{compared-class agreement}
\Rightarrow
v_{33}\text{ separation}
\Rightarrow
N_{\deg E}\text{ compatibility}
\Rightarrow
N_{\deg E}\text{-normalized closure}.
\]

## Boundary

This is a closure lock only in the explicit \(N_{\deg E}\)-normalized setting.

It does not assert unrestricted BEpTy closure.

It does not assert that every possible BEpTy finite-normalization map preserves \(\mathcal E_{\deg}\).

It does not assert normalizer-independence.

The remaining open object is unrestricted BEpTy closure, equivalently a stronger normalizer-independence theorem.
