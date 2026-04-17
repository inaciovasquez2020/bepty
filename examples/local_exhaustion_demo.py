from pathlib import Path
import json

artifact = {
    "name": "local_exhaustion_witness",
    "objects": ["G", "H"],
    "radius": 2,
    "witness": "profile_count_difference",
    "conclusion": "candidate valuation separates"
}

Path("artifacts").mkdir(exist_ok=True)
Path("artifacts/local_exhaustion_witness.json").write_text(
    json.dumps(artifact, indent=2)
)
print("wrote artifacts/local_exhaustion_witness.json")
