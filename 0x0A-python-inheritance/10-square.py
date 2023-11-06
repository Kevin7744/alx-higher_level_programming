#!/usr/bin/python3
"""
Class square that inherits from Rectangle
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ Class square """
    def __init__(self, size):
        """ Instatiation with size """
        self.integer_validator("size", size)
        self._size = size
        super().__init__(size, size)

    def area(self):
        """ returns the area of the square """
        return self.__size ** 2
