#!/usr/bin/python3
"""defines a class to JSON function"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure
     for JSON serialization of an object
     """
    return obj.__dict__
