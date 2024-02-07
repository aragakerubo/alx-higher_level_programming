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

    def to_json(self):
        """Returns the dictionary description of the object

        Returns:
            dict: The dictionary description of the object"""
        return self.__dict__
