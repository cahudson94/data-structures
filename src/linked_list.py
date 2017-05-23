"""Implementation of a linked list data structure."""


class LinkedList(object):
    """Set properties and methods for LinkedList class."""

    def __init__(self, inbound_data=None):
        """Initialize LinkedList object."""
        self.head = None
        self._length = 0
        if type(inbound_data) in [list, tuple, str]:
            for item in inbound_data:
                self.push(item)
        elif inbound_data is not None:
            raise TypeError('Give us an interable please.')

    def push(self, val):
        """Create a new node."""
        if not val:
            raise ValueError('You must give a value.')
        new_node = Node(val, self.head)
        self.head = new_node
        self._length += 1

    def pop(self):
        """Remove node from LinkedList."""
        current_node = self.head
        if current_node is None:
            raise IndexError('Linked list is empty, no node to pop.')
        print(current_node)
        self._length -= 1
        self.head = current_node.next_node

    def size(self):
        """Return the size of a linked list."""
        return self._length

    def search(self, val):
        """Return a node for a given value."""
        current_node = self.head
        while current_node:
            if val == current_node.val:
                return current_node
            current_node = current_node.next_node
        return None

    def remove(self, node):
        """Remove a node from the linked list."""
        current_node = self.head
        previous_node = None
        while current_node != node:
            previous_node = current_node
            current_node = current_node.next_node
            if current_node is None:
                raise ValueError('Node not in linked list.')
        if previous_node is None:
            self.head = current_node.next_node
        else:
            previous_node.next_node = current_node.next_node
        current_node.next_node = None
        self._length -= 1

    def display(self):
        """Return string representing LinkedList as Python tuple."""
        display_string = u''
        current_node = self.head
        while current_node:
                display_string = current_node.val + ' ' + display_string
                current_node = current_node.next_node
        display_string = display_string.strip().replace(' ', ', ')
        display_string = '(' + display_string + ')'
        return display_string

    def __len__(self):
        """Return the size of a linked list, overwriting len method."""
        return self._length

    def __repr__(self):
        """Print the what is returned by display."""
        return self.display()


class Node(object):  # pragma: no cover
    """Set properties and methods for LinkedList class."""

    def __init__(self, val, next_node=None):
        """."""
        self.val = val
        self.next_node = next_node
