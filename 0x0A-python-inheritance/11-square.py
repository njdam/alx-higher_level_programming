#!/usr/bin/python3
"""A file with a Square class inherited from class Rectangle."""

# Importing Rectangle class from 9-rectangle.py file
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class called Square inherited from class Rectangle."""

    def __init__(self, size):
        """Initialization of Square Class, size have to be validated

        Args:
            size (int): is a size of a square and must be an integer.
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        description = "[" + str(__class__.__name__) + "]"
        description += " " + str(self.__size) + "/" + str(self.__size)

        return (description)
