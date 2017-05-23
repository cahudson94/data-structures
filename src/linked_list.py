"""Implementation of a linked list data structure."""


class Linked_List(object):
    """."""

    def __init__(self, head=None):
        """."""
        self.head = head

    def push(self, val):
        """Create a new node."""
        new_node = Node(val)
        new_node.set_next(self.head)
        self.head = new_node

    def search(self, val):
        """Return a node for a given value."""


class Node(object):
    """."""

    def __init__(self, val=None, next_node=None):
        """."""
        self.val = val
        self.next_node = next_node

    def get_val(self):
        """."""
        return self.val

    def get_next(self):
        """."""
        return self.next_node

    def set_next(self, new_node):
        """."""
        self.next_node = new_node
