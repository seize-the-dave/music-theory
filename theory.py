LETTERS = ['A','B','C','D','E','F','G']

MAJOR_SCALES = ['C','G','D','A','E','B','F♯','C♯','G♯','F','B♭','E♭','A♭','D♭','G♭','C♭','F♭']
MINOR_SCALES = ['A','E','B','F♯','C♯','G♯','D♯','A♯','E♯','D','G','C','F','B♭','E♭','A♭','D♭']

NOTES = [
    ['A','B𝄫'],  # WHITE
    ['B♭','A♯'], # BLACK
    ['B','C♭'],  # WHITE
    ['C','B♯'],  # WHITE
    ['C♯','D♭'], # BLACK
    'D',         # WHITE
    ['E♭','D♯'], # BLACK
    ['E','F♭'],  # WHITE
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

    def chord(self, position = 1, inversion = 0):
        first = (position - 1) % 7
        second = (position + 1) % 7
        third = (position + 3) % 7

        if inversion == 1:
            return Chord(self.ascending[second], self.ascending[third], self.ascending[first])
        elif inversion == 2:
            return Chord(self.ascending[third], self.ascending[first], self.ascending[second])
        else:
            return Chord(self.ascending[first], self.ascending[second], self.ascending[third])

    def dominant(self):
        return self.ascending[4]

    def subdominant(self):
        return self.ascending[3]

    def __str__(self):
        return self.tonic + " " + self.pattern + "; ASC=" + str(self.ascending) + "; DESC=" + str(self.descending)

class Chord:
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

        if step_one == "M3":
            if step_two == "M3":
                name += "aug"
                if step_three == "M3":
                    pass
                elif step_three == "m3":
                    name += "7♯5"
            else:
                if step_three == "M3":
                    name += "maj⁷"
                elif step_three == "m3":
                    name += "⁷"
                else:
                    name += "maj"
        else:
            if step_two == "M3":
                name += "min"
                if step_three == "M3":
                    name += "maj7"
                elif step_three == "m3":
                    name += "⁷"
            else:
                name += "dim"
                if step_three == "M3":
                    name += "7♭5"
                elif step_three == "m3":
                    name += "⁷"
        return name

    def __str__(self):
        if self.fourth == None:
            return self.first + "-" + self.second + "-" + self.third + "\t(" + self.notation() + ")"
        else:
            return self.first + "-" + self.second + "-" + self.third + "-" + self.fourth + "\t(" + self.notation() + ")"
