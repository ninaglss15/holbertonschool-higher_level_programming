#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    if not isinstance(roman_string, str):
        return 0
    dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    i = 0
    length = len(roman_string)

    while i < length:
        current_value = dict.get(roman_string[i], 0)
        if i + 1 < length:
            next_value = dict.get(roman_string[i + 1], 0)
            if current_value < next_value:
                total += next_value - current_value
                i += 2
                continue
        total += current_value
        i += 1
    return total
