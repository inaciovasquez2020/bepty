from pathlib import Path

def test_bepty_next_target_doc_exists():
    p = Path("docs/status/BEPTY_NEXT_TARGET_2026_04_17.md")
    assert p.exists()

def test_bepty_next_target_doc_content():
    s = Path("docs/status/BEPTY_NEXT_TARGET_2026_04_17.md").read_text()
    assert "Prove one nontrivial theorem beyond finite normalization." in s
    assert "theory/HighGirthLocalExhaustion.md" in s
    assert "notes/URF_INVARIANT_MATCHING.md" in s
    assert "realize one URF invariant as a BEpTy valuation" in s
