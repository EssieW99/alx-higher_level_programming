#!/usr/bin/python3
"""defines a class"""


class Rectangle:
    """a class on a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes a new instance of the class

        Args:
        width: the width of the rectangle
        height: the rectangle's height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieves the property of the width"""
        return self.width

    @width.setter
    def width(self, value):
        """setter method for the width property"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.width = value

    @property
    def height(self):
        """retrieves the property of the height"""
        return self.height

    @height.setter
    def height(self, value):
        """setter method for the height property"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.height = value
