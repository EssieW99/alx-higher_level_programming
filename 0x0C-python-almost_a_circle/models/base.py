#!/usr/bin/python3
"""defines a class"""
import json


class Base:
    """ a class on a base

    Private class Attribute:
    __nb__objects: number of instances created of the class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """creates a new instance

        Args:
        id(int): the id of the class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """that writes the JSON string representation of
        list_objs to a file
        """
        filename = f"{cls.__name__}.json"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            list_dicts = [obj.to_dictionary() for obj in list_objs]
            file.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation
        json_string
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)