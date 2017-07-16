"""Python implementation of binary heap data structure."""


class BinaryHeap(object):
    """Attributes and methods of the min Binary Heap data structure."""

    def __init__(self, iterable=None):
        """Init binheap."""
        self._list = []
        if type(iterable) in [list, tuple, str]:
            for i in iterable:
                self.push(i)
        elif iterable is not None:
            raise TypeError('Try again with a list, tuple, or string.')

    def push(self, val):
        """Add value to the bottom of heap and bubbles up as appropriate."""
        if type(val) not in [int, float]:
            raise ValueError('Please enter a number.')
        if val in self._list:
            raise ValueError('{} is already in this heap.'.format(val))
        else:
            self._list.append(val)
            curr_index = len(self._list) - 1
            bubble = True
            while bubble and curr_index > 0:
                if curr_index % 2 == 0:
                    par_index = int((curr_index - 2) / 2)
                    if self._list[curr_index] < self._list[par_index]:
                        curr_val = self._list[curr_index]
                        par_val = self._list[par_index]
                        self._list[curr_index] = par_val
                        self._list[par_index] = curr_val
                        curr_index = par_index
                    else:
                        bubble = False
                elif curr_index % 2 != 0:
                    par_index = int((curr_index - 1) / 2)
                    if self._list[curr_index] < self._list[par_index]:
                        curr_val = self._list[curr_index]
                        par_val = self._list[par_index]
                        self._list[curr_index] = par_val
                        self._list[par_index] = curr_val
                        curr_index = par_index
                    else:
                        bubble = False

    def pop(self):
        """Remove top of heap and bubbles last down."""
        if len(self._list) < 1:
            raise IndexError('Nothing to pop on this heap.')
        popped = self._list[0]
        self._list[0] = self._list[-1]
        self._list[-1] = popped
        self._list.pop(-1)
        bubble = True
        curr_index = 0
        while bubble:
            right = False
            left = False
            if (len(self._list) - 1) >= (curr_index * 2) + 2:
                right = (curr_index * 2) + 2
            if (len(self._list) - 1) >= (curr_index * 2) + 1:
                left = (curr_index * 2) + 1
            if right and left and self._list[curr_index] > self._list[left] and self._list[curr_index] > self._list[right]:
                if self._list[right] < self._list[left]:
                    right_child = self._list[right]
                    curr_val = self._list[curr_index]
                    self._list[curr_index] = right_child
                    self._list[right] = curr_val
                    curr_index = right
                else:
                    left_child = self._list[left]
                    curr_val = self._list[curr_index]
                    self._list[curr_index] = left_child
                    self._list[left] = curr_val
                    curr_index = left
            elif left and self._list[curr_index] > self._list[left]:
                left_child = self._list[left]
                curr_val = self._list[curr_index]
                self._list[curr_index] = left_child
                self._list[left] = curr_val
                curr_index = left
            elif right and self._list[curr_index] > self._list[right]:
                right_child = self._list[right]
                curr_val = self._list[curr_index]
                self._list[curr_index] = right_child
                self._list[right] = curr_val
                curr_index = right
            else:
                bubble = False
        return popped
