"""Implementation of a deque data structure."""
from doubly_linked_list import DoublyLinkedList


class Deque(object):
    """Set attributes and methods of Deque object."""

    def __init__(self):
        """Initialize Queue using LinkedList."""
        self._doubly_linked_list = DoublyLinkedList()
        self.head = self._doubly_linked_list.head
        self.tail = self._doubly_linked_list.tail

    def append(self, val):
        """Add value to the front of a Deque."""
        self._doubly_linked_list.append(val)
        self.head = self._doubly_linked_list.head
        self.tail = self._doubly_linked_list.tail

    def appendleft(self, val):
        """Add value to the back of a Deque."""
        self._doubly_linked_list.push(val)
        self.head = self._doubly_linked_list.head
        self.tail = self._doubly_linked_list.tail

    def pop(self):
        """Remove the back of the Deque."""
        popped_node = self._doubly_linked_list.shift()
        self.tail = self._doubly_linked_list.tail
        return popped_node.val

    def popleft(self):
        """Remove the front of the Deque."""
        popped_node = self._doubly_linked_list.pop()
        self.head = self._doubly_linked_list.head
        return popped_node.val

    def peek(self):
        """Return the Deque tail."""
        return self._doubly_linked_list.tail

    def peekleft(self):
        """Return the Deque head."""
        return self._doubly_linked_list.head

    def size(self):
        """Return the size of the queue."""
        return self._doubly_linked_list._length

    def __len__(self):
        """Return the size of Queue, overwriting len method."""
        return self._doubly_linked_list._length
