#!/usr/bin/python3
"""Defines class MagicClass"""
import math


class MagicClass:
    """
    define properties of MagicClass.

    Attributes:
        radius: radius.
    """
    def __init__(self, radius=0):
        """Create new instance MagicClass.

        Args:
            radius: radius.

        Raises:
            TypeError:.
        """
        self.__radius = 0
        if not isinstance(radius, int) and not isinstance(radius, float):
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def area(self):
        """Returns area

        Returns: area
        """
        return math.pi * self.__radius ** 2

    def circumference(self):
        """Returns circumference

        Returns: circumference.
        """
        return 2 * math.pi * self.__radius
