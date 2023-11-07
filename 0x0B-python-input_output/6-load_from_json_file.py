#!/usr/bin/python3
"""defines a deserialization function"""
import json


def load_from_json_file(filename):
    """ creates an Object from a “JSON file”"""
    with open(filename, 'r') as file:
        x = json.load(file)
        return x
