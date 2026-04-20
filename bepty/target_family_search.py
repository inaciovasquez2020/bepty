from __future__ import annotations

from dataclasses import dataclass
from importlib import import_module
from typing import Any, Iterable, Iterator, Optional, Tuple

from .exact_quotient import J
from .valuation_v2 import Phi2, V2


def _resolve(symbol: str):
    injected = globals().get(symbol)
    if callable(injected):
        return injected
    candidates = {
        "finite_normalization": [
            ("bepty.finite_normalization", "finite_normalization"),
            ("bepty.normalization", "finite_normalization"),
            ("bepty.core", "finite_normalization"),
        ],
    }[symbol]
    tried = []
    for module_name, attr_name in candidates:
        try:
            module = import_module(module_name)
            return getattr(module, attr_name)
        except (ModuleNotFoundError, AttributeError) as e:
            tried.append(f"{module_name}:{attr_name} -> {e}")
    raise ImportError(f"unable to resolve {symbol}; tried {tried}")


@dataclass(frozen=True)
class WitnessV2:
    X: Any
    Y: Any
    fn_value: Any
    jx: Any
    jy: Any
    v2x: Any
    v2y: Any


def enumerate_target_family_pairs(objs: Iterable[Any]) -> Iterator[Tuple[Any, Any]]:
    items = list(objs)
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            yield items[i], items[j]


def first_v2_witness(objs: Iterable[Any], phi2: Phi2) -> Optional[WitnessV2]:
    finite_normalization = _resolve("finite_normalization")
    for X, Y in enumerate_target_family_pairs(objs):
        fnx = finite_normalization(X)
        fny = finite_normalization(Y)
        if fnx != fny:
            continue
        v2x = V2(X, phi2)
        v2y = V2(Y, phi2)
        if v2x == v2y:
            continue
        return WitnessV2(
            X=X,
            Y=Y,
            fn_value=fnx,
            jx=J(X),
            jy=J(Y),
            v2x=v2x,
            v2y=v2y,
        )
    return None
