import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import theory
for scale in theory.MAJOR_SCALES:
    print(theory.major_scale(scale))
    print(theory.major_scale(scale, False))

for scale in theory.MINOR_SCALES:
    print(theory.minor_scale(scale))
    print(theory.minor_scale(scale, False))
    print(theory.harmonic_minor_scale(scale))
    print(theory.harmonic_minor_scale(scale, False))
    print(theory.melodic_minor_scale(scale))
    print(theory.melodic_minor_scale(scale, False))

# print(theory.minor_scale('B♭'))