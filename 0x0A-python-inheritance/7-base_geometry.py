#!/usr/bin/python3
"""defines a class"""


class BaseGeometry:
    """a class on a base geometry"""

    def area(self):
        """raises an exception when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates the value

        Args:
        name(str): name with the associated value
        value(int): the value being validated
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
