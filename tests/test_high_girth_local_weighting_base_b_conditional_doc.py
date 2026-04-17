from pathlib import Path

def test_high_girth_local_weighting_base_b_conditional_doc():
    s = Path("theory/HIGH_GIRTH_LOCAL_WEIGHTING_BASE_B_CONDITIONAL.md").read_text()
    assert "Status: CONDITIONAL" in s
    assert "Let B := M + 1" in s
    assert "P_r(G) != P_r(H) => V_{r,B}(G) != V_{r,B}(H)." in s
    assert "bounded-coordinate hypothesis" in s
