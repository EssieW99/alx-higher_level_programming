#!/usr/bin/python3
# 6-print_sorted_dictionary.py
def print_sorted_dictionary(a_dictionary):
    print_dic = list(a_dictionary.keys())
    print_dic.sort()
    for i in print_dic:
        print("{}: {}".format(i, a_dictionary.get(i)))
