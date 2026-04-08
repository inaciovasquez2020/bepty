# BEpTy Foundations

## Primitive datum
\[
A\subseteq B\subseteq X
\]

## Core object
\[
\mathbb E(A,B):=B\setminus A
\]

## Valuation
\[
\beta(A,B):=\Phi(B\setminus A)
\]

## Zero law
\[
\mathbb E(A,A)=\varnothing
\]

## Decomposition law
\[
A\subseteq B\subseteq C
\Rightarrow
\mathbb E(A,C)=\mathbb E(A,B)\sqcup\mathbb E(B,C)
\]

## Finite specialization
\[
\beta(A,B)=|B\setminus A|
\]

## Detection law
\[
\beta(A,B)=0 \iff A=B
\]

## Monotonicity law
\[
A\subseteq B\subseteq C \Rightarrow \beta(A,B)\le \beta(A,C)
\]

## Strict growth
\[
A\subseteq B\subsetneq C \Rightarrow \beta(A,B)<\beta(A,C)
\]

## Unit classification
\[
\beta(A,B)=1 \iff \exists!x\in X\; B=A\cup\{x\}
\]

## DenseAbs classification on finite sets
\[
\mathrm{DenseAbs}(A,B)\iff A=\varnothing
\]


## Topological specialization

\[
X \text{ topological},\qquad A\subseteq B\subseteq X.
\]

\[
\beta_{\mathrm{int}}(A,B):=
\begin{cases}
0,&\operatorname{int}(B\setminus A)=\varnothing,\\
1,&\operatorname{int}(B\setminus A)\neq\varnothing.
\end{cases}
\]

\[
\mathrm{Thin}(A,B)\iff \beta_{\mathrm{int}}(A,B)=0.
\]

## Open Detection

\[
A\subseteq B\subseteq X,\qquad B\setminus A \text{ open in }X
\]

\[
\Longrightarrow\qquad \beta_{\mathrm{int}}(A,B)=0 \iff A=B.
\]

## Closed Shell Detection

\[
A \text{ closed},\quad B \text{ open},\quad A\subseteq B
\]

\[
\Longrightarrow\qquad \beta_{\mathrm{int}}(A,B)=0 \iff A=B.
\]

