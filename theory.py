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
    index = None
    for i in range(len(notes)):
        if type(notes[i] == list) and tonic in notes[i]:
            index = i
        elif type(notes[i] == str) and tonic == notes[i]:
            index = i
    notes = rotate(notes, index)
    # if ascending == False:
    #     notes.reverse()
    
    return notes

def rotate(l, n):
    return l[n:] + l[:n]

def major_scale(note, ascending=True):
    if ascending:
        return extract_notes(make_tonic(note, NOTES), note, 'TTSTTTS', ascending)
    else:
        return extract_notes(make_tonic(note, NOTES), note, 'STTTSTT', ascending)

def minor_scale(note, ascending=True):
    if ascending:
        return extract_notes(make_tonic(note, NOTES), note, 'TSTTSTT', ascending)
    else:
        return extract_notes(make_tonic(note, NOTES), note, 'TTSTTST', ascending)

def harmonic_minor_scale(note, ascending=True):
    if ascending:
        return extract_notes(make_tonic(note, NOTES), note, 'TSTTSAS', ascending)
    else:
        return extract_notes(make_tonic(note, NOTES), note, 'SASTTST', ascending)

def melodic_minor_scale(note, ascending=True):
    if ascending:
        return extract_notes(make_tonic(note, NOTES), note, 'TSTTTTS', ascending)
    else:
        return extract_notes(make_tonic(note, NOTES), note, 'TSTTSTT', ascending)

def extract_notes(notes, tonic, pattern, ascending = True):
    scale = [tonic]
    offset = 0
    last_letter = tonic[0]
    for step in pattern:
        step_change = 0

        if (step == 'T'): # Tone
            step_change = 2
        elif (step == 'A'): # Augmented
            step_change = 3
        else:
            step_change = 1 # Semitone

        if ascending:
            offset += step_change
            this_letter = LETTERS[(LETTERS.index(last_letter) + 1) % len(LETTERS)]
        else:
            offset -= step_change
            this_letter = LETTERS[(LETTERS.index(last_letter) - 1) % len(LETTERS)]

        options = notes[offset % len(notes)]

        if type(options) == str and options[0] == this_letter:
            scale.append(options)
            last_letter = options[0]
        elif type(options) == list:
            for option in options:
                if option[0] == this_letter:
                    scale.append(option)
                    last_letter = this_letter
                
    return scale
