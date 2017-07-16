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
        if self.contains(string):
            raise ValueError('This string is already in the tree.')
        curr = self._root
        for char in string[:-1]:
            if char in curr.keys():
                curr = curr[char]
            else:
                curr[char] = {}
                curr = curr[char]
        if string[-1] in curr.keys():
            curr[string[-1]][None] = None
        else:
            curr[string[-1]] = {None: None}
        self._size += 1

    def contains(self, string):
        """Return true if the string is in the tree else return false."""
        if type(string) != str:
            raise TypeError('This tree only contains strings.')
        if self._size == 0:
            return False
        curr = self._root
        idx = 0
        for char in string:
            if char in curr.keys():
                curr = curr[char]
                idx += 1
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
                path += char
                curr = curr[char]
            path = path[:-1]
            if len(curr) == 1:
                self._clean_up(curr, path)
            else:
                curr.pop(None)
            self._size -= 1
            return
        raise ValueError('This string is not in the tree.')

    def _clean_up(self, curr, path):
        """Clean up the nodes from deletion."""
        path_head = path[0]
        while len(curr) == 1:
            curr = self._root
            for i, char in enumerate(path):
                prev = path[i - 1]
                curr = curr[char]
            path = path[:-1]
        if curr == self._root:
            curr.pop(path_head)
        else:
            curr.pop(prev)
