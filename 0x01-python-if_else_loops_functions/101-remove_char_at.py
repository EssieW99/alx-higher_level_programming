#!/usr/bin/python3
# 101-remove_char_at.py
def remove_char_at(str, n):
    if n < 0 or n > len(str) - 1:
        return str
    else:
        return str[:n] + str[n + 1:]
