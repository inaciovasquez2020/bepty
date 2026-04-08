from examples.search_equal_signature_pairs import search


def test_search_runs_and_returns_none_or_witness():
    out = search(6, 1)
    assert out is None or (
        "G_edges" in out and
        "H_edges" in out and
        "hist_G" in out and
        "hist_H" in out
    )
