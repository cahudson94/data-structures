"""Python implementation of a priority queue sorted by min numbers."""


class PriorityQ(object):
    """Define atributes and methods of PQ class."""

    def __init__(self):
        """Initialize PQ instance."""
        self._list = []

    def insert(self, val, priority=None):
        """Add a value to the PQ."""
        new_item = [priority, val]
        if new_item[0] is None and self._list:
            new_item[0] = self._list[-1][0]
        if new_item[0] is None:
            new_item[0] = 0
        if type(new_item[0]) not in (int, float):
            raise ValueError('Please entera number for priority.')
        if len(self._list) == 0:
            self._list.append(new_item)
            return
        for i in range(len(self._list)):
            if self._list[i][0] > new_item[0]:
                self._list.insert(i, new_item)
                return
        self._list.append(new_item)

    def peek(self):
        """Return the highest priority item in PQ."""
        if len(self._list):
            return self._list[0]
        return "No items in priority queue."

    def pop(self):
        """Remove and return highest priority item in PQ."""
        if len(self._list):
            return self._list.pop(0)
        return "No items to pop in priority queue."
