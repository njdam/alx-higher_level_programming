#!/usr/bin/python3
"""A class Square to define a square with private size and raise Error"""


class Square:
    """Define a square"""

    def __init__(self, size=0):
        """
        Initialisation of new square size;

        Args:
            size (int): is size of new square must be an integer not < 0.
        """
        self.size = size

    @property
    def size(self):
        """Getting current value of size of a square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        If size is not an integer to raise TypeError with a message;
        If is Less than Zero to raise ValueError with a message;
        setting current value to size of a square;

        Args:
            value (int): is size of new square must be an integer not < 0.
        """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """A puplic instance methode to return current square area"""
        return (self.__size ** 2)

    def my_print(self):
        """A function to print # area of square"""
        if self.__size == 0:
            print("")
        else:
            for y in range(self.__size):
                for x in range(self.__size):
                    print("{}".format("#"), end="")
                print("")
