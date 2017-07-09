"""Implementation of a Trie Tree."""


class TrieTree(object):
    """Create a Trie Tree."""

    def __init__(self):
        """Initalize properties of Tree."""
        self._root = Node(None)
        self._size = 0

    def insert(self, string):
        """Insert a string into the Tree."""
        if type(string) != str:
            raise TypeError('This tree only contains strings.')
        if self.contains(string):
            raise ValueError('This string is already in the tree.')
        string = string.lower()
        string += '$'
        curr_node = self._root
        char_count = 0
        while string[char_count] != '$':
            next_list = self._get_node_val(curr_node)
            if next_list:
                for node in next_list:
                    if next_list[node] == string[char_count]:
                        curr_node = node
                if curr_node.val != string[char_count]:
                    new_node = Node(string[char_count])
                    curr_node.next.append(new_node)
                    curr_node = new_node
            else:
                new_node = Node(string[char_count])
                curr_node.next.append(new_node)
                curr_node = new_node
            char_count += 1
        curr_node.next.append(string[char_count])
        self._size += 1

    def contains(self, string):
        """Return true if the string is in the tree else return false."""
        if type(string) != str:
            raise TypeError('This tree only contains strings.')
        if self.size() == 0:
            return False
        string += '$'
        curr_node = self._root
        char_count = 0
        while curr_node != '$':
            next_list = self._get_node_val(curr_node)
            if next_list:
                for node in next_list:
                    if next_list[node] == string[char_count]:
                        curr_node = node
                        if curr_node == '$':
                            return True
                if curr_node.val != string[char_count]:
                    return False
            char_count += 1

    def size(self):
        """Return the amount of words in the tree."""
        return self._size

    def remove(self, string):
        """Remove a string from the tree."""
        if type(string) != str:
            raise TypeError('This tree only contains strings.')
        if self.contains(string):
            curr_node = self._root
            char_count = 0
            prev_node = None
            while len(curr_node.next) > 1:
                next_list = self._get_node_val(curr_node)
                for node in next_list:
                    if next_list[node] == string[char_count]:
                        prev_node = curr_node
                        curr_node = node
                char_count += 1
            prev_node.next.remove(curr_node)
            self._size -= 1
            return
        raise ValueError('This string is not in the tree.')

    def _get_node_val(self, node):
        """Get the list of values for the currents next nodes."""
        nodes = {}
        for i in node.next:
            if i != '$':
                nodes[i] = i.val
            else:
                nodes[i] = i
        return nodes


class Node(object):
    """Nodes for Tree."""

    def __init__(self, val):
        """Make a node instance."""
        self.val = val
        self.next = []
