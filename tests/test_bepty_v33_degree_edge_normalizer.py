from pathlib import Path
import subprocess
import sys


def test_bepty_v33_degree_edge_normalizer_doc_tokens():
    s = Path("docs/math/BEPTY_V33_DEGREE_EDGE_NORMALIZER_2026_05_02.md").read_text()
    assert "Status: EXPLICIT NORMALIZER PACKET" in s
    assert "N_{\\deg E}(X)=\\mathcal E_{\\deg}(X)" in s
    assert "v_{33}(N_{\\deg E}(X))=v_{33}(X)" in s
    assert "unconditional relative to the explicit normalizer" in s
    assert "does not assert unrestricted BEpTy closure" in s


def test_bepty_v33_degree_edge_normalizer_verifier():
    subprocess.run(
        [sys.executable, "scripts/verify_bepty_v33_degree_edge_normalizer.py"],
        check=True,
    )
    artifact = Path("artifacts/bepty_v33_degree_edge_normalizer/normalizer_certificate.json")
    assert artifact.exists()
    s = artifact.read_text()
    assert '"status": "PASS"' in s
    assert '"theorem": "v33(N_degE(X)) = v33(X)"' in s
    assert "It does not assert unrestricted BEpTy closure." in s
