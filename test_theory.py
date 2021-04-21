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

    def test_minor_scale(self):
        root = "C"
        scale = theory.minor_scale(root)

        self.assertListEqual(scale.ascending, ["C", "D", "E♭", "F", "G", "A♭", "B♭", "C"])

    def test_interval(self):
        perfect_unison = theory.Interval("C", "C").notation()

        self.assertEqual(perfect_unison, "P1")
    
    def test_major_chord(self):
        c_major = theory.Chord("C", "E", "G").notation()

        self.assertEqual(c_major, "Cmaj")

    def test_minor_chord(self):
        c_minor = theory.Chord("C", "E♭", "G").notation()

        self.assertEqual(c_minor, "Cmin")

    def test_circle_of_fifths_major_sharps(self):
        root = "C"
        for i in range(8):
            scale = theory.major_scale(root)
            root = scale.dominant()

        self.assertEqual(root, "G♯")

    def test_circle_of_fifths_major_flats(self):
        root = "C"
        for i in range(8):
            scale = theory.major_scale(root)
            root = scale.subdominant()

        self.assertEqual(root, "F♭")

    def test_circle_of_fifths_minor_sharps(self):
        root = "A"
        for i in range(8):
            scale = theory.minor_scale(root)
            root = scale.dominant()

        self.assertEqual(root, "E♯")

    def test_circle_of_fifths_minor_flats(self):
        root = "A"
        for i in range(8):
            scale = theory.minor_scale(root)
            root = scale.subdominant()

        self.assertEqual(root, "D♭")

if __name__ == '__main__':
    unittest.main()