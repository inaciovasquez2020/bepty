import json
from pathlib import Path

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from utils.hasher import certificate_hash

CERT = {
    "certificate_version": "v0.2.0",
    "object_type": "graph",
    "valuation": "dim",
    "radius": 1,
    "graph_A": {
        "name": "theta_3_3_3",
        "edges": [[0,1],[1,2],[2,3],[0,4],[4,5],[5,3],[0,6],[6,7],[7,3]]
    },
    "graph_B": {
        "name": "dumbbell_6_6",
        "edges": [[0,1],[1,2],[2,0],[2,3],[3,4],[4,5],[5,3]]
    },
    "xR_vanishes": False,
    "beta_value": 2,
    "profile_A": {
        "kind": "normalized_rooted_ball_histogram",
        "radius": 1
    },
    "profile_B": {
        "kind": "normalized_rooted_ball_histogram",
        "radius": 1
    }
}

payload = dict(CERT)
payload["hash"] = certificate_hash(payload)

out = Path("artifacts")
out.mkdir(exist_ok=True)
target = out / "bepty_certificate_example.json"
target.write_text(json.dumps(payload, indent=2, sort_keys=True))
print(target)
