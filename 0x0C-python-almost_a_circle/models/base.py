#!/usr/bin/python3
"""Module for Base class"""


import json


class Base:
    """Class that defines a base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new Base.
        Args:
            id (int): id of the base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries
        Args:
            list_dictionaries (list): list of dictionaries
        Returns:
            str: JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file
        Args:
            list_objs (list): list of instances
        Returns:
            None
        """
        filename = cls.__name__ + ".json"
        list_dicts = []
        if list_objs is not None:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w") as file:
            file.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string
        Args:
            json_string (str): JSON string
        Returns:
            list: list of the JSON string representation json_string
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set
        Args:
            dictionary (dict): dictionary representation of an instance
        Returns:
            instance: instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        if cls.__name__ == "Square":
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances
        Returns:
            list: list of instances
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                list_dicts = cls.from_json_string(file.read())
            return [cls.create(**d) for d in list_dicts]
        except:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Writes the CSV string representation of list_objs to a file
        Args:
            list_objs (list): list of instances
        Returns:
            None
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w") as file:
            if list_objs is not None:
                file.write(
                    cls.to_json_string(
                        [obj.to_dictionary() for obj in list_objs]
                    )
                )
            else:
                file.write("[]")

    @classmethod
    def load_from_file_csv(cls):
        """
        Returns a list of instances
        Returns:
            list: list of instances
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r") as file:
                list_dicts = cls.from_json_string(file.read())
            return [cls.create(**d) for d in list_dicts]
        except:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draws the list of rectangles and squares
        Args:
            list_rectangles (list): list of Rectangle instances
            list_squares (list): list of Square instances
        Returns:
            None
        """
        import turtle
        import random

        turtle.title("Rectangles and Squares")
        turtle.bgcolor("white")
        turtle.setup(800, 600)
        turtle.speed(0)
        turtle.hideturtle()

        for rect in list_rectangles:
            turtle.penup()
            turtle.goto(rect.x, rect.y)
            turtle.pendown()
            turtle.color("black")
            turtle.begin_fill()
            for _ in range(2):
                turtle.forward(rect.width)
                turtle.left(90)
                turtle.forward(rect.height)
                turtle.left(90)
            turtle.end_fill()

        for square in list_squares:
            turtle.penup()
            turtle.goto(square.x, square.y)
            turtle.pendown()
            turtle.color("black")
            turtle.begin_fill()
            for _ in range(4):
                turtle.forward(square.size)
                turtle.left(90)
            turtle.end_fill()

        turtle.done()
