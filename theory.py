LETTERS = ['A','B','C','D','E','F','G']

NOTES = [
        'A',
        ['A#','Bb'],
        ['B','Cb'],
        ['B#','C'],
        ['C#','Db'],
        'D',
        ['D#','Eb'],
        ['E','Fb'],
        ['E#','F'],
        ['F#','Gb'],
        'G',
        ['G#','Ab']
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
    return extract_notes(make_tonic(note, NOTES), note, 'WWHWWWH')

def minor_scale(note):
    return extract_notes(make_tonic(note, NOTES), note, 'WHWWHWW')

def extract_notes(notes, tonic, pattern):
    print(tonic)
    scale = [tonic]
    offset = 0
    last_note = tonic[0]
    for step in pattern:
        if (step == 'W'):
            offset += 2
        else:
            offset += 1
        options = notes[offset % len(notes)]
        if type(options) == str:
            scale.append(options)
            last_note = options[0]
        elif type(options) == list:
            starts_with = LETTERS[(LETTERS.index(last_note) + 1) % len(LETTERS)]
            for option in options:
                if option[0] == starts_with:
                    scale.append(option)
                    last_note = starts_with
    return scale
