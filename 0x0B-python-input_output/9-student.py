#!/usr/bin/python3
"""defines a class"""


class Student:
    """a class on a student"""

    def __init__(self, first_name, last_name, age):
        """initialises a new instance of the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns a dictionary representation of a Student instance"""
        return self.__obj__
