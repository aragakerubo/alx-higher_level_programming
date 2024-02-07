#!/usr/bin/python3
"""Module for student"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Instantiation of a student

        Args:
            first_name (str): The first name of the student
            last_name (str): The last name of the student
            age (int): The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns the dictionary description of the object

        Args:
            attrs (list): A list of attributes to return

        Returns:
            dict: The dictionary description of the object"""
        if attrs is None:
            return self.__dict__
        else:
            return {
                key: value
                for key, value in self.__dict__.items()
                if key in attrs
            }

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance

        Args:
            json (dict): The dictionary of attributes to replace
        """
        for key, value in json.items():
            setattr(self, key, value)
