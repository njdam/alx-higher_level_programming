#!/usr/bin/python3
"""A class Square to define a square with private size and raise Error"""


class Square:
    """Define a square"""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialisation of new square size and position of a square

        Args:
            size (int): is size of new square must be an integer not < 0.
            position (int, int): is posistion of a new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getting current value of size of a square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        If size is not an integer to raise TypeError with a message
        If is Less than Zero to raise ValueError with a message
        Setting current value to size of a square

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

    @property
    def position(self):
        """Getting current values of position of a square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """
        If value is not a tuple of two int to raise TypeError with message
        Setting current value to a position of a square

        Args:
            value (int, int): a position of a square must be tuple of 2 int.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """A puplic instance method to return current square area"""
        return (self.__size ** 2)

    def my_print(self):
        """A function to print # area of square at position"""
        if self.__size == 0:
            print("")
            return

        [print("") for y in range(self.__position[1])]
        for y in range(self.__size):
            [print(" ", end="") for space in range(self.__position[0])]
            [print("#", end="") for x in range(self.__size)]

            print("")
