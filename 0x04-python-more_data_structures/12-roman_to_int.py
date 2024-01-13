#!/usr/bin/python3


def roman_to_int(roman_string):
    """Converts a Roman numeral to an integer.

    Args:
        roman_string (str): The Roman numeral to convert.

    Returns:
        int: The converted integer,
        or 0 if roman_string is not a string or None.
    """
    if not isinstance(roman_string, str):
        return 0
    roman_numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    for i, c in enumerate(roman_string):
        if i > 0 and roman_numerals[c] > roman_numerals[roman_string[i - 1]]:
            total += roman_numerals[c] - 2 * roman_numerals[roman_string[i - 1]]
        else:
            total += roman_numerals[c]
    return total
