#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0

    roman_arabic = {
        "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
    }
    roman_string = roman_string[::-1]
    num = 0
    prev = 0
    for symbol in roman_string:
        value = roman_arabic[symbol]
        if value < prev:
            num -= value
        else:
            num += value
        prev = value

    return num
