from __future__ import annotations
from dataclasses import dataclass
from typing import FrozenSet, Tuple

Edge = Tuple[int, int]


def _norm_edge(u: int, v: int) -> Edge:
    return (u, v) if u <= v else (v, u)


@dataclass(frozen=True)
class Graph:
    n: int
    edges: FrozenSet[Edge]

    def has_edge(self, u: int, v: int) -> bool:
        return _norm_edge(u, v) in self.edges

    def degree(self, v: int) -> int:
        return sum(1 for a, b in self.edges if a == v or b == v)


@dataclass(frozen=True)
class FamilyPair:
    base: Graph
    plus: Graph
    minus: Graph
    twist_edge: Edge


def cycle_graph(n: int) -> Graph:
    if n < 3:
        raise ValueError("n >= 3 required")
    edges = {_norm_edge(i, (i + 1) % n) for i in range(n)}
    return Graph(n=n, edges=frozenset(edges))


def two_lift_pair_of_cycle(n: int, twist_index: int = 0) -> FamilyPair:
    if n < 3:
        raise ValueError("n >= 3 required")
    if not (0 <= twist_index < n):
        raise ValueError("twist_index out of range")

    base = cycle_graph(n)
    plus_edges: set[Edge] = set()
    minus_edges: set[Edge] = set()

    def top(i: int) -> int:
        return i

    def bot(i: int) -> int:
        return n + i

    twist_edge = _norm_edge(twist_index, (twist_index + 1) % n)

    for i in range(n):
        j = (i + 1) % n
        e = _norm_edge(i, j)

        plus_edges.add(_norm_edge(top(i), top(j)))
        plus_edges.add(_norm_edge(bot(i), bot(j)))

        if e == twist_edge:
            minus_edges.add(_norm_edge(top(i), bot(j)))
            minus_edges.add(_norm_edge(bot(i), top(j)))
        else:
            minus_edges.add(_norm_edge(top(i), top(j)))
            minus_edges.add(_norm_edge(bot(i), bot(j)))

    plus = Graph(n=2 * n, edges=frozenset(plus_edges))
    minus = Graph(n=2 * n, edges=frozenset(minus_edges))
    return FamilyPair(base=base, plus=plus, minus=minus, twist_edge=twist_edge)


def connected_components(G: Graph) -> int:
    seen = set()
    count = 0
    adj = {v: set() for v in range(G.n)}
    for u, v in G.edges:
        adj[u].add(v)
        adj[v].add(u)
    for s in range(G.n):
        if s in seen:
            continue
        count += 1
        stack = [s]
        seen.add(s)
        while stack:
            x = stack.pop()
            for y in adj[x]:
                if y not in seen:
                    seen.add(y)
                    stack.append(y)
    return count


def cycle_rank(G: Graph) -> int:
    return len(G.edges) - G.n + connected_components(G)


def triangular_prism_graph() -> Graph:
    edges = {
        _norm_edge(0, 1), _norm_edge(1, 2), _norm_edge(2, 0),
        _norm_edge(3, 4), _norm_edge(4, 5), _norm_edge(5, 3),
        _norm_edge(0, 3), _norm_edge(1, 4), _norm_edge(2, 5),
    }
    return Graph(n=6, edges=frozenset(edges))


def k33_graph() -> Graph:
    left = [0, 1, 2]
    right = [3, 4, 5]
    edges = {_norm_edge(u, v) for u in left for v in right}
    return Graph(n=6, edges=frozenset(edges))


def regular_equal_cc_pair() -> FamilyPair:
    base = Graph(n=0, edges=frozenset())
    plus = k33_graph()
    minus = triangular_prism_graph()
    return FamilyPair(base=base, plus=plus, minus=minus, twist_edge=(0, 0))

from .target_family_search import enumerate_target_family_pairs, first_v2_witness
