#!/usr/bin/python3
"""A file that defines a function to write a text in file using JSON repres."""

import json


def save_to_json_file(my_obj, filename):
    """A function to write a text in filename file using JSON representation

    Args:
        my_obj (str): is a text to be written in file using JSON represent.
        filename (file): is a file where to write a text file using JSON rp.
    """

    with open(filename, mode="w") as Myfile:
        Myfile.write(json.dumps(my_obj))
