from __future__ import annotations

import json
from dataclasses import asdict, is_dataclass
from typing import Any

def certificate_to_dict(cert: Any) -> dict:
    if is_dataclass(cert):
        return asdict(cert)
    if isinstance(cert, dict):
        return {
            "signature": dict(cert["signature"]),
            "valuations": dict(cert["valuations"]),
        }
    if hasattr(cert, "signature") and hasattr(cert, "valuations"):
        return {
            "signature": dict(cert.signature),
            "valuations": dict(cert.valuations),
        }
    raise TypeError("unsupported certificate object")

def certificate_to_json(cert: Any) -> str:
    return json.dumps(
        certificate_to_dict(cert),
        sort_keys=True,
        separators=(",", ":"),
    )
