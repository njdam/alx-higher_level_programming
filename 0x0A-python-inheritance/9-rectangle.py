#!/usr/bin/python3
"""A file with a Rectangle class inherited from class BaseGeometry."""

# Importing BaseGeometry class from 7-base_geometry.py file
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class called Rectangle inherited from class BaseGeometry."""

    def __init__(self, width, height):
        """Initialization of Rectangle Class, args have to be validated

        Args:
            width (int): is a width of a rectangle must be an integer.
            height (int): is a height a rectangle must be an integer.
        """
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height

    def __str__(self):
        return (dict_self.__width/self.__height)

    def area(self):
        """Return area of a rectangle."""
        return (self.__width * self.__height)

    def __str__(self):
        """A function to return a description of Rectangle class."""
        description = "[" + str(self.__class__.__name__) + "]"
        description += " " + str(self.__width) + "/" + str(self.__height)

        return (description)
