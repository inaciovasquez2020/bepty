import json

from bepty.multi_valuation_manifest import build_manifest
from bepty.valuation_registry import ValuationRegistry, ValuationSpec

def test_build_manifest():
    reg = ValuationRegistry(
        {
            "phi_dim": ValuationSpec(
                name="phi_dim",
                degree=1,
                window="r2",
                evaluator=lambda K, W: 3,
            ),
            "phi_residue": ValuationSpec(
                name="phi_residue",
                degree=2,
                window="r3",
                evaluator=lambda K, W: 1,
            ),
        }
    )
    manifest = build_manifest(
        None,
        "rX",
        signature_fn=lambda K, W: {"cells": 4, "window": W},
        registry=reg,
    )
    assert manifest["certificate"] == {
        "signature": {"cells": 4, "window": "rX"},
        "valuations": {"phi_dim": 3, "phi_residue": 1},
    }
    assert isinstance(manifest["sha256"], str)
    assert len(manifest["sha256"]) == 64
    assert json.loads(manifest["json"]) == manifest["certificate"]
