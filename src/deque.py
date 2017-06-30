"""Implementation of a dequeue data structure."""
from doubly_linked_list import DoublyLinkedList


class Deque(object):
    """Set attributes and methods of Dequeue object."""

    def __init__(self):
        """Initialize Dequeue using LinkedList."""
        self._doubly_linked_list = DoublyLinkedList()
        self.head = self._doubly_linked_list.head
        self.tail = self._doubly_linked_list.tail

    def append(self, val):
        """Add value to the front of a Dequeue."""
        self._doubly_linked_list.append(val)
        self.head = self._doubly_linked_list.head
        self.tail = self._doubly_linked_list.tail

    def appendleft(self, val):
        """Add value to the back of a Dequeue."""
        self._doubly_linked_list.push(val)
        self.head = self._doubly_linked_list.head
        self.tail = self._doubly_linked_list.tail

    def pop(self):
        """Remove the back of the Dequeue."""
        popped = self._doubly_linked_list.shift()
        self.tail = self._doubly_linked_list.tail
        self.head = self._doubly_linked_list.head
        return popped

    def popleft(self):
        """Remove the front of the Dequeue."""
        popped = self._doubly_linked_list.pop()
        self.head = self._doubly_linked_list.head
        self.tail = self._doubly_linked_list.tail
        return popped

    def peek(self):
        """Return the Dequeue tail."""
        if self._doubly_linked_list.tail is None:
            return None
        return self._doubly_linked_list.tail.val

    def peekleft(self):
        """Return the Dequeue head."""
        if self._doubly_linked_list.head is None:
            return None
        return self._doubly_linked_list.head.val

    def size(self):
        """Return the size of the queue."""
        return self._doubly_linked_list._length

    def __len__(self):
        """Return the size of Dequeue, overwriting len method."""
        return self._doubly_linked_list._length
