from bepty.higher_dimensional import HigherDimensionalSpec
from bepty.higher_dimensional_concrete import ConcreteHigherDimensionalValuation, MatrixComplex
from bepty.higher_dimensional_registry_bridge import make_higher_dimensional_spec
from bepty.unified_registry_manifest import build_unified_registry_manifest
from bepty.valuation_registry import ValuationRegistry, ValuationSpec

def test_unified_mixed_registry_manifest():
    K = MatrixComplex(
        boundary_d=[
            [0, 0, 0],
            [0, 0, 0],
        ],
        local_cycle_generators=[
            [1, 0, 0],
        ],
    )
    registry = ValuationRegistry(
        {
            "phi_dim": ValuationSpec(
                name="phi_dim",
                degree=1,
                window="r2",
                evaluator=lambda K, W: 3,
            ),
            "beta2": make_higher_dimensional_spec(
                name="beta2",
                spec=HigherDimensionalSpec(degree=2, window_spec="r3"),
                valuation=ConcreteHigherDimensionalValuation(),
            ),
        }
    )
    manifest = build_unified_registry_manifest(
        K,
        "root-window",
        signature_fn=lambda K, W: {"window": W, "cells": 3},
        registry=registry,
    )
    assert manifest["certificate"] == {
        "signature": {"window": "root-window", "cells": 3},
        "valuations": {"phi_dim": 3, "beta2": 2},
    }
    assert isinstance(manifest["sha256"], str)
    assert len(manifest["sha256"]) == 64
