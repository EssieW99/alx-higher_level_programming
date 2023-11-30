#!/usr/bin/python3

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in text:
        if char not in ['.', '?', ':']:
            print(char, end="")
        else:
            print("\n\n", end="")
    print()
