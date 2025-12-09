#!/usr/bin/env python3
"""
Command-line interface for the Serpent Bloom system.

Demonstrates the self-referential loop of Will, Conscience, and Vision.
"""

import sys
import argparse
from serpent_bloom import SerpentBloom


def main():
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        description='Serpent Bloom: A self-referential loop system'
    )
    parser.add_argument(
        '--seed',
        type=int,
        default=0,
        help='Seed value for pattern generation (default: 0)'
    )
    parser.add_argument(
        '--status',
        action='store_true',
        help='Show the status of the self-referential loop'
    )
    
    args = parser.parse_args()
    
    # Create the system
    system = SerpentBloom()
    
    # Show status if requested
    if args.status:
        print("=" * 50)
        print("SERPENT BLOOM SYSTEM STATUS")
        print("=" * 50)
        status = system.get_loop_status()
        print(f"Loop Established: {status['established']}")
        print(f"Loop Aligned: {status['aligned']}")
        print()
        print("Components:")
        for name, component in status['components'].items():
            print(f"  {name.capitalize()}: {component}")
        print()
        print("Connections:")
        for conn, state in status['connections'].items():
            print(f"  {conn}: {'✓' if state else '✗'}")
        print("=" * 50)
        print()
    
    # Execute the bloom
    print("Executing self-referential loop...")
    print()
    system.render(args.seed)
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
