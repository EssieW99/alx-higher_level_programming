#!/usr/bin/python3
"""defines a square."""


class Square:
    """This is a Square."""
    def __init__(self, size=0):
        """Initialise the Square instance with a given size."""
        self.__size = size

    @property
    def size(self):
        """Retrives the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size with type and value validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of a square of a given size."""
        return self.__size ** 2

    def my_print(self):
        """Prints in stdout the square with the character #."""
        if self.__size != 0:
            for _ in range(self.__size):
                print('#' * self.__size)
        else:
            print()
