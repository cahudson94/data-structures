"""Tests for linked list implementation."""
from linked_list import Linked_List, Node

EMPTY_LIST = Linked_List()
LIST_OF_THREE = Linked_List()
LIST_OF_THREE.push('one')
LIST_OF_THREE.push('two')
LIST_OF_THREE.push('three')


def test_linked_list_push():
    """Test linked list push method."""
    EMPTY_LIST.push(5)
    assert EMPTY_LIST.head.get_val() == 5


def test_linked_list_len():
    """Test for len method."""
    assert len(LIST_OF_THREE) == 3


def test_linked_list_size():
    """Test for len method."""
    assert LIST_OF_THREE.size() == 3


def test_linked_list_search():
    """Test linked list search method."""
    assert LIST_OF_THREE.search('two').get_val() == 'two'
