"""."""


class BST():
    """."""

    def __init__(self, iterable=None):
        """."""
        self._root = None
        self._length = 0
        self._depth = 0
        self._balance = 0
        if type(iterable) in [tuple, list]:
            for i in iterable:
                if type(i) == int:
                    self.insert(i)
                raise TypeError('''
Try again with only numbers in your list or tuple.''')
        elif type(iterable) == int:
            self.insert(iterable)
        elif iterable is not None:
            raise TypeError('Try again with a list, tuple, or int.')

    def insert(self, val):
        """."""
        if type(val) != int:
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
                        self._balance += 1
                    if right and bal_chg:
                        self._balance -= 1
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
                        self._balance += 1
                    if right and bal_chg:
                        self._balance -= 1
                    return

    def search(self, val):
        """."""
        curr = self._root
        if type(val) != int:
            raise TypeError('This tree only contains numbers.')
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
        if type(val) != int:
            raise TypeError('This tree only contains numbers.')
        if self.search(val):
            return True
        return False

    def balance(self):
        """."""
        return self._balance


class Node():
    """."""

    def __init__(self, val, left=None, right=None):
        """."""
        self.val = val
        self.left = left
        self.right = right
