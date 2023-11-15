#!/usr/bin/python3
"""
Function that returns an object represented by a pytohn string
"""
import json


def from_json_string(my_str):
    """ Returns an object"""
    return json.loads(my_str)
