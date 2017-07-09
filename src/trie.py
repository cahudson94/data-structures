"""Implementation of a Trie Tree."""


class TrieTree(object):
    """Create a Trie Tree."""

    def __init__(self):
        """Initalize properties of Tree."""
        self._root = Node(None, 0)
        self._root.parent.append(None)
        self._size = 0

    def insert(self, string):
        """Insert a string into the Tree."""
        if type(string) != str:
            raise TypeError('This tree only contains strings.')
        if self.contains(string):
            raise ValueError('This string is already in the tree.')
        string += '$'
        curr_node = self._root
        char_count = 0
        curr_depth = 0
        while string[char_count] != '$':
            depth_next_list = self._depth_check(curr_depth)
            if depth_next_list:
                for node in depth_next_list:
                    if depth_next_list[node] == string[char_count]:
                        if node not in curr_node.next:
                            curr_node.next.append(node)
                        curr_node = node
                if (curr_node.val != string[char_count] or
                   string[char_count] == string[char_count - 1]):
                    new_node = Node(string[char_count], curr_depth + 1)
                    curr_node.next.append(new_node)
                    curr_node = new_node
            else:
                new_node = Node(string[char_count], curr_depth + 1)
                curr_node.next.append(new_node)
                curr_node = new_node
            curr_depth += 1
            char_count += 1
        curr_node.next.append(string)
        self._size += 1

    def contains(self, string):
        """Return true if the string is in the tree else return false."""
        if type(string) != str:
            raise TypeError('This tree only contains strings.')
        if self.size() == 0:
            return False
        string += '$'
        if string in self._depth_check(len(string) - 1):
            return True
        return False

    def size(self):
        """Return the amount of words in the tree."""
        return self._size

    def remove(self, string):
        """Remove a string from the tree."""
        if type(string) != str:
            raise TypeError('This tree only contains strings.')
        if self.contains(string):
            string += '$'
            char_count = len(string) - 2
            depth_next_list = self._depth_check(char_count)
            for node in depth_next_list:
                if depth_next_list[node] == string[char_count]:
                    curr_node = node
            curr_node.next.remove(string)
            self._size -= 1
            return
        raise ValueError('This string is not in the tree.')

    def depth_traversal(self, start):
        """From the start do a full traversal of the tree."""
        if len(start) > 1:
            raise ValueError('Please provide a single value to start at.')
        if type(start) != str:
            raise TypeError('This tree only contains strings.')
        path = []
        curr_node = self._find_start(start)
        if curr_node:
            expected_len = 1
            curr_index = 0
            while expected_len:
                if curr_node not in path:
                    path.append(curr_node)
                    print(curr_node.val)
                    for node in curr_node.next:
                        if type(node) != str:
                            expected_len += 1
                    expected_len -= 1
                next_node = curr_node.next[curr_index]
                if type(next_node) != str and next_node not in path:
                    curr_node = next_node
                    curr_index = 0
                elif len(curr_node.next) > 1:
                    curr_index += 1
                else:
                    curr_node = curr_node.parent
            for node in path:
                yield node.val
        else:
            raise ValueError('That starting value isn\'t in the tree.')

    def _depth_check(self, depth):
        """Find all nodes at a depth and return as dict with their values."""
        curr = self._root
        to_visit = [self._root]
        depth_next_list = {}
        while to_visit:
            if curr.depth < depth:
                for node in curr.next:
                    if type(node) != str:
                        to_visit.append(node)
            elif curr.depth == depth:
                for node in curr.next:
                    if type(node) != str:
                        if node not in depth_next_list.keys():
                            depth_next_list[node] = node.val
                    else:
                        if node not in depth_next_list.keys():
                            depth_next_list[node] = node
            curr = to_visit[0]
            to_visit.remove(curr)
        return depth_next_list

    def _find_start(self, node_val):
        """Find the starting node for traversal or return None."""
        curr_node = self._root
        to_visit = []
        start_node = None
        while not start_node:
            next_list = self._get_node_val(curr_node)
            for node in next_list:
                if next_list[node] == node_val:
                    start_node = node
                    return start_node
                if type(node) != str:
                    to_visit.append(node)
            if not to_visit:
                return
            curr_node = to_visit[0]
            to_visit.remove(to_visit[0])

    def _print_tree(self):
        """Visualization of the tree."""
        tree = [[]]
        curr_depth = 0
        to_visit = [self._root]
        while to_visit:
            curr = to_visit[0]
            to_visit.remove(to_visit[0])
            if curr.depth != curr_depth:
                curr_depth = curr.depth
            if len(tree) - 1 < curr_depth:
                tree.append([])
            for node in curr.next:
                if type(node) != str:
                    tree[curr_depth].append(node.val)
                    to_visit.append(node)
                else:
                    tree[curr_depth].append(node)
        for i in range(len(tree)):
            print(tree[i - 1])

    def _get_node_val(self, node):
        """Get the list of values for the currents next nodes."""
        nodes = {}
        for i in node.next:
            if type(node) != str:
                nodes[i] = i.val
            else:
                nodes[i] = i
        return nodes


class Node(object):
    """Nodes for Tree."""

    def __init__(self, val, depth):
        """Make a node instance."""
        self.val = val
        self.depth = depth
        self.parent = []
        self.next = []
