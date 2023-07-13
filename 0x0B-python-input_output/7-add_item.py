#!/usr/bin/python3
"""A file that adds all arguments to a Python list and save them to a file.
"""

import sys


if __name__ == "__main__":
    """Importing save_to_json_file function from 5-save_to_json_file.py"""
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

    """Importing load_from_json_file func from 6-load_from_json_file.py"""
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        obj = load_from_json_file("add_item.json")

    except FileNotFoundError:
        obj = []

    obj.extend(sys.argv[1:])
    save_to_json_file(obj, "add_item.json")
