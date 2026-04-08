# BEpTy Nonredundancy Criterion

## Criterion

BEpTy is standalone-indispensable on a tested family \(\mathcal F\) if there exists a valuation
\[
\beta_\Phi
\]
implemented in this repository such that all of the following hold:

1. there exists a tested pair \((A,B)\in\mathcal F\) with
   \[
   \beta_\Phi(A,B)\neq 0;
   \]

2. there exists a declared baseline comparison class
   \[
   \mathcal C
   \]
   of executable lenses external to the BEpTy valuation layer such that every
   \[
   L\in\mathcal C
   \]
   fails to separate the same tested pair:
   \[
   L(A)=L(B);
   \]

3. no executable witness file in the compared repository class currently computes the same separating quantity as \(\beta_\Phi\) on that tested pair.

## Current instantiated scope

For the present repository state, the tested family is
\[
\mathcal F_8=(G_8^{-},G_8^{+}),
\]
the valuation is
\[
\beta_\Phi(A,B)=
\bigl(
\#\mathrm{cc}(B)-\#\mathrm{cc}(A),
\ \mathrm{cr}(B)-\mathrm{cr}(A)
\bigr),
\]
and the current declared baseline comparison class is the singleton
\[
\mathcal C=\{L_{\deg}\},
\qquad
L_{\deg}(G)=\mathrm{sort}(\deg(v):v\in V(G)).
\]

## Present status

Items (1) and (2) are established on \(\mathcal F_8\).

Item (3) is not yet established.

Therefore standalone indispensability is not yet proved.
