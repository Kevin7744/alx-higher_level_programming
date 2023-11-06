#!/usr/bin/python3
"""
Contains the class BaseGeometry and subclass Rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A Class with private instance width and height
    """
    def __init__(self, width, height):
        """ Private instance width and height """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
