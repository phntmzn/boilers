import numpy as np

CHORD_PATTERNS = {
    # Triads
    'Major': np.array([0, 4, 7]),
    'Minor': np.array([0, 3, 7]),
    'Diminished': np.array([0, 3, 6]),
    'Augmented': np.array([0, 4, 8]),
    
    # 7th Chords
    'Major 7th': np.array([0, 4, 7, 11]),
    'Minor 7th': np.array([0, 3, 7, 10]),
    'Dominant 7th': np.array([0, 4, 7, 10]),
    'Diminished 7th': np.array([0, 3, 6, 9]),
    'Half-Diminished 7th': np.array([0, 3, 6, 10]),
    'Augmented 7th': np.array([0, 4, 8, 10]),

    # Extended Chords
    '9th': np.array([0, 4, 7, 10, 14]),
    'Major 9th': np.array([0, 4, 7, 11, 14]),
    'Minor 9th': np.array([0, 3, 7, 10, 14]),
    '11th': np.array([0, 4, 7, 10, 14, 17]),
    '13th': np.array([0, 4, 7, 10, 14, 21]),

    # Suspended Chords
    'Suspended 2nd (sus2)': np.array([0, 2, 7]),
    'Suspended 4th (sus4)': np.array([0, 5, 7]),
    
    # Added Note Chords
    '6th': np.array([0, 4, 7, 9]),
    'Minor 6th': np.array([0, 3, 7, 9]),
    'Add 9': np.array([0, 4, 7, 14]),
    'Minor Add 9': np.array([0, 3, 7, 14]),

    # Altered Chords
    '7th Flat 5': np.array([0, 4, 6, 10]),
    '7th Sharp 5': np.array([0, 4, 8, 10]),
    'Major 7th Sharp 5': np.array([0, 4, 8, 11]),
    'Minor 7th Flat 5': np.array([0, 3, 6, 10]),
}
