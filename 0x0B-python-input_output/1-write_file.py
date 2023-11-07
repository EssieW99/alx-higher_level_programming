#!/usr/bin/python3
"""defines a file reading function"""


def write_file(filename="", text=""):
    """writes a string to a text file.

    Args:
    filenema: name of file
    text: string to be wriiten to the file

    Returns:
    No. of characters written.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
