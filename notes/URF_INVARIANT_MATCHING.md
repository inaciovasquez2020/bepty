# URF Invariant Matching

## Canonical identification

\[
X_R(G):=Z_1(G)\big/\langle Z_1(B_R(v)) : v\in V(G)\rangle
\]

is the URF residual cycle-space obstruction.

## BEpTy realization

Take

\[
A:=0,\qquad B:=X_R(G),\qquad \Phi(E):=\dim_{\mathbf F_2}(E).
\]

Then

\[
\beta_\Phi(A,B)=\Phi(B\setminus A)
\]

is represented in the URF-facing vector-space form by

\[
\beta^{\dim}_R(G):=\dim_{\mathbf F_2} X_R(G).
\]

## Detection law

\[
\beta^{\dim}_R(G)=0
\iff
Z_1(G)=\langle Z_1(B_R(v)) : v\in V(G)\rangle.
\]

\[
\beta^{\dim}_R(G)>0
\iff
\text{nonlocal residual cycle structure survives local exhaustion.}
\]


## Profiled valuation upgrade
\[
eta^{\mathrm{prof}}_R(G):=\bigl(\dim Z_1(G)-\dim X_R(G),\ \sigma_R(G)\bigr).
\]

Established:
- strictly finer than first Betti rank via `Theta(3,3,3)` vs `Dumbbell(6,6)`.

Open:
- nonrecoverability from the chosen sheaf-theoretic comparison class.
