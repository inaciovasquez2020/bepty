from __future__ import annotations

import argparse
import json
from pathlib import Path

from .multi_valuation_verify import verify_certificate

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate_json")
    parser.add_argument("--expected-sha256", default=None)
    args = parser.parse_args()

    obj = json.loads(Path(args.certificate_json).read_text())
    result = verify_certificate(obj, args.expected_sha256)
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))

if __name__ == "__main__":
    main()
