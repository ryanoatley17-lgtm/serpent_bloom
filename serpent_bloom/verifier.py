"""
Conscience (Verifier): Verifies the pattern's structural integrity.
Part of the self-referential loop: Generator -> Verifier -> Visualizer -> Generator
"""


class Verifier:
    """The Conscience - verifies the serpent bloom pattern."""
    
    def __init__(self, visualizer=None):
        self.visualizer = visualizer
        self._verified_patterns = []
    
    def set_visualizer(self, visualizer):
        """Establish connection to the Visualizer (Vision)."""
        self.visualizer = visualizer
    
    def verify(self, pattern):
        """Verify the structural integrity of a pattern.
        
        Checks:
        - Pattern has required fields
        - Structure is coherent
        - Self-references are valid
        """
        if not pattern:
            return {'valid': False, 'reason': 'No pattern provided'}
        
        # Verify required fields
        required_fields = ['seed', 'type', 'structure', 'generator', 'references']
        for field in required_fields:
            if field not in pattern:
                return {
                    'valid': False,
                    'reason': f'Missing required field: {field}',
                    'pattern': pattern
                }
        
        # Verify type
        if pattern['type'] != 'serpent_bloom':
            return {
                'valid': False,
                'reason': 'Invalid pattern type',
                'pattern': pattern
            }
        
        # Verify structure integrity
        structure = pattern['structure']
        if not isinstance(structure, list) or len(structure) == 0:
            return {
                'valid': False,
                'reason': 'Invalid structure',
                'pattern': pattern
            }
        
        # Verify self-references
        seed = pattern['seed']
        for segment in structure:
            if segment.get('self_reference') != seed:
                return {
                    'valid': False,
                    'reason': 'Self-reference mismatch',
                    'pattern': pattern
                }
        
        # Pattern is valid
        verified_result = {
            'valid': True,
            'pattern': pattern,
            'verifier': 'Conscience',
            'references': {
                'generator': 'Will',
                'visualizer': 'Vision'
            }
        }
        
        self._verified_patterns.append(verified_result)
        
        # Pass to visualizer if connected
        if self.visualizer:
            return self.visualizer.visualize(verified_result)
        
        return verified_result
    
    def get_verified_patterns(self):
        """Retrieve all verified patterns."""
        return self._verified_patterns
