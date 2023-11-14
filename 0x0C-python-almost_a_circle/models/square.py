#!/usr/bin/python3
""" Class square that inherits from Rectangle """

from .rectangle import Rectangle


class Square(Rectangle):
    """ Inherits from class rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes an instance of class Square """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Returns a string representation of the instance """
        a = self.id
        b = self.width
        c = self.x
        d = self.y
        return "[Square] ({}) {}/{} - {}".format(a, c, d, b)

    @property
    def size(self):
        """ retrieves the attribute size """
        return self.width

    @size.setter
    def size(self, value):
        """ Validate and sets the attribut size """
        self.width = value
        self.heght = value

    def update(self, *args, **kwargs):
        """ Update the class square """
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            if kwargs is not None:
                for key, value in kwargs.items():
                    if key == "id":
                        self.id = value
                    if key == "size":
                        self.size = value
                    if key == "y":
                        self.y = value
                    if key == "x":
                        self.x = value

    def to_dictionary(self):
        """ Returns the dictionary representation of a sqaure """
        my_dict = {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y}
        return my_dict
