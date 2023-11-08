#!/usr/bin/python3
"""
Function that writes a string to a text file and returns the number of character written
"""


def write_file(filename="", text=""):
    """ Writes a string to a file """
    with open(filename, "w", encoding='utf-8') as file:
        return f.write(text)
