#!/usr/bin/python3
"""
Module: singly_linked_list

This module defines a `Node` class for a singly linked list
and a `SinglyLinkedList` class to manage ordered insertion.
"""


class Node:
    """
    A class that defines a node of a singly linked list.

    Attributes:
        __data (int): The data stored in the node.
        __next_node (Node or None): A reference to
        the next node in the list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a node with a given data value
        and a reference to the next node.

        Args:
            data (int): The data to store in the node.
            next_node (Node, optional): Reference to
            the next node. Defaults to None.

        Raises:
            TypeError: If `data` is not an integer.
            TypeError: If `next_node` is not a
            Node object or None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieves the data of the node.

        Returns:
            int: The data stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Sets the data of the node, ensuring it is an integer.

        Args:
            value (int): The new data value.

        Raises:
            TypeError: If `value` is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Retrieves the next node in the linked list.

        Returns:
            Node or None: The next node reference.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the next node reference.

        Args:
            value (Node or None): The next node.

        Raises:
            TypeError: If `value` is not a Node object or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    A class that defines a singly linked list with sorted insertion.

    Attributes:
        __head (Node or None): The head of the linked list.
    """

    def __init__(self):
        """
        Initializes an empty singly linked list.
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted
        position in the list (ascending order).

        Args:
            value (int): The value to insert in the list.
        """
        new_node = Node(value)

        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        # Find the correct position to insert
        current = self.__head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        # Insert the new node
        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the linked list.

        Returns:
            str: A newline-separated string of node values.
        """
        node_values = []
        current = self.__head
        while current is not None:
            node_values.append(str(current.data))
            current = current.next_node
        return "\n".join(node_values)
