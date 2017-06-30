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
    """Init empty doubly linked list."""
    return DoublyLinkedList()


@pytest.fixture
def initialize_three_dll():
    """Init doubly linked list and push/append three vals."""
    dll = DoublyLinkedList()
    dll.push('two')
    dll.push('three')
    dll.append('one')
    return dll


@pytest.fixture
def dll_push_one():
    """Init doubly linked list and push one val."""
    dll = DoublyLinkedList()
    dll.push(5)
    return dll


@pytest.fixture
def dll_push_two():
    """Init doubly linked list and push two vals."""
    dll = DoublyLinkedList()
    dll.push(5)
    dll.push(3)
    return dll


@pytest.fixture
def dll_append_one():
    """Init doubly linked list and append one val."""
    dll = DoublyLinkedList()
    dll.append(5)
    return dll


@pytest.fixture
def dll_append_two():
    """Init doubly linked list and append two val."""
    dll = DoublyLinkedList()
    dll.append(5)
    dll.append('cake')
    return dll


@pytest.fixture
def initialize_three_and_pop_dll():
    """Init doubly linked list and add three values then pop one."""
    dll = DoublyLinkedList()
    dll.push('two')
    dll.push('three')
    dll.append('one')
    dll.pop()
    return dll


@pytest.fixture
def initialize_three_and_shift_dll():
    """Init doubly linked list and add three values then pop one."""
    dll = DoublyLinkedList()
    dll.push('two')
    dll.push('three')
    dll.append('one')
    dll.shift()
    return dll


@pytest.fixture
def initialize_two_dll():
    """Init doubly linked list with two values."""
    dll = DoublyLinkedList()
    dll.append('two')
    dll.append('one')
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


def test_dll_push_len(dll_push_one):
    """Test doubly linked list push method adds to len."""
    assert len(dll_push_one) == 1


def test_dll_push_none(initialize_empty_dll):
    """Test ValueError when push method called with no value."""
    with pytest.raises(ValueError):
        initialize_empty_dll.push()


def test_dll_append_to_empty_sets_head(dll_append_one):
    """Test doubly linked list append method sets head when empty."""
    assert dll_append_one.head.val == 5
    assert dll_append_one.head.prev_node is None


def test_dll_append_to_empty_sets_tail(dll_append_one):
    """Test doubly linked list append method."""
    assert dll_append_one.tail.val == 5
    assert dll_append_one.tail.next_node is None


def test_dll_append_to_non_empty_sets_head(dll_append_one):
    """Test doubly linked list append method."""
    dll = dll_append_one
    dll.append('cake')
    assert dll_append_one.head.val == 5
    assert dll_append_one.head.next_node.val == 'cake'
    assert dll_append_one.head.prev_node is None


def test_dll_append_to_non_empty_sets_tail(dll_append_two):
    """Test doubly linked list append method."""
    assert dll_append_two.tail.val == 'cake'
    assert dll_append_two.tail.prev_node.val == 5
    assert dll_append_two.tail.next_node is None


def test_dll_append_len(dll_append_two):
    """Test doubly linked list append method adds to len."""
    assert len(dll_append_two) == 2


def test_dll_append_none(initialize_empty_dll):
    """Test ValueError when doubly linked list appended to with None."""
    with pytest.raises(ValueError):
        EMPTY_LIST_APPEND.append()


def test_dll_pop(initialize_three_dll):
    """Test doubly linked list pop method removes and returns head."""
    assert initialize_three_dll.pop() == 'three'
    assert initialize_three_dll.head.val == 'two'


def test_dll_pop_all(dll_push_two):
    """Test that popping all nodes works."""
    dll_push_two.pop()
    dll_push_two.pop()
    assert dll_push_two.head is None
    assert dll_push_two.tail is None


def test_dll_pop_head_reassign(initialize_three_and_pop_dll):
    """Test doubly linked list pop method sets new head."""
    assert initialize_three_and_pop_dll.head.prev_node is None
    assert initialize_three_and_pop_dll.head.next_node.val == 'one'


def test_dll_pop_len(initialize_three_and_pop_dll):
    """Test doubly linked list pop method changes len."""
    assert len(initialize_three_and_pop_dll) == 2


def test_dll_pop_empty(initialize_empty_dll):
    """Test doubly linked list empty pop method."""
    with pytest.raises(IndexError):
        initialize_empty_dll.pop()


def test_dll_shift(initialize_three_dll):
    """Test doubly linked list shift method removes and returns tail."""
    assert initialize_three_dll.shift() == 'one'
    assert initialize_three_dll.tail.val == 'two'


def test_dll_shift_tail_reassign(initialize_three_and_shift_dll):
    """Test doubly linked list shift method sets new tail."""
    assert initialize_three_and_shift_dll.tail.next_node is None
    assert initialize_three_and_shift_dll.tail.prev_node.val == 'three'


def test_dll_shift_len(initialize_three_and_shift_dll):
    """Test doubly linked list shift method changes len."""
    assert len(initialize_three_and_shift_dll) == 2


def test_dll_shift_empty(initialize_empty_dll):
    """Test shift method on empty list."""
    with pytest.raises(IndexError):
        initialize_empty_dll.shift()


def test_dll_shift_all(dll_push_two):
    """Test that shifting all nodes works."""
    dll_push_two.shift()
    dll_push_two.shift()
    assert dll_push_two.head is None
    assert dll_push_two.tail is None


def test_dll_remove(initialize_three_dll):
    """
    Test doubly linked list remove method.

    Removes specific node and sets new head and tail.
    """
    old = len(initialize_three_dll)
    initialize_three_dll.remove('two')
    assert len(initialize_three_dll) == old - 1
    assert initialize_three_dll.tail.prev_node == initialize_three_dll.head
    assert initialize_three_dll.head.next_node == initialize_three_dll.tail


def test_dll_remove_not_found(initialize_three_dll):
    """Test doubly linked list remove method returns error if not in list."""
    with pytest.raises(ValueError):
        initialize_three_dll.remove('cake')


def test_dll_remove_from_list_of_one(dll_push_one):
    """Test doubly linked list remove method on only node."""
    dll_push_one.remove(5)
    assert len(dll_push_one) == 0
    assert dll_push_one.head is None
    assert dll_push_one.tail is None


def test_dll_remove_from_head(initialize_two_dll):
    """Test doubly linked list remove method on the head of a list of two."""
    initialize_two_dll.remove('one')
    assert len(initialize_two_dll) == 1
    assert initialize_two_dll.tail.prev_node is None
    assert initialize_two_dll.head.next_node is None


def test_dll_remove_from_tail(initialize_two_dll):
    """Test doubly linked list remove method on the tail of a list of two."""
    initialize_two_dll.remove('two')
    assert len(initialize_two_dll) == 1
    assert initialize_two_dll.tail.prev_node is None
    assert initialize_two_dll.head.next_node is None


def test_dll_remove_invalid(initialize_three_dll):
    """Test doubly linked list remove method not in list."""
    with pytest.raises(ValueError):
        initialize_three_dll.remove('cake')


def test_dll_len(initialize_three_dll):
    """Test len method."""
    assert len(initialize_three_dll) == 3


def test_remove_from_empty_dll(initialize_empty_dll):
    """Test remove raises error when dll is empty."""
    with pytest.raises(ValueError):
        initialize_empty_dll.remove('cake')
