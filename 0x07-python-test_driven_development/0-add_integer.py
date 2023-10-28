#!/usr/bin/python3

""" Define function that add two integers """
def add_integer(a, b=98):
    """
    Adds two integers or float.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number. Defaults to 98.

    Returns:
    int: The addition of a and b.
    
    Raise:
    TypeError: If a and b are not integers or floats.

    Examples:
    >>> add_integers(5, 3.8)
    8

    >>> add_integers(2.5, 3)
    5
    >>> add_integers("5", 3.5)
    Traceback (most recent call to last):
        ...
    TypeErro: a must be an integer or b must be an integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("a must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    result = a + b
    return int(result)
