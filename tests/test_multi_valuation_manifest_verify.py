from pathlib import Path

import pytest

from bepty.multi_valuation_manifest import build_manifest
from bepty.multi_valuation_manifest_io import write_manifest
from bepty.multi_valuation_manifest_verify import (
    verify_manifest_file,
    verify_manifest_obj,
)
from bepty.valuation_registry import ValuationRegistry, ValuationSpec

def _registry():
    return ValuationRegistry(
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

def test_verify_manifest_obj():
    manifest = build_manifest(
        None,
        "rX",
        signature_fn=lambda K, W: {"cells": 4, "window": W},
        registry=_registry(),
    )
    assert verify_manifest_obj(manifest) == {
        "ok": True,
        "sha256": manifest["sha256"],
    }

def test_verify_manifest_file(tmp_path: Path):
    manifest = build_manifest(
        None,
        "rX",
        signature_fn=lambda K, W: {"cells": 4, "window": W},
        registry=_registry(),
    )
    path = tmp_path / "manifest.json"
    write_manifest(path, manifest)
    assert verify_manifest_file(str(path)) == {
        "ok": True,
        "sha256": manifest["sha256"],
    }

def test_verify_manifest_obj_rejects_bad_hash():
    manifest = build_manifest(
        None,
        "rX",
        signature_fn=lambda K, W: {"cells": 4, "window": W},
        registry=_registry(),
    )
    manifest["sha256"] = "0" * 64
    with pytest.raises(ValueError):
        verify_manifest_obj(manifest)
