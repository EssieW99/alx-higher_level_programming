#!/usr/bin/python3
"""defines a rectangle."""


class Rectangle:
    """A rectangle class."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialise an instance of the rectangle."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Returns the width of the height."""
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
        """Returns the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets and validates the value of the height."""
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
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """print rectangle with the character(s) stored in print_symbol."""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = ""
        for _ in range(self.__height):
            rect += (str(self.print_symbol) * self.__width) + '\n'
        return rect[:-1]

    def __repr__(self):
        """returns a string rep. to recreate a new instance."""
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """Handle instance deletion."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
