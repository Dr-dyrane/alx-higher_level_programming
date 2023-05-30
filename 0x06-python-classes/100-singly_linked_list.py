#!/usr/bin/python3
# 100-singly_linked_list.py
# Alexander Udeogarahnya <Ogranya.Alex@gmail.com>
"""Define classes for a singly-linked list."""


class Node:
    """
    Represent a node of a singly linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initialize a new Node.

        Args:
            data (int): The data of the node.
            next_node (Node): The next node in the list. Default is None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieve the data of the node.

        Returns:
            The data of the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Set the data of the node.

        Args:
            value (int): The new data of the node.

        Raises:
            TypeError: If value is not an integer.
        """
        if type(value) != int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """
        Retrieve the next node in the list.

        Returns:
            The next node in the list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the next node in the list.

        Args:
            value (Node): The new next node in the list.

        Raises:
            TypeError: If value is not None or a Node object.
        """
        if value is not None and type(value) != Node:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    Represent a singly linked list.
    """

    def __init__(self):
        """
        Initialize a new SinglyLinkedList.
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Insert a new Node into the correct sorted position in the list.

        Args:
            value (int): The value of the new Node.
        """
        new_node = Node(value)

        if self.head is None:
            # List is empty, set the new node as the head
            self.head = new_node
        elif value < self.head.data:
            # New node becomes the new head
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Return a string representation of the list.

        Returns:
            A string representation of the list.
        """
        if self.head is None:
            return ""
        else:
            current = self.head
            result = str(current.data)
            while current.next_node is not None:
                current = current.next_node
                result += "\n" + str(current.data)
            return result
