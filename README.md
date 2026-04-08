# BEpTy

[![CI](https://github.com/inaciovasquez2020/bepty/actions/workflows/ci.yml/badge.svg)](https://github.com/inaciovasquez2020/bepty/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/inaciovasquez2020/bepty)](https://github.com/inaciovasquez2020/bepty/releases/tag/v0.1.0)

BEpTy = Boundary-Encoded presence/Thinness calculus.

Core object:
\[
\mathbb E(A,B)=B\setminus A
\]

Current finite-set laws:
- Zero Law
- Decomposition Law
- Invariance Law
- Finite Detection Law
- Finite Monotonicity Law
- Finite Strict Growth
- Finite Unit Classification
- Finite DenseAbs Classification

Status:
- Foundational formalism
- Standalone repository
- Candidate bridge layer to URF after nontrivial applications


## Repository layout
- `theory/` — core BEpTy definitions and laws
- `notes/` — bridge notes and integration sketches
- `examples/` — concrete worked examples
- `STATUS.md` — live project state

## Release
- Current tag: `v0.1.0`
- Release asset: `BEpTy_NOTE.pdf`

## Next theorem target
- Prove one nontrivial theorem beyond finite normalization.
- Realize one URF invariant as a BEpTy valuation.


## URF-facing examples
- `theory/HighGirthLocalExhaustion.md` — first nontrivial theorem target
- `notes/URF_INVARIANT_MATCHING.md` — URF invariant to BEpTy valuation match
- `examples/c4_vs_tree_demo.md` — minimal cycle-vs-tree worked example
- `examples/local_exhaustion_demo.py` — executable toy demo
