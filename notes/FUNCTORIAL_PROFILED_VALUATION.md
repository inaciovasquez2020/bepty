# Functorial profiled valuation

Let \(R\ge 1\). Define the profiled valuation
\[
\beta^{\mathrm{prof}}_{R}(K):=
\bigl(\beta_1(K),\operatorname{Hist}_{R}^{\beta}(K)\bigr),
\]
where \(\operatorname{Hist}_{R}^{\beta}(K)\) denotes the rooted-ball profile histogram at radius \(R\).

## Admissible morphism invariance

For an admissible morphism \(f:K\to L\) in \(\mathcal C_{\mathrm{exact}}\), define
\[
\beta^{\mathrm{prof}}_{R}(f):
\beta^{\mathrm{prof}}_{R}(K)\to \beta^{\mathrm{prof}}_{R}(L)
\]
by transport of rooted-ball classes under \(f\).

## Theorem

For every admissible morphism \(f:K\to L\),
\[
\beta^{\mathrm{prof}}_{R}(K)=\beta^{\mathrm{prof}}_{R}(L).
\]

## Proof

Because \(f\) is an exact graph isomorphism preserving incidence, degree data, and rooted-ball structure,
it preserves cycle rank and carries each rooted \(R\)-ball in \(K\) to an isomorphic rooted \(R\)-ball in \(L\).
Hence both the Betti rank and the rooted-ball profile histogram are invariant.

## Functoriality

For admissible morphisms \(K \xrightarrow{f} L \xrightarrow{g} M\),
\[
\beta^{\mathrm{prof}}_{R}(g\circ f)=\beta^{\mathrm{prof}}_{R}(g)\circ\beta^{\mathrm{prof}}_{R}(f),
\qquad
\beta^{\mathrm{prof}}_{R}(\mathrm{id}_K)=\mathrm{id}_{\beta^{\mathrm{prof}}_{R}(K)}.
\]

Thus \(\beta^{\mathrm{prof}}_{R}\) is a functorial valuation on \(\mathcal C_{\mathrm{exact}}\).
