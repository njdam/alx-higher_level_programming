#!/usr/bin/python3
# A function to compute a square value of all integers of a matrix.


def square_matrix_simple(matrix=[]):
    def sqr(x):  # This func can be replaced by lambda x: x**2
        return (x**2)

    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append(list(map(sqr, matrix[i])))
        """map send iteratable (x) elements of i in matrix to sqr function
        to return results and listed in new matrix."""

    return (new_matrix)
