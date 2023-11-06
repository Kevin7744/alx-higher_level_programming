#!/usr/bin/python3
"""
Class Rectangle that inherits from BaseGeomtry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """  representaion of a rectangle """
    def __init__(self, width, height):
        """ Instatiation of rectangle """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ returns are of the rectangle """
        return self.__width * self.__height
    
    def __str__(self):
        """ Informal string representation of the rectangle """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height) 
