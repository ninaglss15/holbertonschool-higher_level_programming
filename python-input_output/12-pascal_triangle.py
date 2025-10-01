#!/usr/bin/python3
"""
Module that contains a function to read a text file
"""


def pascal_triangle(n):
    """
    Return a list of lists representing Pascal's triangle of n rows.

    Args:
        n (int): The number of rows of the triangle.

    Returns:
        list: A list of lists, each inner list representing a row of the triangle.
        Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]
        if triangle:
            last_row = triangle[-1]
            row += [last_row[j] + last_row[j + 1] for j in range(len(last_row) - 1)]
            row += [1]
        triangle.append(row)

    return triangle
