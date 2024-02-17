#!/usr/bin/python3
"""Module for Base class"""


import json
import csv
import turtle


class Base:
    """Class that defines a base object"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a new Base object"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                f.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes set"""
        if dictionary is None or dictionary == {}:
            return None
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        if cls.__name__ == "Square":
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as f:
                list_dicts = Base.from_json_string(f.read())
                return [cls.create(**d) for d in list_dicts]
        except:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes the CSV string representation of list_objs to a file"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("")
            else:
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                if cls.__name__ == "Square":
                    fields = ["id", "size", "x", "y"]
                writer = csv.DictWriter(f, fieldnames=fields)
                writer.writeheader()
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Returns a list of instances"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r") as f:
                reader = csv.DictReader(f)
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                if cls.__name__ == "Square":
                    fields = ["id", "size", "x", "y"]
                return [
                    cls.create(**{k: int(v) for k, v in d.items()})
                    for d in reader
                ]
        except:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws rectangles and squares using the turtle module"""
        t = turtle.Turtle()
        t.screen.bgcolor("white")
        t.screen.title("Rectangles and Squares")
        t.shape("turtle")
        t.color("black")
        t.speed(0)
        for r in list_rectangles:
            t.penup()
            t.setpos(r.x, r.y)
            t.pendown()
            t.forward(r.width)
            t.left(90)
            t.forward(r.height)
            t.left(90)
            t.forward(r.width)
            t.left(90)
            t.forward(r.height)
            t.left(90)
        for s in list_squares:
            t.penup()
            t.setpos(s.x, s.y)
            t.pendown()
            t.forward(s.size)
            t.left(90)
            t.forward(s.size)
            t.left(90)
            t.forward(s.size)
            t.left(90)
            t.forward(s.size)
            t.left(90)
        t.hideturtle()
        turtle.done()
