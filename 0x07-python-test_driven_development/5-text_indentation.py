#!/usr/bin/python3
""" 5-text_indentation module"""


def text_indentation(text):
    """function that prints a text with 2 new lines after
    . ? : delimeters

    Args:
    text(str): the string that will be used
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in text:
        if char not in ['.', '?', ':']:
            print(char, end="")
        else:
            print("\n\n", end="")
    print()
