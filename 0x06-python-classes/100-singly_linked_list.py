#!/usr/bin/python3

"""Classes for a singly-linked list."""


class Node:
    """Represent a node in a singly-linked list."""
    def __init__(self, data, next_node=None):
        """
        Initialize node with the given data and
        an optional reference to the next Node.

        Args:
            data (int): The data to be stored in the Node.
            next_node (Node): The next Node in the list. Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represent a singly-linked list."""
    def __init__(self):
        """
        Initialize an empty Singly Linked List.
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Insert a Node with the given value in sorted order in the linked list.
        Args:
            value (int): The value to be inserted in the linked list.
        """
        node = Node(value)
        if self.__head is None:
            self.__head = node
        else:
            prev = None
            cur = self.__head
            while cur is not None:
                if value < cur.data:
                    break
                prev = cur
                cur = cur.next_node
            if prev is not None:
                prev.next_node = node
            else:
                self.__head = node
            node.next_node = cur

    def __str__(self):
        """
        Return a string representation of the linked list.
        """
        cur = self.__head
        my_str = ""
        while cur is not None:
            my_str += str(cur.data)
            my_str += "\n"
            cur = cur.next_node
        return my_str[: -1]
