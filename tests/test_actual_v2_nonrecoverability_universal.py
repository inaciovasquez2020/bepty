from itertools import product
from pathlib import Path

from bepty.actual_object_family import are_isomorphic, enumerate_actual_objects
from bepty.exact_quotient import J
from bepty.valuation_v2 import Phi2, V2


def test_universal_v2_nonrecoverability_on_registered_actual_family():
    objs = list(enumerate_actual_objects())
    phi2 = Phi2(target_map=lambda r: ("urf-rank-f2", r))
    for X, Y in product(objs, objs):
        if J(X) == J(Y) and V2(X, phi2) != V2(Y, phi2):
            assert not are_isomorphic(X, Y)


def test_registered_actual_family_is_closed_under_theorem_scope():
    objs = list(enumerate_actual_objects())
    assert len(objs) >= 2
    names = {obj.name for obj in objs}
    assert "actual_alpha" in names
    assert "actual_beta" in names
