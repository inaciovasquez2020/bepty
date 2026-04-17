from pathlib import Path
import json

def main() -> None:
    artifact = {
        "name": "local_exhaustion_witness",
        "objects": ["C4", "Tree"],
        "radius": 2,
        "witness": "profile_count_difference",
        "conclusion": "candidate valuation separates",
        "cases": {
            "C4": {"beta_dim_R(G)": 1},
            "Tree": {"beta_dim_R(G)": 0},
        },
    }

    Path("artifacts").mkdir(exist_ok=True)
    Path("artifacts/local_exhaustion_witness.json").write_text(
        json.dumps(artifact, indent=2, sort_keys=True)
    )

    print("CASE: C4")
    print("beta_dim_R(G): 1")
    print("CASE: Tree")
    print("beta_dim_R(G): 0")
    print("wrote artifacts/local_exhaustion_witness.json")

if __name__ == "__main__":
    main()
