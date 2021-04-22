LETTERS = ['A','B','C','D','E','F','G']

MAJOR_SCALES = ['C','G','D','A','E','B','F♯','C♯','G♯','F','B♭','E♭','A♭','D♭','G♭','C♭','F♭']
MINOR_SCALES = ['A','E','B','F♯','C♯','G♯','D♯','A♯','E♯','D','G','C','F','B♭','E♭','A♭','D♭']

NOTES = [
    ['A','B𝄫', 'G𝄪'],  # WHITE
    ['B♭','A♯'], # BLACK
    ['B','C♭'],  # WHITE
    ['C','B♯'],  # WHITE
    ['C♯','D♭'], # BLACK
    ['D','C𝄪'], # WHITE
    ['E♭','D♯'], # BLACK
    ['D𝄪','E','F♭'],  # WHITE
    ['F','E♯'],  # WHITE
    ['F♯','G♭'], # BLACK
    ['G','F𝄪'],  # WHITE
    ['G♯','A♭']  # BLACK
]

def make_tonic(tonic, notes, ascending=True):
    return rotate(NOTES, find_note(tonic))

def rotate(l, n):
    return l[n:] + l[:n]

def major_scale(note):
    return extract_notes(make_tonic(note, NOTES), note, 'TTSTTTS', 'STTTSTT', 'major')

def minor_scale(note):
    return extract_notes(make_tonic(note, NOTES), note, 'TSTTSTT', 'TTSTTST', 'natural minor')

def harmonic_minor_scale(note):
    return extract_notes(make_tonic(note, NOTES), note, 'TSTTSAS', 'SASTTST', 'harmonic minor')

def melodic_minor_scale(note):
    return extract_notes(make_tonic(note, NOTES), note, 'TSTTTTS', 'TSTTSTT', 'melodic minor')

def extract_notes(notes, tonic, ascending, descending, pattern):
    ascending_scale = [tonic]

    offset = 0
    last_letter = tonic[0]
    for step in ascending:
        step_change = 0

        if (step == 'T'): # Tone
            step_change = 2
        elif (step == 'A'): # Augmented
            step_change = 3
        else:
            step_change = 1 # Semitone

        offset += step_change
        this_letter = LETTERS[(LETTERS.index(last_letter) + 1) % len(LETTERS)]
        options = notes[offset % len(notes)]

        if type(options) == str and options[0] == this_letter:
            ascending_scale.append(options)
            last_letter = options[0]
        elif type(options) == list:
            for option in options:
                if option[0] == this_letter:
                    ascending_scale.append(option)
                    last_letter = this_letter

        if this_letter != last_letter:
            raise Exception("Couldn't find " + this_letter + " for " + tonic + " scale.  Scale so far: " + str(ascending_scale) + ". Options were " + str(options))

    descending_scale = [tonic]

    offset = 0
    last_letter = tonic[0]
    for step in descending:
        step_change = 0

        if (step == 'T'): # Tone
            step_change = 2
        elif (step == 'A'): # Augmented
            step_change = 3
        else:
            step_change = 1 # Semitone

        offset -= step_change
        this_letter = LETTERS[(LETTERS.index(last_letter) - 1) % len(LETTERS)]
        options = notes[offset % len(notes)]

        if type(options) == str and options[0] == this_letter:
            descending_scale.append(options)
            last_letter = options[0]
        elif type(options) == list:
            for option in options:
                if option[0] == this_letter:
                    descending_scale.append(option)
                    last_letter = this_letter

        if this_letter != last_letter:
            raise Exception("Couldn't find " + this_letter + " for " + tonic + " scale.  Scale so far: " + str(ascending_scale) + ". Options were " + str(options))
                
    return Scale(tonic, pattern, ascending_scale, descending_scale)

def find_note(note):
    for i in range(len(NOTES)):
        if type(NOTES[i] == list) and note in NOTES[i]:
            return i
        elif type(NOTES[i] == str) and note == NOTES[i]:
            return i

class Interval:
    first = None
    second = None

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def quantity(self):
        distance = LETTERS.index(self.second[0]) - LETTERS.index(self.first[0]) + 1
        if distance < 1:
            distance += 7

        return distance

    def quality(self, quantity):
        semitone_span = find_note(self.second) - find_note(self.first)
        if semitone_span < 0:
            semitone_span += 12

        if quantity in (1, 4, 5, 8):
            perfect = None
            if quantity == 1:
                perfect = 0
            elif quantity == 4:
                perfect = 5
            elif quantity == 5:
                perfect = 7
            else:
                perfect = 12

            if semitone_span == perfect - 1:
                return "d"
            elif semitone_span == perfect:
                return "P"
            elif semitone_span == perfect + 1:
                return "A"
            elif semitone_span == perfect + 2:
                return "2A"
            else:
                return "?"
        else:
            major = None
            if quantity == 2:
                major = 2
            elif quantity == 3:
                major = 4
            elif quantity == 6:
                major = 9
            else:
                major = 11

            if semitone_span == major:
                return "M"
            elif semitone_span == major - 1:
                return "m"
            elif semitone_span == major - 2:
                return "d"
            elif semitone_span == major + 1:
                return "A"
            elif semitone_span == major + 2:
                return "2A"
            else:
                return "?"

    def notation(self):
        quantity = self.quantity()

        return self.quality(quantity) + str(quantity)

    def __str__(self):
        return self.first + "-" + self.second + "\t(" + self.notation() + ")"


class Scale:
    tonic = None
    pattern = None
    ascending = None
    descending = None

    def __init__(self, tonic, pattern, ascending, descending):
        self.tonic = tonic
        self.pattern = pattern
        self.ascending = ascending
        self.descending = descending

    def triad(self, position = 1, inversion = 0):
        return self.chord(position, inversion, False)

    def seventh(self, position = 1, inversion = 0):
        return self.chord(position, inversion, True)

    def chord(self, position = 1, inversion = 0, seventh = False):
        first = self.ascending[(position - 1) % 7]
        second = self.ascending[(position + 1) % 7]
        third = self.ascending[(position + 3) % 7]
        fourth = self.ascending[(position + 5) % 7]

        if inversion == 1:
            if seventh:
                return Chord(second, third, fourth, first)
            else:
                return Chord(second, third, first)
        elif inversion == 2:
            if seventh:
                return Chord(third, fourth, first, second)
            else:
                return Chord(third, first, second)
        elif inversion == 3:
            if seventh:
                return Chord(fourth, first, second, third)
            else:
                raise Exception("Triads don't have a third inversion")
        else:
            if seventh:
                return Chord(first, second, third, fourth)
            else:
                return Chord(first, second, third)

    def dominant(self):
        return self.ascending[4]

    def subdominant(self):
        return self.ascending[3]

    def __str__(self):
        return self.tonic + " " + self.pattern + "; ASC=" + str(self.ascending) + "; DESC=" + str(self.descending)

class Chord:
    triads = {
        'M3': {
            'M3': 'aug',
            'm3': 'M'
        },
        'm3': {
            'M3': 'm',
            'm3': 'dim'
        }
    }
    sevenths = {
        'M3': {
            'M3': {
                'M3': None,
                'm3': '+M7'
            },
            'm3': {
                'M3': 'M7', # Major seventh
                'm3': '7' # Dominant seventh
            }
        },
        'm3': {
            'M3': {
                'M3': 'mM7', # Minor major seventh
                'm3': 'm7' # Minor seventh
            },
            'm3': {
                'M3': 'm7♭5', # Half-diminished seventh
                'm3': 'm♭7♭5' # Diminished seventh
            }
        }
    }

    first = None
    second = None
    third = None
    fourth = None

    def __init__(self, first, second, third, fourth = None):
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth

    def notes(self):
        if self.fourth == None:
            return [self.first, self.second, self.third]
        else:
            return [self.first, self.second, self.third, self.fourth]

    def notation(self):
        step_one = Interval(self.first, self.second).notation()
        step_two = Interval(self.second, self.third).notation()
        step_three = None

        if self.fourth != None:
            step_three = Interval(self.third, self.fourth).notation()

        name = self.first

        if step_three == None:
            name += self.triads[step_one][step_two]
        else:
            name += self.sevenths[step_one][step_two][step_three]

        return name

    def __str__(self):
        if self.fourth == None:
            return self.first + "-" + self.second + "-" + self.third + "\t" + self.notation()
        else:
            return self.first + "-" + self.second + "-" + self.third + "-" + self.fourth + "\t" + self.notation()
