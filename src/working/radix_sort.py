"""Radix sort method."""


def radix(data):
    """A sorting method called Radix."""
    try:
        idx = -1
        longest = 0

        for x in data:
            if len(str(x)) > longest:
                longest = len(str(x))

        while idx != -longest - 1:
            buckets = {i: [] for i in range(10)}
            for x in data:
                try:
                    buckets[int(str(x)[idx])].append(x)
                except IndexError:
                    buckets[0].append(x)
                except ValueError:
                    raise TypeError()
            idx -= 1
            sorted_data = []
            for i in range(10):
                for item in buckets[i]:
                    sorted_data.append(item)
            data = sorted_data
        return data
    except TypeError:
        return 'This sorting method sorts only one data type.'


f __name__ == '__main__':  # pragma: no cover
    from timeit import Timer
    best = Timer(
        'radix([x for x in range(100)])',
        "from __main__ import radix"
    )
    worst = Timer(
        'radix([x for x in range(100)][::-1])',
        "from __main__ import radix; from random import randint"
    )
    random = Timer(
        'radix([randint(0, 1000) for x in range(100)][::-1])',
        "from __main__ import radix; from random import randint"
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
