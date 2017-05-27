"""Implementation of a queue data structure."""
from doubly_linked_list import DoublyLinkedList, Node


class Queue(object):
    """Set attributes and methods of Queue object."""

    def __init__(self):
        """Initialize Queue using LinkedList."""
        self._doubly_linked_list = DoublyLinkedList()

    def enqueue(self, val):
        """Add value to a queue."""
        self._doubly_linked_list.append(val)

    def dequeue(self):
        """Remove the head from the queue."""
        self._doubly_linked_list.pop()

    def peek(self):
        """Return the queue head."""
        return self._doubly_linked_list.head

    def size(self):
        """Return the size of the queue."""
        return self._doubly_linked_list._length

    def __len__(self):
        """Return the size of Queue, overwriting len method."""
        return self._doubly_linked_list._length

    def display(self):
        """Display queue."""
        display_string = u''
        current_node = self._doubly_linked_list.head
        while current_node:
                display_string = '{} {}'.format(current_node.val,
                                                display_string)
                current_node = current_node.next_node
        display_string = display_string.strip().replace(' ', ', ')
        display_string = '({})'.format(display_string)
        return display_string


# class QueueNode(object):
#     """Set properties and methods of Node class."""

#     def __init__(self, val):
#         """Create new Node."""
#         self._node = Node(val)
