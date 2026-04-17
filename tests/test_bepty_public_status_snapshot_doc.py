from pathlib import Path

def test_bepty_public_status_snapshot_exists():
    p = Path("docs/status/BEPTY_PUBLIC_STATUS_SNAPSHOT_2026_04_17.md")
    assert p.exists()

def test_bepty_public_status_snapshot_content():
    s = Path("docs/status/BEPTY_PUBLIC_STATUS_SNAPSHOT_2026_04_17.md").read_text()
    assert "Repository Completion: ~99%" in s
    assert "Program-Definitive Completion relative to the declared actual compared class: 100%" in s
    assert "Current actual compared class: {#V, #E, L_deg, I_cc}" in s
    assert "Prove one nontrivial theorem beyond finite normalization." in s
    assert "Realize one URF invariant as a BEpTy valuation." in s
    assert "theory/HighGirthLocalExhaustion.md" in s
    assert "notes/URF_INVARIANT_MATCHING.md" in s
