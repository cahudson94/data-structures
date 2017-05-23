"""Tests for linked list implementation."""
from linked_list import LinkedList, Node

EMPTY_LIST = LinkedList()
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


def test_linked_list_push():
    """Test linked list push method."""
    EMPTY_LIST.push(5)
    assert EMPTY_LIST.head.val == 5


def test_linked_list_push_not_val():
    """."""


def test_linked_list_push_mult():
    """."""


def test_linked_list_pop():
    """Test linked list pop method."""
    POP_LIST.pop()
    assert POP_LIST.head.val == 'two'


def test_linked_list_size():
    """Test for len method."""
    assert LIST_OF_THREE.size() == 3


def test_linked_list_search():
    """Test linked list search method."""
    assert LIST_OF_THREE.search('two').get_val() == 'two'


def test_linked_list_remove():
    """Test linked list remove method."""
    REMOVE_LIST.__repr__()
    REMOVE_LIST.remove(REMOVE_LIST.search('apple'))
    assert len(REMOVE_LIST) == 2


def test_linked_list_display():
    """Test linked list display method."""
    assert LIST_OF_THREE.display() == '(one, two, three)'


def test_linked_list_len():
    """Test for len method."""
    assert len(LIST_OF_THREE) == 3


def test_linked_list_print():
    """Test linked list print method."""
