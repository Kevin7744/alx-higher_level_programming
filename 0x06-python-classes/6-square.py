#!/usr/bin/python3
""" Define a class Square """


class Square:
    """ Private instance attribute size """
    def __init__(self, size=0, position=(0, 0)):
        """ Instation of optional size and optional position
            Args:
                size: (int)
                position: (int)
        """
        self.__size = size
        self.__position = position

    def area(self):
        """ Returns the current area of Square """
        return self.__size ** 2

    @property
    def size(self):
        """ Property to retrieve it"""
        return self.__size

    @size.setter
    def size(self, value):
        """ Property to set it (size)
            Args:
                value: (int) : size of the square
            Raise:
                TypeError
                ValueError
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """ Property to retrieve it """
        return self.__position

    @position.setter
    def position(self, value):
        """ Property to set it (value)
            Args:
                value: (tuple)
            Raise:
                TypeError
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """ Prints in stdout square with character  """
        if self.__size == 0:
            print()
        else:
            for j in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ", end="")
                print("#" * (self.__size))
