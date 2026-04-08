from __future__ import annotations

import hashlib

from .multi_valuation_codec import certificate_to_json

def certificate_sha256(cert) -> str:
    return hashlib.sha256(certificate_to_json(cert).encode("utf-8")).hexdigest()
