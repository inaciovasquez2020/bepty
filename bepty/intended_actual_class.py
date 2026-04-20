from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Sequence, Tuple

from .actual_object_family import (
    ActualBEpTy,
    actual_alpha,
    actual_beta,
    actual_gamma,
)
from .exact_quotient import J
from .valuation_v2 import Phi2, V2


@dataclass(frozen=True)
class IntendedActualBEpTy:
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


def enumerate_intended_actual_objects() -> Tuple[IntendedActualBEpTy, ...]:
    a = actual_alpha()
    b = actual_beta()
    g = actual_gamma()
    return (
        IntendedActualBEpTy(
            name="intended_alpha",
            fn=a.fn,
            lspan=a.lspan,
            cells2=a.cells2,
            spans2=a.spans2,
            incidence2=a.incidence2,
            iso_tag=a.iso_tag,
        ),
        IntendedActualBEpTy(
            name="intended_beta",
            fn=b.fn,
            lspan=b.lspan,
            cells2=b.cells2,
            spans2=b.spans2,
            incidence2=b.incidence2,
            iso_tag=b.iso_tag,
        ),
        IntendedActualBEpTy(
            name="intended_gamma",
            fn=g.fn,
            lspan=g.lspan,
            cells2=g.cells2,
            spans2=g.spans2,
            incidence2=g.incidence2,
            iso_tag=g.iso_tag,
        ),
    )


def reduction_R(x: IntendedActualBEpTy) -> ActualBEpTy:
    for y in (actual_alpha(), actual_beta(), actual_gamma()):
        if x.iso_tag == y.iso_tag:
            return y
    raise ValueError(f"no registered representative for iso_tag={x.iso_tag!r}")


def intended_are_isomorphic(x: IntendedActualBEpTy, y: IntendedActualBEpTy) -> bool:
    return x.iso_tag == y.iso_tag


def actual_family_exhaustion_holds(phi2: Phi2) -> bool:
    for x in enumerate_intended_actual_objects():
        rx = reduction_R(x)
        if J(x) != J(rx):
            return False
        if V2(x, phi2) != V2(rx, phi2):
            return False
        if x.iso_tag != rx.iso_tag:
            return False
    return True
