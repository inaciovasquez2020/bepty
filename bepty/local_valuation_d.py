from __future__ import annotations

class LocalValuationD:
    def cycle_space_dim(self, K, d: int) -> int:
        raise NotImplementedError

    def local_cycle_span_dim(self, K, d: int, window_spec) -> int:
        raise NotImplementedError

    def quotient_dim(self, K, d: int, window_spec) -> int:
        return self.cycle_space_dim(K, d) - self.local_cycle_span_dim(K, d, window_spec)
