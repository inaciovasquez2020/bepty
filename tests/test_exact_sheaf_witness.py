import json
import subprocess
import sys

def test_exact_sheaf_witness_separates_exact_package_and_profiled_betti():
    out = subprocess.check_output([sys.executable, "examples/exact_sheaf_witness.py"], text=True)
    data = json.loads(out)
    assert data["exact_sheaf_equal"] is False
    assert data["beta_prof_equal"] is False
    assert data["exact_nonrecoverability_refuted"] is True
    assert data["theta"]["exact_sheaf"]["num_vertices"] == 8
    assert data["theta"]["exact_sheaf"]["num_edges"] == 9
    assert data["dumbbell"]["exact_sheaf"]["num_vertices"] == 12
    assert data["dumbbell"]["exact_sheaf"]["num_edges"] == 13
