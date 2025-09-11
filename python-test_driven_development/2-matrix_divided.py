#!/usr/bin/python3
"""
Module that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.
    Args:
        matrix: A list of lists of integers or floats.
        div: A number (integer or float).
    Returns:
        A new matrix with elements divided by div, rounded to 2 decimals.
    Raises:
        TypeError: If matrix is not a list of lists
                   of numbers, or if div is not a number,
                   or if rows of the matrix are of inconsistent size,
                   or if the matrix (or any row) is empty.
        ZeroDivisionError: If div is zero.
    """

    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")
    if len(matrix) == 0 or any(len(row) == 0 for row in matrix):
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")
    for row in matrix:
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
