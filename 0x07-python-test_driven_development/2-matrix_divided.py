#!/usr/bin/python3
"""A file 2-matrix_divided.py with matrix_divided function
to divide all elements of matrix by `div` number.
"""


def matrix_divided(matrix, div):
    """A function that returns new matrix with results
    Results is all elements of matrix divided by div number

    Paramenters:
        matrix (matrix): must be a list of a lists of numbers
        div (int): is second parameter and must be an integer
    """

    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix) or
            matrix == [] or not all(isinstance(num, int) or
                isinstance(num, float) for num in [column for row in matrix for column in row])):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    f = lambda x: round(x / div, 2)
    new_matrix = [list(map(f, row)) for row in matrix]

    return (new_matrix)
