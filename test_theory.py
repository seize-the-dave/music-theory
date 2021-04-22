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

    def test_intervals(self):
        root = "C"
        self.assertEqual(theory.Interval(root, "C").notation(), "P1")
        self.assertEqual(theory.Interval(root, "D").notation(), "M2")
        self.assertEqual(theory.Interval(root, "E").notation(), "M3")
        self.assertEqual(theory.Interval(root, "F").notation(), "P4")
        self.assertEqual(theory.Interval(root, "G").notation(), "P5")
        self.assertEqual(theory.Interval(root, "A").notation(), "M6")
        self.assertEqual(theory.Interval(root, "B").notation(), "M7")
    
    def test_major_chord(self):
        c_major = theory.Chord("C", "E", "G").notation()

        self.assertEqual(c_major, "Cmaj")

    def test_major_chord_inversions(self):
        c_major = theory.major_scale("C")

        self.assertListEqual(c_major.chord(1).notes(), ["C", "E", "G"])
        self.assertListEqual(c_major.chord(1, 1).notes(), ["E", "G", "C"])
        self.assertListEqual(c_major.chord(1, 2).notes(), ["G", "C", "E"])

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

    def test_diatonic_chords_for_major_key(self):
        scale = theory.major_scale("C")

        self.assertEqual(scale.chord(1).notation(), "Cmaj")
        self.assertEqual(scale.chord(2).notation(), "Dmin")
        self.assertEqual(scale.chord(3).notation(), "Emin")
        self.assertEqual(scale.chord(4).notation(), "Fmaj")
        self.assertEqual(scale.chord(5).notation(), "Gmaj")
        self.assertEqual(scale.chord(6).notation(), "Amin")
        self.assertEqual(scale.chord(7).notation(), "Bdim")

    def test_diatonic_chords_for_natural_minor_key(self):
        scale = theory.minor_scale("C")

        self.assertEqual(scale.chord(1).notation(), "Cmin")
        self.assertEqual(scale.chord(2).notation(), "Ddim")
        self.assertEqual(scale.chord(3).notation(), "E♭maj")
        self.assertEqual(scale.chord(4).notation(), "Fmin")
        self.assertEqual(scale.chord(5).notation(), "Gmin")
        self.assertEqual(scale.chord(6).notation(), "A♭maj")
        self.assertEqual(scale.chord(7).notation(), "B♭maj")

    def test_diatonic_chords_for_harmonic_minor_key(self):
        scale = theory.harmonic_minor_scale("C")

        self.assertEqual(scale.chord(1).notation(), "Cmin")
        self.assertEqual(scale.chord(2).notation(), "Ddim")
        self.assertEqual(scale.chord(3).notation(), "E♭aug")
        self.assertEqual(scale.chord(4).notation(), "Fmin")
        self.assertEqual(scale.chord(5).notation(), "Gmaj")
        self.assertEqual(scale.chord(6).notation(), "A♭maj")
        self.assertEqual(scale.chord(7).notation(), "Bdim")

    def test_diatonic_chords_for_melodic_minor_key(self):
        scale = theory.melodic_minor_scale("C")

        self.assertEqual(scale.chord(1).notation(), "Cmin")
        self.assertEqual(scale.chord(2).notation(), "Dmin")
        self.assertEqual(scale.chord(3).notation(), "E♭aug")
        self.assertEqual(scale.chord(4).notation(), "Fmaj")
        self.assertEqual(scale.chord(5).notation(), "Gmaj")
        self.assertEqual(scale.chord(6).notation(), "Adim")
        self.assertEqual(scale.chord(7).notation(), "Bdim")

if __name__ == '__main__':
    unittest.main()