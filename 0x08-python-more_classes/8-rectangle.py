#!/usr/bin/python3
"""defines a rectangle."""


class Rectangle:
    """A rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialise an instance."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """returns the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets and validates the value of the width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """returns the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets and validates the value of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """returns the area of a rectangle"""
        return self.__width * self.__height

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """print the rectangle with the character #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = ""
        for _ in range(self.__height):
            rect += (str(self.print_symbol) * self.__width) + '\n'
        return rect[:-1]

    def __repr__(self):
        """return a string representation to recreate a new instance"""
        return ("Rectange({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """Handles deletion of an instance"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
