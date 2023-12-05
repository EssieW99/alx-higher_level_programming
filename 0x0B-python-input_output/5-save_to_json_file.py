#!/usr/bin/python3
"""5-save_to_json_file module"""
import json


def save_to_json_file(my_obj, filename):
    """writes an object to a txt file
    using a JSON representation"""
    data = json.dumps(my_obj, indent=2) 
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(data)
