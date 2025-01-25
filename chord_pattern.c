#include <stdio.h>
#include <string.h>

// Define a structure for chords
typedef struct {
    char name[50];
    int intervals[6]; // Maximum of 6 intervals for extended chords
    int interval_count; // Number of intervals in the chord
} Chord;

// Define the chord patterns
Chord CHORD_PATTERNS[] = {
    // Triads
    {"Major", {0, 4, 7}, 3},
    {"Minor", {0, 3, 7}, 3},
    {"Diminished", {0, 3, 6}, 3},
    {"Augmented", {0, 4, 8}, 3},

    // 7th Chords
    {"Major 7th", {0, 4, 7, 11}, 4},
    {"Minor 7th", {0, 3, 7, 10}, 4},
    {"Dominant 7th", {0, 4, 7, 10}, 4},
    {"Diminished 7th", {0, 3, 6, 9}, 4},
    {"Half-Diminished 7th", {0, 3, 6, 10}, 4},
    {"Augmented 7th", {0, 4, 8, 10}, 4},

    // Extended Chords
    {"9th", {0, 4, 7, 10, 14}, 5},
    {"Major 9th", {0, 4, 7, 11, 14}, 5},
    {"Minor 9th", {0, 3, 7, 10, 14}, 5},
    {"11th", {0, 4, 7, 10, 14, 17}, 6},
    {"13th", {0, 4, 7, 10, 14, 21}, 6},

    // Suspended Chords
    {"Suspended 2nd (sus2)", {0, 2, 7}, 3},
    {"Suspended 4th (sus4)", {0, 5, 7}, 3},

    // Added Note Chords
    {"6th", {0, 4, 7, 9}, 4},
    {"Minor 6th", {0, 3, 7, 9}, 4},
    {"Add 9", {0, 4, 7, 14}, 4},
    {"Minor Add 9", {0, 3, 7, 14}, 4},

    // Altered Chords
    {"7th Flat 5", {0, 4, 6, 10}, 4},
    {"7th Sharp 5", {0, 4, 8, 10}, 4},
    {"Major 7th Sharp 5", {0, 4, 8, 11}, 4},
    {"Minor 7th Flat 5", {0, 3, 6, 10}, 4},
};

// The total number of chords
const int CHORD_COUNT = sizeof(CHORD_PATTERNS) / sizeof(CHORD_PATTERNS[0]);
