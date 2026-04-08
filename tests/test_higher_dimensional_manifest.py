import json

from bepty.higher_dimensional import HigherDimensionalSpec, HigherDimensionalValuation
from bepty.higher_dimensional_manifest import build_higher_dimensional_manifest

class DummyValuation(HigherDimensionalValuation):
    def cycle_space_dim(self, K, d: int) -> int:
        return 7 + d

    def local_cycle_span_dim(self, K, d: int, window_spec) -> int:
        return 3

def test_build_higher_dimensional_manifest():
    manifest = build_higher_dimensional_manifest(
        None,
        spec=HigherDimensionalSpec(degree=2, window_spec="r3"),
        signature_fn=lambda K, d, w: {"degree": d, "window": w, "cells": 5},
        valuation=DummyValuation(),
    )
    assert manifest["certificate"] == {
        "degree": 2,
        "signature": {"degree": 2, "window": "r3", "cells": 5},
        "residual_dim": 6,
    }
    assert isinstance(manifest["sha256"], str)
    assert len(manifest["sha256"]) == 64
    assert json.loads(manifest["json"]) == manifest["certificate"]
