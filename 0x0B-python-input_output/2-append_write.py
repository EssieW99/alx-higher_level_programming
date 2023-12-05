#!/usr/bin/python3
"""2-append_write module"""


def append_write(filename="", text=""):
    """appends a string and returns no of
    characters

    Args:
    filename: the file that will be appended
    text: the text to be added to the file

    Returns:
    No of characters
    """
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text)
    return len(text)
