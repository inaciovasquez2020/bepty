# BEpTy Two-Lift Nonvanishing Note

## Objects

Let
\[
\mathcal F_n=(G_n^{-},G_n^{+})
\]
be the explicit two-lift pair of the cycle \(C_n\) with one twisted edge.

Let
\[
\beta_{\Phi}(A,B)
=
\bigl(
\#\mathrm{cc}(B)-\#\mathrm{cc}(A),
\ \mathrm{cr}(B)-\mathrm{cr}(A)
\bigr),
\]
where \(\#\mathrm{cc}\) is the number of connected components and
\[
\mathrm{cr}(G)=|E(G)|-|V(G)|+\#\mathrm{cc}(G)
\]
is the cycle rank.

## Computed instance

For \(n=8\),
\[
\#\mathrm{cc}(G_8^{+})=2,\qquad \#\mathrm{cc}(G_8^{-})=1,
\]
and
\[
\mathrm{cr}(G_8^{+})=2,\qquad \mathrm{cr}(G_8^{-})=1.
\]

Therefore
\[
\beta_{\Phi}(G_8^{-},G_8^{+})=(1,1)\neq (0,0).
\]

## Theorem

**Theorem.**
For the explicit tested instance \(\mathcal F_8=(G_8^{-},G_8^{+})\),
\[
\beta_{\Phi}(G_8^{-},G_8^{+})\neq 0.
\]

## Witness files

- `bepty/target_family.py`
- `bepty/valuations.py`
- `tests/test_target_family.py`
- `tests/test_component_cycle_valuation.py`
