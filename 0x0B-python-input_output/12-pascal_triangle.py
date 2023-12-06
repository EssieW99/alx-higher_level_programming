#!/usr/bin/python3
"""defines a pascal's triangle function"""


def pascal_triangle(n):
    """
     returns a list of lists of integers
     representing the Pascal’s triangle of n
     """
    if n <= 0:
        return []

    triangle = []

    for a in range(n):
        row = [1] * (a + 1)
        if a >= 2:
            for b in range(1, a):
                row[b] = triangle[a - 1][b - 1] + triangle[a - 1][b]
        triangle.append(row)

    return (triangle)
