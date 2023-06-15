#!/usr/bin/python3
# A function to convert roman number to integer.


def roman_to_int(roman_string):
    rom_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    if not roman_string:
        return (0)

    if not isinstance(roman_string, str):
        return (0)

    result = 0
    prenum = 0
    for char in reversed(roman_string):
        num = rom_num[char]

        if num >= prenum:
            result += num
        else:
            result -= num

        prenum = num

    return (result)
