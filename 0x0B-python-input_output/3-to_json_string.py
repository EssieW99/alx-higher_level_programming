#!/usr/bin/python3
import json
"""3-to_json_string module"""


def to_json_string(my_obj):
    """returns JSON representation of an object

    Args:
    my_obj: the object to be converted to a JSON rep

    Returns:
    A JSON representation
    """
    data = json.dumps(my_obj)
    return data
