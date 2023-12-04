#!/usr/bin/python3
"""0-lookup module"""


def lookup(obj):
    """returns the list of available attributes
    and methods of an object"""
    attr_meth = dir(obj)
    filtered_list = [name for name in attr_meth]
    return filtered_list
