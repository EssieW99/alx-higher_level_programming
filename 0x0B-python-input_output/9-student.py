#!/usr/bin/python3
"""defines a Student class"""


class Student:
    """a Student class"""
    def __init__(self, first_name, last_name, age):
        """Initialises a new instance

        Args:
        first_name (str): the first name of the student
        last_name (str): last name
        age (int): the age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student instance"""
        return self.__dict__
