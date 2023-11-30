#!/usr/bin/python3
"""4-print_square module"""


def print_square(size):
    """function that prints a square
    with the character #

    Args:
    size(int): determines the size of the square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for _ in range(size):
        print("#" * size)
