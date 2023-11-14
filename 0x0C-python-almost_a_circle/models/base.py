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
    
    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSOn string representation of list_objs to a file """
        if list_objs is None:
            list_objs = []

        class_name = cls.__name__
        filename = "{}.json".format(class_name)
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        json_str = cls.to_json_string(list_dicts)
        with open(filename, "w") as f:
            f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the jsson string representation json string """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Creates and return an instance of base class with all attribute 
        already set
        """
        if cls.__name__ == "Rectangle":
            my_obj = cls(1, 1)
        elif cls.__name__ == "Square":
            my_obj = cls(1)
        else:
            return None
        my_obj.update(**dictionary)
        return my_obj

    @classmethod
    def load_from_file(cls):
        """ Creates from a dictionary of existing instance of a class """
        instance_list = []
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, 'r', encoding="utf-8") as f:
                string = f.read()
                json_string = cls.from_json_string(string)
                instance_list = [cls.create(**inst) for inst in json_string]
                return instance_list

        except FileNotFoundError:
            return instance_list
