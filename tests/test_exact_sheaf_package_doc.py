from pathlib import Path

def test_exact_sheaf_package_contains_exact_class_and_recovery_theorem():
    s = Path("notes/EXACT_SHEAF_PACKAGE.md").read_text()
    assert "\\mathcal C_{\\mathrm{exact}}" in s
    assert "\\mathsf{Sh}_{\\mathcal C_{\\mathrm{exact}}}(K)" in s
    assert "(\\#V,\\#E,L_{\\deg},I_{cc})" in s
    assert "Exact recovery theorem" in s
    assert "Consequence for the frontier" in s
