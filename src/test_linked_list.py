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

LONG_LEN_LIST = LinkedList()
LONG_LEN_LIST.push('a')
LONG_LEN_LIST.push('b')
LONG_LEN_LIST.push('c')
LONG_LEN_LIST.push('d')
LONG_LEN_LIST.push('e')
LONG_LEN_LIST.push('f')
LONG_LEN_LIST.push('g')
LONG_LEN_LIST.push('h')
LONG_LEN_LIST.push('i')
LONG_LEN_LIST.push('j')
LONG_LEN_LIST.push('k')


def test_linked_list_not_iter():
    """Test IndexError when linked list instantiated with non-iterable."""
    with pytest.raises(TypeError):
        LinkedList(3)


def test_linked_list_init_list():
    """Test linked list head and len when instantiated with list."""
    linklist = LinkedList([3, 4, 5])
    assert linklist.head.val == 5
    assert len(linklist) == 3


def test_linked_list_init_str():
    """Test linked list head and len when instantiated with string."""
    linkstr = LinkedList('cake')
    assert linkstr.head.val == 'e'
    assert len(linkstr) == 4


def test_linked_list_init_tup():
    """Test linked list head and len when instantiated with tuple."""
    linktup = LinkedList((3, 6, 9, 12, 15))
    assert linktup.head.val == 15
    assert len(linktup) == 5


def test_linked_list_push_to_empty():
    """Test linked list push method to empty list."""
    EMPTY_LIST.push(5)
    assert EMPTY_LIST.head.val == 5


def test_linked_list_push_to_non_empty():
    """Test linked list push method to non empty list."""
    EMPTY_LIST.push(10)
    assert EMPTY_LIST.head.val == 10
    assert EMPTY_LIST.head.next_node.val == 5


def test_linked_list_push_not_val():
    """Test push with non iterable."""
    with pytest.raises(ValueError):
        EMPTY_LIST.push(None)


def test_linked_list_pop_one():
    """Test linked list pop method returns value and changes head once."""
    assert POP_LIST.pop() == 'three'
    assert POP_LIST.head.val == 'two'


def test_linked_list_pop_two():
    """Test linked list pop method returns value and changes head again."""
    assert POP_LIST.pop() == 'two'
    assert POP_LIST.head.val == 'one'


def test_linked_list_pop_empty():
    """Test linked list pop method on empty list for error."""
    with pytest.raises(IndexError):
        EMPTY_LIST_POP.pop()


def test_linked_list_size():
    """Test len of linked list."""
    assert LIST_OF_THREE.size() == 3
    assert LONG_LEN_LIST.size() == 11


def test_linked_list_search():
    """Test linked list search method."""
    assert LIST_OF_THREE.search('two').val == 'two'


def test_linked_list_search_none():
    """Test linked list search method if not in list."""
    assert LIST_OF_THREE.search(1) is None
    assert REMOVE_LIST.search('cake') is None


def test_linked_list_remove():
    """Test linked list remove method and changed length."""
    REMOVE_LIST.remove(REMOVE_LIST.search('apple'))
    assert len(REMOVE_LIST) == 2


def test_linked_list_remove_not_found():
    """Test linked list remove method for not in list."""
    with pytest.raises(ValueError):
        REMOVE_LIST.remove(REMOVE_LIST.search('cake'))


def test_linked_list_remove_head():
    """Test linked list remove method for head reassignment."""
    REMOVE_HEAD.remove(REMOVE_HEAD.search('head'))
    assert REMOVE_HEAD.head.val == 'middle'


def test_linked_list_len():
    """Test for len method of linked list."""
    assert len(LIST_OF_THREE) == 3


def test_linked_list_display():
    """Test linked list display method."""
    assert LIST_OF_THREE.display() == '(one, two, three)'


def test_linked_list_repr():
    """Test linked list print method."""
    assert repr(LIST_OF_THREE) == '(one, two, three)'


def test_linked_list_remove_empty():
    """Test linked list remove raises error when empty."""
    with pytest.raises(ValueError):
        EMPTY_LIST.remove(5)
