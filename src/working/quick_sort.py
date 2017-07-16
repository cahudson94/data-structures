"""Quick sort data structure."""


def quicksort(data):
    """Sorting algorithm for quick sort."""
    try:
        if len(data) > 1:
            mid = data[0]
            left = []
            right = []

            for item in data[1:]:
                # This slows it down by almost a second but covers 2.7
                if not isinstance(item, type(mid)):
                    raise TypeError
                if item >= mid:
                    right.append(item)
                else:
                    left.append(item)

            quicksort(left)
            quicksort(right)

            di = 0
            li = 0
            ri = 0

            while len(left) > li:
                data[di] = left[li]
                li += 1
                di += 1

            data[di] = mid
            di += 1

            while len(right) > ri:
                data[di] = right[ri]
                ri += 1
                di += 1

        return data

    except TypeError:
        return 'This sort method only accepts values of one type in a list.'


if __name__ == '__main__':  # pragma: no cover
    from timeit import Timer
    best = Timer(
        'quicksort([x for x in range(100)])',
        "from __main__ import quicksort"
    )
    worst = Timer(
        'quicksort([x for x in range(100)][::-1])',
        "from __main__ import quicksort"
    )
    random = Timer(
        'quicksort([randint(0, 1000) for x in range(100)][::-1])',
        "from __main__ import quicksort; from random import randint"
    )
    print("""
Quick sort is a sorting algorithm that repeatedly breaks the list of
items to be sorted in half till you have a pair. Then compares each
pair of items and swaps them if they are in the wrong order.
Then works back up to the main list.
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
