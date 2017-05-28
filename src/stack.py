"""Implementation of a stack data structure."""
from linked_list import LinkedList


class Stack(object):
    """Set properties and methods of Stack class."""

    def __init__(self, inbound_data=None):
        """Create new Stack composing from LinkedList."""
        self._linked_list = LinkedList(inbound_data)
        self.head = self._linked_list.head

    def push(self, val):
        """Return a new node on the Stack using LinkedList.push."""
        self._linked_list.push(val)
        self.head = self._linked_list.head

    def pop(self):
        """Return pop method for LinkedList on Stack."""
        self.head = self._linked_list.head
        return self._linked_list.pop()

    def __len__(self):
        """Return the size of the Stack, overwriting len method."""
        return len(self._linked_list)
