#!/usr/bin/python3
"""A file defines a function that add new attribute to an object."""


def add_attribute(obj, attrib, value):
    """A function to add a new attribute to an object if possible

    Args:
        obj (any): is the Python object to add an attribut to it
        attrib (str): is the name of attribute to be added to obj
        value (any): the value of new attribute added.
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")  # If can not add attrib

    setattr(obj, attrib, value)  # Successful attrib is added to obj
