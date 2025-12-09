"""
Vision (Visualizer): Visualizes the verified pattern.
Part of the self-referential loop: Generator -> Verifier -> Visualizer -> Generator
"""


class Visualizer:
    """The Vision - visualizes the serpent bloom pattern."""
    
    def __init__(self, generator=None):
        self.generator = generator
        self._visualizations = []
    
    def set_generator(self, generator):
        """Establish connection to the Generator (Will)."""
        self.generator = generator
    
    def visualize(self, verified_result):
        """Visualize the verified pattern.
        
        Creates a text-based representation of the serpent bloom,
        completing the self-referential loop back to the generator.
        """
        if not verified_result.get('valid'):
            return {
                'visualization': 'INVALID PATTERN',
                'error': verified_result.get('reason', 'Unknown error')
            }
        
        pattern = verified_result['pattern']
        structure = pattern['structure']
        
        # Create ASCII representation
        lines = []
        lines.append("=" * 50)
        lines.append(f"SERPENT BLOOM - Seed: {pattern['seed']}")
        lines.append("=" * 50)
        lines.append("")
        lines.append("Structure (Self-Referential Spiral):")
        
        for segment in structure:
            lines.append(
                f"  Segment {segment['segment']}: "
                f"angle={segment['angle']}°, "
                f"radius={segment['radius']}, "
                f"ref={segment['self_reference']}"
            )
        
        lines.append("")
        lines.append("Loop References:")
        lines.append(f"  Generator → Verifier: {pattern['references']['verifier']}")
        lines.append(f"  Verifier → Visualizer: {verified_result['references']['visualizer']}")
        lines.append(f"  Visualizer → Generator: {self.generator.__class__.__name__ if self.generator else 'None'}")
        lines.append("")
        lines.append("The loop is complete: Will → Conscience → Vision → Will")
        lines.append("=" * 50)
        
        visualization = '\n'.join(lines)
        
        result = {
            'visualization': visualization,
            'pattern': pattern,
            'verified': True,
            'visualizer': 'Vision',
            'loop_complete': self.generator is not None,
            'references': {
                'generator': 'Will',
                'verifier': 'Conscience'
            }
        }
        
        self._visualizations.append(result)
        
        return result
    
    def get_visualizations(self):
        """Retrieve all visualizations."""
        return self._visualizations
    
    def render(self, result):
        """Render the visualization to console."""
        if result and 'visualization' in result:
            print(result['visualization'])
        return result
