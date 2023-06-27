#!/usr/bin/python3
"""A class Square to define a square by private instace attribute size."""


class Square:
    """Define a square"""

    def __init__(self, size):
        """
        For Initializing a new_square.

        Args:
        size (int): is the size of new_square to be initialised with.
        """
        self.__size = size
