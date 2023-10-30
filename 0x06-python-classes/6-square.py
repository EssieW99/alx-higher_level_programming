#!/usr/bin/python3
"""Defines a square."""


class Square:
    """A class square."""
    def __init__(self, size=0, position=(0, 0)):
        """Initialise a square instance with a given size and position."""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Retrives the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square with the value and type validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def size(self):
        """Retrieves the position of the square."""
        return self.__position

    @size.setter
    def size(self, value):
        """Sets the position with the value and type validation."""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 integers")
        if not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the area of a square."""
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character #."""
        if self.__size != 0:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(' ' * self.__position[0] + '#' * self.__size)
