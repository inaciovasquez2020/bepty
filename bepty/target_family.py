from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, Mapping, Optional, Sequence, Tuple


Edge = Tuple[int, int]


def _normalize_edge(u: int, v: int) -> Edge:
    if u == v:
        raise ValueError("loops are not allowed")
    return (u, v) if u < v else (v, u)


class Graph:
    def __init__(
        self,
        *,
        vertices: Sequence[int] | None = None,
        edges: Iterable[Edge] = (),
        n: int | None = None,
    ) -> None:
        if vertices is None:
            if n is None:
                raise TypeError("Graph requires either vertices=... or n=...")
            vertices = tuple(range(n))
        else:
            vertices = tuple(vertices)
            if n is not None and len(vertices) != n:
                raise ValueError("n must match len(vertices)")
        vset = set(vertices)
        if len(vset) != len(vertices):
            raise ValueError("vertices must be unique")
        normalized = tuple(sorted(_normalize_edge(u, v) for u, v in edges))
        if len(set(normalized)) != len(normalized):
            raise ValueError("edges must be unique")
        for u, v in normalized:
            if u not in vset or v not in vset:
                raise ValueError("edge endpoint not in vertices")
        self.vertices: Tuple[int, ...] = vertices
        self.edges: Tuple[Edge, ...] = normalized
        self._edge_set = frozenset(normalized)

    def __repr__(self) -> str:
        return f"Graph(vertices={self.vertices!r}, edges={self.edges!r})"

    @property
    def n(self) -> int:
        return len(self.vertices)

    @property
    def m(self) -> int:
        return len(self.edges)

    @property
    def adjacency(self) -> Dict[int, Tuple[int, ...]]:
        adj = {v: set() for v in self.vertices}
        for u, v in self.edges:
            adj[u].add(v)
            adj[v].add(u)
        return {v: tuple(sorted(adj[v])) for v in self.vertices}

    def has_edge(self, u: int, v: int) -> bool:
        if u == v:
            return False
        return _normalize_edge(u, v) in self._edge_set

    def degree(self, v: int) -> int:
        return len(self.adjacency[v])

    def relabel(self, mapping: Mapping[int, int]) -> "Graph":
        new_vertices = tuple(mapping.get(v, v) for v in self.vertices)
        new_edges = tuple(_normalize_edge(mapping.get(u, u), mapping.get(v, v)) for u, v in self.edges)
        return Graph(vertices=new_vertices, edges=new_edges)


@dataclass(frozen=True)
class GraphFamily:
    plus: Graph
    minus: Graph
    name: str
    twist_index: Optional[int] = None

    @property
    def n(self) -> int:
        return self.plus.n


def connected_components(g: Graph) -> int:
    adj = g.adjacency
    seen = set()
    cc = 0
    for v in g.vertices:
        if v in seen:
            continue
        cc += 1
        stack = [v]
        seen.add(v)
        while stack:
            x = stack.pop()
            for y in adj[x]:
                if y not in seen:
                    seen.add(y)
                    stack.append(y)
    return cc


def cycle_rank(g: Graph) -> int:
    return g.m - g.n + connected_components(g)


def triangular_prism_graph() -> Graph:
    return Graph(
        vertices=(0, 1, 2, 3, 4, 5),
        edges=(
            (0, 1), (1, 2), (0, 2),
            (3, 4), (4, 5), (3, 5),
            (0, 3), (1, 4), (2, 5),
        ),
    )


def k33_graph() -> Graph:
    left = (0, 1, 2)
    right = (3, 4, 5)
    return Graph(
        vertices=left + right,
        edges=tuple((u, v) for u in left for v in right),
    )


def regular_equal_cc_pair() -> GraphFamily:
    return GraphFamily(
        plus=k33_graph(),
        minus=triangular_prism_graph(),
        name="regular_equal_cc_pair",
    )


def two_lift_pair_of_cycle(n: int = 4, twist_index: int = 0) -> GraphFamily:
    if n < 3:
        raise ValueError("n must be at least 3")
    twist_index %= n

    vertices = tuple(range(2 * n))

    def v(layer: int, i: int) -> int:
        return 2 * i + layer

    trivial_edges = []
    twisted_edges = []

    for i in range(n):
        j = (i + 1) % n

        trivial_edges.append((v(0, i), v(0, j)))
        trivial_edges.append((v(1, i), v(1, j)))

        if i == twist_index:
            twisted_edges.append((v(0, i), v(1, j)))
            twisted_edges.append((v(1, i), v(0, j)))
        else:
            twisted_edges.append((v(0, i), v(0, j)))
            twisted_edges.append((v(1, i), v(1, j)))

    return GraphFamily(
        plus=Graph(vertices=vertices, edges=tuple(trivial_edges)),
        minus=Graph(vertices=vertices, edges=tuple(twisted_edges)),
        name="two_lift_pair_of_cycle",
        twist_index=twist_index,
    )


from .actual_object_family import ActualBEpTy, are_isomorphic, enumerate_actual_objects
from .target_family_search import enumerate_target_family_pairs, first_v2_witness

__all__ = [
    "Graph",
    "GraphFamily",
    "connected_components",
    "cycle_rank",
    "triangular_prism_graph",
    "k33_graph",
    "regular_equal_cc_pair",
    "two_lift_pair_of_cycle",
    "ActualBEpTy",
    "are_isomorphic",
    "enumerate_actual_objects",
    "enumerate_target_family_pairs",
    "first_v2_witness",
]
