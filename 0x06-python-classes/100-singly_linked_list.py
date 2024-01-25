#!/usr/bin/python3

"""This module contains a class that defines a singly linked list."""


class Node:
    """This class contains a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initializes a node in a singly linked list.

        Args:
            data (int): The data of the node.
            next_node (Node): The next node in the singly linked list.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """int: The data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Node: The next node in the singly linked list."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """This class contains a singly linked list."""

    def __init__(self):
        """Initializes a singly linked list."""
        self.__head = None

    def __str__(self):
        """Returns a string representation of the singly linked list."""
        string = ""
        current = self.__head
        while current is not None:
            string += str(current.data) + "\n"
            current = current.next_node
        return string[:-1]

    def sorted_insert(self, value):
        """Inserts a node into the singly linked list in sorted order.

        Args:
            value (int): The value of the node to insert.
        """
        new = Node(value)
        if self.__head is None:
            self.__head = new
        elif value < self.__head.data:
            new.next_node = self.__head
            self.__head = new
        else:
            current = self.__head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new.next_node = current.next_node
            current.next_node = new
