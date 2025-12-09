import argparse
import json
import sys
from pathlib import Path

from serpent_bloom_core import (
    verify_eternal_seal,
    verify_external_fingerprints,
    external_fingerprints_present,
)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Verify a Bloom envelope and optional anchored file."
    )
    parser.add_argument("envelope", help="Path to the bloom envelope JSON")
    parser.add_argument(
        "--target",
        help="Optional path to the anchored file; verifies its hash against the envelope",
    )
    args = parser.parse_args()

    envelope_path = Path(args.envelope)
    if not envelope_path.is_file():
        sys.stderr.write(f"Envelope not found: {envelope_path}\n")
        sys.exit(1)

    try:
        envelope = json.loads(envelope_path.read_text())
    except json.JSONDecodeError as exc:
        sys.stderr.write(f"Invalid envelope JSON: {exc}\n")
        sys.exit(1)

    if not verify_eternal_seal(envelope):
        sys.stderr.write("Eternal Seal verification failed.\n")
        sys.exit(1)

    if args.target:
        target_path = Path(args.target)
        if not target_path.is_file():
            sys.stderr.write(f"Target file not found: {target_path}\n")
            sys.exit(1)
        external_ok = verify_external_fingerprints(envelope, target_path=target_path)
    else:
        external_ok = external_fingerprints_present(envelope)

    if not external_ok:
        sys.stderr.write("External fingerprint verification failed.\n")
        sys.exit(1)

    print("Envelope verified.")


if __name__ == "__main__":
    main()
