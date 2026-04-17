from pathlib import Path

def test_bepty_canonical_closure_index_exists():
    p = Path("docs/status/BEPTY_CANONICAL_CLOSURE_INDEX_2026_04_17.md")
    assert p.exists()

def test_bepty_canonical_closure_index_content():
    s = Path("docs/status/BEPTY_CANONICAL_CLOSURE_INDEX_2026_04_17.md").read_text()
    assert "docs/status/BEPTY_PUBLIC_STATUS_SNAPSHOT_2026_04_17.md" in s
    assert "docs/status/BEPTY_NEXT_TARGET_2026_04_17.md" in s
    assert "docs/math/BEPTY_THEOREM_FRONTIER_2026_04_17.md" in s
    assert "docs/math/BEPTY_WEAKEST_MISSING_THEOREM_2026_04_17.md" in s
    assert "docs/status/BEPTY_FRONTIER_REGISTRY_2026_04_17.md" in s
    assert "docs/math/BEPTY_HIGH_GIRTH_SEPARATION_TEMPLATE_2026_04_17.md" in s
    assert "docs/math/BEPTY_CANDIDATE_DATA_REQUIREMENTS_2026_04_17.md" in s
    assert "docs/status/BEPTY_MISSING_INPUT_PACKAGE_2026_04_17.md" in s
    assert "docs/status/BEPTY_CLOSURE_GATE_2026_04_17.md" in s
    assert "theorem closure may be promoted only after all objects listed in the closure gate are instantiated." in s
