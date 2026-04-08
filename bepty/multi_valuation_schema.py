from __future__ import annotations

from typing import Any, Mapping

REQUIRED_TOP_KEYS = ("signature", "valuations")

def validate_certificate_dict(obj: Mapping[str, Any]) -> None:
    for key in REQUIRED_TOP_KEYS:
        if key not in obj:
            raise ValueError(f"missing key: {key}")
    if not isinstance(obj["signature"], dict):
        raise TypeError("signature must be a dict")
    if not isinstance(obj["valuations"], dict):
        raise TypeError("valuations must be a dict")
    for key in obj["valuations"]:
        if not isinstance(key, str):
            raise TypeError("valuation names must be strings")
        if not isinstance(obj["valuations"][key], int):
            raise TypeError("valuation values must be integers")
