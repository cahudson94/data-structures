"""Python implementation of Binary Search Tree."""
from timeit import timeit


class BST():
    """Binary Search Tree."""

    def __init__(self, input=None):
        """Initialize Binary Search tree."""
        self._root = None
        self._length = 0
        self._rdepth = 0
        self._ldepth = 0
        self._depth = 0
        self._balance = 0
        if type(input) in [tuple, list]:
            for i in input:
                if type(i) in [int, float]:
                    self.insert(i)
                else:
                    raise TypeError('''
Try again with only numbers in your list or tuple.''')
        elif type(input) in [int, float]:
            self.insert(input)
        elif input is not None:
            raise TypeError('Try again with a list, tuple, int, or float.')

    def insert(self, val):
        """Insert new node into Binary Search Tree."""
        if type(val) not in [int, float]:
            raise TypeError('You can only add numbers to this tree.')
        curr = self._root
        if curr is None:
            curr = Node(val)
            self._root = curr
            self._length = 1
            self._depth = 1
            return
        while True:
            if val < curr.val:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = Node(val)
                    curr.left.parent = curr
                    self._length += 1
                    self._bal_and_rotate(curr.left)
                    return
            elif val > curr.val:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = Node(val)
                    curr.right.parent = curr
                    self._length += 1
                    self._bal_and_rotate(curr.right)
                    return
            else:
                return

    def delete(self, val):
        """Delete the node with value from the Binary Search Tree."""
        to_del = self.search(val)
        if to_del is None:
            return None
        if to_del != self._root:
            par_for_bal = to_del.parent
        if self._length <= 3:
            self._del_small_tree(val)
            return
        self._length -= 1
        if to_del == self._root:
            self._root_shift(to_del, self._balance)
            par_for_bal = self._root
        elif to_del.left and to_del.right:
            sub_tree = self._tree_depth(to_del)
            sub_balance = sub_tree[0] - sub_tree[1]
            self._root_shift(to_del, sub_balance)
        elif to_del.left:
            if to_del.parent.left == to_del:
                to_del.parent.left = to_del.left
                to_del.left.parent = to_del.parent
            else:
                to_del.parent.right = to_del.left
                to_del.left.parent = to_del.parent
        elif to_del.right:
            if to_del.parent.left == to_del:
                to_del.parent.left = to_del.right
                to_del.right.parent = to_del.parent
            else:
                to_del.parent.right = to_del.right
                to_del.right.parent = to_del.parent
        else:
            self._del_leaf(to_del)
        self._bal_and_rotate(par_for_bal.left or par_for_bal.right or par_for_bal)
        # if par_for_bal.left:
        #     self._bal_and_rotate(par_for_bal.left)
        # elif par_for_bal.right:
        #     self._bal_and_rotate(par_for_bal.right)
        # else:
        #     self._bal_and_rotate(par_for_bal)
        # return

    def search(self, val):
        """Find the node at val in Binary Search Tree."""
        curr = self._root
        if type(val) not in [int, float]:
            raise TypeError('This tree only contains numbers.')
        while curr:
            if val < curr.val:
                curr = curr.left
            elif val > curr.val:
                curr = curr.right
            else:
                return curr

    def size(self):
        """Return the amount of nodes in Binary Search Tree."""
        return self._length

    def depth(self):
        """Return the levels of the Binary Search Tree."""
        return self._depth

    def contains(self, val):
        """Return true if specified val is in tree, false if it is not."""
        return not not self.search(val)

    def balance(self):
        """Return the difference of left and right depth from root."""
        return self._balance

    def in_order(self):
        """Return generator that returns values from BST 'in order'."""
        nodes = []
        curr = self._root
        while len(nodes) != self._length:
            if not curr.right and not curr.left and not curr.parent:
                nodes.append(curr)
            elif curr.left and curr not in nodes and curr.left not in nodes:
                curr = curr.left
            elif not curr.left and curr not in nodes:
                nodes.append(curr)
                if not curr.right:
                    curr = curr.parent
                if curr not in nodes:
                    nodes.append(curr)
            elif curr.right and curr.right not in nodes:
                if curr not in nodes:
                    nodes.append(curr)
                curr = curr.right
            elif not curr.right and curr not in nodes:
                nodes.append(curr)
                curr = curr.parent
            elif not curr.right:
                curr = curr.parent
            else:
                curr = curr.parent
                if curr not in nodes:
                    nodes.append(curr)
        for node in nodes:
            yield node.val

    def pre_order(self):
        """Return generator that returns values from BST 'pre ordered'."""
        nodes = []
        curr = self._root
        while len(nodes) != self._length:
            if curr not in nodes:
                nodes.append(curr)
            if curr.left and curr.left not in nodes:
                curr = curr.left
            elif curr.right and curr.right not in nodes:
                curr = curr.right
            else:
                curr = curr.parent
        for node in nodes:
            yield node.val

    def post_order(self):
        """Return generator that returns values from BST 'post ordered'."""
        nodes = []
        curr = self._root
        while len(nodes) != self._length:
            if not curr.right and not curr.left and not curr.parent:
                nodes.append(curr)
            elif curr.left and curr not in nodes and curr.left not in nodes:
                curr = curr.left
            elif not curr.left and not curr.right and curr not in nodes:
                nodes.append(curr)
                if not curr.right:
                    curr = curr.parent
                    while curr != self._root:
                        if curr.left and curr.left not in nodes:
                            curr = curr.left
                            break
                        elif curr.right and curr.right not in nodes:
                            curr = curr.right
                        elif curr.right:
                            nodes.append(curr)
                            curr = curr.parent
                            if curr == self._root and (len(nodes) ==
                                                       self._length - 1):
                                nodes.append(curr)
                        else:
                            nodes.append(curr)
                            curr = curr.parent
                            if curr == self._root and (len(nodes) ==
                                                       self._length - 1):
                                nodes.append(curr)
            elif curr.right:
                curr = curr.right
        for node in nodes:
            yield node.val

    def breadth_first(self):
        """Return generator that returns values from BST 'breadth first'."""
        nodes = []
        curr_index = 0
        nodes.append(self._root)
        while len(nodes) != self._length:
            if nodes[curr_index].left:
                nodes.append(nodes[curr_index].left)
            if nodes[curr_index].right:
                nodes.append(nodes[curr_index].right)
            curr_index += 1
        for node in nodes:
            yield node.val

    def _bal_and_rotate(self, node):
        """Check balance and rotate as needed for full tree."""
        balanced = False
        curr = node
        if curr != self._root:
            par_bal = self._tree_depth(curr.parent)
            if par_bal[0] > par_bal[1]:
                curr = curr.parent.right
            else:
                curr = curr.parent.left
        while not balanced:
            auto_bal = self._check_bal(curr.parent, curr)
            if len(auto_bal) == 2:
                balanced = True
                self._rdepth = auto_bal[0]
                self._ldepth = auto_bal[1]
                self._balance = self._rdepth - self._ldepth
                self._depth = max([self._rdepth, self._ldepth]) + 1
            elif auto_bal[2] == -2 and auto_bal[3] in [-1, 0]:
                self._rotate_right(auto_bal[0])
                curr = auto_bal[0]
            elif auto_bal[2] == 2 and auto_bal[3] in [1, 0]:
                self._rotate_left(auto_bal[0])
                curr = auto_bal[0]
            elif auto_bal[2] == -2 and auto_bal[3] == 1:
                self._rotate_left(auto_bal[1])
                self._rotate_right(auto_bal[0])
                curr = auto_bal[0]
            elif auto_bal[2] == 2 and auto_bal[3] == -1:
                self._rotate_right(auto_bal[1])
                self._rotate_left(auto_bal[0])
                curr = auto_bal[0]
        return

    def _check_bal(self, par_node, child):
        """Check the for balance of tree or sub tree.

        Continues up till out of balance or complete.
        """
        while True:
            if child.right or child.left:
                child_bal = self._tree_depth(child)
            else:
                child_bal = (0, 0)
            if par_node is not None:
                par_bal = self._tree_depth(par_node)
                bal = par_bal[0] - par_bal[1]
                if bal in range(-1, 2):
                    child = par_node
                    par_node = par_node.parent
                else:
                    return par_node, child, bal, child_bal[0] - child_bal[1]
            else:
                return child_bal[0], child_bal[1]

    def _rotate_right(self, node):
        """Right rotation for current node."""
        curr = node.left
        node.left = curr.right
        if node.left:
            node.left.parent = node
        curr.parent = node.parent
        curr.right = node
        node.parent = curr
        if curr.parent:
            if curr.parent.right == node:
                curr.parent.right = curr
            else:
                curr.parent.left = curr
        else:
            self._root = curr
            curr.parent = None
        return

    def _rotate_left(self, node):
        """Left rotation for current node."""
        curr = node.right
        node.right = curr.left
        if node.right:
            node.right.parent = node
        curr.parent = node.parent
        curr.left = node
        node.parent = curr
        if curr.parent:
            if curr.parent.right == node:
                curr.parent.right = curr
            else:
                curr.parent.left = curr
        else:
            self._root = curr
            curr.parent = None
        return

    def _tree_depth(self, node):
        """Get the depth of the tree or sub tree."""
        l_depth = 0
        r_depth = 0
        visited = []
        right_side = False
        curr = None
        if node.left:
            curr = node.left
        elif node.right:
            curr = node.right
        elif node.parent == self._root:
            if node == node.parent.left:
                l_depth += 1
                return (r_depth, l_depth)
            else:
                r_depth += 1
                return (r_depth, l_depth)
        while True:
            if curr == node.right:
                right_side = True
            elif not node.left:
                right_side = True
            if curr != node:
                if curr == curr.parent.left or not curr.parent.left:
                    if curr not in visited:
                        if right_side:
                            r_depth += 1
                        else:
                            l_depth += 1
                elif curr == node.right:
                    if curr not in visited:
                        if right_side:
                            r_depth += 1
                        else:
                            l_depth += 1
            if curr.left and curr.right:
                if curr not in visited:
                    visited.append(curr)
                if curr.left not in visited:
                    curr = curr.left
                elif curr.right not in visited:
                    if curr == node:
                        right_side = True
                    curr = curr.right
                else:
                    curr = curr.parent
            elif curr.left:
                if curr not in visited:
                    visited.append(curr)
                if curr.left not in visited:
                    curr = curr.left
                else:
                    curr = curr.parent
            elif curr.right:
                if curr not in visited:
                    visited.append(curr)
                if curr.right not in visited:
                    curr = curr.right
                else:
                    curr = curr.parent
            else:
                visited.append(curr)
                curr = curr.parent
            if right_side or not node.right:
                if curr == node:
                    return (r_depth, l_depth)

    def _root_shift(self, node, balance):
        """Delete the root of the tree or sub trees."""
        if balance <= 0:
            curr = node.left
            while curr.right:
                curr = curr.right
            if curr != node.left:
                if curr.left:
                    curr.left.parent = curr.parent
                curr.parent.right = curr.left
                curr.left = node.left
                curr.left.parent = curr
            curr.right = node.right
            if node == self._root:
                self._root = curr
                curr.parent = node.parent
            elif node == node.parent.left:
                node.parent.left = curr
                curr.parent = node.parent
            elif node == node.parent.right:
                node.parent.right = curr
                curr.parent = node.parent
            if curr.right:
                curr.right.parent = curr

        else:
            curr = node.right
            while curr.left:
                curr = curr.left
            if curr != node.right:
                if curr.right:
                    curr.right.parent = curr.parent
                curr.parent.left = curr.right
                curr.right = node.right
                curr.right.parent = curr
            curr.left = node.left
            if node == self._root:
                self._root = curr
                curr.parent = node.parent
            elif node == node.parent.left:
                node.parent.left = curr
                curr.parent = node.parent
            elif node == node.parent.right:
                node.parent.right = curr
                curr.parent = node.parent
            if curr.left:
                curr.left.parent = curr

    def _del_small_tree(self, val):
        """Delete node from tree of three or less."""
        to_del = self.search(val)
        if self._length == 1:
            self._root = None
            self._length = 0
            self._depth = 0
            return
        elif self._length == 2:
            self._length -= 1
            if to_del == self._root and to_del.right:
                self._root = to_del.right
                self._root.parent = None
            elif to_del == self._root and to_del.left:
                self._root = to_del.left
                self._root.parent = None
            else:
                self._del_leaf(to_del)
            self._rdepth = 0
            self._ldepth = 0
            self._depth = 1
            self._balance = 0
            return
        else:
            self._length -= 1
            if to_del == self._root:
                to_del.left.parent = None
                self._root = to_del.left
                to_del.right.parent = self._root
                self._root.right = to_del.right
                self._rdepth = 1
                self._ldepth = 0
                self._balance = 1
            else:
                if to_del == self._root.left:
                    self._rdepth = 1
                    self._ldepth = 0
                    self._balance = 1
                else:
                    self._rdepth = 0
                    self._ldepth = 1
                    self._balance = -1
                self._del_leaf(to_del)
            self._depth = 2

    def _del_leaf(self, node):
        """If the node being deleted is a leaf."""
        par = node.parent
        if node == par.left:
            par.left = None
            node.parent = None
            return
        par.right = None
        node.parent = None
        return


class Node():
    """Create a node to add to the Binary Search Tree."""

    def __init__(self, val, parent=None, left=None, right=None):
        """Initialize a new node."""
        self.val = val
        self.parent = parent
        self.left = left
        self.right = right


def _wrapper(func, *args, **kwargs):  # pragma: no cover
    """Create a value for a function with a specific arguement called to it."""
    def _wrapped():
        return func(*args, **kwargs)
    return _wrapped
    #  code found through Erik Enderlein
    #  he found it at http://pythoncentral.io/time-a-python-function/


if __name__ == '__main__':  # pragma: no cover
    best_stuff_tree = BST()
    find5 = _wrapper(best_stuff_tree.search, 5)
    find24 = _wrapper(best_stuff_tree.search, 24)
    nodes = [5, 3, 8, 2.2, 4, 9.5, 1, 2.6,
             3.3, 4.5, 9, 11, 8.5, 10, 14,
             16, 15, 21, 23, 24]
    for node in nodes:
        best_stuff_tree.insert(node)
    print(timeit(find5))
    print(timeit(find24))
