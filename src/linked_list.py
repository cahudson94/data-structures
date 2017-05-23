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


    def remove(self):
        """Remove a node from the linked list."""


    def search(self, val):
        """Return a node for a given value."""
        current_node = self.head
        while current_node:
            if val == current_node.get_val():
                return current_node
            current_node = current_node.get_next()
        return None

    def size(self):
        """Return the size of a linked list."""
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.get_next()
        return count


    def __len__(self):
        """Return the size of a linked list."""
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.get_next()
        return count


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
