#!/usr/bin/python3
"""defines a class"""


class BaseGeometry:
    """a class on a base geometry"""
    def area(self):
        """raises an exception when called"""
        raise Exception("area() is not implemented")
