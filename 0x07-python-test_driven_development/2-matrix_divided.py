#!/usr/bin/python3
"""2-matrix_divided module"""


def matrix_divided(matrix, div):
    """divides the elements in a matrix by div

    Args:
    matrix: lists of lists containing int or float elements
    div: an int or float number

    Returns:
    A new matrix
    """
    message = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(message)
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(message)
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(message)
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    result = [[round(element / div, 2) for element in row] for row in matrix]
    return result
