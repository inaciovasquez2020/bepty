import json
import subprocess
import sys
from pathlib import Path

from bepty.higher_dimensional import HigherDimensionalSpec, HigherDimensionalValuation
from bepty.higher_dimensional_manifest import build_higher_dimensional_manifest
from bepty.higher_dimensional_manifest_io import write_higher_dimensional_manifest

class DummyValuation(HigherDimensionalValuation):
    def cycle_space_dim(self, K, d: int) -> int:
        return 7 + d

    def local_cycle_span_dim(self, K, d: int, window_spec) -> int:
        return 3

def test_higher_dimensional_manifest_cli(tmp_path: Path):
    manifest = build_higher_dimensional_manifest(
        None,
        spec=HigherDimensionalSpec(degree=2, window_spec="r3"),
        signature_fn=lambda K, d, w: {"degree": d, "window": w, "cells": 5},
        valuation=DummyValuation(),
    )
    path = tmp_path / "higher_manifest.json"
    write_higher_dimensional_manifest(path, manifest)
    out = subprocess.check_output(
        [
            sys.executable,
            "-m",
            "bepty.higher_dimensional_manifest_cli",
            str(path),
        ],
        text=True,
    ).strip()
    assert json.loads(out) == {"ok": True, "sha256": manifest["sha256"]}
