#!/usr/bin/python3
"""A file to define a Python class to JSON function to return a dict."""


def class_to_json(obj):
    """A function to return dictionary representation of simple data strc.
    """

    return (obj.__dict__)
