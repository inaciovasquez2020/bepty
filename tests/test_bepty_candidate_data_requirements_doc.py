from pathlib import Path

def test_bepty_candidate_data_requirements_doc_exists():
    p = Path("docs/math/BEPTY_CANDIDATE_DATA_REQUIREMENTS_2026_04_17.md")
    assert p.exists()

def test_bepty_candidate_data_requirements_doc_content():
    s = Path("docs/math/BEPTY_CANDIDATE_DATA_REQUIREMENTS_2026_04_17.md").read_text()
    assert "explicit pair family F = {G_n,H_n}_{n \\ge 1}" in s
    assert "#V(G_n) = #V(H_n)" in s
    assert "#E(G_n) = #E(H_n)" in s
    assert "L_deg(G_n) = L_deg(H_n)" in s
    assert "I_cc(G_n) = I_cc(H_n)" in s
    assert "explicit BEpTy valuation v" in s
    assert "explicit n with v(G_n) \\neq v(H_n)" in s
    assert "no existence claim is made here" in s
