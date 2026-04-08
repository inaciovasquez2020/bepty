# BEpTy–YM Bridge Note

Define the executable bridge object
\[
\mathrm{Bridge}(A,B)
\]
by the JSON report emitted from
`src/bridge/bepty_ym_bridge.py`.

For the tested pair
\[
(A,B)=\bigl(G_{\mathrm{prism}},G_{K_{3,3}}\bigr),
\]
the bridge certifies
\[
|V(A)|=|V(B)|,\qquad |E(A)|=|E(B)|,\qquad L_{\deg}(A)=L_{\deg}(B),\qquad I_{\mathrm{cc}}(A,B)=0,
\]
while
\[
\beta_{\triangle}(A,B)=\triangle(B)-\triangle(A)=-2\neq 0.
\]

The emitted artifact is
\[
\texttt{artifacts/HED\_MATH\_CONDITIONAL.json}.
\]

Status:
\[
\texttt{conditional-executable-witness}.
\]
