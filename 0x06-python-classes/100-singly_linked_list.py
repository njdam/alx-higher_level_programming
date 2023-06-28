#!/usr/bin/python3
"""A class of Node and class of SinglyLinkedList
for dealing with Python Singly linked list.
"""


class Node:
    """A class Node for defining a node of singly linked list."""

    def __init__(self, data, next_node=None):
        """
        Initialisation of Node to data and new node

        Args:
            data (int): is a integer data to be stored in current node
            next_node (Node): is the next node to new node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getting current data at current Node."""
        return (self.__data)

    @data.setter
    def data(self, value):
        """Setting new value to data of current Node."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")

        self.__data = value

    @property
    def next_node(self):
        """Getting next Node to new Node or current Node."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")

        self.__next_node = value


class SinglyLinkedList:
    """A class SinglyLinkedList for Python singly linked list."""

    def __init__(self):
        """Initalisation of a SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """A public instance to insert new node in increasing order."""
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node

        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node

        else:
            temp = self.__head
            while ((temp.next_node is not None) and
                    (temp.next_node.data < value)):
                temp = temp.next_node

            new_node.next_node = temp.next_node
            temp.next_node = new_node

    def __str__(self):
        """Return string that provide formated representation."""
        svalue = []
        temp = self.__head

        while temp is not None:
            svalue.append(str(temp.data))
            temp = temp.next_node

        return ('\n'.join(svalue))
