"""Test Queue data structure."""
from deque import Deque
import pytest


@pytest.fixture
def build_empty_queue():
    """Build empty queue."""
    q = Deque()
    return q


@pytest.fixture
def build_queue_one_node():
    """Build one-node queue."""
    q = Deque()
    q.append('cake')
    return q


@pytest.fixture
def build_queue_two_nodes():
    """Build two-node queue."""
    q = Deque()
    q.append('blue')
    q.append(2)
    return q


@pytest.fixture
def build_queue_three_nodes():
    """Build three-node queue."""
    q = Deque()
    q.append('apple')
    q.append('peaches')
    q.append('bananas')
    return q


def test_qs_init(build_empty_queue):
    """Test instatiated queue."""
    assert build_empty_queue.head is None


def test_append_empty_queue(build_empty_queue):
    """Test head after append on empty."""
    q = build_empty_queue
    q.append('hi')
    assert q.head.val == 'hi'


def test_append_empty_queue_next(build_empty_queue):
    """Test head.next_node after append on empty."""
    build_empty_queue.append('hi!')
    assert build_empty_queue.head.next_node is None


def test_append_non_empty_queue(build_queue_one_node):
    """Test head after append on non empty."""
    build_queue_one_node.append('pie')
    assert build_queue_one_node.head.val == 'cake'


def test_append_non_empty_queue_next(build_queue_one_node):
    """Test head.next_node after append on non empty."""
    build_queue_one_node.append('pie')
    assert build_queue_one_node.head.next_node.val == 'pie'


def test_next_node_three_nodes(build_queue_three_nodes):
    """Test head.next_node after multiple appends."""
    q = build_queue_three_nodes
    assert q.head.next_node.val == 'peaches'
    assert q.head.next_node.next_node.val == 'bananas'


def test_peekleft_empty_queue(build_empty_queue):
    """Test peekleft method for empty queue."""
    assert build_empty_queue.peekleft() is None


def test_peekleft_one_node(build_queue_one_node):
    """Test peekleft method for one node queue."""
    assert build_queue_one_node.peekleft().val == 'cake'


def test_peekleft_two_nodes(build_queue_two_nodes):
    """Test peekleft method for two node queue."""
    assert build_queue_two_nodes.peekleft().val == 'blue'


def test_peekleft_against_head_two_nodes(build_queue_two_nodes):
    """Test peekleft method for one node queue."""
    assert build_queue_two_nodes.peekleft() == build_queue_two_nodes.head


def test_popleft_empty_queue(build_empty_queue):
    """Test popleft on empty queue raises error."""
    with pytest.raises(IndexError):
        build_empty_queue.popleft()


def test_popleft_once_three_nodes(build_queue_three_nodes):
    """Test head movement on popleft method for one node using peekleft."""
    assert build_queue_three_nodes.popleft() == 'apple'
    assert build_queue_three_nodes.head.val == 'peaches'


def test_popleft_twice_three_nodes(build_queue_three_nodes):
    """Test next node and head after popleft twice."""
    last_before_popleft = build_queue_three_nodes.head.next_node.next_node
    build_queue_three_nodes.popleft()
    build_queue_three_nodes.popleft()
    assert last_before_popleft.val == build_queue_three_nodes.head.val
    assert last_before_popleft.next_node is None


def test_len_empty_queue(build_empty_queue):
    """Test len of empty queue."""
    assert len(build_empty_queue) == 0


def test_len_one_node_queue(build_queue_one_node):
    """Test len of queue of one."""
    assert len(build_queue_one_node) == 1


def test_len_three_node_queue(build_queue_three_nodes):
    """Test len of queue of three."""
    assert len(build_queue_three_nodes) == 3


def test_len_after_queue_on_empty(build_empty_queue):
    """Test change in len after append on empty."""
    q = build_empty_queue
    q.append('hi!')
    assert len(q) == 1


def test_len_after_queue_on_three(build_queue_three_nodes):
    """Test change in len after append on non empty."""
    q = build_queue_three_nodes
    q.append('hi!')
    assert len(q) == 4


def test_len_after_queue_two_on_two(build_queue_two_nodes):
    """Test change in len after append two on non empty."""
    q = build_queue_two_nodes
    q.append('red')
    q.append(4)
    assert len(q) == 4


def test_size_empty_queue(build_empty_queue):
    """Test size of empty queue."""
    assert build_empty_queue.size() == 0


def test_size_one_node_queue(build_queue_one_node):
    """Test size of queue of one."""
    assert build_queue_one_node.size() == 1


def test_size_three_node_queue(build_queue_three_nodes):
    """Test size of queue of three."""
    assert build_queue_three_nodes.size() == 3


def test_size_after_queue_on_empty(build_empty_queue):
    """Test change in size after append on empty."""
    q = build_empty_queue
    q.append('hi!')
    assert q.size() == 1


def test_size_after_queue_on_three(build_queue_three_nodes):
    """Test change in size after append on non empty."""
    q = build_queue_three_nodes
    q.append('hi!')
    assert q.size() == 4


def test_size_after_queue_two_on_two(build_queue_two_nodes):
    """Test change in size after append two on non empty."""
    q = build_queue_two_nodes
    q.append('red')
    q.append(4)
    assert q.size() == 4
