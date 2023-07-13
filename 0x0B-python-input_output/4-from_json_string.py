#!/usr/bin/python3
"""A file to define a function to return JSON representation of an obj"""

import json


def from_json_string(my_str):
    """A function to return Python Object representation of JSON string.

    Args:
        my_str (str): is a string to be return in PyObj repres. of JSON str.
    """

    return (json.loads(my_str))
