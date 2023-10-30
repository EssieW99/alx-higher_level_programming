#!/usr/bin/python3
"""A class that defines a square."""


class Square:
    def __init__(self, size=0):
        """Initialise a Square instance with a particular size."""

        self.__size = size

    @property
    def size(self):
        """Retrive the size of the Square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the Square with value and type validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of a square of a given size."""
        return self.__size * self.__size
