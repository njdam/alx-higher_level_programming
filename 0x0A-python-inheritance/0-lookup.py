#!/usr/bin/python3
"""
A file function to return list of available attributes and methods
"""


def lookup(obj):
    """A function to return list of available attributes
    and methods of an object.

    Args:
        obj (PyObject): is a Python Object.
    """

    return (dir(obj))
