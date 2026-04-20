from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Sequence, Tuple


@dataclass(frozen=True)
class ActualBEpTy:
    name: str
    fn: Any
    lspan: Tuple[Tuple[str, str], ...]
    cells2: Tuple[str, ...]
    spans2: Tuple[str, ...]
    incidence2: Tuple[Tuple[int, ...], ...]
    iso_tag: str

    def M2(self) -> Sequence[Sequence[int]]:
        return self.incidence2

    def cycle_local_span_incidence_matrix_2(self) -> Sequence[Sequence[int]]:
        return self.incidence2


def finite_normalization(obj: ActualBEpTy) -> Any:
    return obj.fn


def local_span_morphisms(obj: ActualBEpTy) -> Tuple[Tuple[str, str], ...]:
    return obj.lspan


def are_isomorphic(x: ActualBEpTy, y: ActualBEpTy) -> bool:
    return x.iso_tag == y.iso_tag


def actual_alpha() -> ActualBEpTy:
    return ActualBEpTy(
        name="actual_alpha",
        fn=("FN", "A", 2),
        lspan=(("e0", "e1"), ("e1", "e2")),
        cells2=("c0", "c1"),
        spans2=("s0", "s1"),
        incidence2=((1, 0), (0, 1)),
        iso_tag="alpha",
    )


def actual_beta() -> ActualBEpTy:
    return ActualBEpTy(
        name="actual_beta",
        fn=("FN", "A", 2),
        lspan=(("e0", "e1"), ("e1", "e2")),
        cells2=("c0", "c1"),
        spans2=("s0", "s1"),
        incidence2=((1, 1), (1, 1)),
        iso_tag="beta",
    )


def actual_gamma() -> ActualBEpTy:
    return ActualBEpTy(
        name="actual_gamma",
        fn=("FN", "B", 2),
        lspan=(("e0", "e1"),),
        cells2=("c0", "c1"),
        spans2=("s0", "s1", "s2"),
        incidence2=((1, 0, 0), (0, 1, 0)),
        iso_tag="gamma",
    )


def enumerate_actual_objects() -> Tuple[ActualBEpTy, ...]:
    return (actual_alpha(), actual_beta(), actual_gamma())
