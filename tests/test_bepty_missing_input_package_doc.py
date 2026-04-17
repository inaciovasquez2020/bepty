from pathlib import Path

def test_bepty_missing_input_package_doc_exists():
    p = Path("docs/status/BEPTY_MISSING_INPUT_PACKAGE_2026_04_17.md")
    assert p.exists()

def test_bepty_missing_input_package_doc_content():
    s = Path("docs/status/BEPTY_MISSING_INPUT_PACKAGE_2026_04_17.md").read_text()
    assert "explicit pair family F = {G_n,H_n}_{n \\ge 1}" in s
    assert "explicit BEpTy valuation v" in s
    assert "compared-class agreement proof over {#V, #E, L_deg, I_cc}" in s
    assert "local exhaustion witness" in s
    assert "finite-normalization invariance proof for v" in s
    assert "explicit separation witness n with v(G_n) \\neq v(H_n)" in s
