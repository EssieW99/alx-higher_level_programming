#!/usr/bin/python3
"""defines a class"""


class Student:
    """a class on a student"""

    def __init__(self, first_name, last_name, age):
        """initialises a new instance of the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns a dictionary representation of a Student instance

        Args:
        attrs: a list of string only attribute names contained in this list
        must be obtained, otherwise all must be retrived

        Returns:
        a dictionary containing the selected attributes of the instance
        """
        if attrs is None:
            return self.__dict__
        selected_attr = {
                key: value
                for key, value in self.__dict__.items()
                if key in attrs
        }
        return selected_attr

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance

        Args:
        a dict where keys are attr names and values are
        attribute values
        """
        for key, value in json.items():
            setattr(self, key, value)
