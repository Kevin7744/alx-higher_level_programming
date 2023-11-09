#!/usr/bin/python3
"""
Function that writes an Object to a text file
Using JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """ Function to write Object """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
