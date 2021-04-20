import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import theory
for scale in theory.MAJOR_SCALES:
    print(theory.major_scale(scale))

for scale in theory.MINOR_SCALES:
    print(theory.minor_scale(scale))

# print(theory.minor_scale('B♭'))