#!/usr/bin/python3
"""Defines the class Node"""


class Node:
    """
    defines properties Node.

    Attributes:
        data: data.
    """
    def __init__(self, data, next_node=None):
        """Creates new instance of node.

        Args:
            __data : data field of node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve the data instance.

        Returns: the data field of  node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Propery setter for data.

        Args:
            value (int):.

        Raises:
            TypeError:
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrive next_node instance.

        Returns: next_node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Property setter for Node.

        Args:
            value (None): next node .

        Raises:
            TypeError:
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Class that defines.

    Attributes:
        head: SinglyLinkedList.
    """
    def __init__(self):
        """Creates new instance.

        Args:
            __head : SinglyLinkedList .
        """
        self.__head = None

    def __str__(self):
        """Represents the class objects as string.

        Returns: string.
        """
        temp_var = self.__head
        print_node = []
        while temp_var:
            print_node.sort()
            print_node.append(str(temp_var.data))
            temp_var = temp_var.next_node

        print_node.sort(key=int)
        return ("\n".join(print_node))

    def sorted_insert(self, value):
        """Inserts new node at a position.

        Args:
            value: value.
        """
        if self.__head is None:
            new_node = Node(value)
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            new_node = Node(value)
            new_node.data = value
            new_node.next_node = self.__head
            self.__head = new_node
