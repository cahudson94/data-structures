"""Radix sort method."""
from random import randint

random_0_to_9 = [randint(0, 9) for x in range(100)]
revers_in_order = [x for x in range(100)][::-1]
random_large = [randint(0, 100000) for x in range(100)][::-1]


def radix(data):
    """A sorting method called Radix."""
    try:
        idx = -1
        longest = 0

        for x in data:
            if not isinstance(x, int):
                    raise TypeError
            if len(str(x)) > longest:
                longest = len(str(x))

        while idx != -longest - 1:
            buckets = {i: [] for i in range(10)}
            for x in data:
                try:
                    buckets[int(str(x)[idx])].append(x)
                except IndexError:
                    buckets[0].append(x)
            idx -= 1
            data_idx = 0
            for i in range(10):
                for item in buckets[i]:
                    data[data_idx] = item
                    data_idx += 1
        return data
    except TypeError:
        return 'This sorting method sorts only one data type.'


if __name__ == '__main__':  # pragma: no cover
    from timeit import Timer
    best = Timer(
        'radix(random_0_to_9)',
        "from __main__ import radix; from __main__ import random_0_to_9"
    )
    worst = Timer(
        'radix(revers_in_order)',
        "from __main__ import radix; from __main__ import revers_in_order"
    )
    random = Timer(
        'radix(random_large)',
        "from __main__ import radix; from __main__ import random_large"
    )
    print("""
Radix sort is a simple sorting algorithm that repeatedly steps through
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
