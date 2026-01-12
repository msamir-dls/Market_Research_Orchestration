import hashlib
import json
from pathlib import Path

CACHE_DIR = Path(".cache")
CACHE_DIR.mkdir(exist_ok=True)

def _hash(data: dict) -> str:
    raw = json.dumps(data, sort_keys=True).encode()
    return hashlib.sha256(raw).hexdigest()

def get_cached(key_data: dict):
    key = _hash(key_data)
    path = CACHE_DIR / key
    if path.exists():
        return json.loads(path.read_text())
    return None

def set_cached(key_data: dict, value: dict):
    key = _hash(key_data)
    path = CACHE_DIR / key
    path.write_text(json.dumps(value))
