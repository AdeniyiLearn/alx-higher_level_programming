#!/usr/bin/python3


def roman_to_int(roman_string):
    """" converts a Roman numeral to an integer.

    args:
        roman_string: a string to be converted.

    Returns: integers.
    """
    record = 0
    roman_d = {
            'I' : 1, 'V' : 5, 'X' : 10,
            'L': 50, 'C' : 100, 'D' : 500,
            'M' : 1000
            }
    if not ininstance(roman_string, str):
        return 0

    for key, value in roman_d.items():
        if key in roman_d:

