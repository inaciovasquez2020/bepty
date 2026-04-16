from pathlib import Path

def test_functorial_profiled_valuation_doc_contains_invariance_and_functoriality():
    s = Path("notes/FUNCTORIAL_PROFILED_VALUATION.md").read_text()
    assert "\\beta^{\\mathrm{prof}}_{R}" in s
    assert "admissible morphism" in s
    assert "Functoriality" in s
    assert "\\beta^{\\mathrm{prof}}_{R}(g\\circ f)" in s
