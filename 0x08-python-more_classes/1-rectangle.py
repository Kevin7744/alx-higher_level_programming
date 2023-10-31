#!/usr/bin/python3
""" Define class rectangle """


class Rectangle:
    """
    Defines rectangle based on 0-rectangle.py
    Args:
        width: Private instance attribute width
               Property setter def width(self, value)
               Raise:
                    TypeError:
                    ValueError:
        height: Private instance attribute width
                Property setter def height(self, value)
                Raise:
                    TypeError:
                    ValueError:
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        horizontal dimension of the rectangle
        Returns: __width(int)
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Args: Value(int)
        Attributes: width
        Raises:
            TypeError: IF value is not an integer
            ValueError : IF value is less than 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width muste be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Vertival dimension of rectangle
        Return: __height(int)
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Args: Value(int)
        Attributes: height
        Raises:
            TypeError : If value is not an integer
            valueError: if value is less than 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
