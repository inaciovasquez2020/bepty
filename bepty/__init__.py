from importlib import import_module

__all__ = [
    "finite_normalization",
    "local_span_morphisms",
    "C_ex",
    "J",
    "LocalValuationD",
    "Phi2",
    "LV2_rank",
    "V2",
    "enumerate_target_family_pairs",
    "first_v2_witness",
]

_EXPORT_MAP = {
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
    "C_ex": [("bepty.exact_quotient", "C_ex")],
    "J": [("bepty.exact_quotient", "J")],
    "LocalValuationD": [
        ("bepty.local_valuation_d", "LocalValuationD"),
        ("bepty.valuation_v2", "LocalValuationD"),
    ],
    "Phi2": [("bepty.valuation_v2", "Phi2")],
    "LV2_rank": [("bepty.valuation_v2", "LV2_rank")],
    "V2": [("bepty.valuation_v2", "V2")],
    "enumerate_target_family_pairs": [
        ("bepty.target_family_search", "enumerate_target_family_pairs"),
        ("bepty.target_family", "enumerate_target_family_pairs"),
    ],
    "first_v2_witness": [
        ("bepty.target_family_search", "first_v2_witness"),
        ("bepty.target_family", "first_v2_witness"),
    ],
}


def __getattr__(name):
    if name not in _EXPORT_MAP:
        raise AttributeError(f"module 'bepty' has no attribute {name!r}")
    tried = []
    for module_name, attr_name in _EXPORT_MAP[name]:
        try:
            module = import_module(module_name)
            value = getattr(module, attr_name)
            globals()[name] = value
            return value
        except (ModuleNotFoundError, AttributeError) as e:
            tried.append(f"{module_name}:{attr_name} -> {e}")
    raise AttributeError(f"unresolved export {name!r}; tried {tried}")


def __dir__():
    return sorted(set(globals()) | set(__all__))
