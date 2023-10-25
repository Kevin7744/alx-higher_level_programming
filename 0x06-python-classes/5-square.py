#!/usr/bin/python3
""" Define a class Square"""


class Square:
    """ Private instance of attribute size """
    def __init__(self, size=0):
        """ Creates a new instance square

        Args:
            Size: must be an integer and not less than (0).
        """
        self.__size = size

    def area(self):
        """ Returns the current area of Square """
        return self.__size ** 2

    @property
    def size(self):
        """ property to retrieve it """
        return self.__size

    @size.setter
    def size(self, value):
        """ Property setter to set it (size)
        Args:
            value: (int): size of the square
        Raises:
            TypeError
            ValueError
        """
        if not isinstance(value, int):
            raise("size must be an integer")
        elif value < 0:
            raise("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """ Public instance method.
            Prints in stdout with character #
        """
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("#" * (self.__size))
