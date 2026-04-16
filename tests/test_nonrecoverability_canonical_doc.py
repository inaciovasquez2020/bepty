from pathlib import Path

def test_nonrecoverability_canonical_doc():
    s = Path("notes/NONRECOVERABILITY_CANONICAL.md").read_text()
    assert "NONRECOVERABLE" in s
    assert "\\beta^{\\mathrm{prof}}_{1}(K)\\neq\\beta^{\\mathrm{prof}}_{1}(L)" in s
