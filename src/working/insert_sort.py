"""Implementation of insert sort."""


def insert_sort(data):
    """Sort data via insertion."""
    try:
        idx = 0
        count = 1
        for x in data[1:]:
            while x < data[idx]:
                data[idx], data[idx + 1] = data[idx + 1], data[idx]
                if idx:
                    idx -= 1
            idx = count
            count += 1
        return data
    except TypeError:
        return ('Please provide an iterable with only one input type.')


if __name__ == '__main__':  # pragma: no cover
    from timeit import Timer
    best = Timer(
        'insert_sort([x for x in range(100)])',
        "from __main__ import insert_sort"
    )
    worst = Timer(
        'insert_sort([x for x in range(100)][::-1])',
        "from __main__ import insert_sort; from random import randint"
    )
    random = Timer(
        'insert_sort([randint(0, 1000) for x in range(100)][::-1])',
        "from __main__ import insert_sort; from random import randint"
    )
    print("""
Insert sort is a simple sorting algorithm that steps through
the list to be sorted, and if a value is lower iterates it forward
to it's appropriate position.
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
