"""."""


class BST():
    """."""

    def __init__(self, iterable=None):
        """."""
        self.head = None
        self._length = 0
        self._depth = 0
        self._balance = 0
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
        path = []
        iteration = 0
        left = False
        right = False
        bal_chg = False
        if curr is None:
            curr = Node(val)
            self.head = curr
            self._length += 1
            path.append(curr)
            if len(path) > self._depth:
                self._depth = len(path)
            return
        path.append(curr)
        while True:
            if val == curr.val:
                return None
            elif val < curr.val and curr.left is None:
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
                    self._balance += 1
                if right and bal_chg:
                    self._balance -= 1
                return
            elif val > curr.val and curr.right is None:
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
                    self._balance += 1
                if right and bal_chg:
                    self._balance -= 1
                return
            elif val < curr.val and curr.left:
                path.append(curr)
                curr = curr.left
                if iteration == 0:
                    left = True
                    iteration += 1
            elif val > curr.val and curr.right:
                path.append(curr)
                curr = curr.right
                if iteration == 0:
                    right = True
                    iteration += 1

    def search(self, val):
        """."""
        curr = self.head
        while True:
            if val == curr.val:
                return curr
            elif curr is None:
                return None
            elif val < curr.val and curr.left:
                curr = curr.left
            elif val > curr.val and curr.right:
                curr = curr.right

    def size(self):
        """."""
        return self._length

    def depth(self):
        """."""
        return self._depth

    def contains(self, val):
        """."""
        if self.search(val):
            return True
        return False

    def balance(self):
        """."""
        return self._balance


class Node():
    """."""

    def __init__(self, val):
        """."""
        self.val = val
        self.left = None
        self.right = None
