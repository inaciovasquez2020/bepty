from pathlib import Path

import pytest

from bepty.higher_dimensional import HigherDimensionalSpec, HigherDimensionalValuation
from bepty.higher_dimensional_manifest import build_higher_dimensional_manifest
from bepty.higher_dimensional_manifest_io import write_higher_dimensional_manifest
from bepty.higher_dimensional_manifest_verify import (
    verify_higher_dimensional_manifest_file,
    verify_higher_dimensional_manifest_obj,
)

class DummyValuation(HigherDimensionalValuation):
    def cycle_space_dim(self, K, d: int) -> int:
        return 7 + d

    def local_cycle_span_dim(self, K, d: int, window_spec) -> int:
        return 3

def _manifest():
    return build_higher_dimensional_manifest(
        None,
        spec=HigherDimensionalSpec(degree=2, window_spec="r3"),
        signature_fn=lambda K, d, w: {"degree": d, "window": w, "cells": 5},
        valuation=DummyValuation(),
    )

def test_verify_higher_dimensional_manifest_obj():
    manifest = _manifest()
    assert verify_higher_dimensional_manifest_obj(manifest) == {
        "ok": True,
        "sha256": manifest["sha256"],
    }

def test_verify_higher_dimensional_manifest_file(tmp_path: Path):
    manifest = _manifest()
    path = tmp_path / "higher_manifest.json"
    write_higher_dimensional_manifest(path, manifest)
    assert verify_higher_dimensional_manifest_file(str(path)) == {
        "ok": True,
        "sha256": manifest["sha256"],
    }

def test_verify_higher_dimensional_manifest_obj_rejects_bad_hash():
    manifest = _manifest()
    manifest["sha256"] = "0" * 64
    with pytest.raises(ValueError):
        verify_higher_dimensional_manifest_obj(manifest)
