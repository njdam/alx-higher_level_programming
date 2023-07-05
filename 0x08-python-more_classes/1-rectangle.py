#!/usr/bin/python3
"""A file containing a class `Rectangle` which defines rectangle."""


class Rectangle:
    """A class Rectangle to define a rectangle."""

    def __init__(self, width=0, height=0):
        """A function to initialize width and height of a rectangle.

        Arg:
            width (int): is a width of rectangle must be an integer.
            height (int): is a height of rectangle must be an integer.
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """A function to retrieve a value of width."""
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """A function to retrieve a value of height."""
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
