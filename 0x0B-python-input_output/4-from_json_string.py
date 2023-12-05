#!/usr/bin/python3
"""4-from_json_string module"""
import json


def from_json_string(my_str):
    """returns an object represented
    by a JSON string"""
    data = json.loads(my_str)
    return data
