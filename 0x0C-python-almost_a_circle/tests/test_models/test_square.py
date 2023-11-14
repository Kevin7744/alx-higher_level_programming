#!/usr/python3
"""This module supplies a unittest for square class attributes and method
"""
import unittest
import io
import sys
from models.square import Square
from models.rectangle import Rectangle


class Testsquare(unittest.TestCase):
    """
    Test class for square instance the inherits from unittest TestCase
    """
    def test_is_subclass(self):
        """
        Tests if Square inherits from Rectangle
        """
        self.assertTrue(issubclass(Square, Rectangle))

    def test_square_str_method(self):
        """
        Tests str method for square class instance
        """
        self.assertEqual(str(Square(2, 0, 0, 4)), "[Square] (4) 0/0 - 2")

    def test_square_area(self):
        """
        Test area method for square instances
        """
        self.assertEqual(Square(3).area(), 9)

    def test_size_validatation(self):
        """
        Tests validation for size attribute
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(3).size = "b"

    def test_square_update_method(self):
        """
        Test update method for square class that updates the attributes
        of a class with arguments or key/value arguments.
        1st argument should be the id attribute
        2nd argument should be the size attribute
        3rd argument should be the x attribute
        4th argument should be the y attribute
        kwargs should be skipped if args exists
        """
        s1 = Square(3, 0, 0, 16)
        self.assertEqual(str(s1), "[Square] (16) 0/0 - 3")
        s1.update(20, id=13)
        self.assertEqual(str(s1), "[Square] (20) 0/0 - 3")
        s1.update(20, 1)
        self.assertEqual(str(s1), "[Square] (20) 0/0 - 1")
        s1.update(20, 1, 2)
        self.assertEqual(str(s1), "[Square] (20) 2/0 - 1")
        s1.update(20, 1, 2, 1)
        self.assertEqual(str(s1), "[Square] (20) 2/1 - 1")
        s1.update(id=14, size=6, x=1, y=3)
        self.assertEqual(str(s1), "[Square] (14) 1/3 - 6")

    def test_to_dictionary_method(self):
        """
        tests method that returns a dict of instance attributes
        """
        s1 = Square(4, 0, 0, 14)
        expected = {'size': 4, 'x': 0, 'y': 0, 'id': 14}
        self.assertDictEqual(expected, s1.to_dictionary())
