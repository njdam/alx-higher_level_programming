#!/usr/bin/python3
"""A file defines a function of 2 matrices multiplication."""


def matrix_mul(m_a, m_b):
    """A function to multiply two matrices

    Args:
        m_a (matrix): is first matrix it's elements must be int/float.
        m_b (matrix): The second matrix it's elements must be int/float.

    Raise:
        TypeError: If either m_a or m_b is not list of lists of int/float
        TypeError: If is empty for either m_a or m_b
        TypeError: If has different size of rows for either m_a or m_b
        ValueError: If m_a and m_b can not be multiplied

    Return:
        new_matrix with result of multiplied matrices m_a and m_b.
    """

    # If matrix is empty
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")

    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    # If matrix is not a list
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # If matrix is not a list of lists
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")

    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # If matrix is not contain elements wich is either integer or float
    if not all((isinstance(num, int) or isinstance(num, float))
               for num in [column for row in m_a for column in row]):
        raise TypeError("m_a should contain only integers or floats")

    if not all((isinstance(num, int) or isinstance(num, float))
               for num in [column for row in m_b for column in row]):
        raise TypeError("m_b should contain only integers or floats")

    # If matrix contain unequally rows
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must should be of the same size")

    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must should be of the same size")

    # if matrix can not be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    buffer_b = []  # Inverting buffer
    for yb in range(len(m_b[0])):
        new_row = []
        for xb in range(len(m_b)):
            new_row.append(m_b[xb][yb])
        buffer_b.append(new_row)

    new_matrix = []
    for row in m_a:
        new_row = []
        for column in buffer_b:
            result = 0
            for x in range(len(buffer_b[0])):
                result += row[x] * column[x]
            new_row.append(result)
        new_matrix.append(new_row)

    return new_matrix
