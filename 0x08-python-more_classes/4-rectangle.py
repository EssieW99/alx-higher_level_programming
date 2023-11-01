#!/usr/bin/python3
"""defines a rectangle."""


class Rectangle:
    """A class on a rectangle."""
    def __init__(self, width=0, height=0):
        """Initialise the instance."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves and returns the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the value of the width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the value of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the rectangle perimeter."""
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = ""
        for _ in range(self.__height):
            rect += ('#' * self.__width) + '\n'
        return rect[:-1]

    def __repr__(self):
        """return a string representation of the rectangle."""
        return ("Rectangle({}, {})".format(self.__width, self.__height))