#!/usr/bin/python3
"""defines a text reading function"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it out"""
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
