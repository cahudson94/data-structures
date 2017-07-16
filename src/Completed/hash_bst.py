"""Python implementation of Binary Search Tree."""


class BST():  # pragma: no cover
    """Binary Search Tree."""

    def __init__(self):
        """Initialize Binary Search tree."""
        self._root = None
        self._length = 0
        self._rdepth = 0
        self._ldepth = 0
        self._depth = 0
        self._balance = 0

    def insert(self, val, list_pair):
        """Insert new node into Binary Search Tree."""
        if type(val) != int:
            raise TypeError('You can only add numbers to this tree.')
        curr = self._root
        if curr is None:
            curr = Node(val)
            curr._list.append(list_pair)
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
                    curr.left._list.append(list_pair)
                    curr.left.parent = curr
                    self._length += 1
                    self._bal_and_rotate(curr.left)
                    return
            elif val > curr.val:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = Node(val)
                    curr.right._list.append(list_pair)
                    curr.right.parent = curr
                    self._length += 1
                    self._bal_and_rotate(curr.right)
                    return
            else:
                current_keys = []
                for item in curr._list:
                    current_keys.append(item[0])
                if list_pair[0] not in current_keys:
                    curr._list.append(list_pair)
                    return
                else:
                    for item in curr._list:
                        if item[0] == list_pair[0]:
                            curr._list[curr._list.index(item)] = list_pair
                    return

    def search(self, val):
        """Find the node at val in Binary Search Tree."""
        curr = self._root
        if type(val) != int:
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
        lside = {}
        rside = {}
        on_right = False
        curr = None
        if node.left:
            curr = node.left
        elif node.right:
            curr = node.right
        while True:
            if curr == node.right:
                on_right = True
            elif not node.left:
                on_right = True
            if curr == node and curr.left and curr.left in lside.keys():
                    curr = curr.right
                    on_right = True
            elif on_right:
                if curr not in rside.keys() and curr.parent in rside.keys():
                    rside[curr] = rside[curr.parent] + 1
                elif curr == node.right:
                    rside[curr] = 1
                if curr.left and curr.left not in rside.keys():
                    curr = curr.left
                elif curr.right and curr.right not in rside.keys():
                    curr = curr.right
                else:
                    curr = curr.parent
            else:
                if curr not in lside.keys() and curr.parent in lside.keys():
                    lside[curr] = lside[curr.parent] + 1
                elif curr == node.left:
                    lside[curr] = 1
                if curr.left and curr.left not in lside.keys():
                    curr = curr.left
                elif curr.right and curr.right not in lside.keys():
                    curr = curr.right
                else:
                    curr = curr.parent
            if on_right or not node.right:
                if curr == node:
                    if rside and lside:
                        return (max(rside.values()),
                                max(lside.values()))
                    elif rside:
                        return (max(rside.values()), 0)
                    else:
                        return (0, max(lside.values()))


class Node():  # pragma: no cover
    """Create a node to add to the Binary Search Tree."""

    def __init__(self, val, parent=None, left=None, right=None):
        """Initialize a new node."""
        self.val = val
        self._list = []
        self.parent = parent
        self.left = left
        self.right = right
