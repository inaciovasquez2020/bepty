from pathlib import Path

def test_high_girth_local_exhaustion_doc():
    s = Path("theory/HIGH_GIRTH_LOCAL_EXHAUSTION_THEOREM.md").read_text()
    assert "Status: OPEN" in s
    assert "B_r(G) != B_r(H)" in s
    assert "first nontrivial theorem target" in s
