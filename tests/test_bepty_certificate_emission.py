import json
import subprocess
import sys
from pathlib import Path

def test_emit_and_verify_certificate():
    subprocess.run([sys.executable, "examples/emit_bepty_certificate.py"], check=True)
    target = Path("artifacts/bepty_certificate_example.json")
    assert target.exists()

    data = json.loads(target.read_text())
    assert data["object_type"] == "graph"
    assert data["valuation"] == "dim"
    assert isinstance(data["hash"], str) and len(data["hash"]) == 64

    subprocess.run(
        [sys.executable, "verifier/verify_bepty_certificate.py", str(target)],
        check=True,
    )
