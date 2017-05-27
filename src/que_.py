"""Implementation of a queue data structure."""
from doubly_linked_list import DoublyLinkedList


class QueueStructure(object):
    """Set attributes and methods of Queue object."""

    def __init__(self):
        """Initialize Queue using LinkedList."""
        self._doubly_linked_list = DoublyLinkedList()
        self.head = self._doubly_linked_list.head

    def enqueue(self, val):
        """Add value to a queue."""
        self._doubly_linked_list.append(val)
        self.head = self._doubly_linked_list.head

    def dequeue(self):
        """Remove the head from the queue."""
        self._doubly_linked_list.pop()
        self.head = self._doubly_linked_list.head

    def peek(self):
        """Return the queue head."""
        return self._doubly_linked_list.head

    def size(self):
        """Return the size of the queue."""
        return self._doubly_linked_list._length

    def __len__(self):
        """Return the size of Queue, overwriting len method."""
        return self._doubly_linked_list._length
