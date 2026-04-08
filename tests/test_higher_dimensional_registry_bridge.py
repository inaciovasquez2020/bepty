from bepty.higher_dimensional import HigherDimensionalSpec
from bepty.higher_dimensional_concrete import ConcreteHigherDimensionalValuation, MatrixComplex
from bepty.higher_dimensional_registry_bridge import (
    build_higher_dimensional_registry,
    make_higher_dimensional_spec,
)

def test_make_higher_dimensional_spec():
    K = MatrixComplex(
        boundary_d=[
            [0, 0, 0],
            [0, 0, 0],
        ],
        local_cycle_generators=[
            [1, 0, 0],
        ],
    )
    spec = HigherDimensionalSpec(degree=2, window_spec="r3")
    valuation = ConcreteHigherDimensionalValuation()
    reg_spec = make_higher_dimensional_spec(
        name="beta2",
        spec=spec,
        valuation=valuation,
    )
    assert reg_spec.name == "beta2"
    assert reg_spec.degree == 2
    assert reg_spec.window == "r3"
    assert reg_spec.evaluator(K, "r3") == 2

def test_build_higher_dimensional_registry():
    K = MatrixComplex(
        boundary_d=[
            [0, 0, 0],
            [0, 0, 0],
        ],
        local_cycle_generators=[
            [1, 0, 0],
        ],
    )
    reg = build_higher_dimensional_registry(
        {
            "beta2": (
                HigherDimensionalSpec(degree=2, window_spec="r3"),
                ConcreteHigherDimensionalValuation(),
            )
        }
    )
    assert reg.evaluate_all(K) == {"beta2": 2}
    assert reg.describe() == {"beta2": {"degree": 2, "window": "r3"}}
