from __future__ import annotations

from typing import Any, Callable

def valuation_factors_through_coordinate(
    sigma_phi: Callable[[Any], Any],
    theta_phi: Callable[[Any], Any],
    G_phi: Callable[[Any], int],
    valuation: Callable[[Any], int],
    K: Any,
) -> bool:
    return valuation(K) == G_phi(theta_phi(sigma_phi(K)))
