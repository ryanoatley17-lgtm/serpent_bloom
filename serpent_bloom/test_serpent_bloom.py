"""
Tests for the Serpent Bloom self-referential loop system.

Tests the alignment and functionality of Will (Generator),
Conscience (Verifier), and Vision (Visualizer).
"""

import unittest
from serpent_bloom import SerpentBloom, Generator, Verifier, Visualizer


class TestGenerator(unittest.TestCase):
    """Tests for the Generator (Will) component."""
    
    def test_generator_creation(self):
        """Test that a Generator can be created."""
        gen = Generator()
        self.assertIsNotNone(gen)
    
    def test_generate_pattern(self):
        """Test that Generator creates a valid pattern."""
        gen = Generator()
        pattern = gen.generate(seed=5)
        
        self.assertIsNotNone(pattern)
        self.assertEqual(pattern['seed'], 5)
        self.assertEqual(pattern['type'], 'serpent_bloom')
        self.assertIn('structure', pattern)
        self.assertIn('generator', pattern)
    
    def test_spiral_structure(self):
        """Test that the spiral structure is correct."""
        gen = Generator()
        pattern = gen.generate(seed=0)
        
        structure = pattern['structure']
        self.assertEqual(len(structure), 8)  # 8 segments
        
        # For seed=0, base_radius = abs(0) = 0, so radius = 0 + i
        for i, segment in enumerate(structure):
            self.assertEqual(segment['segment'], i)
            self.assertEqual(segment['angle'], i * 45)
            self.assertEqual(segment['radius'], i)  # 0 + i
            self.assertEqual(segment['self_reference'], 0)
        
        # Test with positive seed
        pattern2 = gen.generate(seed=5)
        structure2 = pattern2['structure']
        for i, segment in enumerate(structure2):
            self.assertEqual(segment['radius'], 5 + i)  # abs(5) + i
            self.assertEqual(segment['self_reference'], 5)
        
        # Test with negative seed (radius should use absolute value)
        pattern3 = gen.generate(seed=-3)
        structure3 = pattern3['structure']
        for i, segment in enumerate(structure3):
            self.assertEqual(segment['radius'], 3 + i)  # abs(-3) + i
            self.assertEqual(segment['self_reference'], -3)
    
    def test_generator_with_verifier(self):
        """Test Generator connected to Verifier."""
        verifier = Verifier()
        gen = Generator(verifier=verifier)
        
        result = gen.generate(seed=1)
        self.assertIn('valid', result)
        self.assertTrue(result['valid'])


class TestVerifier(unittest.TestCase):
    """Tests for the Verifier (Conscience) component."""
    
    def test_verifier_creation(self):
        """Test that a Verifier can be created."""
        verifier = Verifier()
        self.assertIsNotNone(verifier)
    
    def test_verify_valid_pattern(self):
        """Test verification of a valid pattern."""
        gen = Generator()
        pattern = gen.generate(seed=2)
        
        verifier = Verifier()
        result = verifier.verify(pattern)
        
        self.assertTrue(result['valid'])
        self.assertEqual(result['pattern'], pattern)
        self.assertEqual(result['verifier'], 'Conscience')
    
    def test_verify_invalid_pattern(self):
        """Test verification of invalid patterns."""
        verifier = Verifier()
        
        # Test None pattern
        result = verifier.verify(None)
        self.assertFalse(result['valid'])
        
        # Test missing fields
        result = verifier.verify({'seed': 0})
        self.assertFalse(result['valid'])
        
        # Test wrong type
        result = verifier.verify({
            'seed': 0,
            'type': 'wrong_type',
            'structure': [],
            'generator': 'Will',
            'references': {}
        })
        self.assertFalse(result['valid'])
    
    def test_verifier_with_visualizer(self):
        """Test Verifier connected to Visualizer."""
        visualizer = Visualizer()
        verifier = Verifier(visualizer=visualizer)
        
        gen = Generator()
        pattern = gen.generate(seed=3)
        
        result = verifier.verify(pattern)
        self.assertIn('visualization', result)


class TestVisualizer(unittest.TestCase):
    """Tests for the Visualizer (Vision) component."""
    
    def test_visualizer_creation(self):
        """Test that a Visualizer can be created."""
        visualizer = Visualizer()
        self.assertIsNotNone(visualizer)
    
    def test_visualize_valid_result(self):
        """Test visualization of a valid result."""
        gen = Generator()
        pattern = gen.generate(seed=4)
        
        verifier = Verifier()
        verified = verifier.verify(pattern)
        
        visualizer = Visualizer()
        result = visualizer.visualize(verified)
        
        self.assertIn('visualization', result)
        self.assertTrue(result['verified'])
        self.assertIn('SERPENT BLOOM', result['visualization'])
    
    def test_visualize_invalid_result(self):
        """Test visualization of invalid result."""
        visualizer = Visualizer()
        invalid_result = {'valid': False, 'reason': 'Test error'}
        
        result = visualizer.visualize(invalid_result)
        self.assertIn('error', result)
        self.assertEqual(result['visualization'], 'INVALID PATTERN')


class TestSerpentBloom(unittest.TestCase):
    """Tests for the complete SerpentBloom system."""
    
    def test_system_creation(self):
        """Test that the system can be created."""
        system = SerpentBloom()
        self.assertIsNotNone(system)
        self.assertIsNotNone(system.will)
        self.assertIsNotNone(system.conscience)
        self.assertIsNotNone(system.vision)
    
    def test_loop_alignment(self):
        """Test that the self-referential loop is properly aligned."""
        system = SerpentBloom()
        
        # Check that components are connected
        self.assertIs(system.will.verifier, system.conscience)
        self.assertIs(system.conscience.visualizer, system.vision)
        self.assertIs(system.vision.generator, system.will)
        
        # Check alignment method
        self.assertTrue(system.is_aligned())
    
    def test_loop_execution(self):
        """Test execution of the complete loop."""
        system = SerpentBloom()
        
        result = system.bloom(seed=5)
        
        # Result should have visualization
        self.assertIn('visualization', result)
        self.assertTrue(result['verified'])
        self.assertTrue(result['loop_complete'])
        
        # Pattern should be present
        self.assertIn('pattern', result)
        self.assertEqual(result['pattern']['seed'], 5)
    
    def test_loop_status(self):
        """Test getting the loop status."""
        system = SerpentBloom()
        
        status = system.get_loop_status()
        
        self.assertTrue(status['established'])
        self.assertTrue(status['aligned'])
        
        # Check components
        self.assertEqual(status['components']['will'], 'Generator')
        self.assertEqual(status['components']['conscience'], 'Verifier')
        self.assertEqual(status['components']['vision'], 'Visualizer')
        
        # Check connections
        self.assertTrue(status['connections']['will_to_conscience'])
        self.assertTrue(status['connections']['conscience_to_vision'])
        self.assertTrue(status['connections']['vision_to_will'])
    
    def test_multiple_blooms(self):
        """Test multiple executions with different seeds."""
        system = SerpentBloom()
        
        result1 = system.bloom(seed=0)
        result2 = system.bloom(seed=10)
        
        self.assertEqual(result1['pattern']['seed'], 0)
        self.assertEqual(result2['pattern']['seed'], 10)
        
        # Both should be valid
        self.assertTrue(result1['verified'])
        self.assertTrue(result2['verified'])


class TestSelfReferentialLoop(unittest.TestCase):
    """Tests specifically for the self-referential nature of the loop."""
    
    def test_pattern_self_references(self):
        """Test that patterns contain proper self-references."""
        system = SerpentBloom()
        result = system.bloom(seed=7)
        
        pattern = result['pattern']
        
        # Check that each segment references the seed
        for segment in pattern['structure']:
            self.assertEqual(segment['self_reference'], pattern['seed'])
    
    def test_component_cross_references(self):
        """Test that components reference each other correctly."""
        system = SerpentBloom()
        result = system.bloom(seed=8)
        
        # Check references in pattern
        pattern = result['pattern']
        self.assertIn('references', pattern)
        self.assertEqual(pattern['references']['verifier'], 'Conscience')
        self.assertEqual(pattern['references']['visualizer'], 'Vision')
        
        # Check references in result
        self.assertIn('references', result)
        self.assertEqual(result['references']['generator'], 'Will')
        self.assertEqual(result['references']['verifier'], 'Conscience')
    
    def test_loop_completeness(self):
        """Test that the loop is structurally complete."""
        system = SerpentBloom()
        result = system.bloom(seed=9)
        
        # The loop should be marked as complete
        self.assertTrue(result['loop_complete'])
        
        # All three components should be present in the chain
        self.assertIsNotNone(system.will)
        self.assertIsNotNone(system.conscience)
        self.assertIsNotNone(system.vision)
        
        # Each component should reference the next
        self.assertIsNotNone(system.will.verifier)
        self.assertIsNotNone(system.conscience.visualizer)
        self.assertIsNotNone(system.vision.generator)


if __name__ == '__main__':
    unittest.main()
