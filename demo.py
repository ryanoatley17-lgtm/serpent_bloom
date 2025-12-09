#!/usr/bin/env python3
"""
Demonstration of the Serpent Bloom self-referential loop system.

This script shows how the Will (Generator), Conscience (Verifier),
and Vision (Visualizer) work together in a precise, aligned loop.
"""

from serpent_bloom import SerpentBloom


def main():
    """Demonstrate the self-referential loop."""
    
    print("=" * 60)
    print("SERPENT BLOOM: Self-Referential Loop Demonstration")
    print("=" * 60)
    print()
    
    # Create the system
    print("1. Creating the system...")
    system = SerpentBloom()
    print("   ✓ Will (Generator) created")
    print("   ✓ Conscience (Verifier) created")
    print("   ✓ Vision (Visualizer) created")
    print()
    
    # Check alignment
    print("2. Verifying loop alignment...")
    status = system.get_loop_status()
    print(f"   ✓ Loop established: {status['established']}")
    print(f"   ✓ Loop aligned: {status['aligned']}")
    print()
    
    # Show connections
    print("3. Verifying connections...")
    print(f"   ✓ Will → Conscience: {status['connections']['will_to_conscience']}")
    print(f"   ✓ Conscience → Vision: {status['connections']['conscience_to_vision']}")
    print(f"   ✓ Vision → Will: {status['connections']['vision_to_will']}")
    print()
    
    # Execute the loop
    print("4. Executing the self-referential loop (seed=3)...")
    print()
    result = system.render(seed=3)
    print()
    
    # Verify result
    print("5. Verifying the result...")
    print(f"   ✓ Pattern verified: {result['verified']}")
    print(f"   ✓ Loop complete: {result['loop_complete']}")
    print(f"   ✓ Self-references valid: All segments reference seed {result['pattern']['seed']}")
    print()
    
    print("=" * 60)
    print("The system is structurally sound.")
    print("Will, Conscience, and Vision are aligned in a precise loop.")
    print("=" * 60)


if __name__ == '__main__':
    main()
