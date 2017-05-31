"""Tests for stack class implementation."""
from stack import Stack
import pytest

EMPTY_STACK_FOR_PUSH = Stack()
EMPTY_STACK_FOR_POP = Stack()

POP_LIST = Stack()
POP_LIST.push('one')
POP_LIST.push(2)
POP_LIST.push('three')

LIST_OF_THREE = Stack()
LIST_OF_THREE.push(3)
LIST_OF_THREE.push(['one', 'two', 'three'])
LIST_OF_THREE.push((1, 2, 3))

LIST_LIST = Stack([3, 2, 1])

TUPLE_LIST = Stack((2, 4, 9))

STRING_LIST = Stack('cake')

LEN_OF_SIX = Stack('cake')
LEN_OF_SIX.push('pie')
LEN_OF_SIX.push(42)


def test_stack_init_list():
    """Test length and head of Stack when instantiated with a list."""
    assert len(LIST_LIST) == 3
    assert LIST_LIST._linked_list.head.val == 1


def test_stack_init_tuple():
    """Test length and head of Stack when instantiated with a tuple."""
    assert len(TUPLE_LIST) == 3
    assert TUPLE_LIST._linked_list.head.val == 9


def test_stack_init_string():
    """Test length and head of Stack when instantiated with a string."""
    assert len(STRING_LIST) == 4
    assert STRING_LIST._linked_list.head.val == 'e'


def test_stack_init_not_iter():
    """Test IndexError when Stack instantiated with non-iterable."""
    with pytest.raises(TypeError):
        Stack(3)


def test_stack_push_none():
    """Test ValueError when push method called with arg of None."""
    with pytest.raises(ValueError):
        EMPTY_STACK_FOR_PUSH.push(None)


def test_stack_push_one():
    """Test Stack push method with valid arg."""
    EMPTY_STACK_FOR_PUSH.push(5)
    assert EMPTY_STACK_FOR_PUSH._linked_list.head.val == 5


def test_stack_push_two():
    """Test Stack push method with valid arg."""
    EMPTY_STACK_FOR_PUSH.push(7)
    assert EMPTY_STACK_FOR_PUSH._linked_list.head.val == 7


def test_stack_pop_one():
    """Test stack pop method for string."""
    assert POP_LIST.pop().val == 'three'
    assert POP_LIST._linked_list.head.val == 2


def test_stack_pop_two():
    """Test stack pop method for int."""
    assert POP_LIST.pop().val == 2
    assert POP_LIST._linked_list.head.val == 'one'


def test_stack_pop_tup():
    """Test stack pop method for tup as node val."""
    assert LIST_OF_THREE.pop().val == (1, 2, 3)
    assert LIST_OF_THREE._linked_list.head.val == ['one', 'two', 'three']


def test_stack_pop_list():
    """Test stack pop method for list as node val."""
    assert LIST_OF_THREE.pop().val == ['one', 'two', 'three']
    assert LIST_OF_THREE._linked_list.head.val == 3


def test_stack_pop_empty():
    """Test IndexError when pop method called on empty stack."""
    with pytest.raises(IndexError):
        EMPTY_STACK_FOR_POP.pop()


def test_stack_len():
    """Test for len method."""
    assert len(LEN_OF_SIX) == 6
    assert len(STRING_LIST) == 4
