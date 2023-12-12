#!/usr/bin/python3
"""defines a subclass"""
from models.base import Base


class Rectangle(Base):
    """a subclass of class Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialises a new instance of the class

        Args:
        width(int): the width of the rectangle
        height(int): the rectangle's height
        x(int): the rectangle's x coordinates
        y(int): the rectangle's y coordinates
        id(int): the rectangle's id
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter method for the width property"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter method for the height property"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter method for the height property"""
        return self.__height

    @height.setter
    def height(self, value):
        """getter method for the height property"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter method for the x property"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter method for the x property"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter method for the y property"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter method for the y property"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area value of the Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """that prints in stdout the Rectangle instance
        with the character #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = ""
        for a in range(self.__y):
            print()
        for _ in range(self.__height):
            rect += ((" " * self.__x + "#" * self.__width) + '\n')
        rect.rstrip()
        print(rect, end="")

    def __str__(self):
        """returns a string representation of the rectangle"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id,
            self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """updates the attributes of the rectangle

        Args:
        args(int): non-keyworded arguments
            first argument - id
            second argument - width
            third argument - height
            fourth argument - x
            fifth argument - y
        kwargs(dict): keyworded arguments
        """
        if args:
            if args[0] is None:
                self.__init__(self.__width, self.__height, self.__x, self.__y)
            else:
                if len(args) >= 1:
                    self.id = args[0]
                if len(args) >= 2:
                    self.__width = args[1]
                if len(args) >= 3:
                    self.__height = args[2]
                if len(args) >= 4:
                    self.__x = args[3]
                if len(args) >= 5:
                    self.__y = args[4]

        if kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {
            "id": self.id,
            "width": self.__width,
            "height": self.__height,
            "x": self.__x,
            "y": self.__y
        }
