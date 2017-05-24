"""Tests for linked list implementation."""
from linked_list import LinkedList
import pytest

EMPTY_LIST = LinkedList()
EMPTY_LIST_POP = LinkedList()

POP_LIST = LinkedList()
POP_LIST.push('one')
POP_LIST.push('two')
POP_LIST.push('three')

LIST_OF_THREE = LinkedList()
LIST_OF_THREE.push('one')
LIST_OF_THREE.push('two')
LIST_OF_THREE.push('three')

REMOVE_LIST = LinkedList()
REMOVE_LIST.push('orange')
REMOVE_LIST.push('apple')
REMOVE_LIST.push('grape')

REMOVE_HEAD = LinkedList()
REMOVE_HEAD.push('tail')
REMOVE_HEAD.push('middle')
REMOVE_HEAD.push('head')


def test_linked_list_push():
    """Test linked list push method."""
    EMPTY_LIST.push(5)
    assert EMPTY_LIST.head.val == 5


def test_linked_list_not_iter():
    """Test IndexError when Stack instantiated with non-iterable."""
    with pytest.raises(TypeError):
        LinkedList(3)


def test_linked_list_iter():
    """Test IndexError when Stack instantiated with non-iterable."""
    assert LinkedList([3, 4, 5, 6]).head.val == 6
    assert LinkedList((3, 4, 5, 6)).head.val == 6
    assert LinkedList('cake').head.val == 'e'
    assert len(LinkedList([3, 4, 5, 6])) == 4
    assert LinkedList([3, 4, 5, 6]).search(4).val == 4


def test_linked_list_push_not_val():
    """Test push when no value added as arg."""
    with pytest.raises(ValueError):
        EMPTY_LIST.push()


def test_linked_list_pop():
    """Test linked list pop method."""
    POP_LIST.pop()
    assert POP_LIST.head.val == 'two'


def test_linked_list_pop_empty():
    """Test linked list pop method."""
    with pytest.raises(IndexError):
        EMPTY_LIST_POP.pop()


def test_linked_list_size():
    """Test for len method."""
    assert LIST_OF_THREE.size() == 3


def test_linked_list_search():
    """Test linked list search method."""
    assert LIST_OF_THREE.search('two').val == 'two'


def test_linked_list_search_none():
    """Test linked list search method."""
    assert LIST_OF_THREE.search(1) is None


def test_linked_list_remove():
    """Test linked list remove method."""
    REMOVE_LIST.remove(REMOVE_LIST.search('apple'))
    assert len(REMOVE_LIST) == 2


def test_linked_list_remove_not_found():
    """Test linked list remove method."""
    with pytest.raises(ValueError):
        REMOVE_LIST.remove(REMOVE_LIST.search('cake'))


def test_linked_list_remove_head():
    """Test linked list remove method."""
    REMOVE_HEAD.remove(REMOVE_HEAD.search('head'))
    assert REMOVE_HEAD.head.val == 'middle'


def test_linked_list_len():
    """Test for len method."""
    assert len(LIST_OF_THREE) == 3


def test_linked_list_display():
    """Test linked list display method."""
    assert LIST_OF_THREE.display() == '(one, two, three)'


# def test_linked_list_print():
#     """Test linked list print method."""
#     assert print(LIST_OF_THREE) == '(one, two, three)'


def test_linked_list_repr():
    """Test linked list print method."""
    assert repr(LIST_OF_THREE) == '(one, two, three)'
