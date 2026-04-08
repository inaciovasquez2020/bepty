from bepty.higher_dimensional import HigherDimensionalSpec
from bepty.higher_dimensional_concrete import ConcreteHigherDimensionalValuation, MatrixComplex
from bepty.higher_dimensional_registry_bridge import build_higher_dimensional_registry
from bepty.unified_registry_manifest import build_unified_registry_manifest

def test_unified_registry_manifest_with_higher_dimensional_backend():
    K = MatrixComplex(
        boundary_d=[
            [0, 0, 0],
            [0, 0, 0],
        ],
        local_cycle_generators=[
            [1, 0, 0],
        ],
    )
    registry = build_higher_dimensional_registry(
        {
            "beta2": (
                HigherDimensionalSpec(degree=2, window_spec="r3"),
                ConcreteHigherDimensionalValuation(),
            )
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
        "valuations": {"beta2": 2},
    }
    assert isinstance(manifest["sha256"], str)
    assert len(manifest["sha256"]) == 64
