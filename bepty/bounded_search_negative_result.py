from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Iterable, Mapping
import hashlib
import json

@dataclass(frozen=True)
class NegativeResultCertificate:
    search_name: str
    bound: int
    explored: int
    found: bool
    witness: Any | None
    signature_image_size: int

def run_bounded_search(
    objects: Iterable[Any],
    *,
    predicate: Callable[[Any], bool],
    signature: Callable[[Any], Any],
    bound: int,
    search_name: str = "bounded_search",
) -> NegativeResultCertificate:
    seen_signatures = set()
    explored = 0
    for obj in objects:
        if explored >= bound:
            break
        explored += 1
        seen_signatures.add(signature(obj))
        if predicate(obj):
            return NegativeResultCertificate(
                search_name=search_name,
                bound=bound,
                explored=explored,
                found=True,
                witness=obj,
                signature_image_size=len(seen_signatures),
            )
    return NegativeResultCertificate(
        search_name=search_name,
        bound=bound,
        explored=explored,
        found=False,
        witness=None,
        signature_image_size=len(seen_signatures),
    )

def certificate_to_dict(cert: NegativeResultCertificate) -> dict[str, Any]:
    return {
        "search_name": cert.search_name,
        "bound": cert.bound,
        "explored": cert.explored,
        "found": cert.found,
        "witness": cert.witness,
        "signature_image_size": cert.signature_image_size,
    }

def certificate_to_json(cert: NegativeResultCertificate) -> str:
    return json.dumps(
        certificate_to_dict(cert),
        sort_keys=True,
        separators=(",", ":"),
    )

def certificate_sha256(cert: NegativeResultCertificate) -> str:
    return hashlib.sha256(certificate_to_json(cert).encode("utf-8")).hexdigest()

def validate_certificate_dict(obj: Mapping[str, Any]) -> None:
    required = (
        "search_name",
        "bound",
        "explored",
        "found",
        "witness",
        "signature_image_size",
    )
    for key in required:
        if key not in obj:
            raise ValueError(f"missing key: {key}")
    if not isinstance(obj["search_name"], str):
        raise TypeError("search_name must be a str")
    if not isinstance(obj["bound"], int):
        raise TypeError("bound must be an int")
    if not isinstance(obj["explored"], int):
        raise TypeError("explored must be an int")
    if not isinstance(obj["found"], bool):
        raise TypeError("found must be a bool")
    if not isinstance(obj["signature_image_size"], int):
        raise TypeError("signature_image_size must be an int")

def verify_certificate(
    cert: NegativeResultCertificate,
    expected_sha256: str | None = None,
) -> dict[str, Any]:
    obj = certificate_to_dict(cert)
    validate_certificate_dict(obj)
    actual = certificate_sha256(cert)
    if expected_sha256 is not None and actual != expected_sha256:
        raise ValueError("hash mismatch")
    return {"ok": True, "sha256": actual}

def build_manifest(cert: NegativeResultCertificate) -> dict[str, Any]:
    obj = certificate_to_dict(cert)
    validate_certificate_dict(obj)
    payload = certificate_to_json(cert)
    return {
        "certificate": obj,
        "sha256": certificate_sha256(cert),
        "json": payload,
    }
