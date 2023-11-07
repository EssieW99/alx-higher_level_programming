#!/usr/bin/python3
"""defines a Student class"""


class Student:
    """A student class"""
    def __init__(self, first_name, last_name, age):
        """I nitialises a new instance.

        Args:
        first_name (str): first name of the student
        last_name (str): last name of the student
        age (int): age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if attrs and isinstance(attrs, list):
            return {k: geattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
