import json
import subprocess
import sys
from pathlib import Path

import jsonschema

def test_emit_and_verify_certificate():
    subprocess.run([sys.executable, "examples/emit_bepty_certificate.py"], check=True)
    target = Path("artifacts/bepty_certificate_example.json")
    assert target.exists()

    data = json.loads(target.read_text())
    schema = json.loads(Path("schemas/bepty_certificate.schema.json").read_text())
    jsonschema.validate(instance=data, schema=schema)

    assert data["certificate_version"] == "v0.2.0"
    assert data["object_type"] == "graph"
    assert data["valuation"] == "dim"
    assert isinstance(data["hash"], str) and len(data["hash"]) == 64

    subprocess.run(
        [sys.executable, "verifier/verify_bepty_certificate.py", str(target)],
        check=True,
    )

def test_verify_rejects_malformed_certificate():
    bad = Path("tests/fixtures/invalid_bepty_certificate.json")
    proc = subprocess.run(
        [sys.executable, "verifier/verify_bepty_certificate.py", str(bad)],
        capture_output=True,
        text=True,
    )
    assert proc.returncode != 0
    assert "schema validation failed" in proc.stdout

def test_verify_rejects_hash_tampered_certificate():
    bad = Path("tests/fixtures/tampered_bepty_certificate.json")
    proc = subprocess.run(
        [sys.executable, "verifier/verify_bepty_certificate.py", str(bad)],
        capture_output=True,
        text=True,
    )
    assert proc.returncode != 0
    assert "hash mismatch" in proc.stdout
