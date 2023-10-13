#!/usr/bin/python3
# 0-square_matrix_simple.py
def square_matrix_simple(matrix=[]):
    for row in matrix:
        for i in row:
            i = i**2
            print("{:d}".format(i), end=" ")
