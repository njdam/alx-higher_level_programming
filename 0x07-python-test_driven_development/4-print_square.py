#!/usr/bin/python3
"""A file for function to print a square by # with area of size square"""


def print_square(size):
    """A function to print a square with area of size square

    Parameter:
        size (int): is size length of a square and must be an integer

    Raises:
        TypeError: if size is a float number or if is not an integer
        ValueError: if size is integer but is less than 0.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for y in range(size):
        for x in range(size):
            print("#", end="")
        print("")
