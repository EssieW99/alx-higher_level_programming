#!/usr/bin/python3
# 0-square_matrix_simple.py
def square_matrix_simple(matrix=[]):
    rows = len(matrix)
    columns = len(matrix[0])
    new = matrix.copy()
    for i in range(rows):
        new[i] = list(map(lambda x: x**2, matrix[i]))
    return new
