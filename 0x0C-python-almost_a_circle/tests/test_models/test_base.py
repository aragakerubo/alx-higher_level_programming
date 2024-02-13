#!/usr/bin/python3
"""Module for tests for the Base class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json
import os


class TestBase(unittest.TestCase):
    """Tests for the Base class"""

    def test_no_id(self):
        """Test for no id"""
        b = Base()
        self.assertEqual(b.id, 1)

    def test_id(self):
        """Test for id"""
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_id_none(self):
        """Test for id as None"""
        b = Base(None)
        self.assertEqual(b.id, 2)

    def test_to_json_string(self):
        """Test for to_json_string method"""
        r = Rectangle(10, 7, 2, 8)
        d = r.to_dictionary()
        j = Base.to_json_string([d])
        self.assertEqual(json.loads(j), json.loads(json.dumps([d])))

    def test_to_json_string_empty(self):
        """Test for to_json_string method with empty list"""
        j = Base.to_json_string([])
        self.assertEqual(json.loads(j), json.loads("[]"))

    def test_to_json_string_none(self):
        """Test for to_json_string method with None"""
        j = Base.to_json_string(None)
        self.assertEqual(json.loads(j), json.loads("[]"))

    def test_save_to_file(self):
        """Test for save_to_file method"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(
                json.loads(file.read()),
                json.loads(
                    json.dumps([r1.to_dictionary(), r2.to_dictionary()])
                ),
            )

    def test_save_to_file_empty(self):
        """Test for save_to_file method with empty list"""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(json.loads(file.read()), json.loads("[]"))

    def test_save_to_file_none(self):
        """Test for save_to_file method with None"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(json.loads(file.read()), json.loads("[]"))

    def test_from_json_string(self):
        """Test for from_json_string method"""
        l = [{"id": 89, "width": 10, "height": 4}]
        s = Rectangle.from_json_string(json.dumps(l))
        self.assertEqual(s, l)

    def test_from_json_string_empty(self):
        """Test for from_json_string method with empty list"""
        s = Rectangle.from_json_string("")
        self.assertEqual(s, [])

    def test_from_json_string_none(self):
        """Test for from_json_string method with None"""
        s = Rectangle.from_json_string(None)
        self.assertEqual(s, [])

    def test_create(self):
        """Test for create method"""
        r = Rectangle(3, 5, 1)
        d = r.to_dictionary()
        r2 = Rectangle.create(**d)
        self.assertNotEqual(r, r2)
