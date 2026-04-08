# BEpTy Exclusion Theorem Relative to the Current Compared Executable Class

## Compared executable class

Fix
\[
\mathcal R_{\mathrm{URF,current}}=\{\#V,\#E,L_{\deg}\},
\]
where
\[
\#V(G)=|V(G)|,\qquad \#E(G)=|E(G)|,\qquad
L_{\deg}(G)=\mathrm{sort}(\deg(v):v\in V(G)).
\]

## Tested family

Let
\[
\mathcal F_8=(G_8^{-},G_8^{+})
\]
be the explicit two-lift pair from `bepty/target_family.py`.

## BEpTy valuation

Let
\[
\beta_\Phi(A,B)=
\bigl(
\#\mathrm{cc}(B)-\#\mathrm{cc}(A),
\ \mathrm{cr}(B)-\mathrm{cr}(A)
\bigr).
\]

## Exclusion theorem

For every
\[
R\in \mathcal R_{\mathrm{URF,current}},
\]
one has
\[
R(G_8^{-})=R(G_8^{+}),
\]
while
\[
\beta_\Phi(G_8^{-},G_8^{+})=(1,1)\neq (0,0).
\]

Therefore the current BEpTy separating capability on the tested family is nonredundant relative to the exact compared executable class
\[
\mathcal R_{\mathrm{URF,current}}.
\]

## Scope

This proves nonredundancy only relative to the exact finite class
\[
\{\#V,\#E,L_{\deg}\}.
\]
No claim is made beyond that class.
