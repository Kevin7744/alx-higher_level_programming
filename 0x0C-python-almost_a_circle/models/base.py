#!/usr/bin/python3
"""
Definition of class Base
"""


class Base:
    """
    args:
        private attribute: __nb_objects(This will be the base)
        id: default None
    """
    __nb_objects = 0
    def __init__(self, id=None):
        if id != None:
            self.id = id
        else: 
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
