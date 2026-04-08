## Higher-dimensional generalization

Implemented package-level skeleton for `LocalValuationD` with quotient valuation
\[
\beta_d(K)=\dim_{\mathbb F_2}(Z_d(K)/\mathcal L_d(K)).
\]
Current repository status: architecture exported at package root, quotient-dimension sanity test passing, full higher-dimensional cycle/local-span implementation still open.

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



## Multi-valuation calculus

Implemented `MultiValuationCertificate` and `MultiValuationFactorization` as the repository-level skeleton for bundled valuations beyond `Z1`, now supporting direct valuation-registry integration with passing executable sanity tests.


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


## Profiled Betti separation
- Established witness:
  - `Theta(3,3,3)` and `Dumbbell(6,6)` have equal first Betti number `2`
  - but distinct profiled valuations:
    - `beta_prof_1(Theta(3,3,3)) = (2, {6:3})`
    - `beta_prof_1(Dumbbell(6,6)) = (2, {6:2, 12:1})`
- Current proved claim:
  - `beta_prof_R` is strictly finer than first Betti rank.
- Open frontier:
  - nonrecoverability from the chosen sheaf-theoretic comparison class.


## Sheaf-profile frontier
- Provisional comparison class fixed in `notes/SHEAF_COMPARISON_CLASS.md`
- Executable target demo: `examples/sheaf_profile_target.py`
- Current status:
  - provisional equal-sheaf witness passes
  - profiled valuation still separates
- Next formal requirement:
  - replace the provisional sheaf class by an exact categorical comparison class
  - prove or refute nonrecoverability for that exact class


## Admissible morphism layer
- Note: `notes/ADMISSIBLE_MORPHISMS.md`
- Exact sheaf package: `notes/EXACT_SHEAF_PACKAGE.md`
- Executable invariance toy demo: `examples/admissible_morphism_demo.py`


## Normalized rooted-ball profile witness
Current executable witness layer:
\[
\dim H_1(\Theta_{3,3,3};\mathbb F_2)=\dim H_1(D_{6,6};\mathbb F_2)=2,
\]
\[
\{\!\{\beta_1(B_1(v;\Theta_{3,3,3}))\}\!\}
=
\{\!\{0\}\!\}
=
\{\!\{\beta_1(B_1(v;D_{6,6}))\}\!\},
\]
but
\[
\operatorname{Hist}_1(\Theta_{3,3,3})\neq \operatorname{Hist}_1(D_{6,6}),
\qquad
\operatorname{Hist}_R(K):=\frac{1}{|V(K)|}\{\!\{\operatorname{code}(B_R(v;K),v)\}\!\}_{v\in V(K)}.
\]


## Current verification status
- certificate layer: schema-normalized, version-pinned, hash-normalized
- verifier layer: accepts valid certificates; rejects malformed and tampered certificates
- CI status: recovered to green after workflow-header normalization


## Completion snapshot
- repository hygiene: 96%
- executable certificate stack: 98%
- schema / verifier normalization: 98%
- CI stability: 96%
- canonical `(k=1, Phi=dim)` witness layer: 96%
- overall engineering completion: 94%
- overall mathematical-program completion: 88%

## Valuation registry

Implemented `ValuationSpec` and `ValuationRegistry` as the canonical descriptor layer for multi-valuation evaluation and schema-normalized registry export.

## Multi-valuation codec

Implemented deterministic JSON serialization for bundled multi-valuation certificates, with sorted-key normalization and executable codec tests.

## Multi-valuation hashing

Implemented deterministic SHA-256 hashing for bundled multi-valuation certificates on top of the normalized JSON codec, with executable hash-consistency tests.

## Multi-valuation schema

Implemented deterministic structural validation for bundled multi-valuation certificate dictionaries, with executable acceptance and rejection tests.

## Multi-valuation verification

Implemented normalized certificate verification combining schema validation and deterministic hash checking, with executable acceptance and rejection tests.

## Multi-valuation CLI

Implemented a minimal CLI entry path for normalized certificate verification from JSON, with an executable end-to-end subprocess test.

## Multi-valuation round-trip codec

Extended the deterministic codec with `certificate_from_dict` and `certificate_from_json`, giving a normalized round-trip transport path with executable round-trip tests.

## Multi-valuation bundle builder

Implemented `build_certificate` as the canonical construction path from a valuation registry and signature function to a bundled multi-valuation certificate, with an executable end-to-end builder test.

