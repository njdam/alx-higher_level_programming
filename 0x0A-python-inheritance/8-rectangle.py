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
        self.integer_validator("Width", width)
        self.__width = width

        self.integer_validator("Height", height)
        self.__height = height
