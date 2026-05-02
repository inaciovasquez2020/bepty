# BEpTy v33 Degree-Edge Finite Normalizer

Status: EXPLICIT NORMALIZER PACKET

## Normalizer

Define the finite normalizer

\[
N_{\deg E}(X)=\mathcal E_{\deg}(X),
\]

where

\[
\mathcal E_{\deg}(X)=
\{\!\{\{\deg_X(u),\deg_X(w)\}:\{u,w\}\in E(X)\}\!\}.
\]

This sends a finite graph to its degree-labeled edge-incidence multiset.

## Valuation

\[
v_{33}(X)=\#\{\{u,w\}\in E(X):\deg_X(u)=3,\deg_X(w)=3\}.
\]

Equivalently,

\[
v_{33}(X)=
\operatorname{mult}_{\{3,3\}}\bigl(N_{\deg E}(X)\bigr).
\]

## Theorem

For every finite graph \(X\),

\[
v_{33}(N_{\deg E}(X))=v_{33}(X),
\]

where the left side means extraction of the \(\{3,3\}\)-multiplicity from the normalized object.

## Proof

By definition, \(N_{\deg E}(X)\) is exactly the multiset of unordered degree labels over edges of \(X\).

The valuation \(v_{33}\) counts exactly the multiplicity of the unordered degree-label pair \(\{3,3\}\) in that multiset.

Therefore normalization by \(N_{\deg E}\) preserves \(v_{33}\).

## Closure consequence

The high-girth local \(v_{33}\) packet is unconditional relative to the explicit normalizer \(N_{\deg E}\).

## Boundary

This packet defines an explicit finite normalizer sufficient for the \(v_{33}\) closure packet.

It does not assert that every possible BEpTy finite-normalization map preserves \(\mathcal E_{\deg}\).

It does not assert unrestricted BEpTy closure beyond the declared \(N_{\deg E}\)-normalized setting.
