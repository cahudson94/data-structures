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
    bh.push(2.254)
    return bh


@pytest.fixture
def build_heap_of_five():
    """Init an empty bin heap."""
    bh = BinaryHeap()
    bh.push(2)
    bh.push(7)
    bh.push(15)
    bh.push(6.5)
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
    bh.push(1.5)
    bh.push(3)
    bh.push(8)
    bh.push(9)
    return bh


def test_bheap_init_empty():
    """Init with no arg."""


def test_bheap_init_tuple_one_val():
    """Init with one-item tuple."""


def test_bheap_init_tuple_mult_val():
    """Init with longer tuple."""


def test_bheap_init_list_one_val():
    """Init with one-item list."""


def test_bheap_init_list_mult_val():
    """Init with longer list."""


def test_bheap_init_list_one_bad_val():
    """Init with longer list and one bad val."""
    assert list has good vals before bad
    raises error


def test_bheap_push_string():
    """Test error on pushing string."""


def test_bheap_push_none():
    """Test error on pushing None."""


def test_bheap_push_dict():
    """Test error on pushing dicts."""


def test_bheap_push_bool():
    """Test error on pushing bool."""


def test_bheap_push_one_to_empty():
    """Test pushing one valid val."""


def test_bheap_push_mult_to_empty():
    """Test pushing multiple vals."""


def test_bheap_push_one_to_many():
    """Test pushing one valid val."""


def test_bheap_push_mult_to_many():
    """Test pushing multiple vals."""


def test_bheap_push_val_top():
    """Test pushing lowest val in min heap."""


def test_bheap_push_val_end():
    """Test pushing end in min heap."""


def test_bheap_push_val_middle():
    """Test pushing middle val to correct index."""


def test_bheap_pop_empty_heap():
    """Test raised error on pop empty heap."""
    with pytest.raises():


def test_bheap_pop_once_left():
    """Test pop on value on a left branch."""


def test_bheap_pop_once_right():
    """Test pop on value on a right branch."""


def test_bheap_pop_mult():
    """Test pop on multiple values."""


def test_bheap_pop_all():
    """Test pop on all list items."""


def test_bheap_push_pop():
    """Test pushing and then popping."""


def test_bheap_pop_push():
    """Test popping and pushing."""


def test_bheap_push_pop():
    """Test pushing twice and then popping."""


def test_bheap_pop_push():
    """Test popping twice and pushing."""


def test_bheap_pop_push_equal():
    """Test popping twice and pushing twice."""
