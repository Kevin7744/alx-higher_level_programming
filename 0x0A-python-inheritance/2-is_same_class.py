#!/usr/bin/python3
"""
Function defintion
"""


def is_same_class(obj, a_class):
    """
    Returns True is the object is 'exactly' an instance of the specified
    class
    """
    return (type(obj) == a_class)
