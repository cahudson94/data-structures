"""Tests for bubble sort."""
from bubble_sort import bubble_sort
import pytest

PARAMS_TABLE = [
    ([234, 23, 52, 66], [23, 52, 66, 234]),
    ([4, 3, 2, 1], [1, 2, 3, 4]),
    ((99, 22, 55, 4, 66, 87, 23, 11), [4, 11, 22, 23, 55, 66, 87, 99]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
]


def test_strings_error_handling_in_bubble_sort():
    """Test that an error is thrown if there is a string."""
    with pytest.raises(TypeError):
        bubble_sort([1, 'blkja', 2324, 3])


def test_iterable_type_error_handling():
    """Test if not list or tuple, ValueError raised."""
    with pytest.raises(TypeError):
        bubble_sort(('sfajlfka', 1, 5))


@pytest.mark.parametrize('data, result', PARAMS_TABLE)
def test_bubble_sort(data, result):
    """Parametrized test for the bubble sort."""
    assert bubble_sort(data) == result
