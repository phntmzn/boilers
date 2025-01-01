import numpy as np

chords = {
    "Major": {
        "Inversion 0": np.array([0, 4, 7]),
        "Inversion 1": np.array([4, 7, 12]),
        "Inversion 2": np.array([7, 12, 16])
    },
    "Minor": {
        "Inversion 0": np.array([0, 3, 7]),
        "Inversion 1": np.array([3, 7, 12]),
        "Inversion 2": np.array([7, 12, 15])
    },
    "Diminished": {
        "Inversion 0": np.array([0, 3, 6]),
        "Inversion 1": np.array([3, 6, 12]),
        "Inversion 2": np.array([6, 12, 15])
    },
    "Augmented": {
        "Inversion 0": np.array([0, 4, 8]),
        "Inversion 1": np.array([4, 8, 12]),
        "Inversion 2": np.array([8, 12, 16])
    },
    "Major 7th": {
        "Inversion 0": np.array([0, 4, 7, 11]),
        "Inversion 1": np.array([4, 7, 11, 12]),
        "Inversion 2": np.array([7, 11, 12, 16]),
        "Inversion 3": np.array([11, 12, 16, 19])
    },
    "Minor 7th": {
        "Inversion 0": np.array([0, 3, 7, 10]),
        "Inversion 1": np.array([3, 7, 10, 12]),
        "Inversion 2": np.array([7, 10, 12, 15]),
        "Inversion 3": np.array([10, 12, 15, 19])
    },
    "9 sus": {
        "Inversion 0": np.array([0, 2, 7, 10]),
        "Inversion 1": np.array([2, 7, 10, 12]),
        "Inversion 2": np.array([7, 10, 12, 14]),
        "Inversion 3": np.array([10, 12, 14, 19])
    },
    "6": {
        "Major 6": {
            "Inversion 0": np.array([0, 4, 7, 9]),
            "Inversion 1": np.array([4, 7, 9, 12]),
            "Inversion 2": np.array([7, 9, 12, 16]),
            "Inversion 3": np.array([9, 12, 16, 19])
        },
        "Minor 6": {
            "Inversion 0": np.array([0, 3, 7, 9]),
            "Inversion 1": np.array([3, 7, 9, 12]),
            "Inversion 2": np.array([7, 9, 12, 15]),
            "Inversion 3": np.array([9, 12, 15, 19])
        }
    },
    "5": {
        "Inversion 0": np.array([0, 7]),
        "Inversion 1": np.array([7, 12]),
        "Inversion 2": np.array([12, 19])
    }
}

print(chords)
