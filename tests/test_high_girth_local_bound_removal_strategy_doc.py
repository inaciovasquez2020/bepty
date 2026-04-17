from pathlib import Path

def test_high_girth_local_bound_removal_strategy_doc():
    s = Path("theory/HIGH_GIRTH_LOCAL_BOUND_REMOVAL_STRATEGY.md").read_text()
    assert "Status: OPEN" in s
    assert "B_r(X) := S_r(X) + 1." in s
    assert "W_r(X) := \\sum_{i=1}^{m} p_i(X) B_r(X)^{i-1}." in s
    assert "comparison-normalized canonicalization of the base" in s
