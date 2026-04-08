from __future__ import annotations

import json
from pathlib import Path
from typing import Any

def write_higher_dimensional_manifest(path: str | Path, manifest: dict[str, Any]) -> None:
    Path(path).write_text(
        json.dumps(manifest, sort_keys=True, separators=(",", ":"))
    )

def read_higher_dimensional_manifest(path: str | Path) -> dict[str, Any]:
    return json.loads(Path(path).read_text())
