"""Implementation of bubble sort."""


def bubble_sort(data):
    """Sort the given input if it contains numbers or return error."""
    try:
        curr = list(data)
        prev = []
        idx = 0
        size = len(curr) - 1
        while curr != prev:
            prev = curr[:]
            if idx == size and curr == prev:
                return curr
            if not isinstance((curr[idx + 1]), type(curr[idx])):
                    raise TypeError()
            if curr[idx] > curr[idx + 1]:
                curr[idx], curr[idx + 1] = curr[idx + 1], curr[idx]
                if curr[idx + 1] == curr[size]:
                    size -= 1
                    idx = -1
            elif idx != size:
                prev = []
            idx += 1
    except TypeError:
        raise TypeError('Please only pass in an iterable of numbers.')


if __name__ == '__main__':  # pragma: no cover
    from timeit import Timer
    best = Timer(
        'bubble_sort([x for x in range(100)])',
        "from __main__ import bubble_sort"
    )
    worst = Timer(
        'bubble_sort([x for x in range(100)][::-1])',
        "from __main__ import bubble_sort; from random import randint"
    )
    random = Timer(
        'bubble_sort([randint(0, 1000) for x in range(100)][::-1])',
        "from __main__ import bubble_sort; from random import randint"
    )
    print("""
Bubble sort is a simple sorting algorithm that repeatedly steps through
the list to be sorted, compares each pair of adjacent items and swaps
them if they are in the wrong order.
""")
    print("#================= best case search 10000x ==============#")
    print(best.timeit(number=1000))
    print('')
    print("#================= worse case search 10000x==============#")
    print(worst.timeit(number=1000))
    print('')
    print("#================= random case search 10000x=============#")
    print(worst.timeit(number=1000))
    print('')
