from pathlib import Path
import json

def test_urf_binding_doc_and_certificate_exist():
    s = Path("notes/URF_VALUATION_BINDING.md").read_text()
    assert "I_{\\mathrm{URF}}" in s
    assert "certificate-backed separation theorem" in s
    cert = json.loads(Path("artifacts/exact_sheaf_separation_certificate.json").read_text())
    assert cert["claims"]["exact_sheaf_equal"] is False
    assert cert["claims"]["beta_prof_1_equal"] is False
    assert cert["claims"]["urf_valuation_equal"] is False
