#!/usr/bin/python3
"""A file bearing a class Rectangle which inherited from Base."""

from models.base import Base
import sys


class Rectangle(Base):
    """A Rectangle class which inherited from Base class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialisation of Rectangle class with #nt args

        Args:
            width (int): is width of rectangle must be an integer
            height (int): is height of rectangle must be an integer
            x (int): is value of x must be an int
            y (int): is value of y must be an int
            id (int): is value of id must not be a None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # Getting and Setting value of width
    @property
    def width(self):
        """Retrieving a value of width."""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Setting width to a value."""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    # Getting and Setting value of height
    @property
    def height(self):
        """Retrieving a value of height."""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Setting height to a value."""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    # Getting and Setting value of x
    @property
    def x(self):
        """Retrieving a value of x."""
        return (self.__x)

    @x.setter
    def x(self, value):
        """Setting x to a value."""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    # Getting and Setting value of y
    @property
    def y(self):
        """Retrieving a value of y."""
        return (self.__y)

    @y.setter
    def y(self, value):
        """Setting y to a value."""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """A function to return area of a rectangle."""
        return (self.__width * self.__height)

    def display(self):
        """A function to print area of rectangle by # display."""
        for y in range(self.__y):
            print("")  # to print new line before printing rectangle

        for h in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")  # to print spaces before hashes
            for w in range(self.__width):
                print("#", end="")

            print("")  # to print new line after printing width

    def update(self, *args, **kwargs):
        """A function to update rectangle args."""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
            """ Or this below
            for key in kwargs:
                if key == "id":
                    self.id = kwargs[key]
                if key == "width":
                    self.__width = kwargs[key]
                if key == "height":
                    self.__height = kwargs[key]
                if key == "x":
                    self.__x = kwargs[key]
                if key == "y":
                    self.__y = kwargs[key]
            """

    def __str__(self):
        """A function for returning string representation of rectangle."""
        string = "[" + str(getattr(Rectangle, '__name__')) + "]"
        string += " " + str(f"({self.id}) {self.__x}/{self.__y}")
        string += " " + str(f"- {self.__width}/{self.__height}")

        return (string)
