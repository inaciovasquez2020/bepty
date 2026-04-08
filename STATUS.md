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
