"""Test for doubly-linked list data structure."""
from doubly_linked_list import DoublyLinkedList
import pytest


EMPTY_LIST_PUSH = DoublyLinkedList()
EMPTY_LIST_APPEND = DoublyLinkedList()
EMPTY_LIST = DoublyLinkedList()

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


def test_dll_push():
    """Test doubly linked list push method."""
    EMPTY_LIST_PUSH.push(5)
    assert EMPTY_LIST_PUSH.head.val == 5
    assert EMPTY_LIST_PUSH.tail.val == 5


def test_dll_push_none():
    """Test IndexError when Stack instantiated with non-iterable."""
    with pytest.raises(ValueError):
        EMPTY_LIST_PUSH.push()


def test_dll_init_non_itr():
    """Test IndexError when Stack instantiated with non-iterable."""
    with pytest.raises(TypeError):
        DoublyLinkedList(3)


def test_dll_append():
    """Test doubly linked list append method."""
    EMPTY_LIST_APPEND.append(5)
    assert EMPTY_LIST_APPEND.head.val == 5
    assert EMPTY_LIST_APPEND.tail.val == 5


def test_dll_append_none():
    """Test ValueError when doubly linked list appended to with None."""
    with pytest.raises(ValueError):
        EMPTY_LIST_APPEND.append()


def test_dll_pop():
    """."""
    popped = POP_LIST.pop()
    assert popped.val == 'three'
    assert POP_LIST.head.val == 'two'


def test_dll_pop_empty():
    """Test doubly linked list empty pop method."""
    with pytest.raises(IndexError):
        EMPTY_LIST.pop()


# def test_dll_shift():
#     """Test doubly linked list shift method."""
#     shifted = SHIFT_LIST.shift()
#     assert shifted.val == 'one'
#     assert SHIFT_LIST.tail.val == 'two'
#     # import
#     # new_tail = dll.tail.previous
#     # assert dll.shift() == (old tail)
#     # assert dll.tail = new_tail


def test_dll_shift_empty():
    """."""
    with pytest.raises(IndexError):
        EMPTY_LIST.shift()


# def test_dll_remove():
#     """."""
#     old = len(REMOVE_LIST)
#     REMOVE_LIST.remove('two')
#     assert len(REMOVE_LIST) == old - 1
#     assert REMOVE_LIST.tail.prev_node == REMOVE_LIST.head.next_node


def test_dll_remove_invalid():
    """Test doubly linked list remove method not in list."""
    with pytest.raises(ValueError):
        SHIFT_LIST.remove('cake')


def test_dll_len():
    """Test doubly linked list remove method."""
    assert len(POP_LIST) == 2
