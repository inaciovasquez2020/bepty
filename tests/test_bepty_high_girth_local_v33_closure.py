from pathlib import Path
import subprocess
import sys


def test_bepty_high_girth_local_v33_doc_tokens():
    s = Path("docs/math/BEPTY_HIGH_GIRTH_LOCAL_V33_CLOSURE_2026_05_02.md").read_text()
    assert "Status: PROPOSED CLOSURE PACKET" in s
    assert "girth}(G)>2R+1" in s
    assert "v_{33}" in s
    assert "{#V,#E,L_{\\deg},I_{cc}}" in s
    assert "finite-normalization invariance lemma" in s


def test_bepty_high_girth_local_v33_verifier():
    subprocess.run(
        [sys.executable, "scripts/verify_bepty_high_girth_local_v33_closure.py"],
        check=True,
    )
    artifact = Path("artifacts/bepty_high_girth_local_v33/witness.json")
    assert artifact.exists()
    s = artifact.read_text()
    assert '"status": "PASS"' in s
    assert '"v33_G": 1' in s
    assert '"v33_H": 0' in s
