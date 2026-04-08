from pathlib import Path

from bepty.multi_valuation_manifest import build_manifest
from bepty.multi_valuation_manifest_io import read_manifest, write_manifest
from bepty.valuation_registry import ValuationRegistry, ValuationSpec

def test_manifest_io_roundtrip(tmp_path: Path):
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
    path = tmp_path / "manifest.json"
    write_manifest(path, manifest)
    assert read_manifest(path) == manifest
