from pathlib import Path

def test_high_girth_local_comparison_normalization_gap_doc():
    s = Path("theory/HIGH_GIRTH_LOCAL_COMPARISON_NORMALIZATION_GAP.md").read_text()
    assert "Status: OPEN" in s
    assert "\\widetilde W_r(X;G,H)" in s
    assert "N_r(G,H) is symmetric and canonical" in s
    assert "HIGH_GIRTH_LOCAL_BOUND_REMOVAL_GAP" in s
