"""Test for doubly-linked list data structure."""
from doubly_linked_list import DoublyLinkedList
import pytest


EMPTY_LIST_PUSH = DoublyLinkedList()
EMPTY_LIST_APPEND = DoublyLinkedList()

POP_LIST = DoublyLinkedList()
POP_LIST.push('one')
POP_LIST.push('two')
POP_LIST.push('three')

SHIFT_LIST = DoublyLinkedList()
SHIFT_LIST.push('one')
SHIFT_LIST.push('two')
SHIFT_LIST.push('three')

REMOVE_LIST = DoublyLinkedList()
REMOVE_LIST.push('one')
REMOVE_LIST.push('two')
REMOVE_LIST.push('three')

REMOVE_HEAD = DoublyLinkedList()
REMOVE_HEAD.push('one')
REMOVE_HEAD.push('two')

REMOVE_TAIL = DoublyLinkedList()
REMOVE_TAIL.push('one')
REMOVE_TAIL.push('two')


@pytest.fixture
def initialize_empty_dll():
    """Init doubly linked list."""
    return DoublyLinkedList()


@pytest.fixture
def initialize_three_dll():
    """Init doubly linked list."""
    dll = DoublyLinkedList()
    dll.push('one')
    dll.push('two')
    dll.push('three')
    return dll


@pytest.fixture
def dll_push_one():
    """Init doubly linked list."""
    dll = DoublyLinkedList()
    dll.push(5)
    return dll


@pytest.fixture
def dll_push_two():
    """Init doubly linked list."""
    dll = DoublyLinkedList()
    dll.push(5)
    dll.push(3)
    return dll


def test_dll_init(initialize_empty_dll):
    """Test doubly linked list instantiated."""
    assert initialize_empty_dll.head is None
    assert initialize_empty_dll.tail is None


def test_dll_push_to_empty_sets_head(dll_push_one):
    """Test doubly linked list push method sets head."""
    assert dll_push_one.head.val == 5
    assert dll_push_one.head.prev_node is None


def test_dll_push_to_empty_sets_tail(dll_push_one):
    """Test doubly linked list push method sets tail when empty."""
    assert dll_push_one.tail.val == 5
    assert dll_push_one.tail.next_node is None


def test_dll_push_to_non_empty_sets_head(dll_push_one):
    """Test doubly linked list push method sets head."""
    dll = dll_push_one
    dll.push(3)
    assert dll.head.val == 3
    assert dll.head.next_node.val == 5
    assert dll.head.prev_node is None


def test_dll_push_to_non_empty_sets_tail(dll_push_two):
    """Test doubly linked list push method sets tail when empty."""
    assert dll_push_two.tail.val == 5
    assert dll_push_two.tail.prev_node.val == 3
    assert dll_push_two.tail.next_node is None


def test_dll_push_none(initialize_empty_dll):
    """Test ValueError when push method called with no value."""
    with pytest.raises(ValueError):
        initialize_empty_dll.push()


def test_dll_append_to_empty_sets_head():
    """Test doubly linked list append method."""
    EMPTY_LIST_APPEND.append(5)
    assert EMPTY_LIST_APPEND.head.val == 5
    assert EMPTY_LIST_APPEND.head.prev_node is None


def test_dll_append_to_empty_sets_tail():
    """Test doubly linked list append method."""
    assert EMPTY_LIST_APPEND.tail.val == 5
    assert EMPTY_LIST_APPEND.tail.next_node is None


def test_dll_append_to_non_empty_sets_head():
    """Test doubly linked list append method."""
    EMPTY_LIST_APPEND.append('cake')
    assert EMPTY_LIST_APPEND.head.val == 5
    assert EMPTY_LIST_APPEND.head.next_node.val == 'cake'
    assert EMPTY_LIST_APPEND.head.prev_node is None


def test_dll_append_to_non_empty_sets_tail():
    """Test doubly linked list append method."""
    assert EMPTY_LIST_APPEND.tail.val == 'cake'
    assert EMPTY_LIST_APPEND.tail.prev_node.val == 5
    assert EMPTY_LIST_APPEND.tail.next_node is None


def test_dll_append_none():
    """Test ValueError when doubly linked list appended to with None."""
    with pytest.raises(ValueError):
        EMPTY_LIST_APPEND.append()


def test_dll_pop():
    """."""
    popped = POP_LIST.pop()
    assert popped.val == 'three'
    assert POP_LIST.head.val == 'two'


def test_dll_pop_head_reassign():
    """."""
    assert POP_LIST.head.prev_node is None
    assert POP_LIST.head.next_node.val == 'one'


def test_dll_pop_len():
    """."""
    assert len(POP_LIST) == 2


def test_dll_pop_empty(initialize_empty_dll):
    """Test doubly linked list empty pop method."""
    with pytest.raises(IndexError):
        initialize_empty_dll.pop()


def test_dll_shift():
    """Test doubly linked list shift method."""
    shifted = SHIFT_LIST.shift()
    assert shifted.val == 'one'
    assert SHIFT_LIST.tail.val == 'two'


def test_dll_shift_tail_reassign():
    """."""
    assert SHIFT_LIST.tail.next_node is None
    assert SHIFT_LIST.tail.prev_node.val == 'three'


def test_dll_shift_len():
    """."""
    assert len(SHIFT_LIST) == 2


def test_dll_shift_empty(initialize_empty_dll):
    """Test shift method on empty list."""
    with pytest.raises(IndexError):
        initialize_empty_dll.shift()


def test_dll_remove():
    """."""
    old = len(REMOVE_LIST)
    REMOVE_LIST.remove('two')
    assert len(REMOVE_LIST) == old - 1
    assert REMOVE_LIST.tail.prev_node == REMOVE_LIST.head
    assert REMOVE_LIST.head.next_node == REMOVE_LIST.tail


def test_dll_remove_not_found():
    """."""
    with pytest.raises(ValueError):
        REMOVE_TAIL.remove('cake')


def test_dll_remove_from_head():
    """."""
    REMOVE_HEAD.remove('two')
    assert len(REMOVE_HEAD) == 1
    assert REMOVE_HEAD.tail.prev_node is None
    assert REMOVE_HEAD.head.next_node is None


def test_dll_remove_from_tail():
    """."""
    REMOVE_TAIL.remove('one')
    assert len(REMOVE_TAIL) == 1
    assert REMOVE_TAIL.tail.prev_node is None
    assert REMOVE_TAIL.head.next_node is None


def test_dll_remove_invalid():
    """Test doubly linked list remove method not in list."""
    with pytest.raises(ValueError):
        SHIFT_LIST.remove('cake')


def test_dll_len(initialize_three_dll):
    """Test len method."""
    assert len(initialize_three_dll) == 3
