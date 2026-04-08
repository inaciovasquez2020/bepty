from __future__ import annotations

from typing import Any, Callable, Mapping

from .higher_dimensional import HigherDimensionalSpec, HigherDimensionalValuation
from .valuation_registry import ValuationRegistry, ValuationSpec

def make_higher_dimensional_spec(
    *,
    name: str,
    spec: HigherDimensionalSpec,
    valuation: HigherDimensionalValuation,
) -> ValuationSpec:
    return ValuationSpec(
        name=name,
        degree=spec.degree,
        window=spec.window_spec,
        evaluator=lambda K, W: valuation.residual_dim(K, spec.degree, W),
    )

def build_higher_dimensional_registry(
    specs: Mapping[str, tuple[HigherDimensionalSpec, HigherDimensionalValuation]],
) -> ValuationRegistry:
    return ValuationRegistry(
        {
            name: make_higher_dimensional_spec(
                name=name,
                spec=spec,
                valuation=valuation,
            )
            for name, (spec, valuation) in specs.items()
        }
    )
