#!/usr/bin/python3
"""0-read_file module"""


def read_file(filename=""):
    """reads a txt file and prints it to stdout"""
    with open(filename, 'r', encoding="utf-8") as file:
        for line in file:
            print(line, end='')
