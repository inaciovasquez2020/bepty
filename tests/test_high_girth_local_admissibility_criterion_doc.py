from pathlib import Path

def test_high_girth_local_admissibility_criterion_doc():
    s = Path("theory/HIGH_GIRTH_LOCAL_ADMISSIBILITY_CRITERION.md").read_text()
    assert "Status: OPEN" in s
    assert "depends only on rooted radius-r profile data" in s
    assert "admissibility_criterion => HIGH_GIRTH_LOCAL_ADMISSIBILITY_GAP" in s
    assert "Specify the exact BEpTy admissibility axioms" in s
