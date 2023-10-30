#!/usr/bin/python3

""" Define class rectangle besed on 1-rectangle.py"""
class Rectangle:
    """
    Attribute : 
        width: private instance attribute width
        height: private instance attribute height
    public instance method def area(self)
    public instance method def perimeter(self)
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Property to retriev it

        Args: Width

        Raise:
            TypeError: must be an int
            ValueError: must be greater than 0
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ Property setter to set it
            Args : width(int)
        """
        if type(value) is not int:
            raise("width must be an integer")
        elif value < 0:
            raise("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Property to retrieve it
        
        Args: width
        """
        return self.__height
    
    @height.setter
    def height(self, value):
        """
        Property setter to set it

        Args: height

        Raise:
            typeError: must be an int
            ValueError: must be greater than 0
        """
        if type(value) is not int:
            raise("height must be an integer")
        elif value < 0:
            raise("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates are of rectangle
        Args: Width, height

        Returns : area
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        Calculates perimeter of rectangle
        Args: width, height

        Returns: Perimeter
        """
        perimeter = ((self.__width + self.__height) * 2)
        if self.__height == 0 or self.__width == 0:
             return 0
        else:
            return perimeter
