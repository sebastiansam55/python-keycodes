#!/usr/bin/python3
from string import ascii_lowercase

keys = {
    "(no event indicated)": {
            "plaintext": "(no event indicated)", "shifted": "",
            "evdev": -3, "decimal": 0, "hex": 0x00,
            "javascript": -1},
    "ErrorRollOver": {
            "plaintext": "ErrorRollOver", "shifted": "",
            "evdev": -3, "decimal": 1, "hex": 0x01,
            "javascript": -1},
    "POSTFail": {
            "plaintext": "POSTFail", "shifted": "",
            "evdev": -3, "decimal": 2, "hex": 0x02,
            "javascript": -1},
    "ErrorUndefined": {
            "plaintext": "ErrorUndefined", "shifted": "",
            "evdev": -3, "decimal": 3, "hex": 0x03,
            "javascript": -1},
    "a": {
            "plaintext": "a", "shifted": "A",
            "evdev": 30, "decimal": 4, "hex": 0x04,
            "javascript": 65},
    "b": {
            "plaintext": "b", "shifted": "B",
            "evdev": 48, "decimal": 5, "hex": 0x05,
            "javascript": 66},
    "c": {
            "plaintext": "c", "shifted": "C",
            "evdev": 46, "decimal": 6, "hex": 0x06,
            "javascript": 67},
    "d": {
            "plaintext": "d", "shifted": "D",
            "evdev": 32, "decimal": 7, "hex": 0x07,
            "javascript": 68},
    "e": {
            "plaintext": "e", "shifted": "E",
            "evdev": 18, "decimal": 8, "hex": 0x08,
            "javascript": 69},
    "f": {
            "plaintext": "f", "shifted": "F",
            "evdev": 33, "decimal": 9, "hex": 0x09,
            "javascript": 70},
    "g": {
            "plaintext": "g", "shifted": "G",
            "evdev": 34, "decimal": 10, "hex": 0x0A,
            "javascript": 71},
    "h": {
            "plaintext": "h", "shifted": "H",
            "evdev": 35, "decimal": 11, "hex": 0x0B,
            "javascript": 72},
    "i": {
            "plaintext": "i", "shifted": "I",
            "evdev": 23, "decimal": 12, "hex": 0x0C,
            "javascript": 73},
    "j": {
            "plaintext": "j", "shifted": "J",
            "evdev": 36, "decimal": 13, "hex": 0x0D,
            "javascript": 74},
    "k": {
            "plaintext": "k", "shifted": "K",
            "evdev": 37, "decimal": 14, "hex": 0x0E,
            "javascript": 75},
    "l": {
            "plaintext": "l", "shifted": "L",
            "evdev": 38, "decimal": 15, "hex": 0x0F,
            "javascript": 76},
    "m": {
            "plaintext": "m", "shifted": "M",
            "evdev": 50, "decimal": 16, "hex": 0x10,
            "javascript": 77},
    "n": {
            "plaintext": "n", "shifted": "N",
            "evdev": 49, "decimal": 17, "hex": 0x11,
            "javascript": 78},
    "o": {
            "plaintext": "o", "shifted": "O",
            "evdev": 24, "decimal": 18, "hex": 0x12,
            "javascript": 79},
    "p": {
            "plaintext": "p", "shifted": "P",
            "evdev": 25, "decimal": 19, "hex": 0x13,
            "javascript": 80},
    "q": {
            "plaintext": "q", "shifted": "Q",
            "evdev": 16, "decimal": 20, "hex": 0x14,
            "javascript": 81},
    "r": {
            "plaintext": "r", "shifted": "R",
            "evdev": 19, "decimal": 21, "hex": 0x15,
            "javascript": 82},
    "s": {
            "plaintext": "s", "shifted": "S",
            "evdev": 31, "decimal": 22, "hex": 0x16,
            "javascript": 83},
    "t": {
            "plaintext": "t", "shifted": "T",
            "evdev": 20, "decimal": 23, "hex": 0x17,
            "javascript": 84},
    "u": {
            "plaintext": "u", "shifted": "U",
            "evdev": 22, "decimal": 24, "hex": 0x18,
            "javascript": 85},
    "v": {
            "plaintext": "v", "shifted": "V",
            "evdev": 47, "decimal": 25, "hex": 0x19,
            "javascript": 86},
    "w": {
            "plaintext": "w", "shifted": "W",
            "evdev": 17, "decimal": 26, "hex": 0x1A,
            "javascript": 87},
    "x": {
            "plaintext": "x", "shifted": "X",
            "evdev": 45, "decimal": 27, "hex": 0x1B,
            "javascript": 88},
    "y": {
            "plaintext": "y", "shifted": "Y",
            "evdev": 21, "decimal": 28, "hex": 0x1C,
            "javascript": 89},
    "z": {
            "plaintext": "z", "shifted": "Z",
            "evdev": 44, "decimal": 29, "hex": 0x1D,
            "javascript": 90},
    "1": {
            "plaintext": "1", "shifted": "!",
            "evdev": 2, "decimal": 30, "hex": 0x1E,
            "javascript": 49},
    "2": {
            "plaintext": "2", "shifted": "@",
            "evdev": 3, "decimal": 31, "hex": 0x1F,
            "javascript": 50},
    "3": {
            "plaintext": "3", "shifted": "#",
            "evdev": 4, "decimal": 32, "hex": 0x20,
            "javascript": 51},
    "4": {
            "plaintext": "4", "shifted": "$",
            "evdev": 5, "decimal": 33, "hex": 0x21,
            "javascript": 52},
    "5": {
            "plaintext": "5", "shifted": "%",
            "evdev": 6, "decimal": 34, "hex": 0x22,
            "javascript": 53},
    "6": {
            "plaintext": "6", "shifted": "^",
            "evdev": 7, "decimal": 35, "hex": 0x23,
            "javascript": 54},
    "7": {
            "plaintext": "7", "shifted": "&",
            "evdev": 8, "decimal": 36, "hex": 0x24,
            "javascript": 55},
    "8": {
            "plaintext": "8", "shifted": "*",
            "evdev": 9, "decimal": 37, "hex": 0x25,
            "javascript": 56},
    "9": {
            "plaintext": "9", "shifted": "(",
            "evdev": 10, "decimal": 38, "hex": 0x26,
            "javascript": 57},
    "0": {
            "plaintext": "0", "shifted": ")",
            "evdev": 11, "decimal": 39, "hex": 0x27,
            "javascript": 48},
    "Return (ENTER)": {
            "plaintext": "Return (ENTER)", "shifted": "",
            "evdev": 28, "decimal": 40, "hex": 0x28,
            "javascript": 13},
    "ESCAPE": {
            "plaintext": "ESCAPE", "shifted": "",
            "evdev": 1, "decimal": 41, "hex": 0x29,
            "javascript": 27},
    "DELETE (Backspace)": {
            "plaintext": "DELETE (Backspace)", "shifted": "",
            "evdev": 14, "decimal": 42, "hex": 0x2A,
            "javascript": 8},
    "Tab": {
            "plaintext": "Tab", "shifted": "",
            "evdev": 15, "decimal": 43, "hex": 0x2B,
            "javascript": 9},
    " ": {
            "plaintext": " ", "shifted": "",
            "evdev": 57, "decimal": 44, "hex": 0x2C,
            "javascript": 32},
    "-": {
            "plaintext": "-", "shifted": "(",
            "evdev": 12, "decimal": 45, "hex": 0x2D,
            "javascript": -1},
    "=": {
            "plaintext": "=", "shifted": "+",
            "evdev": 13, "decimal": 46, "hex": 0x2E,
            "javascript": -1},
    "[": {
            "plaintext": "[", "shifted": "{",
            "evdev": 26, "decimal": 47, "hex": 0x2F,
            "javascript": -1},
    "]": {
            "plaintext": "]", "shifted": "}",
            "evdev": 27, "decimal": 48, "hex": 0x30,
            "javascript": -1},
    "\\": {
            "plaintext": "\\", "shifted": "|",
            "evdev": 43, "decimal": 49, "hex": 0x31,
            "javascript": -1},
    "Non-US # and ~": {
            "plaintext": "Non-US # and ~", "shifted": "",
            "evdev": 42, "decimal": 50, "hex": 0x32,
            "javascript": -1},
    ";": {
            "plaintext": ";", "shifted": ":",
            "evdev": 39, "decimal": 51, "hex": 0x33,
            "javascript": -1},
    "'": {
            "plaintext": "'", "shifted": "\"",
            "evdev": 40, "decimal": 52, "hex": 0x34,
            "javascript": -1},
    "`": {
            "plaintext": "`", "shifted": "~",
            "evdev": 41, "decimal": 53, "hex": 0x35,
            "javascript": -1},
    ",": {
            "plaintext": ",", "shifted": "",
            "evdev": 51, "decimal": 54, "hex": 0x36,
            "javascript": -1},
    ".": {
            "plaintext": ".", "shifted": ">",
            "evdev": 52, "decimal": 55, "hex": 0x37,
            "javascript": -1},
    "/": {
            "plaintext": "/", "shifted": "?",
            "evdev": 53, "decimal": 56, "hex": 0x38,
            "javascript": -1},
    "Caps Lock": {
            "plaintext": "Caps Lock", "shifted": "",
            "evdev": 58, "decimal": 57, "hex": 0x39,
            "javascript": -1},
    "F1": {
            "plaintext": "F1", "shifted": "",
            "evdev": 59, "decimal": 58, "hex": 0x3A,
            "javascript": 112},
    "F2": {
            "plaintext": "F2", "shifted": "",
            "evdev": 60, "decimal": 59, "hex": 0x3B,
            "javascript": 113},
    "F3": {
            "plaintext": "F3", "shifted": "",
            "evdev": 61, "decimal": 60, "hex": 0x3C,
            "javascript": 114},
    "F4": {
            "plaintext": "F4", "shifted": "",
            "evdev": 62, "decimal": 61, "hex": 0x3D,
            "javascript": 115},
    "F5": {
            "plaintext": "F5", "shifted": "",
            "evdev": 63, "decimal": 62, "hex": 0x3E,
            "javascript": 116},
    "F6": {
            "plaintext": "F6", "shifted": "",
            "evdev": 64, "decimal": 63, "hex": 0x3F,
            "javascript": 117},
    "F7": {
            "plaintext": "F7", "shifted": "",
            "evdev": 65, "decimal": 64, "hex": 0x40,
            "javascript": 118},
    "F8": {
            "plaintext": "F8", "shifted": "",
            "evdev": 66, "decimal": 65, "hex": 0x41,
            "javascript": 119},
    "F9": {
            "plaintext": "F9", "shifted": "",
            "evdev": 67, "decimal": 66, "hex": 0x42,
            "javascript": 120},
    "F10": {
            "plaintext": "F10", "shifted": "",
            "evdev": 68, "decimal": 67, "hex": 0x43,
            "javascript": 121},
    "F11": {
            "plaintext": "F11", "shifted": "",
            "evdev": 87, "decimal": 68, "hex": 0x44,
            "javascript": 122},
    "F12": {
            "plaintext": "F12", "shifted": "",
            "evdev": 88, "decimal": 69, "hex": 0x45,
            "javascript": 123},
    "PrintScreen": {
            "plaintext": "PrintScreen", "shifted": "",
            "evdev": 124, "decimal": 70, "hex": 0x46,
            "javascript": -1},
    "Scroll Lock": {
            "plaintext": "Scroll Lock", "shifted": "",
            "evdev": 70, "decimal": 71, "hex": 0x47,
            "javascript": -1},
    "Pause": {
            "plaintext": "Pause", "shifted": "",
            "evdev": 119, "decimal": 72, "hex": 0x48,
            "javascript": -1},
    "Insert": {
            "plaintext": "Insert", "shifted": "",
            "evdev": 110, "decimal": 73, "hex": 0x49,
            "javascript": -1},
    "Home": {
            "plaintext": "Home", "shifted": "",
            "evdev": 102, "decimal": 74, "hex": 0x4A,
            "javascript": -1},
    "PageUp": {
            "plaintext": "PageUp", "shifted": "",
            "evdev": 104, "decimal": 75, "hex": 0x4B,
            "javascript": -1},
    "Delete Forward": {
            "plaintext": "Delete Forward", "shifted": "",
            "evdev": 111, "decimal": 76, "hex": 0x4C,
            "javascript": -1},
    "End": {
            "plaintext": "End", "shifted": "",
            "evdev": 107, "decimal": 77, "hex": 0x4D,
            "javascript": -1},
    "PageDown": {
            "plaintext": "PageDown", "shifted": "",
            "evdev": 109, "decimal": 78, "hex": 0x4E,
            "javascript": -1},
    "RightArrow": {
            "plaintext": "RightArrow", "shifted": "",
            "evdev": 106, "decimal": 79, "hex": 0x4F,
            "javascript": -1},
    "LeftArrow": {
            "plaintext": "LeftArrow", "shifted": "",
            "evdev": 105, "decimal": 80, "hex": 0x50,
            "javascript": -1},
    "DownArrow": {
            "plaintext": "DownArrow", "shifted": "",
            "evdev": 108, "decimal": 81, "hex": 0x51,
            "javascript": -1},
    "UpArrow": {
            "plaintext": "UpArrow", "shifted": "",
            "evdev": 103, "decimal": 82, "hex": 0x52,
            "javascript": -1},
    "KPNum Lock and Clear": {
            "plaintext": "Num Lock and Clear", "shifted": "",
            "evdev": 69, "decimal": 83, "hex": 0x53,
            "javascript": -1},
    "KP/": {
            "plaintext": "/", "shifted": "",
            "evdev": 95, "decimal": 84, "hex": 0x54,
            "javascript": -1},
    "KP*": {
            "plaintext": "*", "shifted": "",
            "evdev": 100, "decimal": 85, "hex": 0x55,
            "javascript": -1},
    "KP-": {
            "plaintext": "-", "shifted": "",
            "evdev": 105, "decimal": 86, "hex": 0x56,
            "javascript": -1},
    "KP+": {
            "plaintext": "+", "shifted": "",
            "evdev": 106, "decimal": 87, "hex": 0x57,
            "javascript": -1},
    "KPENTER": {
            "plaintext": "ENTER", "shifted": "",
            "evdev": 108, "decimal": 88, "hex": 0x58,
            "javascript": -1},
    "KP1": {
            "plaintext": "1", "shifted": "E",
            "evdev": 93, "decimal": 89, "hex": 0x59,
            "javascript": -1},
    "KP2": {
            "plaintext": "2", "shifted": "D",
            "evdev": 98, "decimal": 90, "hex": 0x5A,
            "javascript": -1},
    "KP3": {
            "plaintext": "3", "shifted": "P",
            "evdev": 103, "decimal": 91, "hex": 0x5B,
            "javascript": -1},
    "KP4": {
            "plaintext": "4", "shifted": "L",
            "evdev": 92, "decimal": 92, "hex": 0x5C,
            "javascript": -1},
    "KP5": {
            "plaintext": "5", "shifted": "",
            "evdev": 97, "decimal": 93, "hex": 0x5D,
            "javascript": -1},
    "KP6": {
            "plaintext": "6", "shifted": "R",
            "evdev": 102, "decimal": 94, "hex": 0x5E,
            "javascript": -1},
    "KP7": {
            "plaintext": "7", "shifted": "H",
            "evdev": 91, "decimal": 95, "hex": 0x5F,
            "javascript": -1},
    "KP8": {
            "plaintext": "8", "shifted": "U",
            "evdev": 96, "decimal": 96, "hex": 0x60,
            "javascript": -1},
    "KP9": {
            "plaintext": "9", "shifted": "P",
            "evdev": 101, "decimal": 97, "hex": 0x61,
            "javascript": -1},
    "KP0": {
            "plaintext": "0", "shifted": "I",
            "evdev": 99, "decimal": 98, "hex": 0x62,
            "javascript": -1},
    "KP.": {
            "plaintext": ".", "shifted": "D",
            "evdev": 104, "decimal": 99, "hex": 0x63,
            "javascript": -1},
    "Non-US \\ and": {
            "plaintext": "Non-US \\ and", "shifted": "",
            "evdev": 45, "decimal": 100, "hex": 0x64,
            "javascript": -1},
    "Application": {
            "plaintext": "Application", "shifted": "",
            "evdev": 129, "decimal": 101, "hex": 0x65,
            "javascript": -1},
    "Power": {
            "plaintext": "Power", "shifted": "",
            "evdev": 116, "decimal": 102, "hex": 0x66,
            "javascript": -1},
    "KP=": {
            "plaintext": "=", "shifted": "",
            "evdev": 117, "decimal": 103, "hex": 0x67,
            "javascript": -1},
    "F13": {
            "plaintext": "F13", "shifted": "",
            "evdev": 183, "decimal": 104, "hex": 0x68,
            "javascript": 124},
    "F14": {
            "plaintext": "F14", "shifted": "",
            "evdev": 184, "decimal": 105, "hex": 0x69,
            "javascript": 125},
    "F15": {
            "plaintext": "F15", "shifted": "",
            "evdev": 185, "decimal": 106, "hex": 0x6A,
            "javascript": 126},
    "F16": {
            "plaintext": "F16", "shifted": "",
            "evdev": 186, "decimal": 107, "hex": 0x6B,
            "javascript": 127},
    "F17": {
            "plaintext": "F17", "shifted": "",
            "evdev": 187, "decimal": 108, "hex": 0x6C,
            "javascript": 128},
    "F18": {
            "plaintext": "F18", "shifted": "",
            "evdev": 188, "decimal": 109, "hex": 0x6D,
            "javascript": 129},
    "F19": {
            "plaintext": "F19", "shifted": "",
            "evdev": 189, "decimal": 110, "hex": 0x6E,
            "javascript": 130},
    "F20": {
            "plaintext": "F20", "shifted": "",
            "evdev": 190, "decimal": 111, "hex": 0x6F,
            "javascript": 131},
    "F21": {
            "plaintext": "F21", "shifted": "",
            "evdev": 191, "decimal": 112, "hex": 0x70,
            "javascript": 132},
    "F22": {
            "plaintext": "F22", "shifted": "",
            "evdev": 192, "decimal": 113, "hex": 0x71,
            "javascript": 133},
    "F23": {
            "plaintext": "F23", "shifted": "",
            "evdev": 193, "decimal": 114, "hex": 0x72,
            "javascript": 134},
    "F24": {
            "plaintext": "F24", "shifted": "",
            "evdev": 194, "decimal": 115, "hex": 0x73,
            "javascript": 135},
    "Execute": {
            "plaintext": "Execute", "shifted": "",
            "evdev": -3, "decimal": 116, "hex": 0x74,
            "javascript": -1},
    "Help": {
            "plaintext": "Help", "shifted": "",
            "evdev": 138, "decimal": 117, "hex": 0x75,
            "javascript": -1},
    "Menu": {
            "plaintext": "Menu", "shifted": "",
            "evdev": -3, "decimal": 118, "hex": 0x76,
            "javascript": -1},
    "Select": {
            "plaintext": "Select", "shifted": "",
            "evdev": -3, "decimal": 119, "hex": 0x77,
            "javascript": -1},
    "Stop": {
            "plaintext": "Stop", "shifted": "",
            "evdev": -3, "decimal": 120, "hex": 0x78,
            "javascript": -1},
    "Again": {
            "plaintext": "Again", "shifted": "",
            "evdev": -3, "decimal": 121, "hex": 0x79,
            "javascript": -1},
    "Undo": {
            "plaintext": "Undo", "shifted": "",
            "evdev": -3, "decimal": 122, "hex": 0x7A,
            "javascript": -1},
    "Cut": {
            "plaintext": "Cut", "shifted": "",
            "evdev": -3, "decimal": 123, "hex": 0x7B,
            "javascript": -1},
    "Copy": {
            "plaintext": "Copy", "shifted": "",
            "evdev": -3, "decimal": 124, "hex": 0x7C,
            "javascript": -1},
    "Paste": {
            "plaintext": "Paste", "shifted": "",
            "evdev": -3, "decimal": 125, "hex": 0x7D,
            "javascript": -1},
    "Find": {
            "plaintext": "Find", "shifted": "",
            "evdev": -3, "decimal": 126, "hex": 0x7E,
            "javascript": -1},
    "Mute": {
            "plaintext": "Mute", "shifted": "",
            "evdev": -3, "decimal": 127, "hex": 0x7F,
            "javascript": -1},
    "Volume Up": {
            "plaintext": "Volume Up", "shifted": "",
            "evdev": -3, "decimal": 128, "hex": 0x80,
            "javascript": -1},
    "Volume Down": {
            "plaintext": "Volume Down", "shifted": "",
            "evdev": -3, "decimal": 129, "hex": 0x81,
            "javascript": -1},
    "Locking Caps Lock": {
            "plaintext": "Locking Caps Lock", "shifted": "",
            "evdev": -3, "decimal": 130, "hex": 0x82,
            "javascript": -1},
    "Locking Num Lock": {
            "plaintext": "Locking Num Lock", "shifted": "",
            "evdev": -3, "decimal": 131, "hex": 0x83,
            "javascript": -1},
    "Locking Scroll Lock": {
            "plaintext": "Locking Scroll Lock", "shifted": "",
            "evdev": -3, "decimal": 132, "hex": 0x84,
            "javascript": -1},
    "KPComma": {
            "plaintext": "Comma", "shifted": "",
            "evdev": 107, "decimal": 133, "hex": 0x85,
            "javascript": -1},
    "KPEqual Sign": {
            "plaintext": "Equal Sign", "shifted": "",
            "evdev": -3, "decimal": 134, "hex": 0x86,
            "javascript": -1},
    "International1": {
            "plaintext": "International1", "shifted": "",
            "evdev": 56, "decimal": 135, "hex": 0x87,
            "javascript": -1},
    "International2": {
            "plaintext": "International2", "shifted": "",
            "evdev": -3, "decimal": 136, "hex": 0x88,
            "javascript": -1},
    "International3": {
            "plaintext": "International3", "shifted": "",
            "evdev": -3, "decimal": 137, "hex": 0x89,
            "javascript": -1},
    "International4": {
            "plaintext": "International4", "shifted": "",
            "evdev": -3, "decimal": 138, "hex": 0x8A,
            "javascript": -1},
    "International5": {
            "plaintext": "International5", "shifted": "",
            "evdev": -3, "decimal": 139, "hex": 0x8B,
            "javascript": -1},
    "International6": {
            "plaintext": "International6", "shifted": "",
            "evdev": -3, "decimal": 140, "hex": 0x8C,
            "javascript": -1},
    "International7": {
            "plaintext": "International7", "shifted": "",
            "evdev": -3, "decimal": 141, "hex": 0x8D,
            "javascript": -1},
    "International8": {
            "plaintext": "International8", "shifted": "",
            "evdev": -3, "decimal": 142, "hex": 0x8E,
            "javascript": -1},
    "International9": {
            "plaintext": "International9", "shifted": "",
            "evdev": -3, "decimal": 143, "hex": 0x8F,
            "javascript": -1},
    "LANG1": {
            "plaintext": "LANG1", "shifted": "",
            "evdev": -3, "decimal": 144, "hex": 0x90,
            "javascript": -1},
    "LANG2": {
            "plaintext": "LANG2", "shifted": "",
            "evdev": -3, "decimal": 145, "hex": 0x91,
            "javascript": -1},
    "LANG3": {
            "plaintext": "LANG3", "shifted": "",
            "evdev": -3, "decimal": 146, "hex": 0x92,
            "javascript": -1},
    "LANG4": {
            "plaintext": "LANG4", "shifted": "",
            "evdev": -3, "decimal": 147, "hex": 0x93,
            "javascript": -1},
    "LANG5": {
            "plaintext": "LANG5", "shifted": "",
            "evdev": -3, "decimal": 148, "hex": 0x94,
            "javascript": -1},
    "LANG6": {
            "plaintext": "LANG6", "shifted": "",
            "evdev": -3, "decimal": 149, "hex": 0x95,
            "javascript": -1},
    "LANG7": {
            "plaintext": "LANG7", "shifted": "",
            "evdev": -3, "decimal": 150, "hex": 0x96,
            "javascript": -1},
    "LANG8": {
            "plaintext": "LANG8", "shifted": "",
            "evdev": -3, "decimal": 151, "hex": 0x97,
            "javascript": -1},
    "LANG9": {
            "plaintext": "LANG9", "shifted": "",
            "evdev": -3, "decimal": 152, "hex": 0x98,
            "javascript": -1},
    "Alternate Erase": {
            "plaintext": "Alternate Erase", "shifted": "",
            "evdev": -3, "decimal": 153, "hex": 0x99,
            "javascript": -1},
    "SysReq/Attention": {
            "plaintext": "SysReq/Attention", "shifted": "",
            "evdev": -3, "decimal": 154, "hex": 0x9A,
            "javascript": -1},
    "Cancel": {
            "plaintext": "Cancel", "shifted": "",
            "evdev": -3, "decimal": 155, "hex": 0x9B,
            "javascript": -1},
    "Clear": {
            "plaintext": "Clear", "shifted": "",
            "evdev": -3, "decimal": 156, "hex": 0x9C,
            "javascript": -1},
    "Prior": {
            "plaintext": "Prior", "shifted": "",
            "evdev": -3, "decimal": 157, "hex": 0x9D,
            "javascript": -1},
    "Return": {
            "plaintext": "Return", "shifted": "",
            "evdev": -3, "decimal": 158, "hex": 0x9E,
            "javascript": -1},
    "Separator": {
            "plaintext": "Separator", "shifted": "",
            "evdev": -3, "decimal": 159, "hex": 0x9F,
            "javascript": -1},
    "Out": {
            "plaintext": "Out", "shifted": "",
            "evdev": -3, "decimal": 160, "hex": 0xA0,
            "javascript": -1},
    "Oper": {
            "plaintext": "Oper", "shifted": "",
            "evdev": -3, "decimal": 161, "hex": 0xA1,
            "javascript": -1},
    "Clear/Again": {
            "plaintext": "Clear/Again", "shifted": "",
            "evdev": -3, "decimal": 162, "hex": 0xA2,
            "javascript": -1},
    "CrSel/Props": {
            "plaintext": "CrSel/Props", "shifted": "",
            "evdev": -3, "decimal": 163, "hex": 0xA3,
            "javascript": -1},
    "ExSel": {
            "plaintext": "ExSel", "shifted": "",
            "evdev": -3, "decimal": 164, "hex": 0xA4,
            "javascript": -1},
    "KP00": {
            "plaintext": "00", "shifted": "",
            "evdev": -3, "decimal": 176, "hex": 0xB0,
            "javascript": -1},
    "KP000": {
            "plaintext": "000", "shifted": "",
            "evdev": -3, "decimal": 177, "hex": 0xB1,
            "javascript": -1},
    "KP(": {
            "plaintext": "(", "shifted": "",
            "evdev": -3, "decimal": 182, "hex": 0xB6,
            "javascript": -1},
    "KP)": {
            "plaintext": ")", "shifted": "",
            "evdev": -1, "decimal": 183, "hex": 0xB7,
            "javascript": -1},
    "KP{": {
            "plaintext": "{", "shifted": "",
            "evdev": -1, "decimal": 184, "hex": 0xB8,
            "javascript": -1},
    "KP}": {
            "plaintext": "}", "shifted": "",
            "evdev": -1, "decimal": 185, "hex": 0xB9,
            "javascript": -1},
    "KPTab": {
            "plaintext": "Tab", "shifted": "",
            "evdev": -1, "decimal": 186, "hex": 0xBA,
            "javascript": -1},
    "KPBackspace": {
            "plaintext": "Backspace", "shifted": "",
            "evdev": -1, "decimal": 187, "hex": 0xBB,
            "javascript": -1},
    "KPA": {
            "plaintext": "A", "shifted": "",
            "evdev": -1, "decimal": 188, "hex": 0xBC,
            "javascript": -1},
    "KPB": {
            "plaintext": "B", "shifted": "",
            "evdev": -1, "decimal": 189, "hex": 0xBD,
            "javascript": -1},
    "KPC": {
            "plaintext": "C", "shifted": "",
            "evdev": -1, "decimal": 190, "hex": 0xBE,
            "javascript": -1},
    "KPD": {
            "plaintext": "D", "shifted": "",
            "evdev": -1, "decimal": 191, "hex": 0xBF,
            "javascript": -1},
    "KPE": {
            "plaintext": "E", "shifted": "",
            "evdev": -1, "decimal": 192, "hex": 0xC0,
            "javascript": -1},
    "KPF": {
            "plaintext": "F", "shifted": "",
            "evdev": -1, "decimal": 193, "hex": 0xC1,
            "javascript": -1},
    "KPXOR": {
            "plaintext": "XOR", "shifted": "",
            "evdev": -1, "decimal": 194, "hex": 0xC2,
            "javascript": -1},
    "KP^": {
            "plaintext": "^", "shifted": "",
            "evdev": -1, "decimal": 195, "hex": 0xC3,
            "javascript": -1},
    "KP%": {
            "plaintext": "%", "shifted": "",
            "evdev": -1, "decimal": 196, "hex": 0xC4,
            "javascript": -1},
    "KP<": {
            "plaintext": "<", "shifted": "",
            "evdev": -1, "decimal": 197, "hex": 0xC5,
            "javascript": -1},
    "KP>": {
            "plaintext": ">", "shifted": "",
            "evdev": -1, "decimal": 198, "hex": 0xC6,
            "javascript": -1},
    "KP&": {
            "plaintext": "&", "shifted": "",
            "evdev": -1, "decimal": 199, "hex": 0xC7,
            "javascript": -1},
    "KP&&": {
            "plaintext": "&&", "shifted": "",
            "evdev": -1, "decimal": 200, "hex": 0xC8,
            "javascript": -1},
    "KP": {
            "plaintext": "", "shifted": "",
            "evdev": -1, "decimal": 201, "hex": 0xC9,
            "javascript": -1},
    "KP": {
            "plaintext": "", "shifted": "",
            "evdev": -1, "decimal": 202, "hex": 0xCA,
            "javascript": -1},
    "KP:": {
            "plaintext": ":", "shifted": "",
            "evdev": -1, "decimal": 203, "hex": 0xCB,
            "javascript": -1},
    "KP#": {
            "plaintext": "#", "shifted": "",
            "evdev": -1, "decimal": 204, "hex": 0xCC,
            "javascript": -1},
    "KPSpace": {
            "plaintext": "Space", "shifted": "",
            "evdev": -1, "decimal": 205, "hex": 0xCD,
            "javascript": -1},
    "KP@": {
            "plaintext": "@", "shifted": "",
            "evdev": -1, "decimal": 206, "hex": 0xCE,
            "javascript": -1},
    "KP!": {
            "plaintext": "!", "shifted": "",
            "evdev": -1, "decimal": 207, "hex": 0xCF,
            "javascript": -1},
    "KPMemory Store": {
            "plaintext": "Memory Store", "shifted": "",
            "evdev": -1, "decimal": 208, "hex": 0xD0,
            "javascript": -1},
    "KPMemory Recall": {
            "plaintext": "Memory Recall", "shifted": "",
            "evdev": -1, "decimal": 209, "hex": 0xD1,
            "javascript": -1},
    "KPMemory Clear": {
            "plaintext": "Memory Clear", "shifted": "",
            "evdev": -1, "decimal": 210, "hex": 0xD2,
            "javascript": -1},
    "KPMemory Add": {
            "plaintext": "Memory Add", "shifted": "",
            "evdev": -1, "decimal": 211, "hex": 0xD3,
            "javascript": -1},
    "KPMemory Subtract": {
            "plaintext": "Memory Subtract", "shifted": "",
            "evdev": -1, "decimal": 212, "hex": 0xD4,
            "javascript": -1},
    "KPMemory Multiply": {
            "plaintext": "Memory Multiply", "shifted": "",
            "evdev": -1, "decimal": 213, "hex": 0xD5,
            "javascript": -1},
    "KPMemory Divide": {
            "plaintext": "Memory Divide", "shifted": "",
            "evdev": -1, "decimal": 214, "hex": 0xD6,
            "javascript": -1},
    "KP+/-": {
            "plaintext": "+/-", "shifted": "",
            "evdev": -1, "decimal": 215, "hex": 0xD7,
            "javascript": -1},
    "KPClear": {
            "plaintext": "Clear", "shifted": "",
            "evdev": -1, "decimal": 216, "hex": 0xD8,
            "javascript": -1},
    "KPClear Entry": {
            "plaintext": "Clear Entry", "shifted": "",
            "evdev": -1, "decimal": 217, "hex": 0xD9,
            "javascript": -1},
    "KPBinary": {
            "plaintext": "Binary", "shifted": "",
            "evdev": -1, "decimal": 218, "hex": 0xDA,
            "javascript": -1},
    "KPOctal": {
            "plaintext": "Octal", "shifted": "",
            "evdev": -1, "decimal": 219, "hex": 0xDB,
            "javascript": -1},
    "KPDecimal": {
            "plaintext": "Decimal", "shifted": "",
            "evdev": -1, "decimal": 220, "hex": 0xDC,
            "javascript": -1},
    "KPHexadecimal": {
            "plaintext": "Hexadecimal", "shifted": "",
            "evdev": -3, "decimal": 221, "hex": 0xDD,
            "javascript": -1},
    "LeftControl": {
            "plaintext": "LeftControl", "shifted": "",
            "evdev": 29, "decimal": 224, "hex": 0xE0,
            "javascript": -1},
    "LeftShift": {
            "plaintext": "LeftShift", "shifted": "",
            "evdev": 42, "decimal": 225, "hex": 0xE1,
            "javascript": -1},
    "LeftAlt": {
            "plaintext": "LeftAlt", "shifted": "",
            "evdev": 56, "decimal": 226, "hex": 0xE2,
            "javascript": -1},
    "Left GUI": {
            "plaintext": "Left GUI", "shifted": "",
            "evdev": 125, "decimal": 227, "hex": 0xE3,
            "javascript": -1},
    "RightControl": {
            "plaintext": "RightControl", "shifted": "",
            "evdev": 97, "decimal": 228, "hex": 0xE4,
            "javascript": -1},
    "RightShift": {
            "plaintext": "RightShift", "shifted": "",
            "evdev": 54, "decimal": 229, "hex": 0xE5,
            "javascript": -1},
    "RightAlt": {
            "plaintext": "RightAlt", "shifted": "",
            "evdev": 100, "decimal": 230, "hex": 0xE6,
            "javascript": -1},
    "Right GUI": {
            "plaintext": "Right GUI", "shifted": "",
            "evdev": 126, "decimal": 231, "hex": 0xE7,
            "javascript": -1},
}

def add_evdev_shift(shift, unshift):
    keys[shift]["evdev"] = [[42], int(keys[unshift]["evdev"])]

keys['<'] = keys[','].copy()
keys['>'] = keys['.'].copy()
keys['"'] = keys['\''].copy()
keys[':'] = keys[';'].copy()
keys['!'] = keys['1'].copy()
keys['@'] = keys['2'].copy()
keys['#'] = keys['3'].copy()
keys['$'] = keys['4'].copy()
keys['%'] = keys['5'].copy()
keys['^'] = keys['6'].copy()
keys['&'] = keys['7'].copy()
keys['*'] = keys['8'].copy()
keys['('] = keys['9'].copy()
keys[')'] = keys['0'].copy()
keys['{'] = keys['['].copy()
keys['}'] = keys[']'].copy()
keys['?'] = keys['/'].copy()
keys['~'] = keys['`'].copy()
keys['_'] = keys['-'].copy()
keys['+'] = keys['='].copy()
keys['|'] = keys['\\'].copy()

shifted = "<>\":!@#$%^&*(){}?~_+|"
unshifted = ",.';1234567890[]/`-=\\"

for shift, unshift in zip(shifted, unshifted):
    add_evdev_shift(shift, unshift)
# add upper cases:
for ch in ascii_lowercase:
    keys[ch.upper()] = keys[ch].copy()
    keys[ch.upper()]["evdev"] = [[42], int(keys[ch]["evdev"])]
