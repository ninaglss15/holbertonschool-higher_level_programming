#!/usr/bin/python3

def pascal_triangle(n):
    if n <= 0:
        return []
    triangle = []
    for i in range(n):
        row = [1]
        if triangle:
            last_row = triangle[-1]
            row += [last_row[j] + last_row[j+1] for j in range(len(last_row)-1)]
            row += [1]
        triangle.append(row)
    return triangle
