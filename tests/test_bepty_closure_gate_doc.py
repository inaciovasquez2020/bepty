from pathlib import Path

def test_bepty_closure_gate_exists():
    p = Path("docs/status/BEPTY_CLOSURE_GATE_2026_04_17.md")
    assert p.exists()

def test_bepty_closure_gate_content():
    s = Path("docs/status/BEPTY_CLOSURE_GATE_2026_04_17.md").read_text()
    assert "Provide all six objects:" in s
    assert "explicit pair family F = {G_n,H_n}_{n \\ge 1}" in s
    assert "explicit BEpTy valuation v" in s
    assert "compared-class agreement proof over {#V,#E,L_deg,I_cc}" in s
    assert "local exhaustion witness" in s
    assert "finite-normalization invariance proof for v" in s
    assert "explicit separation witness n with v(G_n) != v(H_n)" in s
    assert "theorem closure remains OPEN" in s
