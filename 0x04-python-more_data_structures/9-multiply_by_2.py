#!/usr/bin/python3
# 9-multiply_by_2.py
def multiply_by_2(a_dictionary):
    cpy_dic = a_dictionary.copy()
    list_kys = list(cpy_dic.keys())
    for key in list_kys:
        cpy_dic[key] *= 2
    return cpy_dic
