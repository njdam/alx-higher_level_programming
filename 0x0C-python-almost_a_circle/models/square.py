#!/usr/bin/python3
"""A file bearing class Square inherited from class Rectangle."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """A class Square inherits Rectangle to deal with a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialisation of Square class

        Args:
            size (int): is a size of square must be an integer
            x (int): is a cordinate at x-axis where square start
            y (int): is a cordinate at y-axis where square start
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getting value of a size."""
        return (self.width)

    @size.setter
    def size(self, value):
        """A function to set a value to size."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """A function that assigning all args in their corresponding var."""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]

        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """A function for returning string representation of rectangle."""
        string = "[" + str(getattr(Square, '__name__')) + "]"
        string += " " + str(f"({self.id}) {self.x}/{self.y}")
        string += " " + str(f"- {self.size}")

        return (string)
