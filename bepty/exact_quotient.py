from __future__ import annotations

from importlib import import_module
from typing import Any, Tuple


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
        "local_span_morphisms": [
            ("bepty.local_span", "local_span_morphisms"),
            ("bepty.span", "local_span_morphisms"),
            ("bepty.core", "local_span_morphisms"),
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


def C_ex(obj: Any) -> Tuple[Any, Any]:
    finite_normalization = _resolve("finite_normalization")
    local_span_morphisms = _resolve("local_span_morphisms")
    return (finite_normalization(obj), tuple(local_span_morphisms(obj)))


def J(obj: Any) -> Tuple[Any, Any]:
    return C_ex(obj)
