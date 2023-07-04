#!/usr/bin/python3
"""A file with a function to find max integer in a list."""


def max_integer(list=[]):
    """A function to search and return a maximum integer
    if a list is empty return None

    Parameter:
        list (int): is list of integers and if is None return None.
    """

    if len(list) == 0:
        return (None)

    maximum = list[0]
    for i in range(1, len(list)):
        if list[i] > maximum:
            maximum = list[i]

    return (maximum)
