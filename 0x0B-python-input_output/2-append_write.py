#!/usr/bin/python3
"""A file that defines a function to write a text in file."""


def append_write(filename="", text=""):
    """A function to write a text in filename file

    Args:
        filename (file): is a file where to write a text.
        text (str): is a text to be written in file.
    """

    with open(filename, mode="a", encoding="utf-8") as Myfile:
        lens = Myfile.write(text)
        return (lens)
