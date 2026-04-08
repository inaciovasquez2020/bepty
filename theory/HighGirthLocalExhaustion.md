# High-Girth Local Exhaustion Collapse

## Definitions

\[
X_R(G):=Z_1(G)\big/\langle Z_1(B_R(v)) : v\in V(G)\rangle.
\]

\[
\beta^{\dim}_R(G):=\dim_{\mathbf F_2} X_R(G).
\]

\[
\mathrm{LocalExhaustion}_R(G):=
\begin{cases}
0,&X_R(G)=0,\\
1,&X_R(G)\neq 0.
\end{cases}
\]

## Target theorem

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
\beta^{\dim}_R(G)=\dim_{\mathbf F_2} Z_1(G).
\]

## Proof skeleton

It suffices to prove:

\[
\forall v\in V(G),\ \operatorname{girth}(G)>2R \Rightarrow B_R(v)\text{ is acyclic.}
\]

Then

\[
Z_1(B_R(v))=0
\]

for every \(v\), hence

\[
\langle Z_1(B_R(v)) : v\in V(G)\rangle = 0,
\]

so

\[
X_R(G)=Z_1(G)/0=Z_1(G).
\]
