import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Dict

import serpent_bloom_core as core


ROOT = Path(__file__).resolve().parent.parent


def _load_envelope(path: Path) -> Dict:
    return json.loads(path.read_text())


class BloomTests(unittest.TestCase):
    def test_generate_envelope_binds_external_fingerprint(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            target = Path(temp_dir) / "anchor.bin"
            target.write_bytes(b"anchor-me")
            fingerprint = {
                "algorithm": core.HASH_ALGORITHM,
                "hash": core.hash_file(target),
                "target": target.name,
            }

            envelope = core.generate_envelope(external_fingerprints=[fingerprint])

            self.assertEqual(envelope["external_fingerprints"][0]["hash"], fingerprint["hash"])
            self.assertTrue(core.verify_eternal_seal(envelope))
            self.assertTrue(core.verify_external_fingerprints(envelope, target))

    def test_external_verification_fails_when_target_changes(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            target = Path(temp_dir) / "original.bin"
            target.write_bytes(b"original")
            fingerprint = {
                "algorithm": core.HASH_ALGORITHM,
                "hash": core.hash_file(target),
                "target": target.name,
            }
            envelope = core.generate_envelope(external_fingerprints=[fingerprint])

            target.write_bytes(b"mutated")
            self.assertFalse(core.verify_external_fingerprints(envelope, target))

    def test_bloom_anchor_cli_outputs_bound_envelope(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            tmp_path = Path(temp_dir)
            target = tmp_path / "document.bin"
            target.write_bytes(b"document")

            output_path = tmp_path / "bound_envelope.json"
            result = subprocess.run(
                [
                    sys.executable,
                    str(ROOT / "bloom_anchor.py"),
                    str(target),
                    "-o",
                    str(output_path),
                ],
                capture_output=True,
                text=True,
                check=False,
            )

            self.assertEqual(result.returncode, 0, msg=result.stderr)
            envelope = _load_envelope(output_path)
            self.assertEqual(envelope["external_fingerprints"][0]["hash"], core.hash_file(target))
            self.assertTrue(core.verify_eternal_seal(envelope))

    def test_bloom_verifier_cli_rejects_tampered_target(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            tmp_path = Path(temp_dir)
            target = tmp_path / "payload.bin"
            target.write_bytes(b"payload")

            envelope_path = tmp_path / "envelope.json"
            subprocess.run(
                [
                    sys.executable,
                    str(ROOT / "bloom_anchor.py"),
                    str(target),
                    "-o",
                    str(envelope_path),
                ],
                check=True,
            )

            target.write_bytes(b"tampered")
            verifier = subprocess.run(
                [
                    sys.executable,
                    str(ROOT / "bloom_verifier.py"),
                    str(envelope_path),
                    "--target",
                    str(target),
                ],
                capture_output=True,
                text=True,
                check=False,
            )

            self.assertNotEqual(verifier.returncode, 0)
            self.assertIn("External fingerprint verification failed", verifier.stderr)
