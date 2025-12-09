import json
import hashlib
from pathlib import Path
from typing import Dict, List, Optional, Any


HASH_ALGORITHM = "sha3-512"


def _hash_bytes(content: bytes) -> str:
    return hashlib.sha3_512(content).hexdigest()


def canonical_dumps(payload: Dict[str, Any]) -> str:
    """
    Canonical, deterministic JSON encoding for hashing.
    """
    return json.dumps(payload, sort_keys=True, separators=(",", ":"))


def hash_file(path: Path) -> str:
    data = path.read_bytes()
    return _hash_bytes(data)


def mint_eternal_seal(envelope_without_seal: Dict[str, Any]) -> str:
    """
    Computes the Eternal Seal hash for a bloom envelope, excluding any
    existing eternal_seal field.
    """
    payload = {k: v for k, v in envelope_without_seal.items() if k != "eternal_seal"}
    return _hash_bytes(canonical_dumps(payload).encode("utf-8"))


def generate_envelope(external_fingerprints: Optional[List[Dict[str, Any]]] = None,
                      payload: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Generates a Bloom envelope and mints an Eternal Seal that binds any supplied
    external fingerprints into the artifact.
    """
    envelope = {
        "version": "1.1",
        "payload": payload or {},
        "external_fingerprints": external_fingerprints or [],
    }
    envelope["eternal_seal"] = mint_eternal_seal(envelope)
    return envelope


def verify_eternal_seal(envelope: Dict[str, Any]) -> bool:
    seal = envelope.get("eternal_seal")
    if not seal:
        return False
    expected = mint_eternal_seal(envelope)
    return seal == expected


def verify_external_fingerprints(
    envelope: Dict[str, Any],
    target_path: Path,
    *,
    allow_empty: bool = False,
) -> bool:
    """
    Validates external fingerprint anchors. Requires a target_path and compares
    its hash to recorded fingerprints. When allow_empty is True, envelopes with
    no supported fingerprints are treated as passing.
    """
    fingerprints = envelope.get("external_fingerprints") or []
    if not fingerprints:
        return allow_empty

    target_hash = hash_file(target_path)
    supported_seen = False
    for fingerprint in fingerprints:
        if fingerprint.get("algorithm") != HASH_ALGORITHM:
            continue
        supported_seen = True
        if fingerprint.get("hash") == target_hash:
            return True
    if not supported_seen:
        return allow_empty
    return False


def external_fingerprints_present(envelope: Dict[str, Any]) -> bool:
    """
    Presence-only check for external fingerprints.
    """
    fingerprints = envelope.get("external_fingerprints") or []
    return any(fp.get("algorithm") == HASH_ALGORITHM for fp in fingerprints)
