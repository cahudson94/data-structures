"""Implementation of a linked list data structure."""


class Stack(object):
    """Set properties and methods of Stack class."""

    def __init__(self, inbound_data=None):
        """Create new Stack."""
        self.top = None
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
        new_node = Node(val, self.top)
        self.top = new_node
        self._length += 1

    def pop(self):
        """Pop method for Stack."""
        current_node = self.top
        if current_node is None:
            raise IndexError('Linked list is empty, no node to pop.')
        print(current_node)
        self._length -= 1
        self.top = current_node.next_node

    def __len__(self):
        """Return the size of a linked list, overwriting len method."""
        return self._length


class Node(object):
    """Set properties and methods of Node class."""

    def __init__(self, val, next_node=None):
        """Create new Node."""
        self.val = val
        self.next_node = next_node
