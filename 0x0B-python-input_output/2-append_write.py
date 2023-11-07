#!/bin/usr/python3
"""defines a file appending function"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8)

    Args:
    filename: the text file
    text: the string to be appended to the file

    Returns:
    No. of characters appended
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
