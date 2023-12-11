#!/usr/bin/python3
"""defines a class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """represents a class of a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """initialises a new instance of the class

        Args:
        size(int): the size of the square
        x(int): the square's x coordinates
        y(int): the square's y coordinates
        id(int): the square's id
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """the getter method for the size property"""
        return self.width

    @size.setter
    def size(self, value):
        """the setter method for the size property"""
        self.width = value
        self.height = value

    def __str__(self):
        """returns a representation of the square"""
        return ("[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """assignes attributes

        Args:
        args(int): non-keyworded variables
        first attribute - id
        second attribute - size
        third attribute - x
        fourth attribute - y

        kwargs(dict): key-worded variables
        """
        if args:
            if args[0] is None:
                self.__init__(self.size, self.x, self.y)
            else:
                if len(args) >= 1:
                    self.id = args[0]
                if len(args) >= 2:
                    self.size = args[1]
                if len(args) >= 3:
                    self.x = args[2]
                if len(args) >= 4:
                    self.y = args[3]

        if kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns  the dictionary representation of a Square"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
