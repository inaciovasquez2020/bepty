from pathlib import Path
import json
import subprocess
import sys


def test_bepty_final_status_index_doc_tokens():
    s = Path("docs/status/BEPTY_FINAL_STATUS_INDEX_2026_05_02.md").read_text()
    assert "Status: FINAL STATUS INDEX" in s
    assert "N_{\\deg E}\\text{-NORMALIZED CLOSURE ONLY}" in s
    assert "Normalizer Dichotomy / Maximality lock" in s
    assert "\\mathsf{AdmNorm}_{\\mathrm{BEpTy}}\\subseteq\\mathsf{AdmNorm}_{v33}" in s
    assert "This does not assert unrestricted BEpTy closure." in s
    assert "This does not assert normalizer-independence." in s
    assert "This does not promote beyond \\(N_{\\deg E}\\)-normalized closure." in s


def test_bepty_final_status_index_verifier():
    subprocess.run(
        [sys.executable, "scripts/verify_bepty_final_status_index.py"],
        check=True,
    )
    artifact = Path("artifacts/bepty_final_status_index/final_status_index_certificate.json")
    assert artifact.exists()
    data = json.loads(artifact.read_text())
    assert data["status"] == "PASS"
    assert data["classification"] == "FINAL_STATUS_INDEX_LOCK"
    assert data["repository_status"] == "N_DEGE_NORMALIZED_CLOSURE_ONLY"
    assert "unrestricted BEpTy closure" in data["not_claimed"]
