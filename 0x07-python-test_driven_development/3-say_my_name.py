#!/usr/bin/python3
"""
"3-say_my_name" module.
supplies one function, say_my_name.
"""


def say_my_name(first_name, last_name=""):
    """ Prints 'my name is' followed by first and last name
owhich is optional"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is", first_name, last_name)
