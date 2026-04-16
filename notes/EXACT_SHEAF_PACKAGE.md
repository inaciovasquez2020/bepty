# Exact sheaf package

## Purpose

Fix an exact categorical comparison class \(\mathcal C_{\mathrm{exact}}\) for the BEpTy sheaf-profile frontier.

## Objects

An object of \(\mathcal C_{\mathrm{exact}}\) is a finite connected graph \(K\) together with its exact comparison package
\[
\operatorname{Pkg}(K):=(\#V(K),\#E(K),L_{\deg}(K),I_{cc}(K)),
\]
where:

- \(\#V(K)\) is the number of vertices;
- \(\#E(K)\) is the number of edges;
- \(L_{\deg}(K)\) is the degree histogram;
- \(I_{cc}(K)\) is the connected-component size multiset.

For connected graphs, \(I_{cc}(K)=\{|V(K)|\}\).

## Admissible morphisms

A morphism \(f:K\to L\) in \(\mathcal C_{\mathrm{exact}}\) is an isomorphism of graphs satisfying:
1. \(f\) is bijective on vertices;
2. \(uv\in E(K)\iff f(u)f(v)\in E(L)\);
3. rooted-ball incidence and degree data are preserved exactly.

Thus admissible morphisms are exact structure-preserving graph isomorphisms.

## Exact sheaf functor

Define
\[
\mathsf{Sh}_{\mathcal C_{\mathrm{exact}}}(K):=\operatorname{Pkg}(K).
\]

This is the exact categorical comparison class used by the repository after replacing the provisional sheaf class.

## Isomorphism invariants

By construction, \(\mathsf{Sh}_{\mathcal C_{\mathrm{exact}}}(K)\) is determined by the invariant tuple
\[
(\#V,\#E,L_{\deg},I_{cc})(K).
\]

## Exact recovery theorem

**Theorem.**
For all finite graphs \(K,L\),
\[
\mathsf{Sh}_{\mathcal C_{\mathrm{exact}}}(K)\cong \mathsf{Sh}_{\mathcal C_{\mathrm{exact}}}(L)
\Longrightarrow
(\#V,\#E,L_{\deg},I_{cc})(K)=
(\#V,\#E,L_{\deg},I_{cc})(L).
\]

**Proof.**
Since \(\mathsf{Sh}_{\mathcal C_{\mathrm{exact}}}(K)=\operatorname{Pkg}(K)\) and
\(\mathsf{Sh}_{\mathcal C_{\mathrm{exact}}}(L)=\operatorname{Pkg}(L)\),
an isomorphism of exact sheaf packages is equality of the package data.
Hence each component of the tuple agrees.

## Consequence for the frontier

The exact class eliminates ambiguity at the level of the declared actual compared class.
Therefore the remaining frontier is not exact-class recoverability of
\((\#V,\#E,L_{\deg},I_{cc})\); it is whether finer BEpTy valuations, such as profiled Betti data,
factor functorially through the exact class.

## Status

- Exact comparison class fixed.
- Exact recovery theorem fixed.
- Witness-pair test required next.
