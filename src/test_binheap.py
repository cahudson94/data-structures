"""Test for Binary Heap data structure."""
from binheap import BinaryHeap
import pytest


@pytest.fixture
def build_empty_heap():
    """Init an empty bin heap."""
    bh = BinaryHeap()
    return bh


@pytest.fixture
def build_heap_of_one():
    """Init an empty bin heap."""
    bh = BinaryHeap()
    bh.push(1)
    return bh


@pytest.fixture
def build_heap_of_two():
    """Init an empty bin heap."""
    bh = BinaryHeap()
    bh.push(6)
    bh.push(2)
    return bh


@pytest.fixture
def build_heap_of_five():
    """Init an empty bin heap."""
    bh = BinaryHeap()
    bh.push(2)
    bh.push(7)
    bh.push(15)
    bh.push(6)
    bh.push(27)
    return bh


@pytest.fixture
def build_heap_of_ten():
    """Init an empty bin heap."""
    bh = BinaryHeap()
    bh.push(2)
    bh.push(7)
    bh.push(15)
    bh.push(6)
    bh.push(27)
    bh.push(16)
    bh.push(1)
    bh.push(3)
    bh.push(8)
    bh.push(9)
    return bh
