#!/usr/bin/python3
"""
Class definition BaseGeometry
"""


class BaseGeometry:
    """
    Public instance method: def area(self)
    public instance method: def integer_validator(self, name, value)
    """
    def area(self):
        """ Raises an exception when called """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates that value is an integer greater than 0 """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
