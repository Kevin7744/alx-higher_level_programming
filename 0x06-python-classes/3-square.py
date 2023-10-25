#!/usr/bin/python3
""" Define a class Square"""


class Square:
    """ Private instance attribute: Size """

    def __init__(self, size=0):
        """ Creates a mew instance square.


        Args:
            Size: Must be an integer and size not less than (0)
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0 ")
        else:
            self.__size = size

    def area(self):
        """ Returns the current square area """
        return self.__size ** 2
