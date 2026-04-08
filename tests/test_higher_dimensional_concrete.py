from bepty.higher_dimensional import HigherDimensionalSpec, build_higher_dimensional_certificate
from bepty.higher_dimensional_concrete import ConcreteHigherDimensionalValuation, MatrixComplex
from bepty.higher_dimensional_manifest import build_higher_dimensional_manifest
from bepty.higher_dimensional_manifest_verify import verify_higher_dimensional_manifest_obj

def test_concrete_higher_dimensional_residual():
    K = MatrixComplex(
        boundary_d=[
            [1, 1, 0],
            [0, 1, 1],
        ],
        local_cycle_generators=[
            [1, 1, 1],
        ],
    )
    v = ConcreteHigherDimensionalValuation()
    assert v.cycle_space_dim(K, 2) == 1
    assert v.local_cycle_span_dim(K, 2, "r3") == 1
    assert v.residual_dim(K, 2, "r3") == 0

def test_concrete_higher_dimensional_certificate_and_manifest():
    K = MatrixComplex(
        boundary_d=[
            [0, 0, 0],
            [0, 0, 0],
        ],
        local_cycle_generators=[
            [1, 0, 0],
        ],
    )
    v = ConcreteHigherDimensionalValuation()
    spec = HigherDimensionalSpec(degree=2, window_spec="r3")
    cert = build_higher_dimensional_certificate(
        K,
        spec=spec,
        signature_fn=lambda K, d, w: {"degree": d, "window": w, "cells": 3},
        valuation=v,
    )
    assert cert.residual_dim == 2
    manifest = build_higher_dimensional_manifest(
        K,
        spec=spec,
        signature_fn=lambda K, d, w: {"degree": d, "window": w, "cells": 3},
        valuation=v,
    )
    assert verify_higher_dimensional_manifest_obj(manifest) == {
        "ok": True,
        "sha256": manifest["sha256"],
    }
