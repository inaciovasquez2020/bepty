# BEpTy V2 Nonrecoverability Theorem

## Status
CONDITIONAL

## Exact comparison class
For every BEpTy object \(X\), define
\[
C_{\mathrm{ex}}(X) := (\mathrm{FN}(X), \mathrm{LSpan}(X)),
\qquad
J(X) := C_{\mathrm{ex}}(X).
\]

## V2 valuation
Define
\[
LV^{(2)}(X) := \operatorname{rank}_{\mathbf F_2}(M_2(X)),
\qquad
V_2(X) := \Phi_2(LV^{(2)}(X)).
\]

## Registered theorem schema
\[
J(X)\cong J(Y)\ \wedge\ V_2(X)\neq V_2(Y)\ \Longrightarrow\ X\not\cong Y.
\]

## First repository-native witness class
ConcreteBEpTy

## Finish condition
Replace `CONDITIONAL` by `PROVED` only after the theorem schema is discharged for the repository-native object family with executable witness certification and no injected test monkeypatches.
