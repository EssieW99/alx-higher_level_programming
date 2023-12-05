#!/usr/bin/python3
"""defines a class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a subclass of BaseGeometry"""

    def __init__(self, width, height):
        """initialises a new instance of the class

        Args:
        width(int): width of the rectangle
        height(int): height of the rectangle
        """
        self.integer_validator("width", width)
        self.__weight = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns the area of the rectangle"""
        return width * height

    def ___str__(self):
        """returns a string representation of the rectangle"""
        return ("[Rectangle]: {}/{}".format(width, height))
