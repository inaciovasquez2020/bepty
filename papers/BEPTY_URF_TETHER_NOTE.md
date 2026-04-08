# BEpTy URF Tether Note

## Chosen URF invariant

For the tested two-lift family
\[
\mathcal F_8=(G_8^{-},G_8^{+}),
\]
define the URF-side invariant
\[
I_{\mathrm{cc}}(A,B):=\#\mathrm{cc}(B)-\#\mathrm{cc}(A).
\]

## Chosen BEpTy valuation

Define
\[
\beta_{\Phi}(A,B)=
\bigl(
\#\mathrm{cc}(B)-\#\mathrm{cc}(A),
\ \mathrm{cr}(B)-\mathrm{cr}(A)
\bigr).
\]

## Tether implication on the tested family

For every tested pair \((A,B)\) in the current two-lift family scope,
\[
I_{\mathrm{cc}}(A,B)\neq 0 \;\Rightarrow\; \beta_{\Phi}(A,B)\neq (0,0).
\]

Indeed, the first coordinate of \(\beta_{\Phi}(A,B)\) is exactly \(I_{\mathrm{cc}}(A,B)\).

## Computed instance

For
\[
(G_8^{-},G_8^{+}),
\]
we have
\[
I_{\mathrm{cc}}(G_8^{-},G_8^{+})=1\neq 0,
\]
hence
\[
\beta_{\Phi}(G_8^{-},G_8^{+})=(1,1)\neq (0,0).
\]

## Scope

This is a theorem-level tether on the explicit tested family.
It is not yet a portfolio non-redundancy theorem.

## Witness files

- `bepty/valuations.py`
- `tests/test_component_cycle_valuation.py`
- `tests/test_urf_tether.py`
