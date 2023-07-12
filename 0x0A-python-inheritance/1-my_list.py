#!/usr/bin/python3
"""A file with a class MyList that inherits from list."""


class MyList(list):
    """A class MyList that inherits from list"""

    def print_sorted(self):
        """A function to print sorted element of a list"""

        print(sorted(self))
