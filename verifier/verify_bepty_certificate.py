import json
import sys
from pathlib import Path

import jsonschema

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from utils.hasher import certificate_hash

def verify(path_str: str) -> int:
    path = Path(path_str)
    data = json.loads(path.read_text())

    schema = json.loads(Path("schemas/bepty_certificate.schema.json").read_text())
    try:
        jsonschema.validate(instance=data, schema=schema)
    except jsonschema.ValidationError as e:
        print(f"schema validation failed: {e.message}")
        return 1

    required = ["object_type", "valuation", "radius", "xR_vanishes", "beta_value", "hash"]
    for key in required:
        if key not in data:
            print(f"missing required field: {key}")
            return 1

    if data["object_type"] not in {"graph", "simplicial_complex"}:
        print("invalid object_type")
        return 1

    if data["valuation"] not in {"dim", "entropy", "euler"}:
        print("invalid valuation")
        return 1

    if not isinstance(data["radius"], (int, float)) or data["radius"] < 0:
        print("invalid radius")
        return 1

    if not isinstance(data["xR_vanishes"], bool):
        print("invalid xR_vanishes")
        return 1

    if not isinstance(data["beta_value"], int):
        print("invalid beta_value")
        return 1

    supplied_hash = data["hash"]
    expected_hash = certificate_hash(data)

    if supplied_hash != expected_hash:
        print("hash mismatch")
        return 1

    print("certificate valid")
    return 0

if __name__ == "__main__":
    raise SystemExit(verify(sys.argv[1]))
