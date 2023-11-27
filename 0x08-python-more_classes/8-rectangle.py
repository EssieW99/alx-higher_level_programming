#!/usr/bin/python3
"""defines a class"""


class Rectangle:
    """a class on a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initialises a new instance of a class

        Args:
        width(int): the rectangle's width
        height(int): the rectangle's height
        """
        self.width = width
        sellf.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter method for the width property"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter method for the width property"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter method for the height property"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter method for the height property"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """returns the area of the rectangle"""
        return self.width * self.height

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
        if self.width == 0 or self.height == 0:
            return 0
        return ((self.width * 2) + (self.height * 2))

    def __str__(self):
        """returns a string representation of the rectangle"""
        if self.width == 0 or self.height == 0:
            return ""
        rect_str = ""
        for _ in range(self.height):
            rect_str += (str(self.print_symbol) * self.width + '\n')
        return rect_str.rstrip()

    def __repr__(self):
        """returns a string representation
        of the rectangle for eval()"""
        return ("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        """prints a message when an instance is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
