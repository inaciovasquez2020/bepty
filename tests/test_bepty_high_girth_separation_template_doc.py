from pathlib import Path

def test_bepty_high_girth_separation_template_exists():
    p = Path("docs/math/BEPTY_HIGH_GIRTH_SEPARATION_TEMPLATE_2026_04_17.md")
    assert p.exists()

def test_bepty_high_girth_separation_template_content():
    s = Path("docs/math/BEPTY_HIGH_GIRTH_SEPARATION_TEMPLATE_2026_04_17.md").read_text()
    assert "explicit family F = {G_n,H_n}_{n \\ge 1}" in s
    assert "explicit BEpTy valuation v" in s
    assert "#V(G_n) = #V(H_n)" in s
    assert "#E(G_n) = #E(H_n)" in s
    assert "L_deg(G_n) = L_deg(H_n)" in s
    assert "I_cc(G_n) = I_cc(H_n)" in s
    assert "v(G_n) \\neq v(H_n)" in s
    assert "It does not claim existence of F or v." in s
