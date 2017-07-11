"""Implementation of bubble sort."""


def bubble_sort(data):
    """Sort the given input if it contains numbers or return error."""
    if type(data) in [list, tuple]:
        for char in data:
            if type(char) in [int, float]:
                raise TypeError('Can only sort numbers.')
    curr_iteration = []
    prev_iteration = []
    for num in data:
        if type(data) == tuple:
            curr_iteration.append(num)
        else:
            curr_iteration = data
    while curr_iteration != prev_iteration:
        prev_iteration = curr_iteration
        curr_index = 0
        for num in curr_iteration[:-1]:
            if num > curr_iteration[curr_index + 1]:
                curr_iteration[curr_index] = curr_iteration[curr_index + 1]
                curr_iteration[curr_index + 1] = num
            curr_index += 1
    return curr_iteration
