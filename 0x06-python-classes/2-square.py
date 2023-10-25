#!/usr/bin/python3
""" Define class Square """


class Square:
    """ Private instance attribute: size """

    def __init__(self, size=0):
        """ Create a new instance square.


        Args:
            Size: Must be an integer and not less than (0)
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__eize = size
