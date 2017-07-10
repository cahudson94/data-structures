"""Implementation of a Trie Tree."""


class TrieTree(object):
    """Create a Trie Tree."""

    def __init__(self):
        """Initalize properties of Tree."""
        self._root = Node(None, 0)
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
        if type(start) != str:
            raise TypeError('This tree only contains strings.')
        words = []
        curr_node = self._find_start(start)
        if not curr_node:
            raise ValueError('That prefix isn\'t in the tree.')
        if curr_node.val:
            to_visit = [curr_node]
            while to_visit:
                curr_node = to_visit[0]
                for node in curr_node.next:
                    if type(node) == str:
                        words.append(node[:-1])
                    else:
                        to_visit.append(node)
                to_visit.remove(curr_node)
            for word in words:
                if word.startswith(start):
                    yield word

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
        curr_index = 0
        prev = None
        while curr_index != len(node_val):
            prev = curr_node
            next_list = self._get_node_val(curr_node)
            for node in next_list:
                if next_list[node] == node_val[curr_index]:
                    curr_node = node
            curr_index += 1
            if prev == curr_node:
                return
        return curr_node

    def _get_node_val(self, node):
        """Get the list of values for the currents next nodes."""
        nodes = {}
        for i in node.next:
            if type(i) != str:
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
        self.next = []
