from pathlib import Path

def test_high_girth_local_bound_removal_gap_doc():
    s = Path("theory/HIGH_GIRTH_LOCAL_BOUND_REMOVAL_GAP.md").read_text()
    assert "Status: OPEN" in s
    assert "without dependence on an a priori coordinate bound M" in s
    assert "HIGH_GIRTH_LOCAL_WEIGHTING_BASE_B_CONDITIONAL" in s
    assert "HIGH_GIRTH_LOCAL_VALUATION_LEMMA" in s
