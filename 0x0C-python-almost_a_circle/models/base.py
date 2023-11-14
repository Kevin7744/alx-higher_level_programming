#!/usr/bin/python3
"""
Definition of class Base
"""
import json


class Base:
    """
    args:
        private attribute: __nb_objects(This will be the base)
        id: default None
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns a JSONstring representation """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
