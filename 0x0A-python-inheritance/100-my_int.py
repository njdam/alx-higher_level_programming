#!/usr/bin/python3
"""A file with a class MyInt inherited from int class."""


class MyInt(int):
    """A class MyInt inherited from class int."""

    def __eq__(self, other):
        """Checks reverse of if is equal to other"""
        return (super().__ne__(other))  # Reverses the == operator

    def __ne__(self, other):
        """Checks reverse of if is not equal to other"""
        return (super().__eq__(other))  # Reverses the != operator
