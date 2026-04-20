from dataclasses import dataclass

from bepty.exact_quotient import C_ex, J
from bepty.valuation_v2 import Phi2, LV2_rank, V2
from bepty.target_family_search import first_v2_witness


def finite_normalization(obj):
    return obj.fn


def local_span_morphisms(obj):
    return obj.lspan


class Dummy:
    def __init__(self, fn, lspan, m2, name):
        self.fn = fn
        self.lspan = lspan
        self._m2 = m2
        self.name = name

    def cycle_local_span_incidence_matrix_2(self):
        return self._m2


import bepty.exact_quotient as eq
import bepty.valuation_v2 as vv


eq.finite_normalization = finite_normalization
eq.local_span_morphisms = local_span_morphisms


def test_c_ex_and_j():
    x = Dummy("n", [("a", "b")], [[1, 0], [0, 1]], "x")
    assert C_ex(x) == ("n", (("a", "b"),))
    assert J(x) == ("n", (("a", "b"),))


def test_lv2_and_v2():
    x = Dummy("n", [("a", "b")], [[1, 0], [0, 1]], "x")
    phi2 = Phi2(target_map=lambda r: ("urf-rank", r))
    assert LV2_rank(x) == 2
    assert V2(x, phi2) == ("urf-rank", 2)


def test_first_v2_witness():
    x = Dummy("same", [("a", "b")], [[1, 0], [0, 1]], "x")
    y = Dummy("same", [("a", "b")], [[1, 1], [1, 1]], "y")
    phi2 = Phi2(target_map=lambda r: ("urf-rank", r))

    import bepty.target_family_search as tfs
    tfs.finite_normalization = finite_normalization

    w = first_v2_witness([x, y], phi2)
    assert w is not None
    assert w.fn_value == "same"
    assert w.jx == w.jy
    assert w.v2x != w.v2y
