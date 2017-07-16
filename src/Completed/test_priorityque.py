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
    assert build_empty_pq.peek() == 'greetings!'


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
    assert build_empty_pq.peek() == {'favorite': 'red'}
    assert len(build_empty_pq._list) == 1


def test_insert_one_with_top_priority_one_item_pq(build_one_item_pq):
    """Insert one with top priority, one-item PQ."""
    build_one_item_pq.insert({'favorite': 'red'}, 10)
    assert build_one_item_pq.peek() == {'favorite': 'red'}
    assert len(build_one_item_pq._list) == 2


def test_insert_one_with_top_priority_full_pq(build_mult_item_pq):
    """Insert one with top priority, full PQ."""
    build_mult_item_pq.insert('my face', -10)
    assert build_mult_item_pq.peek() == 'my face'
    assert len(build_mult_item_pq._list) == 4


def test_insert_one_with_middle_priority_full_pq(build_mult_item_pq):
    """Insert one with middle priority, full PQ."""
    build_mult_item_pq.insert('my face', 2)
    assert build_mult_item_pq._list[1] == [2, 'my face']
    assert len(build_mult_item_pq._list) == 4


def test_insert_one_with_priority_one_item_pq(build_one_item_pq):
    """Insert one with last priority, one-item PQ."""
    build_one_item_pq.insert([12, 15, 27], 100)
    assert build_one_item_pq._list[1] == [100, [12, 15, 27]]
    assert len(build_one_item_pq._list) == 2


def test_insert_one_with_priority_full_pq(build_mult_item_pq):
    """Insert one with last priority, full PQ."""
    build_mult_item_pq.insert([12, 15, 27], 100)
    assert build_mult_item_pq._list[-1] == [100, [12, 15, 27]]
    assert len(build_mult_item_pq._list) == 4


def test_insert_one_with_one_without_priority_full_pq(build_mult_item_pq):
    """Insert two, one with top priority, one with no priority."""
    build_mult_item_pq.insert('bits and pieces', -10)
    build_mult_item_pq.insert([12, 15, 27])
    assert build_mult_item_pq._list[0] == [-10, 'bits and pieces']
    assert build_mult_item_pq._list[-1] == [5, [12, 15, 27]]
    assert len(build_mult_item_pq._list) == 5


def test_insert_two_with_middle_priority_full_pq(build_mult_item_pq):
    """Insert two with middle priority."""
    build_mult_item_pq.insert('bits and pieces', 3.3)
    build_mult_item_pq.insert([12, 15, 27], 4.7)
    assert build_mult_item_pq._list[2] == [3.3, 'bits and pieces']
    assert build_mult_item_pq._list[3] == [4.7, [12, 15, 27]]
    assert len(build_mult_item_pq._list) == 5


def test_insert_two_with_same_val_different_priority(build_one_item_pq):
    """Insert two with same val, different priorities."""
    build_one_item_pq.insert('pie', 100)
    build_one_item_pq.insert('pie', 50)
    assert build_one_item_pq._list[2] == [100, 'pie']
    assert build_one_item_pq._list[1] == [50, 'pie']
    assert len(build_one_item_pq._list) == 3


def test_peek_empty_pq(build_empty_pq):
    """Peek with empty PQ."""
    with pytest.raises(IndexError):
        build_empty_pq.peek()


def test_peek_one_item_pq(build_one_item_pq):
    """Peek with empty PQ."""
    peeked = build_one_item_pq.peek()
    assert peeked == 'cake'


def test_peek_full_pq(build_mult_item_pq):
    """Peek with empty PQ."""
    peeked = build_mult_item_pq.peek()
    assert peeked == 'Hello!'


def test_peek_mult_pops(build_mult_item_pq):
    """Check peek after multiple pops."""
    assert build_mult_item_pq.pop() == 'Hello!'
    assert build_mult_item_pq.pop() == [2, 3]
    assert build_mult_item_pq.peek() == 3


def test_peek_after_pop(build_one_item_pq):
    """Check peek after 1 insert, 1 pop."""
    build_one_item_pq.insert('content', 20)
    assert build_one_item_pq.pop() == 'cake'
    assert build_one_item_pq.peek() == 'content'


def test_peek_after_inserts_one_pop(build_mult_item_pq):
    """Check peek after 2 inserts, 1 pop."""
    build_mult_item_pq.insert('content', 20)
    build_mult_item_pq.insert('my face', -100)
    assert build_mult_item_pq.pop() == 'my face'
    assert build_mult_item_pq.peek() == 'Hello!'


def test_pop_all(build_mult_item_pq):
    """Pop all items in a PQ."""
    assert build_mult_item_pq.pop() == 'Hello!'
    assert build_mult_item_pq.pop() == [2, 3]
    assert build_mult_item_pq.pop() == 3
    assert len(build_mult_item_pq._list) == 0


def test_pop_one(build_one_item_pq):
    """Pop one item."""
    assert build_one_item_pq.pop() == 'cake'


def test_pop_empty(build_empty_pq):
    """Pop empty list."""
    with pytest.raises(IndexError):
        build_empty_pq.pop()
