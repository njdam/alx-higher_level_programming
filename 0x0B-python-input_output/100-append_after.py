#!/usr/bin/python3
"""A function to insert a line of text to a file."""


def append_after(filename="", search_string="", new_string=""):
    """A function to insert a line of text to a file.

    Args:
        filename (str): is a file where to insert a text.
        search_string (str): is a string to search for within the file.
        new_string (str): is a string to be inserted.
    """

    text = ""
    with open(filename) as myfile:
        for line in myfile:
            text += line
            if search_string in line:
                text += new_string

    with open(filename, mode="w") as my_file:
        my_file.write(text)
