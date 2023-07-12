#!/usr/bin/python3
"""A function to return True or False"""


def inherits_from(obj, a_class):
    """A function to return True if object is an instance of a class
    that inherited (directly/indirect) from specified class otherwise False.

    Args:
        obj (PyObject): is an instance attribute for specified class
        a_class (class): is a specified class.
    """

    return (issubclass(type(obj), a_class) and type(obj) != a_class)
