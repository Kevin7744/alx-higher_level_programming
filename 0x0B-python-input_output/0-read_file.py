#!/usr/bin.python3
"""
Function that reads a text file(UTF8) and prints to stdout
"""


def read_file(filename=""):
    """ Reads a file """
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end="")
