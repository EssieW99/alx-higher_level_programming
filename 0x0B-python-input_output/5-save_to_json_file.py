#!/usr/bin/python3
"""defines a serialization to a text file function"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file using a JSON representation.

    Args:
    my_obj: the object
    filename: the text file
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
