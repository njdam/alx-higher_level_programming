#!/usr/bin/python3
"""This file bear a class Base which will be a base of all other classes."""

import json
import csv
import turtle


class Base:
    """A class Base which is a base of all other classes in this project."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialisation of class Base

        Args:
            id (int): is Base class id which is an integer.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """A function to return JSON string representation of dictionary."""

        if list_dictionaries is None or not list_dictionaries:
            return ("[]")

        return (json.dumps(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """A function to return a JSON string."""
        if json_string is None or not json_string:
            return ([])

        return (json.loads(json_string))

    @classmethod
    def save_to_file(cls, list_objs):
        """A function to save JSON string represantation to a file."""
        filename = f"{cls.__name__}.json"
        data = [obj.to_dictionary() for obj in list_objs] if list_objs else []
        json_str = cls.to_json_string(data)
        with open(filename, mode='w') as file:
            file.write(json_str)

    @classmethod
    def create(cls, **dictionary):
        """A function `create(**dict)` to return an instance with all
        attributes already set.
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)

        elif cls.__name__ == "Square":
            dummy_instance = cls(1)

        else:
            raise ValueError(f"Unsupported class: {cls.__name__}")

        dummy_instance.update(**dictionary)  # Updating by **kwargs method

        return (dummy_instance)

    @classmethod
    def load_from_file(cls):
        """A function `load_from_file` to return a list of instances."""
        filename = f"{cls.__name__}.json"

        try:
            with open(filename, mode='r') as file:
                data = cls.from_json_string(file.read())
                return ([cls.create(**dic) for dic in data])

        except FileNotFoundError:
            return ([])

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """A func to write CSV serialization of a list of objs to a file."""
        filename = f"{cls.__name__}.csv"
        with open(filename, "w", newline="") as csv_file:

            if list_objs is None or list_objs == []:
                csv_file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                the_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                for obj in list_objs:
                    the_writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """A function `load_from_file_csv` to return a list of instances."""
        filename = f"{cls.__name__}.csv"

        try:
            with open(filename, "r", newline="") as csv_file:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csv_file, fieldnames=fieldnames)
                list_dicts = [dict([y, int(x)] for y, x in dicts.items())
                              for dicts in list_dicts]
                return ([cls.create(**dicts) for dicts in list_dicts])
        except IOError:
            return ([])

    @staticmethod
    def draw(list_rectangles, list_squares):
        """A function to draw Rectangles and Squares using turtle module."""
        tur = turtle.Turtle()
        tur.screen.bgcolor("#b7312c")
        tur.pensize(3)
        tur.shape("turtle")

        tur.color("#ffffff")
        for r in list_rectangles:
            tur.showturtle()
            tur.up()
            tur.goto(r.x, r.y)
            tur.down()

            for i in range(2):
                tur.forward(rec.width)
                tur.left(90)
                tur.forward(rec.height)
                tur.left(90)
            tur.hideturtle()

        tur.color("#b5e3d8")
        for s in list_squares:
            tur.showturtle()
            tur.up()
            tur.goto(s.x, s.y)
            tur.down()

            for i in range(2):
                tur.forward(s.width)
                tur.left(90)
                tur.forward(s.height)
                tur.left(90)
            tur.hideturtle()

        turtle.exitonclick()
