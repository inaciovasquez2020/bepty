from __future__ import annotations

import argparse
import json

from .higher_dimensional_manifest_verify import verify_higher_dimensional_manifest_file

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest_json")
    args = parser.parse_args()
    result = verify_higher_dimensional_manifest_file(args.manifest_json)
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))

if __name__ == "__main__":
    main()
