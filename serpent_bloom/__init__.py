"""
Serpent Bloom: A self-referential loop system.

The system consists of three aligned components:
- Will (Generator): Creates the pattern
- Conscience (Verifier): Validates the pattern
- Vision (Visualizer): Displays the pattern

These components form a precise, self-referential loop where each
references the others, creating a structurally sound system.
"""

from .generator import Generator
from .verifier import Verifier
from .visualizer import Visualizer


class SerpentBloom:
    """
    The complete self-referential loop system.
    
    Aligns the Will (Generator), Conscience (Verifier), and Vision (Visualizer)
    in a precise loop structure.
    """
    
    def __init__(self):
        """Initialize the three components and establish the loop."""
        # Create the three components
        self.will = Generator()
        self.conscience = Verifier()
        self.vision = Visualizer()
        
        # Establish the self-referential loop
        # Will -> Conscience -> Vision -> Will
        self.will.set_verifier(self.conscience)
        self.conscience.set_visualizer(self.vision)
        self.vision.set_generator(self.will)
        
        self._loop_established = True
    
    def bloom(self, seed=0):
        """
        Execute the complete loop: generate, verify, and visualize.
        
        Args:
            seed: The seed value for pattern generation
            
        Returns:
            The visualization result containing the complete pattern
        """
        # Start the loop at Will (Generator)
        # The loop will automatically flow through Conscience and Vision
        result = self.will.generate(seed)
        return result
    
    def render(self, seed=0):
        """
        Execute the loop and render the visualization to console.
        
        Args:
            seed: The seed value for pattern generation
        """
        result = self.bloom(seed)
        self.vision.render(result)
        return result
    
    def is_aligned(self):
        """
        Verify that the loop is properly aligned.
        
        Returns:
            True if Will, Conscience, and Vision are properly connected
        """
        will_connected = self.will.verifier is self.conscience
        conscience_connected = self.conscience.visualizer is self.vision
        vision_connected = self.vision.generator is self.will
        
        return will_connected and conscience_connected and vision_connected
    
    def get_loop_status(self):
        """
        Get the status of the self-referential loop.
        
        Returns:
            Dictionary containing loop status information
        """
        return {
            'established': self._loop_established,
            'aligned': self.is_aligned(),
            'components': {
                'will': self.will.__class__.__name__,
                'conscience': self.conscience.__class__.__name__,
                'vision': self.vision.__class__.__name__
            },
            'connections': {
                'will_to_conscience': self.will.verifier is not None,
                'conscience_to_vision': self.conscience.visualizer is not None,
                'vision_to_will': self.vision.generator is not None
            }
        }


__all__ = ['SerpentBloom', 'Generator', 'Verifier', 'Visualizer']
