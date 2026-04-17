from pathlib import Path

def test_ym_os_spectral_gap_extraction_doc_contains_gap_reduction():
    s = Path("docs/math/YM_OS_SPECTRAL_GAP_EXTRACTION.md").read_text()
    assert "spectral-gap extraction from the YM OS limit package" in s
    assert "\\operatorname{Spec}(H)\\cap(0,m)=\\varnothing" in s
    assert "\\langle \\psi,e^{-tH}\\psi\\rangle \\le e^{-mt}\\|\\psi\\|^2" in s
    assert "\\psi_F := [F] \\in \\mathcal H" in s
    assert "\\langle \\Omega,\\Theta F\\, \\tau_t(F)\\Omega\\rangle \\le C e^{-mt}" in s
    assert "prove an exponential Euclidean decay bound for one canonical reflected observable from the base family" in s
    assert "Action 1.12: spectral-gap extraction reduces to exponential Euclidean decay of one canonical reflected observable." in s
