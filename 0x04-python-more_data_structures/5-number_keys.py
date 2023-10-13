#!/usr/bin/python3
# 5-number_keys.py
def number_keys(a_dictionary):
    sum = 0
    no_keys = list(a_dictionary.keys())
    for i in no_keys:
        sum += 1
    return sum
