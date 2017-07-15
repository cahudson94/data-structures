"""Python implementation of Binary Search Tree."""
from timeit import timeit


class BST():
    """Binary Search Tree."""

    def __init__(self, iterable=None):
        """Initialize Binary Search tree."""
        self._root = None
        self._length = 0
        self._depth = 0
        self._balance = 0
        if type(iterable) in [tuple, list]:
            for i in iterable:
                if type(i) in [int, float]:
                    self.insert(i)
                else:
                    raise TypeError('''
Try again with only numbers in your list or tuple.''')
        elif type(iterable) == int:
            self.insert(iterable)
        elif iterable is not None:
            raise TypeError('Try again with a list, tuple, int, or float.')

    def insert(self, val):
        """Insert new node into Binary Search Tree."""
        if type(val) not in [int, float]:
            raise TypeError('You can only add numbers to this tree.')
        curr = self._root
        path = []
        iteration = 0
        left = False
        right = False
        bal_chg = False
        if curr is None:
            curr = Node(val)
            self._root = curr
            self._length += 1
            path.append(curr)
            if len(path) > self._depth:
                self._depth = len(path)
            return
        path.append(curr)
        while True:
            if val == curr.val:
                return
            elif val < curr.val:
                if curr.left:
                    path.append(curr)
                    curr = curr.left
                    if iteration == 0:
                        left = True
                        iteration += 1
                else:
                    curr.left = Node(val)
                    self._length += 1
                    path.append(curr.left)
                    if len(path) > self._depth:
                        self._depth = len(path)
                        bal_chg = True
                    if iteration == 0:
                        left = True
                        iteration += 1
                    if left and bal_chg:
                        self._balance -= 1
                    if right and bal_chg:
                        self._balance += 1
                    return
            elif val > curr.val:
                if curr.right:
                    path.append(curr)
                    curr = curr.right
                    if iteration == 0:
                        right = True
                        iteration += 1
                else:
                    curr.right = Node(val)
                    self._length += 1
                    path.append(curr.right)
                    if len(path) > self._depth:
                        self._depth = len(path)
                        bal_chg = True
                    if iteration == 0:
                        right = True
                        iteration += 1
                    if left and bal_chg:
                        self._balance -= 1
                    if right and bal_chg:
                        self._balance += 1
                    return

    def search(self, val):
        """Find the node at val in Binary Search Tree."""
        curr = self._root
        if type(val) not in [int, float]:
            raise TypeError('This tree only contains numbers.')
        while True:
            if curr is None:
                return None
            elif val == curr.val:
                return curr
            elif val < curr.val:
                curr = curr.left
            elif val > curr.val:
                curr = curr.right

    def size(self):
        """Return the amount of nodes in Binary Search Tree."""
        return self._length

    def depth(self):
        """Return the levels of the Binary Search Tree."""
        return self._depth

    def contains(self, val):
        """Return true if specified val is in tree, false if it is not."""
        if type(val) not in [int, float]:
            raise TypeError('This tree only contains numbers.')
        if self.search(val):
            return True
        return False

    def balance(self):
        """Return the difference of left and right depth from root."""
        return self._balance


class Node():
    """Create a node to add to the Binary Search Tree."""

    def __init__(self, val, left=None, right=None):
        """Initialize a new node."""
        self.val = val
        self.left = left
        self.right = right


def wrapper(func, *args, **kwargs):  # pragma: no cover
    """Create a value for a function with a specific arguement called to it."""
    def wrapped():
        return func(*args, **kwargs)
    return wrapped
    #  code found through Erik Enderlein
    #  he found it at http://pythoncentral.io/time-a-python-function/


if __name__ == '__main__':  # pragma: no cover
    best_stuff_tree = BST()
    find5 = wrapper(best_stuff_tree.search, 5)
    find24 = wrapper(best_stuff_tree.search, 24)
    nodes = [5, 3, 8, 2.2, 4, 9.5, 1, 2.6,
             3.3, 4.5, 9, 11, 8.5, 10, 14,
             16, 15, 21, 23, 24]
    for node in nodes:
        best_stuff_tree.insert(node)
    print(timeit(find5))
    print(timeit(find24))
