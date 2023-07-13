#!/usr/bin/python3
"""A file to define a function for Pascal's Triangle."""


def pascal_triangle(n):
    """A function to represent Pascal's Triangle of size n and
    returns a list of lists of integers representing a triangle.
    """

    if n <= 0:
        return []

    P_triangle = [[1]]
    while len(P_triangle) != n:
        P_tri = P_triangle[-1]
        tmp = [1]
        for x in range(len(P_tri) - 1):
            tmp.append(P_tri[x] + P_tri[x + 1])

        tmp.append(1)
        P_triangle.append(tmp)

    return (P_triangle)
