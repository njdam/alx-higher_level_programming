#!/usr/bin/python3
"""This file bear a class Base which will be a base of all other classes."""

import json


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
