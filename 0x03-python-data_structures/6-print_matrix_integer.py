#!/usr/bin/python3
# 6-print_matrix_integer.py
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in row:
            print("{:d}".format(i), end=" ")
        print()
