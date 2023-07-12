#!/usr/bin/python3
"""A function to return True or False"""


def is_kind_of_class(obj, a_class):
    """A function to return True if object is an instance of or if the
    object is an instance of a class that inherited from otherwise False.

    Args:
        obj (PyObject): is an instance attribute for specified class
        a_class (class): is a specified class.
    """

    return (isinstance(obj, a_class))
