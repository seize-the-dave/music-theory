LETTERS = ['A','B','C','D','E','F','G']

MAJOR_SCALES = ['C','G','D','A','E','B','F♯','C♯','G♯','F','B♭','E♭','A♭','D♭','G♭','C♭','F♭']
MINOR_SCALES = ['A','E','B','F♯','C♯','G♯','D♯','A♯','E♯','D','G','C','F','B♭','E♭','A♭','D♭']

NOTES = [
        ['A','B𝄫'],
        ['B♭','A♯'],
        ['B','C♭'],
        ['C','B♯'],
        ['C♯','D♭'],
        'D',
        ['E♭','D♯'],
        ['E','F♭'],
        ['F','E♯'],
        ['F♯','G♭'],
        ['G','F𝄪'],
        ['G♯','A♭']
    ]

def make_tonic(tonic, notes):
    index = None
    for i in range(len(notes)):
        if type(notes[i] == list) and tonic in notes[i]:
            index = i
        elif type(notes[i] == str) and tonic == notes[i]:
            index = i
    return rotate(notes, index)

def rotate(l, n):
    return l[n:] + l[:n]

def major_scale(note):
    return extract_notes(make_tonic(note, NOTES), note, 'TTSTTTS')

def minor_scale(note):
    return extract_notes(make_tonic(note, NOTES), note, 'TSTTSTT')

def extract_notes(notes, tonic, pattern):
    scale = [tonic]
    offset = 0
    last_letter = tonic[0]
    for step in pattern:
        if (step == 'T'):
            offset += 2
        else:
            offset += 1
        options = notes[offset % len(notes)]
        this_letter = LETTERS[(LETTERS.index(last_letter) + 1) % len(LETTERS)]

        found = False
        if type(options) == str and options[0] == this_letter:
            scale.append(options)
            last_letter = options[0]
            found = True
        elif type(options) == list:
            for option in options:
                if option[0] == this_letter:
                    scale.append(option)
                    last_letter = this_letter
                    found = True
        if found == False:
            print("Couldn't find note matching " + this_letter + " for " + tonic)
            print("Progress: " + str(scale))
            print("Was looking in " + str(options))
                
    return scale
