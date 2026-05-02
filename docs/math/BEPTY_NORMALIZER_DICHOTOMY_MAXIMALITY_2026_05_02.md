# BEpTy Normalizer Dichotomy / Maximality Theorem

Status: MAXIMALITY THEOREM PACKET

## Setup

Let \(\mathcal N\) be any proposed class of BEpTy finite normalizers.

Let

\[
\mathcal E_{\deg}(X)
\]

be the degree-labeled edge-incidence multiset.

Let

\[
v_{33}(X)
=
\#\{\{u,w\}\in E(X):\deg_X(u)=3,\deg_X(w)=3\}.
\]

Equivalently,

\[
v_{33}(X)=m_{33}(X),
\]

where \(m_{33}(X)\) is the multiplicity of the \((3,3)\)-edge stratum inside
\(\mathcal E_{\deg}(X)\).

The repository already proves the compatibility reduction:

\[
\mathcal E_{\deg}(N(X))=\mathcal E_{\deg}(X)
\Rightarrow
v_{33}(N(X))=v_{33}(X).
\]

## Theorem: Normalizer Dichotomy / Maximality

For every proposed class \(\mathcal N\) of finite BEpTy normalizers, exactly one of the following cases holds.

### Preservation case

\[
\forall N\in\mathcal N,\ \forall X,\qquad
\mathcal E_{\deg}(N(X))=\mathcal E_{\deg}(X).
\]

Then

\[
\forall N\in\mathcal N,\ \forall X,\qquad
v_{33}(N(X))=v_{33}(X).
\]

Thus \(\mathcal N\subseteq\mathsf{AdmNorm}_{v33}\), and \(\mathcal N\)-uniform \(v_{33}\)-closure is certified.

### Obstruction case

\[
\exists N\in\mathcal N,\ \exists X,\qquad
\mathcal E_{\deg}(N(X))\ne\mathcal E_{\deg}(X).
\]

Then \(\mathcal N\)-uniform \(v_{33}\)-closure is not certified by the current BEpTy packets.

If, more strongly,

\[
m_{33}(N(X))\ne m_{33}(X),
\]

then

\[
v_{33}(N(X))\ne v_{33}(X),
\]

so \(\mathcal N\)-uniform \(v_{33}\)-closure fails.

## Proof

The preservation case and obstruction case are mutually exclusive and exhaustive because the obstruction case is the negation of the preservation case.

In the preservation case, fix \(N\in\mathcal N\) and \(X\). The hypothesis gives

\[
\mathcal E_{\deg}(N(X))=\mathcal E_{\deg}(X).
\]

The locked compatibility reduction gives

\[
v_{33}(N(X))=v_{33}(X).
\]

Since \(N\) and \(X\) were arbitrary, \(\mathcal N\)-uniform \(v_{33}\)-closure follows.

In the obstruction case, some \(N\in\mathcal N\) changes \(\mathcal E_{\deg}\) on some \(X\). The current repository contains no theorem proving \(v_{33}\)-closure for such a normalizer. Thus \(\mathcal N\)-uniform closure is not certified by the current packets.

If the obstruction changes the \((3,3)\)-edge multiplicity, then since \(v_{33}=m_{33}\),

\[
m_{33}(N(X))\ne m_{33}(X)
\Rightarrow
v_{33}(N(X))\ne v_{33}(X).
\]

Therefore \(\mathcal N\)-uniform closure fails.

## Maximality conclusion

Canonical status token: \(N_{\deg E}-normalized closure\).

The repository is maximally closed at \(N_{\deg E}\)-normalized closure unless a foundational admissible-normalizer class is added and proved to imply \(\mathsf{AdmNorm}_{v33}\).

Equivalently:

\[
\mathcal N\text{-uniform closure is certified exactly when }
\mathcal N\subseteq\mathsf{AdmNorm}_{v33}.
\]

## Boundary

This packet does not assert unrestricted BEpTy closure.

This packet does not assert normalizer-independence.

This packet does not declare \(\mathsf{AdmNorm}_{v33}\) as a foundational BEpTy axiom.

This packet does not promote the repository status beyond \(N_{\deg E}\)-normalized closure.
