"""Test Dequeue data structure."""
from deque import Deque
import pytest


@pytest.fixture
def build_empty_dequeue():
    """Build empty dequeue."""
    q = Deque()
    return q


@pytest.fixture
def build_dequeue_one_node():
    """Build one-node dequeue."""
    q = Deque()
    q.append('cake')
    return q


@pytest.fixture
def build_dequeue_two_nodes():
    """Build two-node dequeue."""
    q = Deque()
    q.append('blue')
    q.append(2)
    return q


@pytest.fixture
def build_dequeue_three_nodes():
    """Build three-node dequeue."""
    q = Deque()
    q.append('apple')
    q.append('peaches')
    q.append('bananas')
    return q


def test_qs_init(build_empty_dequeue):
    """Test instatiated dequeue."""
    assert build_empty_dequeue.head is None
    assert build_empty_dequeue.tail is None


def test_append_empty_dequeue(build_empty_dequeue):
    """Test head after append on empty."""
    q = build_empty_dequeue
    q.append('hi')
    assert q.head.val == 'hi'
    assert q.tail.val == 'hi'


def test_append_left_empty_dequeue(build_empty_dequeue):
    """Test head after append on empty."""
    q = build_empty_dequeue
    q.appendleft('hi')
    assert q.head.val == 'hi'
    assert q.tail.val == 'hi'


def test_append_empty_queue_next(build_empty_dequeue):
    """Test head and tail next_node after append on empty."""
    build_empty_dequeue.append('hi!')
    assert build_empty_dequeue.head.next_node is None
    assert build_empty_dequeue.tail.next_node is None
    assert build_empty_dequeue.head.prev_node is None
    assert build_empty_dequeue.tail.prev_node is None


def test_append_non_empty_queue(build_dequeue_one_node):
    """Test head and tail after append on non empty."""
    build_dequeue_one_node.append('pie')
    assert build_dequeue_one_node.head.val == 'cake'
    assert build_dequeue_one_node.tail.val == 'pie'


def test_append_left_non_empty_queue(build_dequeue_one_node):
    """Test head and tail vals after append on non empty."""
    build_dequeue_one_node.appendleft('pie')
    assert build_dequeue_one_node.head.val == 'pie'
    assert build_dequeue_one_node.tail.val == 'cake'


def test_append_non_empty_queue_next(build_dequeue_one_node):
    """Test head and tail next_node after append on non empty."""
    build_dequeue_one_node.append('pie')
    assert build_dequeue_one_node.head.next_node.val == 'pie'
    assert build_dequeue_one_node.tail.prev_node.val == 'cake'


def test_append_left_non_empty_queue_next(build_dequeue_one_node):
    """Test head and tail next_node after append on non empty."""
    build_dequeue_one_node.appendleft('pie')
    assert build_dequeue_one_node.head.next_node.val == 'cake'
    assert build_dequeue_one_node.tail.prev_node.val == 'pie'


def test_next_node_three_nodes(build_dequeue_three_nodes):
    """Test head and tail next_node after multiple appends."""
    q = build_dequeue_three_nodes
    assert q.head.next_node.val == 'peaches'
    assert q.head.next_node.next_node.val == 'bananas'


def test_prev_node_three_nodes(build_dequeue_three_nodes):
    """Test head.next_node after multiple appends."""
    q = build_dequeue_three_nodes
    assert q.tail.prev_node.val == 'peaches'
    assert q.tail.prev_node.prev_node.val == 'apple'


def test_peek_empty_dequeue(build_empty_dequeue):
    """Test peek method for empty queue."""
    assert build_empty_dequeue.peek() is None


def test_peek_one_node(build_dequeue_one_node):
    """Test peek method for one node queue."""
    assert build_dequeue_one_node.peek().val == 'cake'


def test_peek_two_nodes(build_dequeue_two_nodes):
    """Test peek method for two node queue."""
    assert build_dequeue_two_nodes.peek().val == 2


def test_peek_against_head_two_nodes(build_dequeue_two_nodes):
    """Test peek method for one node dequeue."""
    assert build_dequeue_two_nodes.peek() == build_dequeue_two_nodes.tail


def test_peekleft_empty_dequeue(build_empty_dequeue):
    """Test peekleft method for empty queue."""
    assert build_empty_dequeue.peekleft() is None


def test_peekleft_one_node(build_dequeue_one_node):
    """Test peekleft method for one node queue."""
    assert build_dequeue_one_node.peekleft().val == 'cake'


def test_peekleft_two_nodes(build_dequeue_two_nodes):
    """Test peekleft method for two node queue."""
    assert build_dequeue_two_nodes.peekleft().val == 'blue'


def test_peekleft_against_head_two_nodes(build_dequeue_two_nodes):
    """Test peekleft method for one node dequeue."""
    assert build_dequeue_two_nodes.peekleft() == build_dequeue_two_nodes.head


def test_popleft_empty_dequeue(build_empty_dequeue):
    """Test popleft on empty queue raises error."""
    with pytest.raises(IndexError):
        build_empty_dequeue.popleft()


def test_pop_empty_dequeue(build_empty_dequeue):
    """Test pop on empty queue raises error."""
    with pytest.raises(IndexError):
        build_empty_dequeue.pop()


def test_popleft_once_three_nodes(build_dequeue_three_nodes):
    """Test head movement on popleft method for one node using peekleft."""
    assert build_dequeue_three_nodes.popleft() == 'apple'
    assert build_dequeue_three_nodes.head.val == 'peaches'
    assert build_dequeue_three_nodes.tail.val == 'bananas'


def test_popleft_twice_three_nodes(build_dequeue_three_nodes):
    """Test next node, prev_node, tail and head after popleft twice."""
    last_before_popleft = build_dequeue_three_nodes.head.next_node.next_node
    build_dequeue_three_nodes.popleft()
    build_dequeue_three_nodes.popleft()
    assert last_before_popleft == build_dequeue_three_nodes.head
    assert last_before_popleft == build_dequeue_three_nodes.tail
    assert last_before_popleft.next_node is None
    assert last_before_popleft.prev_node is None


def test_pop_once_three_nodes(build_dequeue_three_nodes):
    """Test head, tail on popleft method for one node using peekleft."""
    assert build_dequeue_three_nodes.pop() == 'bananas'
    assert build_dequeue_three_nodes.tail.val == 'peaches'
    assert build_dequeue_three_nodes.head.val == 'apple'


def test_pop_twice_three_nodes(build_dequeue_three_nodes):
    """Test next node, prev_node, tail and head after popleft twice."""
    last_before_pop = build_dequeue_three_nodes.tail.prev_node.prev_node
    build_dequeue_three_nodes.pop()
    build_dequeue_three_nodes.pop()
    assert last_before_pop == build_dequeue_three_nodes.tail
    assert last_before_pop == build_dequeue_three_nodes.head
    assert last_before_pop.next_node is None
    assert last_before_pop.prev_node is None


def test_len_empty_dequeue(build_empty_dequeue):
    """Test len of empty queue."""
    assert len(build_empty_dequeue) == 0


def test_len_one_node_dequeue(build_dequeue_one_node):
    """Test len of queue of one."""
    assert len(build_dequeue_one_node) == 1


def test_len_three_node_dequeue(build_dequeue_three_nodes):
    """Test len of queue of three."""
    assert len(build_dequeue_three_nodes) == 3


def test_len_after_dequeue_on_empty(build_empty_dequeue):
    """Test change in len after append on empty."""
    q = build_empty_dequeue
    q.append('hi!')
    assert len(q) == 1


def test_len_after_dequeue_on_three(build_dequeue_three_nodes):
    """Test change in len after append on non empty."""
    q = build_dequeue_three_nodes
    q.append('hi!')
    assert len(q) == 4


def test_len_after_dequeue_two_on_two(build_dequeue_two_nodes):
    """Test change in len after append two on non empty."""
    q = build_dequeue_two_nodes
    q.append('red')
    q.append(4)
    assert len(q) == 4


def test_size_empty_dequeue(build_empty_dequeue):
    """Test size of empty queue."""
    assert build_empty_dequeue.size() == 0


def test_size_one_node_dequeue(build_dequeue_one_node):
    """Test size of queue of one."""
    assert build_dequeue_one_node.size() == 1


def test_size_three_node_dequeue(build_dequeue_three_nodes):
    """Test size of dequeue of three."""
    assert build_dequeue_three_nodes.size() == 3


def test_size_after_dequeue_on_empty(build_empty_dequeue):
    """Test change in size after append on empty."""
    q = build_empty_dequeue
    q.append('hi!')
    assert q.size() == 1


def test_size_after_dequeue_on_three(build_dequeue_three_nodes):
    """Test change in size after append on non empty."""
    q = build_dequeue_three_nodes
    q.append('hi!')
    assert q.size() == 4


def test_size_after_dequeue_two_on_two(build_dequeue_two_nodes):
    """Test change in size after append two on non empty."""
    q = build_dequeue_two_nodes
    q.append('red')
    q.append(4)
    assert q.size() == 4
