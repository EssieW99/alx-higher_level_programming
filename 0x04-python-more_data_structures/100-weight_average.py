#!/usr/bin/python3
# 100-weight_average.py
def weight_average(my_list=[]):
    total = 0
    total_weight = 0
    if not my_list:
        return 0
    for score, weight in my_list:
        total += score * weight
        total_weight += weight
    weighted_average = total / total_weight
    return weighted_average
