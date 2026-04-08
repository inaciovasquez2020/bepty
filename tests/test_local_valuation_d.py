from bepty.local_valuation_d import LocalValuationD

class Dummy(LocalValuationD):
    def cycle_space_dim(self, K, d: int) -> int:
        return 7

    def local_cycle_span_dim(self, K, d: int, window_spec) -> int:
        return 3

def test_quotient_dim():
    assert Dummy().quotient_dim(None, 2, None) == 4
