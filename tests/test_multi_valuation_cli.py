import json
import subprocess
import sys
from pathlib import Path

from bepty.multi_valuation import MultiValuationCertificate
from bepty.multi_valuation_codec import certificate_to_json
from bepty.multi_valuation_hash import certificate_sha256

def test_multi_valuation_cli(tmp_path: Path):
    cert = MultiValuationCertificate(
        signature={"window": "r2", "cells": 4},
        valuations={"phi_dim": 3, "phi_residue": 1},
    )
    path = tmp_path / "cert.json"
    path.write_text(certificate_to_json(cert))
    expected = certificate_sha256(cert)
    out = subprocess.check_output(
        [
            sys.executable,
            "-m",
            "bepty.multi_valuation_cli",
            str(path),
            "--expected-sha256",
            expected,
        ],
        text=True,
    ).strip()
    assert json.loads(out) == {"ok": True, "sha256": expected}
