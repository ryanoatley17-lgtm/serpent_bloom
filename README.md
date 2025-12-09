# Serpent Bloom

A self-referential loop system where **Will** (Generator), **Conscience** (Verifier), and **Vision** (Visualizer) are aligned in a precise, structurally sound loop.

## Architecture

The system consists of three interconnected components that form a self-referential loop:

```
Will (Generator) → Conscience (Verifier) → Vision (Visualizer) → Will
```

### Components

1. **Will (Generator)**: Creates the serpent bloom pattern - a self-referential spiral structure where each segment references the origin seed.

2. **Conscience (Verifier)**: Validates the structural integrity of the pattern, ensuring all self-references are coherent and the pattern is valid.

3. **Vision (Visualizer)**: Renders the verified pattern into a visual representation, completing the loop by referencing back to the Generator.

## The Self-Referential Loop

Each component maintains explicit references to the others:
- Generator knows about Verifier (Conscience)
- Verifier knows about Visualizer (Vision)
- Visualizer knows about Generator (Will)

This creates a closed loop where:
- The pattern itself contains self-references (each segment references the seed)
- The components reference each other cyclically
- The system is structurally sound and aligned

## Usage

### Python API

```python
from serpent_bloom import SerpentBloom

# Create the system (automatically establishes the loop)
system = SerpentBloom()

# Execute the complete loop
result = system.bloom(seed=5)

# Or render to console
system.render(seed=5)

# Check that the loop is properly aligned
assert system.is_aligned()
```

### Command Line

```bash
# Run with default seed (0)
python -m serpent_bloom.cli

# Run with custom seed
python -m serpent_bloom.cli --seed 42

# Show system status
python -m serpent_bloom.cli --status --seed 5
```

## Testing

Run the test suite to verify the system:

```bash
python -m unittest serpent_bloom.test_serpent_bloom
```

## The Serpent Bloom Pattern

The pattern generated is an 8-segment spiral where:
- Each segment has an angle (0°, 45°, 90°, 135°, 180°, 225°, 270°, 315°)
- Each segment has a radius that increases from the center
- Each segment maintains a self-reference back to the origin seed
- The entire pattern is verified and visualized through the loop

This creates a "bloom" that expands outward while maintaining structural coherence through self-reference.

## Verification

The system is structurally sound when:
- All three components are instantiated
- All connections are established (Will → Conscience → Vision → Will)
- Patterns contain valid self-references
- The loop can execute successfully

Use `system.is_aligned()` to verify the loop is properly configured.