# BEpTy Baseline Comparison Note

## Family

Let
\[
\mathcal F_8=(G_8^{-},G_8^{+})
\]
be the explicit two-lift pair from `bepty/target_family.py`.

## Baseline local lens

Define the baseline local lens
\[
L_{\deg}(G)=\mathrm{sort}\bigl(\deg(v):v\in V(G)\bigr).
\]

## Computed equality

For the tested instance,
\[
L_{\deg}(G_8^{-})=L_{\deg}(G_8^{+})=(2,2,\dots,2).
\]

Hence the baseline local degree lens does not separate the pair.

## BEpTy separation

The BEpTy valuation
\[
\beta_{\Phi}(A,B)=
\bigl(
\#\mathrm{cc}(B)-\#\mathrm{cc}(A),
\ \mathrm{cr}(B)-\mathrm{cr}(A)
\bigr)
\]
satisfies
\[
\beta_{\Phi}(G_8^{-},G_8^{+})=(1,1)\neq (0,0).
\]

## Conclusion

For the tested instance \(\mathcal F_8\),
\[
L_{\deg}(G_8^{-})=L_{\deg}(G_8^{+})
\quad\text{but}\quad
\beta_{\Phi}(G_8^{-},G_8^{+})\neq 0.
\]

Thus BEpTy defeats the stated baseline local lens on this family.

## Witness files

- `tests/test_local_baseline_failure.py`
- `tests/test_component_cycle_valuation.py`
