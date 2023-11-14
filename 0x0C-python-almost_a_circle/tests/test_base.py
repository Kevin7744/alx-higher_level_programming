#!/usr/bin/python3
""" This module supplies a unittest for base class attributes and method
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json


class Testbase(unittest.TestCase):
    """
    Test class for base that inherits from unitest TestCase
    """
    def test_base_id(self):
        """
        Tests assignment of id attribute to class instance
        """
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)
        self.assertEqual(Base().id, 3)
        self.assertEqual(Base(12).id, 12)
        self.assertEqual(Base().id, 4)

    def test_to_json_string_method(self):
        """
        Tests a static method that takes a list of dictionaries and returns
        a JSON string representation of the dictionaries in the list
        """
        r1 = Rectangle(3, 4, 0, 0, 50)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        expected = [{'id': 50, 'width': 3, 'height': 4, 'x': 0, 'y': 0}]
        self.assertEqual(json.dumps(expected), json_dictionary)

        json_dictionary = Base.to_json_string([])
        self.assertEqual(json_dictionary, "[]")

        json_dictionary = Base.to_json_string(None)
        self.assertEqual(json_dictionary, "[]")

    def test_save_to_file_method(self):
        """
        Tests class method that writes json string representation of
        objects in a list to a file.
        """
        r1 = Rectangle(12, 5, 0, 1, 16)
        r2 = Rectangle(10, 2, 4, 3, 23)
        Rectangle.save_to_file([r1, r2])
        exp = [{'width': 12, 'height': 5, 'x': 0, 'y': 1, 'id': 16}]
        exp.append({'width': 10, 'height': 2, 'x': 4, 'y': 3, 'id': 23})
        with open("Rectangle.json", "r") as f:
            file_data = json.load(f)
        self.assertEqual(file_data, exp)

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            file_data = json.load(f)
        self.assertEqual(file_data, [])

    def test_from_json_string(self):
        """
        Tests a static method that deserialized a Json string and returns
        a list
        """
        list_input = [{"id": 89, "width": 3, "height": 6}]
        json_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_input)
        self.assertIsInstance(json_input, str)
        self.assertIsInstance(list_output, list)
        list_input = None
        list_output = Rectangle.from_json_string(list_input)
        self.assertEqual(list_output, [])

    def test_create_method(self):
        """
        Tests a method that creates and return an instance with all attributes
        already set.
        """
        r1 = Rectangle(7, 2)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertEqual(str(r1), str(r2))
        self.assertNotEqual(r1, r2)

        s1 = Square(5)
        s1_dict = s1.to_dictionary()
        s2 = Square.create(**s1_dict)
        self.assertEqual(str(s1), str(s2))
        self.assertNotEqual(s1, s2)

    def test_load_from_file_method(self):
        """
        Tests a class method that creates instances from saved dict
        and returns a list of created instances
        """
        r1 = Rectangle(4, 1)
        rect_list = [r1]
        Rectangle.save_to_file(rect_list)
        output = Rectangle.load_from_file()
        for inst in output:
            self.assertNotEqual(id(r1), id(inst))

        s1 = Square(4)
        sq_list = [s1]
        Rectangle.save_to_file(sq_list)
        output = Square.load_from_file()
        for inst in output:
            self.assertNotEqual(id(inst), id(s1))
