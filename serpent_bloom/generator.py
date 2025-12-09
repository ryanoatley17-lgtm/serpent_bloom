"""
Will (Generator): Generates the fundamental pattern.
Part of the self-referential loop: Generator -> Verifier -> Visualizer -> Generator
"""


class Generator:
    """The Will - generates the serpent bloom pattern."""
    
    def __init__(self, verifier=None):
        self.verifier = verifier
        self._pattern = None
    
    def set_verifier(self, verifier):
        """Establish connection to the Verifier (Conscience)."""
        self.verifier = verifier
    
    def generate(self, seed=0):
        """Generate a serpent bloom pattern based on seed.
        
        The pattern is a self-referential spiral structure that
        expands outward while referencing its origin.
        """
        # Generate the serpent bloom pattern
        pattern = {
            'seed': seed,
            'type': 'serpent_bloom',
            'structure': self._create_spiral(seed),
            'generator': 'Will',
            'references': {
                'verifier': 'Conscience',
                'visualizer': 'Vision'
            }
        }
        
        self._pattern = pattern
        
        # Pass to verifier if connected
        if self.verifier:
            return self.verifier.verify(pattern)
        
        return pattern
    
    def _create_spiral(self, seed):
        """Create the spiral structure of the serpent bloom.
        
        The spiral always expands outward from the center, using the
        absolute value of the seed as the starting radius.
        """
        spiral = []
        base_radius = abs(seed)  # Ensure non-negative radius
        for i in range(8):  # 8 petals/segments
            angle = i * 45  # 45 degrees per segment
            radius = base_radius + i
            spiral.append({
                'segment': i,
                'angle': angle,
                'radius': radius,
                'self_reference': seed  # Each segment references the origin
            })
        return spiral
    
    def get_pattern(self):
        """Retrieve the current pattern."""
        return self._pattern
