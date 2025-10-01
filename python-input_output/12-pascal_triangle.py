#!/usr/bin/python3

"""Module for generating Pascal's triangle."""


def pascal_triangle(n):
    """Generate Pascal's triangle up to n rows."""
    if n <= 0:
        return []
    triangle = []
    for row in range(n):
        if row == 0:
            triangle.append([1])
        else:
            prev = triangle[-1]
            next = [1]
            for i in range(1, row):
                next.append(prev[i - 1] + prev[i])
            next.append(1)
            triangle.append(next)
    return triangle
