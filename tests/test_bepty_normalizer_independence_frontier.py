from pathlib import Path
import json
import subprocess
import sys


def test_bepty_normalizer_independence_frontier_doc_tokens():
    s = Path("docs/status/BEPTY_NORMALIZER_INDEPENDENCE_FRONTIER_2026_05_02.md").read_text()
    assert "Status: FRONTIER_OPEN" in s
    assert "remaining obstruction is unrestricted normalizer-independence" in s
    assert "This does not assert unrestricted BEpTy closure unless normalizer-independence is proved." in s
    assert "This does not promote \\(N_{\\deg E}\\)-normalized closure to unrestricted closure." in s
    assert "Unrestricted closure requires a theorem about all admissible BEpTy normalizers." in s
    assert "If admissible normalizers are unconstrained, unrestricted normalizer-independence is false." in s
    assert "N_0(X)=\\varnothing" in s
    assert "v_{33}(N_0(G_m))\\ne v_{33}(G_m)" in s


def test_bepty_normalizer_independence_frontier_verifier():
    subprocess.run(
        [sys.executable, "scripts/verify_bepty_normalizer_independence_frontier.py"],
        check=True,
    )
    artifact = Path("artifacts/bepty_normalizer_independence_frontier/status.json")
    assert artifact.exists()
    data = json.loads(artifact.read_text())
    assert data["status"] == "FRONTIER_OPEN"
    assert data["current_closure"] == "N_DEGE_NORMALIZED_CLOSURE_ONLY"
    assert data["remaining_obstruction"] == "normalizer-independence / unrestricted BEpTy closure"
    assert "unrestricted BEpTy closure" in data["not_claimed"]
