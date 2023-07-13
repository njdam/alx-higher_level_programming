#!/usr/bin/python3
"""A file that defines a function to write a text in file."""


def write_file(filename="", text=""):
    """A function to write a text in filename file

    Args:
        filename (file): is a file where to write a text.
        text (str): is a text to be written in file.
    """

    try:
        with open(filename, mode="w", encoding="utf-8") as Myfile:
            lens = Myfile.write(text)
            return (lens)

    except IOError:
        return (0)
