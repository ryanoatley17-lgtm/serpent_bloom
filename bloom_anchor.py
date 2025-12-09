import argparse
import json
import sys
from pathlib import Path

from serpent_bloom_core import generate_envelope, hash_file, HASH_ALGORITHM


def build_fingerprint(target: Path) -> dict:
    return {
        "algorithm": HASH_ALGORITHM,
        "hash": hash_file(target),
        "target": target.name,
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Bind a target file into a Bloom envelope via external fingerprint."
    )
    parser.add_argument("target", help="Path to the file to anchor")
    parser.add_argument(
        "-o", "--output", help="Optional output file for the bound envelope (defaults to stdout)"
    )
    args = parser.parse_args()

    target_path = Path(args.target)
    if not target_path.is_file():
        sys.stderr.write(f"Target file not found: {target_path}\n")
        sys.exit(1)

    fingerprint = build_fingerprint(target_path)
    envelope = generate_envelope(external_fingerprints=[fingerprint])
    envelope_json = json.dumps(envelope, indent=2)

    if args.output:
        Path(args.output).write_text(envelope_json)
    else:
        sys.stdout.write(envelope_json)


if __name__ == "__main__":
    main()
