"""Testing for quick sort."""
from quick_sort import quicksort
import pytest
from random import randint


TEST_PARAMS = [
    ([i for i in range(50)]),
    ([randint(1, 500) for i in range(50)]),
    ([5, 9, 1, 2, 6]),
    ([234, 23, 52, 66]),
    ([4, 3, 2, 1]),
    ([99, 22, 55, 4, 66, 87, 23, 11]),
    ([1, 2, 3, 4, 5]),
]


@pytest.mark.parametrize('data', TEST_PARAMS)
def test_quick_sort(data):
    """Test quick sort against data and sorted version of data."""
    assert quicksort(data) == sorted(data)


def test_strings_error_handling_in_quick_sort():
    """Test that an error is thrown if there is a string."""
    assert quicksort([1, 'blkja', 2324, 3]) == 'This sort method \
only accepts values of one type in a list.'


def test_iterable_type_error_handling():
    """Test if not list or tuple, ValueError raised."""
    assert quicksort(('sfajlfka', 1, 5)) == 'This sort method \
only accepts values of one type in a list.'
