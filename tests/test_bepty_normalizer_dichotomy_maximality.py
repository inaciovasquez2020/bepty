from pathlib import Path
import json
import subprocess
import sys


def test_bepty_normalizer_dichotomy_maximality_doc_tokens():
    s = Path("docs/math/BEPTY_NORMALIZER_DICHOTOMY_MAXIMALITY_2026_05_02.md").read_text()
    assert "Status: MAXIMALITY THEOREM PACKET" in s
    assert "Normalizer Dichotomy / Maximality" in s
    assert "Preservation case" in s
    assert "Obstruction case" in s
    assert "N_{\\deg E}-normalized closure" in s
    assert "\\mathsf{AdmNorm}_{v33}" in s


def test_bepty_normalizer_dichotomy_maximality_status_boundaries():
    s = Path("docs/status/BEPTY_NORMALIZER_DICHOTOMY_MAXIMALITY_STATUS_2026_05_02.md").read_text()
    assert "This does not assert unrestricted BEpTy closure." in s
    assert "This does not assert normalizer-independence." in s
    assert "This does not declare \\(\\mathsf{AdmNorm}_{v33}\\) as a foundational BEpTy axiom." in s
    assert "This certifies maximality of the current \\(N_{\\deg E}\\)-normalized closure status under the existing repository assumptions." in s
    assert "Any future unrestricted promotion requires a foundational admissible-normalizer class implying \\(\\mathsf{AdmNorm}_{v33}\\)." in s


def test_bepty_normalizer_dichotomy_maximality_verifier():
    subprocess.run(
        [sys.executable, "scripts/verify_bepty_normalizer_dichotomy_maximality.py"],
        check=True,
    )
    artifact = Path("artifacts/bepty_normalizer_dichotomy_maximality/maximality_certificate.json")
    assert artifact.exists()
    data = json.loads(artifact.read_text())
    assert data["status"] == "PASS"
    assert data["classification"] == "NORMALIZER_DICHOTOMY_MAXIMALITY_LOCK"
    assert data["current_repository_status"] == "N_DEGE_NORMALIZED_CLOSURE_ONLY"
    assert data["class_checks"]["Class A {N_degE}"]["case"] == "PRESERVATION_CASE"
    assert data["class_checks"]["Class B {N0}"]["case"] == "OBSTRUCTION_CASE"
    assert data["class_checks"]["Class C {N_degE,N0}"]["case"] == "OBSTRUCTION_CASE"
