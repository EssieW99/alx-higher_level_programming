#!/usr/bin/python3
# 9-max_integer.py
def max_integer(my_list=[]):
    if len(my_list) == "":
        return None
    max_number = my_list[0]
    for index in range(len(my_list)):
        if my_list[index] > max_number:
            max_number = my_list[index]

    return max_number
