from pathlib import Path
import subprocess
import sys


def test_bepty_v33_finite_normalization_doc_tokens():
    s = Path("docs/math/BEPTY_V33_FINITE_NORMALIZATION_COMPATIBILITY_2026_05_02.md").read_text()
    assert "Status: CONDITIONAL LEMMA PACKET" in s
    assert "v_{33}(N(X))=v_{33}(X)" in s
    assert "\\mathcal E_{\\deg}(N(X))=\\mathcal E_{\\deg}(X)" in s
    assert "It does not assert" in s
    assert "remaining unconditional obligation" in s.lower()


def test_bepty_v33_finite_normalization_verifier():
    subprocess.run(
        [sys.executable, "scripts/verify_bepty_v33_finite_normalization_compatibility.py"],
        check=True,
    )
    artifact = Path("artifacts/bepty_v33_finite_normalization/compatibility_reduction.json")
    assert artifact.exists()
    s = artifact.read_text()
    assert '"status": "PASS"' in s
    assert "degree-labeled edge-incidence multiset preservation implies v33 preservation" in s
