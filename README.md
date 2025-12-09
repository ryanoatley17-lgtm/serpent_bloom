# serpent_bloom

## Anchoring a file

Create a Bloom envelope that binds to a specific file:

```bash
python bloom_anchor.py path/to/contract.pdf > bound_envelope.json
```

## Verifying

Verify the Eternal Seal and the anchored file fingerprint:

```bash
python bloom_verifier.py bound_envelope.json --target path/to/contract.pdf
```
