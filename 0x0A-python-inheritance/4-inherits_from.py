#!/usr/bin/python3
"""
Function defintion inherits_from(obj, a_class)
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or inderictly) from the specified class
    Otherwise False
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
