from pathlib import Path

def test_readme_has_closure_path():
    s = Path("README.md").read_text()
    assert "## Canonical Closure Path" in s
    assert "docs/status/BEPTY_CANONICAL_CLOSURE_INDEX_2026_04_17.md" in s
    assert "docs/status/BEPTY_CLOSURE_GATE_2026_04_17.md" in s
    assert "docs/math/BEPTY_WEAKEST_MISSING_THEOREM_2026_04_17.md" in s

def test_readme_states_open_gate():
    s = Path("README.md").read_text()
    assert "Theorem closure remains OPEN until all closure-gate objects are instantiated." in s
