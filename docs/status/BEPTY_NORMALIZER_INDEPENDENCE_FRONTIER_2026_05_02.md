# BEpTy Normalizer-Independence Frontier

Status: FRONTIER_OPEN

## Current locked closure

The repository currently has only the explicit \(N_{\deg E}\)-normalized closure.

The locked normalizer is

\[
N_{\deg E}(X)=\mathcal E_{\deg}(X).
\]

The locked valuation is

\[
v_{33}(X)=\#\{\{u,w\}\in E(X):\deg_X(u)=3,\deg_X(w)=3\}.
\]

The locked normalized identity is

\[
v_{33}(N_{\deg E}(X))=v_{33}(X).
\]

## Remaining obstruction

The remaining obstruction is unrestricted normalizer-independence.

The missing theorem is

\[
\forall N\in\mathsf{AdmNorm}_{\mathrm{BEpTy}},\ \forall X,\qquad
v_{33}(N(X))=v_{33}(X).
\]

A stronger sufficient theorem is

\[
\forall N\in\mathsf{AdmNorm}_{\mathrm{BEpTy}},\ \forall X,\qquad
\mathcal E_{\deg}(N(X))=\mathcal E_{\deg}(X).
\]

The repository already records the reduction

\[
\mathcal E_{\deg}(N(X))=\mathcal E_{\deg}(X)
\Rightarrow
v_{33}(N(X))=v_{33}(X).
\]

## Conditional refutation of unconstrained normalizers

If admissible normalizers are unconstrained, unrestricted normalizer-independence is false.

Let

\[
N_0(X)=\varnothing.
\]

For the high-girth witness \(G_m\),

\[
v_{33}(G_m)=1.
\]

But

\[
v_{33}(N_0(G_m))=v_{33}(\varnothing)=0.
\]

Thus

\[
v_{33}(N_0(G_m))\ne v_{33}(G_m).
\]

Therefore unrestricted closure requires a nontrivial admissibility condition on normalizers.

## Required future theorem

To promote beyond the current lock, prove one of the following.

### Route A

Show that the existing BEpTy admissible normalizer definition implies

\[
\mathcal E_{\deg}(N(X))=\mathcal E_{\deg}(X).
\]

### Route B

Add an explicit admissibility class

\[
N\in\mathsf{AdmNorm}_{v33}
\iff
\forall X,\ \mathcal E_{\deg}(N(X))=\mathcal E_{\deg}(X).
\]

Then the closure remains admissibility-relative.

### Route C

If no admissibility condition is available, keep unrestricted closure refuted by the constant normalizer counterexample.

## Boundary

This does not assert unrestricted BEpTy closure unless normalizer-independence is proved.

This does not promote \(N_{\deg E}\)-normalized closure to unrestricted closure.

Unrestricted closure requires a theorem about all admissible BEpTy normalizers.

If admissible normalizers are unconstrained, unrestricted normalizer-independence is false.
