#!/usr/bin/python3
"""making pascal's triangle"""


def pascal_triangle(n):
    """
    a function that returns a list
    of integers that represents pascal's triangle
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        if (i == 0):
            triangle.append([1])
        else:
            current = []
            for j in range(i + 1):
                if (j == 0 or j == i):
                    current.append(1)
                else:
                    current.append(triangle[i - 1][j - 1] +
                                   triangle[i - 1][j])

            triangle.append(current)

    return triangle
