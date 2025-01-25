#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>

std::unordered_map<std::string, std::vector<int>> CHORD_PATTERNS = {
    // Triads
    {"Major", {0, 4, 7}},
    {"Minor", {0, 3, 7}},
    {"Diminished", {0, 3, 6}},
    {"Augmented", {0, 4, 8}},

    // 7th Chords
    {"Major 7th", {0, 4, 7, 11}},
    {"Minor 7th", {0, 3, 7, 10}},
    {"Dominant 7th", {0, 4, 7, 10}},
    {"Diminished 7th", {0, 3, 6, 9}},
    {"Half-Diminished 7th", {0, 3, 6, 10}},
    {"Augmented 7th", {0, 4, 8, 10}},

    // Extended Chords
    {"9th", {0, 4, 7, 10, 14}},
    {"Major 9th", {0, 4, 7, 11, 14}},
    {"Minor 9th", {0, 3, 7, 10, 14}},
    {"11th", {0, 4, 7, 10, 14, 17}},
    {"13th", {0, 4, 7, 10, 14, 21}},

    // Suspended Chords
    {"Suspended 2nd (sus2)", {0, 2, 7}},
    {"Suspended 4th (sus4)", {0, 5, 7}},

    // Added Note Chords
    {"6th", {0, 4, 7, 9}},
    {"Minor 6th", {0, 3, 7, 9}},
    {"Add 9", {0, 4, 7, 14}},
    {"Minor Add 9", {0, 3, 7, 14}},

    // Altered Chords
    {"7th Flat 5", {0, 4, 6, 10}},
    {"7th Sharp 5", {0, 4, 8, 10}},
    {"Major 7th Sharp 5", {0, 4, 8, 11}},
    {"Minor 7th Flat 5", {0, 3, 6, 10}}
};
