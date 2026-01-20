# test_corealchemylink.py
"""
Tests for CoreAlchemyLink module.
"""

import unittest
from corealchemylink import CoreAlchemyLink

class TestCoreAlchemyLink(unittest.TestCase):
    """Test cases for CoreAlchemyLink class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CoreAlchemyLink()
        self.assertIsInstance(instance, CoreAlchemyLink)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CoreAlchemyLink()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
