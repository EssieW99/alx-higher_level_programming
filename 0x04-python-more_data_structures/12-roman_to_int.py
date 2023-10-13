#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dic = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
            }
    if roman_string is None:
        return 0
    if not isinstance(roman_string, str):
        return 0
    number = 0
    prev_number = 0
    for roman in roman_string[::-1]:
        value = roman_dic.get(roman, 0)
        if value < prev_number:
            number -= value
        else:
            number += value
        prev_number = value
    return number
