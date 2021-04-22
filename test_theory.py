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

        self.assertEqual(c_major, "CM")

    def test_major_chord_inversions(self):
        c_major = theory.major_scale("C")

        self.assertListEqual(c_major.chord(1).notes(), ["C", "E", "G"])
        self.assertListEqual(c_major.chord(1, 1).notes(), ["E", "G", "C"])
        self.assertListEqual(c_major.chord(1, 2).notes(), ["G", "C", "E"])

    def test_minor_chord(self):
        c_minor = theory.Chord("C", "E♭", "G").notation()

        self.assertEqual(c_minor, "Cm")

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

        self.assertEqual(scale.chord(1).notation(), "CM")
        self.assertEqual(scale.chord(2).notation(), "Dm")
        self.assertEqual(scale.chord(3).notation(), "Em")
        self.assertEqual(scale.chord(4).notation(), "FM")
        self.assertEqual(scale.chord(5).notation(), "GM")
        self.assertEqual(scale.chord(6).notation(), "Am")
        self.assertEqual(scale.chord(7).notation(), "Bdim")

    def test_diatonic_chords_for_natural_minor_key(self):
        scale = theory.minor_scale("C")

        self.assertEqual(scale.chord(1).notation(), "Cm")
        self.assertEqual(scale.chord(2).notation(), "Ddim")
        self.assertEqual(scale.chord(3).notation(), "E♭M")
        self.assertEqual(scale.chord(4).notation(), "Fm")
        self.assertEqual(scale.chord(5).notation(), "Gm")
        self.assertEqual(scale.chord(6).notation(), "A♭M")
        self.assertEqual(scale.chord(7).notation(), "B♭M")

    def test_diatonic_chords_for_harmonic_minor_key(self):
        scale = theory.harmonic_minor_scale("C")

        self.assertEqual(scale.chord(1).notation(), "Cm")
        self.assertEqual(scale.chord(2).notation(), "Ddim")
        self.assertEqual(scale.chord(3).notation(), "E♭aug")
        self.assertEqual(scale.chord(4).notation(), "Fm")
        self.assertEqual(scale.chord(5).notation(), "GM")
        self.assertEqual(scale.chord(6).notation(), "A♭M")
        self.assertEqual(scale.chord(7).notation(), "Bdim")

    def test_diatonic_chords_for_melodic_minor_key(self):
        scale = theory.melodic_minor_scale("C")

        self.assertEqual(scale.chord(1).notation(), "Cm")
        self.assertEqual(scale.chord(2).notation(), "Dm")
        self.assertEqual(scale.chord(3).notation(), "E♭aug")
        self.assertEqual(scale.chord(4).notation(), "FM")
        self.assertEqual(scale.chord(5).notation(), "GM")
        self.assertEqual(scale.chord(6).notation(), "Adim")
        self.assertEqual(scale.chord(7).notation(), "Bdim")

    def test_all_diatonic_sevenths(self):
        for key in theory.MAJOR_SCALES:
            scale = theory.minor_scale("C")
            for inversion in range(0,3):
                print(scale.seventh(1, inversion))
                print(scale.seventh(2, inversion))
                print(scale.seventh(3, inversion))
                print(scale.seventh(4, inversion))
                print(scale.seventh(5, inversion))
                print(scale.seventh(6, inversion))
                print(scale.seventh(7, inversion))
                break
            break

        # for key in theory.MINOR_SCALES:
        #     scale = theory.minor_scale(key)
        #     for inversion in range(0,2):
        #         print(scale.chord(1, inversion))
        #         print(scale.chord(2, inversion))
        #         print(scale.chord(3, inversion))
        #         print(scale.chord(4, inversion))
        #         print(scale.chord(5, inversion))
        #         print(scale.chord(6, inversion))
        #         print(scale.chord(7, inversion))

        # for key in theory.MINOR_SCALES:
        #     scale = theory.harmonic_minor_scale(key)
        #     for inversion in range(0,2):
        #         print(scale.chord(1, inversion))
        #         print(scale.chord(2, inversion))
        #         print(scale.chord(3, inversion))
        #         print(scale.chord(4, inversion))
        #         print(scale.chord(5, inversion))
        #         print(scale.chord(6, inversion))
        #         print(scale.chord(7, inversion))

        # for key in theory.MINOR_SCALES:
        #     scale = theory.melodic_minor_scale(key)
        #     for inversion in range(0,2):
        #         print(scale.chord(1, inversion))
        #         print(scale.chord(2, inversion))
        #         print(scale.chord(3, inversion))
        #         print(scale.chord(4, inversion))
        #         print(scale.chord(5, inversion))
        #         print(scale.chord(6, inversion))
        #         print(scale.chord(7, inversion))

if __name__ == '__main__':
    unittest.main()