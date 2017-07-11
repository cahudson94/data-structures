"""Implementation of bubble sort."""


def bubble_sort(data):
    """Sort the given input if it contains numbers or return error."""
    if type(data) in [list, tuple]:
        for char in data:
            if type(char) not in [int, float]:
                raise TypeError('Can only sort numbers.')
    else:
        raise TypeError('Please provide an iterable of numbers.')
    current = []
    prev = []
    if type(data) == tuple:
        for num in data:
            current.append(num)
    else:
        current = data
    idx = 0
    size = len(current) - 1
    while current != prev:
        prev = current[:]
        if idx == size + 1:
            idx = 0
        if current[idx] > current[idx + 1]:
            temp = current[idx]
            current[idx] = current[idx + 1]
            current[idx + 1] = temp
            if current[idx + 1] == current[size]:
                size -= 1
            print(size)
            print(current)
            print(idx)
        elif size != 0:
            prev = []
        idx += 1
    return current
