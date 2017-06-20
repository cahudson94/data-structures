"""."""


class BST():
    """."""

    def __init__(self, iterable=None):
        """."""
        self.head = None
        self._length = 0
        if type(iterable) in [tuple, list]:
            for i in iterable:
                self.insert(i)
        elif type(iterable) == int:
            self.insert(iterable)
        elif iterable is not None:
            raise TypeError('Try again with a list, tuple, or int.')

    def insert(self, val):
        """."""
        curr = self.head
        if self.head is None:
            self.head = Node(val)
            self._length += 1
        while True:
            if val == curr.val:
                return None
            elif val < curr.val and curr.left is None:
                curr.left = Node(val)
                self._length += 1
                break
            elif val > curr.val and curr.right is None:
                curr.right = Node(val)
                self._length += 1
                break
            elif val < curr.val and curr.left:
                curr = curr.left
            elif val > curr.val and curr.right:
                curr = curr.right

    def search(self, val):
        """."""
        curr = self.head
        while True:
            if val == curr.val:
                return curr
            elif val < curr.val and curr.left:
                curr = curr.left
            elif val > curr.val and curr.right:
                curr = curr.right

    def size(self):
        """."""
        return self._length


class Node():
    """."""

    def __init__(self, val):
        """."""
        self.val = val
        self.left = None
        self.right = None
