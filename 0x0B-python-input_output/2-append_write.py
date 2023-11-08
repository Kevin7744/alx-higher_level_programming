#!/usr/bin/python3
"""
Function that appends a string at the end of a file
"""


def append_write(filename="", text=""):
    """ Appends a string to file """
    with open(filename, "a", encoding='utf-8') as file:
        return file.append(text)
