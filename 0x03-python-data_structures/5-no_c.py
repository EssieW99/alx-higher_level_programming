#!/usr/bin/python3
# 5-no_c.py
def no_c(my_string):
    new_string = ""
    for char in my_string:
        if char != 'C' and char != 'c':
            new_string += char
    return new_string
