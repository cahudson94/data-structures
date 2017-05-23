"""Tests for linked list implementation."""
from linked_list import Linked_List, Node

EMPTY_LIST = Linked_List()


def test_linked_list_push():
    """Test linked list push method."""
    EMPTY_LIST.push(5)
    assert EMPTY_LIST.head.get_val() == 5


# def test_linked_list_search():
#     """Test linked list search method."""
#     assert Linked_List.search == Linked_List.search
