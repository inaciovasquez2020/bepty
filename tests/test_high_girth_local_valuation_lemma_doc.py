from pathlib import Path

def test_high_girth_local_valuation_lemma_doc():
    s = Path("theory/HIGH_GIRTH_LOCAL_VALUATION_LEMMA.md").read_text()
    assert "Status: OPEN" in s
    assert "P_r(G) != P_r(H)" in s
    assert "V_r(G) != V_r(H)" in s
    assert "single weakest missing lemma" in s
