#!/usr/bin/python3
# 9-print_last_digit.py
def print_last_digit(number):
    g = abs(number) % 10
    print("{}".format(g), end="")
    return g
