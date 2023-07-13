#!/usr/bin/python3
"""A file that define a function to create an Object from a JSON file."""

import json


def load_from_json_file(filename):
    """A function to create an Object from a JSON file

    Args:
        filename (json file): is a json file to be used.
    """

    with open(filename) as myfile:
        return (json.load(myfile))
