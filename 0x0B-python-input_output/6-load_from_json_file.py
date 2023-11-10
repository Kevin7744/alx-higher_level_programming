#!/usr/bin.python3
""" Fucntion that creates an object from json file """
import json


def load_from_json_file(filename):
    """ creates an object """
    with open(filename) as file:
        return json.load(f)
