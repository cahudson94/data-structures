"""Testing for inesrt sort."""
from insert_sort import insert_sort
import pytest
from random import randint


TEST_PARAMS = [
    ([i for i in range(50)]),
    ([randint(1, 500) for i in range(50)]),
    ([5, 9, 1, 2, 6])
]


@pytest.mark.parametrize('data', TEST_PARAMS)
def test_insert_sort(data):
    """Test insert sort against data and sorted version of data."""
    assert insert_sort(data) == sorted(data)
