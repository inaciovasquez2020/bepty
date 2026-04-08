# Exact Sheaf Package

## Definition
\[
\mathbf{Sh}_{\mathbb F_2}(G):=\text{the category of }\mathbb F_2\text{-valued cellular sheaves on }G.
\]

\[
\mathcal I_{\mathrm{sheaf}}^{\mathrm{exact}}(G)
:=
\Bigl(
\mathbf{Sh}_{\mathbb F_2}(G),
\Gamma_G,
H^0_G,
H^1_G
\Bigr),
\]
\[
\Gamma_G:\mathbf{Sh}_{\mathbb F_2}(G)\to \mathbf{Vect}_{\mathbb F_2},
\qquad
H^i_G:\mathbf{Sh}_{\mathbb F_2}(G)\to \mathbf{Vect}_{\mathbb F_2}.
\]

## Open problem
\[
\exists G,H,\exists R\ge 0,\qquad
\mathcal I_{\mathrm{sheaf}}^{\mathrm{exact}}(G)\cong
\mathcal I_{\mathrm{sheaf}}^{\mathrm{exact}}(H)
\quad\land\quad
\beta^{\mathrm{prof}}_R(G)\neq\beta^{\mathrm{prof}}_R(H).
\]

## Colimit presentation and kernel obstruction

Let
\[
\mathcal D_R(K)
=
\Bigl(
\{Z_1(B_R(v;K))\}_{v\in V(K)},
\{Z_1(B_R(u;K)\cap B_R(v;K))\}_{\{u,v\}\in E(\Gamma_R(K))}
\Bigr).
\]

Set
\[
C_R(K):=
\Bigl(\bigoplus_{v\in V(K)} Z_1(B_R(v;K))\Bigr)\Big/\mathcal R_R(K),
\]
\[
\mathcal R_R(K):=
\left\langle
\iota_{uv\to u}(z)-\iota_{uv\to v}(z)
\;\middle|\;
\{u,v\}\in E(\Gamma_R(K)),\ z\in Z_1(B_R(u;K)\cap B_R(v;K))
\right\rangle .
\]

Then
\[
C_R(K)\cong \operatorname{colim}\mathcal D_R(K)
\text{ in }\mathbf{Vect}_{\mathbb F_2}.
\]

Let
\[
j_v:Z_1(B_R(v;K))\hookrightarrow Z_1(K)
\text{ be the inclusion.}
\]

The map
\[
\Phi_K:\bigoplus_{v\in V(K)} Z_1(B_R(v;K))\to X_R(K),
\qquad
\Phi_K((z_v)_v):=\sum_v j_v(z_v),
\]
vanishes on \(\mathcal R_R(K)\), hence descends to a canonical surjection
\[
\pi_K:C_R(K)\twoheadrightarrow X_R(K).
\]

Define
\[
\kappa_R(K):=\dim\ker(\pi_K).
\]

Then
\[
\dim X_R(K)=\dim C_R(K)-\kappa_R(K),
\]
and therefore
\[
\beta_R(K)=\dim Z_1(K)-\dim C_R(K)+\kappa_R(K).
\]

Minimal missing lemma:
\[
\ker(\pi_K)
\text{ is determined by the exact sheaf package }
\mathcal I_{\mathrm{sheaf}}^{\mathrm{exact}}(K,R).
\]
