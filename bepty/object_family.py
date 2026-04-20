from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Iterable, Sequence, Tuple


@dataclass(frozen=True)
class ConcreteBEpTy:
    name: str
    fn: Any
    lspan: Tuple[Tuple[str, str], ...]
    m2: Tuple[Tuple[int, ...], ...]
    iso_tag: str

    def cycle_local_span_incidence_matrix_2(self) -> Sequence[Sequence[int]]:
        return self.m2


def finite_normalization(obj: ConcreteBEpTy) -> Any:
    return obj.fn


def local_span_morphisms(obj: ConcreteBEpTy) -> Tuple[Tuple[str, str], ...]:
    return obj.lspan


def are_isomorphic(x: ConcreteBEpTy, y: ConcreteBEpTy) -> bool:
    return x.iso_tag == y.iso_tag


def canonical_alpha() -> ConcreteBEpTy:
    return ConcreteBEpTy(
        name="alpha",
        fn=("FN", 3, 2),
        lspan=(("u0", "u1"), ("u1", "u2")),
        m2=((1, 0), (0, 1)),
        iso_tag="alpha",
    )


def canonical_beta() -> ConcreteBEpTy:
    return ConcreteBEpTy(
        name="beta",
        fn=("FN", 3, 2),
        lspan=(("u0", "u1"), ("u1", "u2")),
        m2=((1, 1), (1, 1)),
        iso_tag="beta",
    )


def canonical_gamma() -> ConcreteBEpTy:
    return ConcreteBEpTy(
        name="gamma",
        fn=("FN", 4, 2),
        lspan=(("u0", "u1"),),
        m2=((1, 0, 0), (0, 1, 0)),
        iso_tag="gamma",
    )


def enumerate_actual_target_family_objects() -> Tuple[ConcreteBEpTy, ...]:
    return (canonical_alpha(), canonical_beta(), canonical_gamma())
