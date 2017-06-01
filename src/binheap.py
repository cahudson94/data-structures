"""Python implementation of binary heap data structure."""


class BinaryHeap(object):
    """Attributes and methods of the min Binary Heap data structure."""

    def __init__(self):
        """Init binheap."""
        self.list = []

    def push(self, val):
        """Add value to the bottom of heap and bubbles up as appropriate."""
        if val is None:
            raise ValueError('Please enter a value')
        if val in self.list:
            raise ValueError('{} is already in this heap.'.format(val))
        else:
            print(self.list)
            self.list.append(val)
            curr_index = len(self.list) - 1
            print('current index:', curr_index)
            bubble = True
            while bubble and curr_index > 0:
                if curr_index % 2 == 0:
                    par_index = int((curr_index - 2) / 2)
                    print('right, cur/par:', curr_index, par_index)
                    if self.list[curr_index] < self.list[par_index]:
                        curr_val = self.list[curr_index]
                        par_val = self.list[par_index]
                        self.list[curr_index] = par_val
                        self.list[par_index] = curr_val
                        curr_index = par_index
                    else:
                        bubble = False
                elif curr_index % 2 != 0:
                    par_index = int((curr_index - 1) / 2)
                    print('left, cur/par:', curr_index, par_index)
                    if self.list[curr_index] < self.list[par_index]:
                        curr_val = self.list[curr_index]
                        par_val = self.list[par_index]
                        self.list[curr_index] = par_val
                        self.list[par_index] = curr_val
                        curr_index = par_index
                    else:
                        bubble = False

    def pop(self):
        """Remove top of heap and bubbles last down."""
        if len(self.list) < 1:
            raise IndexError('Nothing to pop on this heap.')
        popped = self.list[0]
        self.list[0] = self.list[-1]
        self.list[-1] = popped
        self.list.pop(-1)
        bubble = True
        curr_index = 0
        while bubble:
            right = False
            left = False
            if (len(self.list) - 1) >= (curr_index * 2) + 2:
                right = (curr_index * 2) + 2
            if (len(self.list) - 1) >= (curr_index * 2) + 1:
                left = (curr_index * 2) + 1
            if right and left:
                if self.list[curr_index] > self.list[left]:
                    if self.list[curr_index] > self.list[right]:
                        if self.list[right] < self.list[left]:
                            right_child = self.list[right]
                            curr_val = self.list[curr_index]
                            self.list[curr_index] = right_child
                            self.list[right] = curr_val
                            curr_index = right
                        else:
                            left_child = self.list[left]
                            curr_val = self.list[curr_index]
                            self.list[curr_index] = left_child
                            self.list[left] = curr_val
                            curr_index = left
            elif right:
                if self.list[curr_index] > self.list[right]:
                    right_child = self.list[right]
                    curr_val = self.list[curr_index]
                    self.list[curr_index] = right_child
                    self.list[right] = curr_val
                    curr_index = right
            elif left:
                if self.list[curr_index] > self.list[left]:
                    left_child = self.list[left]
                    curr_val = self.list[curr_index]
                    self.list[curr_index] = left_child
                    self.list[left] = curr_val
                    curr_index = left
            else:
                bubble = False
        return popped
