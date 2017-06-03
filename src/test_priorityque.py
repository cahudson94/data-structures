"""Test for Priority Queue data structure."""
import pytest
from priorityque import PriorityQ

# Fixture: Create empty PQ
# Fixture: Create one-item PQ
# Fixture: Create full pq


@pytest.fixture
def build_empty_pq():
    """Build empty pq."""
    return PriorityQ()


@pytest.fixture
def build_one_item_pq():
    """Build one-item pq."""
    p = PriorityQ()
    p.insert('cake', 12)
    return p


@pytest.fixture
def build_mult_item_pq():
    """Build pq with multiple items."""
    p = PriorityQ()
    p.insert('Hello!', 1)
    p.insert([2, 3], 3)
    p.insert(3, 5)
    return p


def test_invalid_priority_list(build_empty_pq):
    """Test ValueError for invalid priority: list."""
    with pytest.raises(ValueError):
        build_empty_pq.insert('content', [3])


def test_invalid_priority_str(build_empty_pq):
    """Test ValueError with invalid priority: string."""
    with pytest.raises(ValueError):
        build_empty_pq.insert('content', 'ok')


def test_invalid_priority_dict(build_empty_pq):
    """Test ValueError with invalid priority: dict.."""
    with pytest.raises(ValueError):
        build_empty_pq.insert('content', {'cookies': 'vanilla'})


def test_invalid_priority_tuple(build_empty_pq):
    """Test ValueError with invalid priority: dict.."""
    with pytest.raises(ValueError):
        build_empty_pq.insert('content', ('1', 1))


def test_insert_no_priority_empty_pq(build_empty_pq):
    """Insert one with no priority, empty PQ."""
    build_empty_pq.insert('greetings!')
    assert build_empty_pq.peek() == [0, 'greetings!']


def test_insert_no_priority_one_item_pq(build_one_item_pq):
    """Insert one with no priority, one-item PQ."""
    build_one_item_pq.insert('greetings!')
    assert [12, 'greetings!'] in build_one_item_pq._list


def test_insert_no_priority_full_pq(build_mult_item_pq):
    """Insert one with no priority, full PQ."""
    build_mult_item_pq.insert([1, 2, 3, 4])
    assert [5, [1, 2, 3, 4]] in build_mult_item_pq._list
    assert [5, [1, 2, 3, 4]] == build_mult_item_pq._list[-1]


def test_insert_one_with_priority_empty_pq(build_empty_pq):
    """Insert one with priority, empty PQ."""
    build_empty_pq.insert({'favorite': 'red'}, -1)
    assert build_empty_pq.peek() == [-1, {'favorite': 'red'}]
    assert len(build_empty_pq._list) == 1


def test_insert_one_with_top_priority_one_item_pq(build_one_item_pq):
    """Insert one with top priority, one-item PQ."""
    build_one_item_pq.insert({'favorite': 'red'}, 10)
    assert build_one_item_pq.peek() == [10, {'favorite': 'red'}]
    assert len(build_one_item_pq._list) == 2


def test_insert_one_with_top_priority_full_pq(build_mult_item_pq):
    """Insert one with top priority, full PQ."""
    build_mult_item_pq.insert('my face', -10)
    assert build_mult_item_pq.peek() == [-10, 'my face']
    assert len(build_mult_item_pq._list) == 4


def test_insert_one_with_middle_priority_full_pq(build_mult_item_pq):
    """Insert one with middle priority, empty PQ."""
    build_mult_item_pq.insert('my face', -10)
    assert build_mult_item_pq.peek() == [-10, 'my face']
    assert len(build_mult_item_pq._list) == 4


"""Insert one with middle priority, empty PQ."""
"""Insert one with middle priority, full PQ."""
"""Insert one with priority, empty PQ."""
"""Insert one with last priority, one-item PQ."""
"""Insert one with last priority, full PQ."""
"""Insert two, one with top priority, one with no priority."""
"""Insert two with middle priority."""
"""Insert two with same val, different priorities."""


# Peek:
"""Peek with empty PQ."""
"""Peek with one item PQ."""
"""Peek with full PQ."""
"""Check peek after multiple pops."""
"""Check peek after 1 insert, 1 pop."""
"""Check peek after 2 inserts, 1 pop."""


# Pop:
"""Pop all items in a PQ."""
"""Check peek after multiple pops."""
"""Pop one item."""
"""Pop empty list."""
