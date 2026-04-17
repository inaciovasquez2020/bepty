from pathlib import Path

def test_high_girth_local_weighting_separation_gap_doc():
    s = Path("theory/HIGH_GIRTH_LOCAL_WEIGHTING_SEPARATION_GAP.md").read_text()
    assert "Status: OPEN" in s
    assert "universally valid canonical weight vector" in s
    assert "P_r(G) != P_r(H)" in s
    assert "HIGH_GIRTH_LOCAL_VALUATION_LEMMA" in s
