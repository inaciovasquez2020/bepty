from pathlib import Path
import json
import subprocess
import sys

def test_nonrecoverability_search_produces_decision_artifacts():
    out = subprocess.check_output([sys.executable, "tools/search_equal_package_nonrecoverability.py"], text=True)
    data = json.loads(out)
    assert "pairs_found" in data
    assert "decision_path" in data
    assert Path("artifacts/equal_package_candidates.json").exists()
    assert Path("notes/NONRECOVERABILITY_DECISION.md").exists()
    if data["pairs_found"] > 0:
        cert = json.loads(Path("artifacts/nonrecoverability_certificate.json").read_text())
        assert cert["status"] == "NONRECOVERABLE"
        assert cert["left"]["beta_prof"] != cert["right"]["beta_prof"]
        assert cert["left"]["V"] != cert["right"]["V"] or cert["left"]["E"] != cert["right"]["E"]
    else:
        cert = json.loads(Path("artifacts/symbolic_reconstruction_candidate.json").read_text())
        assert cert["deterministic_on_tested_domain"] is True
