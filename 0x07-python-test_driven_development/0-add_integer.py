#!/usr/bin/python3
"""A function to add two integers."""


def add_integer(a, b=98):
    """A function that returns sum of a and b

    Args:
        a (int): is firt parameter must be an integer
        b (int): is second parameter must be an integer.
    """

    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")

    elif (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")

    else:
        return (int(a) + int(b))
