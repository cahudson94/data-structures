"""Python implementation for doubly-linked list data structure."""


class DoublyLinkedList(object):
    """Sets properties and methods of a doubly linked list."""

    def __init__(self):
        """Create new instance of DoublyLinkedList object."""
        self.tail = None
        self.head = None
        self._length = 0

    def push(self, val=None):
        """Instantiate and push new node."""
        if val is None:
            raise ValueError('You must give a value.')
        new_node = Node(val, self.head)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self._length += 1
            return
        self.head.prev_node = new_node
        self.head = new_node
        self._length += 1

    def append(self, val=None):
        """Instantiate and append new node."""
        if val is None:
            raise ValueError('You must give a value.')
        new_node = Node(val, None, self.tail)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self._length += 1
            return
        self.tail.next_node = new_node
        self.tail = new_node
        self._length += 1

    def pop(self):
        """Remove and return node from head of doubly linked list."""
        current_node = self.head
        if current_node is None:
            raise IndexError('Nothing to pop.')
        self.head = current_node.next_node
        current_node.next_node.prev_node = None
        self._length -= 1
        return current_node.val

    def shift(self):
        """Remove and return node from tail of doubly linked list."""
        current_node = self.tail
        if current_node is None:
            raise IndexError('Nothing to shift.')
        self.tail = current_node.prev_node
        current_node.prev_node.next_node = None
        self._length -= 1
        return current_node.val

    def remove(self, val):
        """Find and remove the first Node with a given value."""
        current_item = self.head
        while current_item.val != val:
            current_item = current_item.next_node
            if current_item is None:
                raise ValueError('Node not in doubly linked list.')
        if current_item.prev_node is None:
            self.head = current_item.next_node
            self.head.prev_node = None
        elif current_item.next_node is None:
            self.tail = current_item.prev_node
            self.tail.next_node = None
        else:
            current_item.prev_node.next_node = current_item.next_node
            current_item.next_node.prev_node = current_item.prev_node
        self._length -= 1

    def __len__(self):
        """Return the size of a doubly linked list, overwriting len method."""
        return self._length


class Node(object):
    """Set properties and methods of Node class."""

    def __init__(self, val, next_node=None, prev_node=None):
        """Create new Node."""
        self.val = val
        self.next_node = next_node
        self.prev_node = prev_node
