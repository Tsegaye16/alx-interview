#!/usr/bin/python3
"""Making pascal's triangle"""

def pascal_triangle(n):
    """
    a function that dispalys a list of
    integer that represent triangle
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [i]
        if triangle:
            prev = triangle[-1]
            row.extend([prev[j] + prev[j + 1] for j in
                range(len(prev) - 1)])

        row.append(1)
        trinagle.append(row)

    return (triangle)
