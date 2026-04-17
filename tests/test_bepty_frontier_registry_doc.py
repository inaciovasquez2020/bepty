from pathlib import Path

def test_bepty_frontier_registry_doc_exists():
    p = Path("docs/status/BEPTY_FRONTIER_REGISTRY_2026_04_17.md")
    assert p.exists()

def test_bepty_frontier_registry_doc_content():
    s = Path("docs/status/BEPTY_FRONTIER_REGISTRY_2026_04_17.md").read_text()
    assert "finite normalization over the declared actual compared class" in s
    assert "explicit high-girth local exhaustion family F" in s
    assert "explicit BEpTy valuation v beyond the current actual compared class" in s
    assert "docs/math/BEPTY_WEAKEST_MISSING_THEOREM_2026_04_17.md" in s
