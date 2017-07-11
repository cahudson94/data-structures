"""Implementation of a Trie Tree."""


class TrieTree(object):
    """Create a Trie Tree."""

    def __init__(self):
        """Initalize properties of Tree."""
        self._root = {}
        self._size = 0

    def insert(self, string):
        """Insert a string into the Tree."""
        if type(string) != str:
            raise TypeError('This tree only contains strings.')
        if len(string) < 1:
            raise ValueError('You must give at least one character.')
        if self.contains(string):
            raise ValueError('This string is already in the tree.')
        curr = self._root
        for char in string[:-1]:
            if char in curr.keys():
                curr = curr[char]
            else:
                curr[char] = {}
                curr = curr[char]
        curr[string[-1]] = {None: ''}
        self._size += 1

    def contains(self, string):
        """Return true if the string is in the tree else return false."""
        if type(string) != str:
            raise TypeError('This tree only contains strings.')
        if self.size() == 0:
            return False
        curr = self._root
        for char in string:
            if char in curr.keys():
                curr = curr[char]
            else:
                return False
        if None in curr.keys():
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
            curr = self._root
            path = ''
            for char in string:
                path += char, ','
                curr = curr[char]
            path = path[:-3]
            if len(curr.keys()) == 1:
                self._clean_up(curr, path)
            else:
                curr.pop(None)
            self._size -= 1
            return
        raise ValueError('This string is not in the tree.')

    def depth_traversal(self, start):
        """From the start do a full traversal of the tree."""
        if type(start) != str:
            raise TypeError('This tree only contains strings.')
        return_chars = []
        root = self._find_start(start)
        if not root:
            raise ValueError('That prefix isn\'t in the tree.')
        return_chars.append(start)
        to_visit = []
        for key in root.keys():
            to_visit.append(key)
        tree = self._find_all_paths(root, to_visit)
        for char in tree:
            return_chars.append(char)
        for string in return_chars:
            yield string

    def _clean_up(self, curr, path):
        """Find all nodes at a depth and return as dict with their values."""
        while len(curr.keys()) == 1:
            for char in path:
                curr = self._root
                curr = curr[char]
            path = path[:-2]
        curr.pop(None)

    def _find_start(self, prefix):
        """Find the starting node for traversal or return None."""
        curr = self._root
        for char in prefix:
            if char in curr.keys():
                curr = curr[char]
            else:
                return
        return curr

    # def _find_all_paths(self, path, children):
    #     """Find all characters under the path."""
    #     curr = path[children[0]]
    #     sub_trees = {}
    #     curr_path = []
    #     return_chars = []
    #     while None not in curr.keys():
    #         return_chars.append(children[0])
    #         children.remove(children[0])
