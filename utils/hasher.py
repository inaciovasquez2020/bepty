import json
import hashlib

def canonical_json_bytes(data):
    """Enforce key sorting and eliminate whitespace for a stable digest."""
    return json.dumps(data, sort_keys=True, separators=(',', ':')).encode('utf-8')

def certificate_hash(data):
    """Compute SHA256 hash excluding the hash field itself."""
    cert_copy = data.copy()
    cert_copy.pop("hash", None)
    payload = canonical_json_bytes(cert_copy)
    return hashlib.sha256(payload).hexdigest()
