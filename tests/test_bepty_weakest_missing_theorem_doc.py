from pathlib import Path

def test_bepty_weakest_missing_theorem_doc_exists():
    p = Path("docs/math/BEPTY_WEAKEST_MISSING_THEOREM_2026_04_17.md")
    assert p.exists()

def test_bepty_weakest_missing_theorem_doc_content():
    s = Path("docs/math/BEPTY_WEAKEST_MISSING_THEOREM_2026_04_17.md").read_text()
    assert "explicit high-girth local exhaustion family F" in s
    assert "explicit BEpTy valuation v" in s
    assert "current actual compared class {#V, #E, L_deg, I_cc}" in s
    assert "theory/HighGirthLocalExhaustion.md" in s
