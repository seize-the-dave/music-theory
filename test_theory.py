import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import theory
import unittest

class TestTheory(unittest.TestCase):
    
    def test_major_scale(self):
        root = "C"
        scale = theory.major_scale(root)

        self.assertListEqual(scale.ascending, ["C", "D", "E", "F", "G", "A", "B", "C"])

    def test_interval(self):
        perfect_unison = theory.Interval("C", "C").notation()

        self.assertEqual(perfect_unison, "P1")