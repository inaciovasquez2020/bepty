from pathlib import Path

def test_bepty_theorem_frontier_doc_exists():
    p = Path("docs/math/BEPTY_THEOREM_FRONTIER_2026_04_17.md")
    assert p.exists()

def test_bepty_theorem_frontier_doc_content():
    s = Path("docs/math/BEPTY_THEM_FRONTIER_2026_04_17.md").read_text() if False else Path("docs/math/BEPTY_THEOREM_FRONTIER_2026_04_17.md").read_text()
    assert "High-girth local exhaustion theorem." in s
    assert "theory/HighGirthLocalExhaustion.md" in s
    assert "URF invariant realization" in s
