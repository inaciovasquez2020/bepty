# BEpTy High-Girth Local v33 Closure

Status: PROPOSED CLOSURE PACKET

## Corrected local-ball lemma

For induced metric balls, the admissible statement is:

\[
\operatorname{girth}(G)>2R+1
\Rightarrow
\forall v\in V(G),\ B_R(v)\text{ is acyclic}.
\]

The older bound \(2R\) is insufficient.

## Explicit family

For \(m\ge4\), let \(C_m\) be the cycle on vertices \(0,\dots,m-1\).

Define \(G_m\) by attaching two leaves to adjacent cycle vertices \(0\) and \(1\).

Define \(H_m\) by attaching two leaves to nonadjacent cycle vertices \(0\) and \(2\).

## Compared-class agreement

Canonical compared-class token: `{#V,#E,L_{\deg},I_{cc}}`.

For every \(m\ge4\):

\[
#V(G_m)=#V(H_m)=m+2,
\]

\[
#E(G_m)=#E(H_m)=m+2,
\]

\[
L_{\deg}(G_m)=L_{\deg}(H_m)=\{3,3,2^{m-2},1,1\},
\]

\[
I_{cc}(G_m)=I_{cc}(H_m)=1.
\]

## Valuation

Define

\[
v_{33}(X)=\#\{\{u,w\}\in E(X):\deg(u)=3,\deg(w)=3\}.
\]

This valuation is finite, isomorphism-invariant, radius-1 local, and computable from degree-labeled edge incidence.

## Separation

For every \(m\ge4\):

\[
v_{33}(G_m)=1,\qquad v_{33}(H_m)=0.
\]

Thus \(v_{33}\) is not determined by the compared class
\(\{#V,#E,L_{\deg},I_{cc}\}\).

## Local exhaustion witness

For \(R=1\), both \(G_m\) and \(H_m\) have girth \(m\ge4>3=2R+1\).

Therefore every induced radius-1 ball is acyclic.

## Remaining theorem-level obligation

Prove or declare that the finite normalization layer preserves degree-labeled edge-incidence valuations such as \(v_{33}\).

If this compatibility is absent, the result remains conditional on that finite-normalization invariance lemma.
