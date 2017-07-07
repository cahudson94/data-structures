"""Hash table data structure using Binary Search Tree."""
from hash_bst import BST


class HashTable(object):
    """Create Hash Table with set size."""

    def __init__(self, size, hash_type=None):
        """Initialize a hash table with a hash function or default."""
        self._buckets = []
        for i in range(size):
            self._buckets.append(BST())
        if hash_type is None:
            self._hash = self._mega_hash
        else:
            self._hash == hash_type

    def get(self, key):
        """
        Return the value associated with the key in the hash table.

        If there is no value or key raise KeyError.
        """
        hash_val = self._hash(key)
        modulo_val = hash_val % len(self._buckets)
        node = self._buckets[modulo_val].search(hash_val)
        if node:
            for pair in node._list:
                if pair[0] == key:
                    return pair[1]
        raise KeyError("Key is not in Hash Table.")

    def set(self, key, val):
        """Add key value pairs to hash table."""
        hash_val = self._hash(key)
        modulo_val = hash_val % len(self._buckets)
        self._buckets[modulo_val].insert(hash_val, (key, val))

    def _mega_hash(self, key):
        """MEGAAAA Hash a key."""
        big_diff = ord(key[-1]) * 7879
        lil_diff = 0
        for char in key:
            lil_diff += ord(char)
        return int(((lil_diff + big_diff) * 11839) / 503)


def naive_hash(key):
    """Additive hashing method."""
    hash_val = 0
    for char in key:
        hash_val += ord(char)
    return hash_val
