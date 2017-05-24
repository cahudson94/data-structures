"""Implementation of a linked list data structure."""
from linked_list import LinkedList


class Stack(object):
    """Set properties and methods of Stack class."""

    def __init__(self, inbound_data=None):
        """Create new Stack composing from LinkedList."""
        self.inbound_data = None
        self._linked_list = LinkedList(inbound_data)

    def push(self, val):
        """Return a new node on the Stack using LinkedList.push."""
        self._linked_list.push(val)

    def pop(self):
        """Return pop method for LinkedList on Stack."""
        return self._linked_list.pop()

    def __len__(self):
        """Return the size of the Stack, overwriting len method."""
        return len(self._linked_list)


class Node(object):
    """Set properties and methods of Node class."""

    def __init__(self, val, next_node=None):
        """Create new Node."""
        self._node = Node(val, next_node)
