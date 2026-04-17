from pathlib import Path

def test_high_girth_local_pair_base_candidate_doc():
    s = Path("theory/HIGH_GIRTH_LOCAL_PAIR_BASE_CANDIDATE.md").read_text()
    assert "Status: CONDITIONAL" in s
    assert "N_r(G,H) := 1 + max\\{S_r(G), S_r(H)\\}." in s
    assert "\\widetilde W_r(X;G,H)" in s
    assert "coordinate bound" in s
