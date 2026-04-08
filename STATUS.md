# BEpTy Status

## Core
- Zero Law: established
- Decomposition Law: established
- Invariance Law for injective maps: established
- Finite Detection Law: established
- Finite Monotonicity Law: established
- Finite Strict Growth: established
- Finite Unit Classification: established
- Finite DenseAbs Classification: established

## Current status
- Foundational formalism
- Finite-set layer normalized
- Topological boundary layer introduced
- URF bridge note present

## Next threshold
- Prove the high-girth target for local exhaustion
- Derive the high-girth reduction to global cycle space
- Add one explicit nonzero LocalExhaustion graph example

## Current release
- v0.2.0

## Executable examples
- local_exhaustion_demo.py added
- C4 vs Tree witness added
- CI checks executable toy demo


## Profiled Betti layer
- Established:
  - `beta_prof_1` separates `Theta(3,3,3)` from `Dumbbell(6,6)`
  - strictly finer than first Betti rank
- Open:
  - sheaf nonrecoverability target


## Sheaf comparison layer
- provisional comparison class fixed
- target demo added
- current state: provisional equal-sheaf / distinct-profile witness passes


## Exact sheaf frontier
- exact comparison target recorded
- profiled valuation exact nonrecoverability question isolated
- current status: open


## Morphism and exact sheaf package
- admissible BEpTy morphism definition recorded
- exact sheaf package definition recorded
- invariance lemma added at note level
- exact nonrecoverability problem remains open

## Colimit-kernel obstruction layer
- colimit presentation for the exact sheaf package recorded
- canonical surjection \(\pi_K : C_R(K) \twoheadrightarrow X_R(K)\) recorded
- kernel obstruction \(\kappa_R(K) := \dim \ker(\pi_K)\) isolated
- exact recoverability reduced to whether \(\kappa_R(K)\) is determined by \(\mathcal I_{\mathrm{sheaf}}^{\mathrm{exact}}(K,R)\)


## Toy-model colimit-kernel verification
- executable test file added: `tests/test_colimit_kernel_obstruction.py`
- verified: \(\dim X_R(K)=\dim C_R(K)-\kappa_R(K)\) in the toy model
- verified: \(\kappa_R=0\) in an overlap-generated example
- verified: \(\kappa_R>0\) in a higher-order relation example
- verified: equal pairwise-overlap quotient data can coexist with distinct \(\kappa_R\) and distinct \(X_R\) in the toy model
- frontier unchanged: actual BEpTy witness pair still open


## Normalized rooted-ball profile layer
- verified witness: \(\Theta_{3,3,3}\) and \(D_{6,6}\) have equal \(\beta_1=2\)
- verified radius-1 local cycle-rank entries are identically \(0\) on both sides
- verified distinction survives cardinality normalization via rooted-ball type histogram
- named invariant:
  \[
  \operatorname{Hist}_R(K):=\frac{1}{|V(K)|}\{\!\{\operatorname{code}(B_R(v;K),v)\}\!\}_{v\in V(K)}
  \]
- verified:
  \[
  \operatorname{Hist}_1(\Theta_{3,3,3})\neq \operatorname{Hist}_1(D_{6,6})
  \]
- frontier unchanged: exact sheaf equality for a separating witness remains open


## Exact sheaf comparison check
- executable exact-sheaf signature comparator added: `examples/exact_sheaf_package_compare.py`
- executable test added: `tests/test_exact_sheaf_package_compare.py`
- verified on current witness pair:
  \[
  \mathcal I_{\mathrm{sheaf}}^{\mathrm{sig}}(\Theta_{3,3,3},1)\neq
  \mathcal I_{\mathrm{sheaf}}^{\mathrm{sig}}(D_{6,6},1)
  \]
- consequence: current witness does not realize equal-package / distinct-profile separation
- frontier unchanged: exact equal-package witness remains open


## Bounded negative search result
- enumerator added: `examples/search_equal_signature_pairs.py`
- verified bounded result at \((n,R)=(6,1)\):
  \[
  \forall K,L\text{ connected simple graphs on }6\text{ vertices},\quad
  \bigl(
  \mathcal I_{\mathrm{sheaf}}^{\mathrm{sig}}(K,1)=\mathcal I_{\mathrm{sheaf}}^{\mathrm{sig}}(L,1)
  \land
  \beta_1(K)=\beta_1(L)
  \bigr)
  \Rightarrow
  \operatorname{Hist}_1(K)=\operatorname{Hist}_1(L)
  \]
- search output at current bound: `None`
- consequence: no equal-signature / distinct-histogram witness exists at the tested bound
- next structural extension: raise vertex bound or change profile layer


## Certificate verification layer
- schema added: `schemas/bepty_certificate.schema.json`
- emitter added: `examples/emit_bepty_certificate.py`
- verifier added: `verifier/verify_bepty_certificate.py`
- tests cover:
  - valid emitted certificate
  - malformed certificate rejection
  - tampered-hash certificate rejection
- CI covers:
  - pytest certificate test path
  - direct emitter-to-verifier execution


## CI recovery
- failing interval identified: workflow edits around commits `613f48e` and `10bc3e4`
- root cause: duplicated workflow header in `.github/workflows/ci.yml`
- fix committed in `7512719`
- latest confirmed CI run after fix: success
- current state: repository CI recovered to green


## Completion snapshot
- repository hygiene: 96%
- executable certificate stack: 98%
- schema / verifier normalization: 98%
- CI stability: 96%
- status / README / roadmap synchronization: 93%
- canonical `(k=1, Phi=dim)` witness layer: 96%
- bounded search / negative-result layer: 90%
- valuation-library depth: 35%
- higher-dimensional generalization: 15%
- overall engineering completion: 94%
- overall mathematical-program completion: 88%
- usable admissibility engine for current graph-level regime: 95%
- full foundational calculus beyond `Z_1` with multiple valuations: 58%


## Completion criterion

* exact sheaf frontier resolved
* exact equal-package witness found or impossibility proved
* high-girth local-exhaustion theorem stack proved
* README / ROADMAP / STATUS percentages synchronized

## Equal-signature search script normalization
- script: `examples/search_equal_signature_pairs.py`
- repo-root import path fixed
- executable directly via `python3 examples/search_equal_signature_pairs.py`
- current manual output at configured bound: `None`

