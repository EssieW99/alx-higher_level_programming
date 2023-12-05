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
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
