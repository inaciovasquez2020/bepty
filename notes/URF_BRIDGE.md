# BEpTy to URF Bridge

Candidate interface:
- absence as residual structure
- local exhaustion failure
- invariant-valued remainder
- obstruction as nonzero residual under admissible valuation

Import condition:
- prove one nontrivial theorem beyond finite-set normalization
- identify one URF invariant expressible as a BEpTy valuation


## Local exhaustion interface

\[
X_R(G):=Z_1(G)\big/\langle Z_1(B_R(v)) : v\in V(G)\rangle.
\]

\[
\Phi_{\neq 0}(E):=
\begin{cases}
0,&E=0,\\
1,&E\neq 0.
\end{cases}
\]

\[
\mathrm{LocalExhaustion}_R(G):=\Phi_{\neq 0}(X_R(G)).
\]

\[
\mathrm{LocalExhaustion}_R(G)=0
\iff
Z_1(G)=\langle Z_1(B_R(v)) : v\in V(G)\rangle.
\]

\[
\mathrm{LocalExhaustion}_R(G)=1
\iff
Z_1(G)\neq \langle Z_1(B_R(v)) : v\in V(G)\rangle.
\]

## First URF-facing theorem target

\[
\operatorname{girth}(G)>2R
\Rightarrow
\forall v\in V(G),\ Z_1(B_R(v))=0.
\]

\[
\operatorname{girth}(G)>2R
\Rightarrow
X_R(G)=Z_1(G).
\]

\[
\operatorname{girth}(G)>2R
\Rightarrow
\mathrm{LocalExhaustion}_R(G)=
\begin{cases}
0,&Z_1(G)=0,\\
1,&Z_1(G)\neq 0.
\end{cases}
\]

## Refinement target

\[
\beta^{\dim}_{R}(G):=\dim_{\mathbf F_2} X_R(G).
\]

\[
\beta^{\dim}_{R}(G)=0
\iff
\mathrm{LocalExhaustion}_R(G)=0.
\]

