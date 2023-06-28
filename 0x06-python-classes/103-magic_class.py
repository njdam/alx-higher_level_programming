#!/usr/bin/python3
"""A Python MagicClass do the same as exactly a Python bytecode"""


class MagicClass:
    import math

    def __init__(self, radius=0):
        """
        For Initialization of MagicClass

        Args:
            radius (int or float): is a radius of a new MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """For returning current area of MagicClass."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """For returning current circumference of MagicClass."""
        return (2 * math.pi * self.__radius)