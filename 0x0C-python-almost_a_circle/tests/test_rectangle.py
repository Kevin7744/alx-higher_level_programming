#!/usr/bin/python3
""" This module supplies a unittest for rectangle class attributes and method
"""
import unittest
import io
import sys
from models.rectangle import Rectangle
from models.base import Base


class Testrectangle(unittest.TestCase):
    """
    Test class for base that inherits from unitest TestCase
    """
    def test_rectangle_id(self):
        """
        Tests assignment of id attribute to class instance
        """
        self.assertEqual(Rectangle(10, 2, 0, 0, 12).id, 12)

    def test_is_subclass(self):
        """
        Tests if Rectangle is a subclass of Base class it inherits from
        """
        self.assertTrue(issubclass(Rectangle, Base))

    def test_TypeError_exception_message(self):
        """
        Tests for validation of width, height, x and y for Rectangle
        instance with values not integers
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rect = Rectangle("a", 4)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rect = Rectangle(True, 4)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rect = Rectangle(5, False)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rect = Rectangle(4, 4, "c", 1)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rect = Rectangle(4, 4, 3, "z")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rect = Rectangle(4, 4, 3, False)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rect = Rectangle(4, 4, 3, [2, 1, 3])

    def test_ValueError_exception_message(self):
        """
        Tests for validation of width, height, x and y for Rectangle
        instance with values < 0
        """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rect = Rectangle(-3, 5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rect = Rectangle(0, 5)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rect = Rectangle(2, -5)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rect = Rectangle(2, 0)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            rect = Rectangle(2, 5, -2, 5)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            rect = Rectangle(2, 5, 4, -1)

    def test_area_method(self):
        """
        Tests area method with different values
        """
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(10, 1).area(), 10)
        self.assertEqual(Rectangle(10, 3).area(), 30)

    def test_display_method(self):
        """
        Tests display method
        """

        expected_output = "##\n##\n##\n"
        captured_output = io.StringIO()
        sys.stdout = captured_output
        Rectangle(2, 3).display()
        actual = captured_output.getvalue()
        sys.stdout = sys.stdout
        self.assertEqual(expected_output, actual)

        expected_output = "##\n##\n"
        captured_output = io.StringIO()
        sys.stdout = captured_output
        Rectangle(2, 2).display()
        actual = captured_output.getvalue()
        sys.stdout = sys.stdout
        self.assertEqual(expected_output, actual)

    def test__str__magic_method(self):
        """
        Tests the magic method __Str__ that is to return
        a string representation of a class
        """
        r1 = Rectangle(2, 4, 2, 5, 14)
        self.assertEqual(str(r1), "[Rectangle] (14) 2/5 - 2/4")

        r1 = Rectangle(2, 2, 0, 0, 15)
        self.assertEqual(str(r1), "[Rectangle] (15) 0/0 - 2/2")

    def test_display_method(self):
        """
        Tests display method that prints in stdout the Rectangle instance
        with the character # by taking care of x ad y
        """

        expected_output = "\n  ####\n"
        captured_output = io.StringIO()
        sys.stdout = captured_output
        Rectangle(4, 1, 2, 1).display()
        actual = captured_output.getvalue()
        sys.stdout = sys.stdout
        self.assertEqual(expected_output, actual)

        expected_output = " ##\n ##\n"
        captured_output = io.StringIO()
        sys.stdout = captured_output
        Rectangle(2, 2, 1).display()
        actual = captured_output.getvalue()
        sys.stdout = sys.stdout
        self.assertEqual(expected_output, actual)

    def test_update_method(self):
        """
        Tests update method that assigns an argument or key value arguments
        to each attribute
        1st argument should be the id attribute
        2nd argument should be the width attribute
        3rd argument should be the height attribute
        4th argument should be the x attribute
        5th argument should be the y attribute
        kwargs must be skipped if args exist

        """
        r1 = Rectangle(3, 5, 0, 0, 3)
        self.assertEqual(str(r1), "[Rectangle] (3) 0/0 - 3/5")
        r1.update(60)
        self.assertEqual(str(r1), "[Rectangle] (60) 0/0 - 3/5")
        r1.update(23, 5)
        self.assertEqual(str(r1), "[Rectangle] (23) 0/0 - 5/5")
        r1.update(23, 5, 2)
        self.assertEqual(str(r1), "[Rectangle] (23) 0/0 - 5/2")
        r1.update(23, 5, 2, 4)
        self.assertEqual(str(r1), "[Rectangle] (23) 4/0 - 5/2")
        r1.update(23, 5, 2, 4, 7)
        self.assertEqual(str(r1), "[Rectangle] (23) 4/7 - 5/2")
        r1.update(30, id=15)
        self.assertEqual(str(r1), "[Rectangle] (30) 4/7 - 5/2")
        r1.update(id=15, width=4, height=6, x=3, y=2)
        self.assertEqual(str(r1), "[Rectangle] (15) 3/2 - 4/6")

    def test_to_dictionary(self):
        """
        Tests the method to_dictionary that returns a dictionary representation
        of a Rectangle.
        """
        r1 = Rectangle(4, 6, 0, 0, 21)
        expected = {'width': 4, 'height': 6, 'x': 0, 'y': 0, 'id': 21}
        self.assertDictEqual(expected, r1.to_dictionary())
