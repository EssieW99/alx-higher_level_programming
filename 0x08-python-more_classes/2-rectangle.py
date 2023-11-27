#!/usr/bin/python3
"""defines a class"""


class Rectangle:
    """a class on a rectangle"""

    def __init__(self, width=0, height=0):
        """initializes a new instance of the class

        Args:
        width: the width of the rectangle
        height: the rectangle's height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """the getter method for the width property"""
        return self.__width

    @width.setter
    def width(self, value):
        """the setter method for the width property"""
        if is not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """the getter method for the height property"""
        return self.__height

    @width.setter
    def height(self, width=0, height=0):
        """the setter method for the height property"""
        if is not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the rectangle's area"""
        return self.width * self.height

    def perimeter(self):
        """returns the rectangele perimeter"""
        return ((self.width * 2) + (self.height * 2))
