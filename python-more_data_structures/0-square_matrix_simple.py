#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    new_matrix = []
    sqrt_row = []

    for row in matrix:
        sqrt_row = []
        for element in row:
            result = element**2
            sqrt_row.append(result)
        new_matrix.append(sqrt_row)

    return new_matrix
