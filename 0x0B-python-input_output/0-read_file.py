#!/usr/bin/python3
"""A function to read a text file (UTF8) and print it to stdout."""


def read_file(filename=""):
    """A function to read a text file (UTF8) and print it to stdout.

    Args:
        filename (file): is a file to be read.
    """

    with open(filename, mode="r", encoding="utf-8") as myFile:
        data = myFile.read()
        print(data, end="")
