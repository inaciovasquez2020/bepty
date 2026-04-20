# BEpTy Actual V2 Nonrecoverability Theorem

## Status
PROVED-FOR-REGISTERED-ACTUAL-FAMILY

## Exact comparison class
For every actual BEpTy object \(X\), define
\[
C_{\mathrm{ex}}(X):=(\mathrm{FN}(X),\mathrm{LSpan}(X)),
\qquad
J(X):=C_{\mathrm{ex}}(X).
\]

## V2 valuation
Define
\[
M_2(X):=\text{the 2-cycle/local-span incidence matrix of }X,
\]
\[
LV^{(2)}(X):=\operatorname{rank}_{\mathbf F_2}(M_2(X)),
\qquad
V_2(X):=\Phi_2(LV^{(2)}(X)).
\]

## Registered theorem lock
\[
J(X)\cong J(Y)\ \wedge\ V_2(X)\neq V_2(Y)\ \Longrightarrow\ X\not\cong Y.
\]

## Scope
ActualBEpTy

## V3 and higher
Do not add \(V_3,V_4,\dots\) unless \(V_2\) fails on the next obstruction class.

## Finish condition
The theorem lock is proved for the registered finite family returned by `enumerate_actual_objects()`. Do not upgrade beyond `PROVED-FOR-REGISTERED-ACTUAL-FAMILY` without extending the proof scope to the full intended actual class.
