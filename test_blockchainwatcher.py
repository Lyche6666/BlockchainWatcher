# test_blockchainwatcher.py
"""
Tests for BlockchainWatcher module.
"""

import unittest
from blockchainwatcher import BlockchainWatcher

class TestBlockchainWatcher(unittest.TestCase):
    """Test cases for BlockchainWatcher class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockchainWatcher()
        self.assertIsInstance(instance, BlockchainWatcher)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockchainWatcher()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
