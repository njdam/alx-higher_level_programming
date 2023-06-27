#!/usr/bin/python3
"""A class Square to define a square with private size and raise Error"""


class Square:
    """Define a square"""

    def __init__(self, size=0):
        """
        If size is not an integer to raise TypeError with a message;
        If is Less than Zero to raise ValueError with a message;

        Args:
            size (int): is size of new square must be an integer not < 0.
        """
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """A puplic instance methode to return current square area"""
        return (self.__size ** 2)
