# BEpTy Actual Compared Executable Class Scope

## Definition

Define the full intended compared executable capability class for the current repository state by
\[
\mathcal R_{\mathrm{URF,actual}}
=
\{\#V,\#E,L_{\deg},I_{\mathrm{cc}}\},
\]
where
\[
\#V(G)=|V(G)|,\qquad
\#E(G)=|E(G)|,
\]
\[
L_{\deg}(G)=\mathrm{sort}(\deg(v):v\in V(G)),
\qquad
I_{\mathrm{cc}}(A,B)=\#\mathrm{cc}(B)-\#\mathrm{cc}(A).
\]

## Status partition

The singleton-graph invariants
\[
\#V,\#E,L_{\deg}
\]
do not separate the tested pair
\[
(G_8^{-},G_8^{+}).
\]

The pair invariant
\[
I_{\mathrm{cc}}
\]
does separate the tested pair and is already tethered to the first coordinate of
\[
\beta_\Phi(A,B)=
\bigl(
\#\mathrm{cc}(B)-\#\mathrm{cc}(A),
\ \mathrm{cr}(B)-\mathrm{cr}(A)
\bigr).
\]

## Consequence

Therefore unconditional nonredundancy against the full class
\[
\mathcal R_{\mathrm{URF,actual}}
\]
is false under this definition, because
\[
I_{\mathrm{cc}}(G_8^{-},G_8^{+})\neq 0
\]
already separates the tested pair.

Hence the strongest correct completion statement remains relative to the exact exclusion class
\[
\{\#V,\#E,L_{\deg}\}.
\]
