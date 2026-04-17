from pathlib import Path

def test_high_girth_local_valuation_construction_doc():
    s = Path("theory/HIGH_GIRTH_LOCAL_VALUATION_CONSTRUCTION.md").read_text()
    assert "Status: CONDITIONAL" in s
    assert "V_r(G) = \\sum_{i=1}^{m} i * p_i(G)." in s
    assert "universally valid canonical weighting scheme" in s
