#!/usr/bin/python3
"""A function to return True or False"""


def is_same_class(obj, a_class):
    """A function to return True if object is exactly
    an instance of specified class otherwise False.

    Args:
        obj (PyObject): is an instance attribute for specified class
        a_class (class): is a specified class.
    """

    if type(obj) == a_class:
        return (True)

    return (False)
