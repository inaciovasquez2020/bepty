from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Dict, Mapping

@dataclass(frozen=True)
class ValuationSpec:
    name: str
    degree: int
    window: Any
    evaluator: Callable[[Any, Any], int]

class ValuationRegistry:
    def __init__(self, specs: Mapping[str, ValuationSpec]) -> None:
        self.specs: Dict[str, ValuationSpec] = dict(specs)

    def evaluate_all(self, K: Any) -> Dict[str, int]:
        return {
            name: spec.evaluator(K, spec.window)
            for name, spec in self.specs.items()
        }

    def describe(self) -> Dict[str, Dict[str, Any]]:
        return {
            name: {"degree": spec.degree, "window": spec.window}
            for name, spec in self.specs.items()
        }
