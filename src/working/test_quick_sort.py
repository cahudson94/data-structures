"""Testing for inesrt sort."""
from quick_sort import quicksort
import pytest
from random import randint


TEST_PARAMS = [
    ([i for i in range(50)]),
    ([randint(1, 500) for i in range(50)]),
    ([5, 9, 1, 2, 6])
]


PARAMS_TABLE = [
    ([234, 23, 52, 66], [23, 52, 66, 234]),
    ([4, 3, 2, 1], [1, 2, 3, 4]),
    ([99, 22, 55, 4, 66, 87, 23, 11], [4, 11, 22, 23, 55, 66, 87, 99]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
]


@pytest.mark.parametrize('data', TEST_PARAMS)
def test_insert_sort(data):
    """Test insert sort against data and sorted version of data."""
    assert quicksort(data) == sorted(data)


def test_strings_error_handling_in_bubble_sort():
    """Test that an error is thrown if there is a string."""
    assert quicksort([1, 'blkja', 2324, 3]) == 'This sort method \
only accepts values of one type in a list.'


def test_iterable_type_error_handling():
    """Test if not list or tuple, ValueError raised."""
    assert quicksort(('sfajlfka', 1, 5)) == 'This sort method \
only accepts values of one type in a list.'


@pytest.mark.parametrize('data, result', PARAMS_TABLE)
def test_bubble_sort(data, result):
    """Parametrized test for the bubble sort."""
    assert quicksort(data) == result
