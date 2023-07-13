#!/usr/bin/python3
"""A file to define a function to return JSON representation of an obj"""

import json


def to_json_string(my_obj):
    """A function to return JSON representation of an object.

    Args:
        my_obj (str): is a Python object of a string.
    """

    return (json.dumps(my_obj))
