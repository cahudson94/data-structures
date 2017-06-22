"""Test Queue data structure."""
from que_ import QueueStructure
import pytest


@pytest.fixture
def build_empty_queue():
    """Build empty queue."""
    q = QueueStructure()
    return q


@pytest.fixture
def build_queue_one_node():
    """Build one-node queue."""
    q = QueueStructure()
    q.enqueue('cake')
    return q


@pytest.fixture
def build_queue_two_nodes():
    """Build two-node queue."""
    q = QueueStructure()
    q.enqueue('blue')
    q.enqueue(2)
    return q


@pytest.fixture
def build_queue_three_nodes():
    """Build three-node queue."""
    q = QueueStructure()
    q.enqueue('apple')
    q.enqueue('peaches')
    q.enqueue('bananas')
    return q


def test_qs_init(build_empty_queue):
    """Test instatiated queue."""
    assert build_empty_queue.head is None


def test_enqueue_empty_queue(build_empty_queue):
    """Test head after enqueue on empty."""
    q = build_empty_queue
    q.enqueue('hi')
    assert q.head.val == 'hi'


def test_enqueue_empty_queue_next(build_empty_queue):
    """Test head.next_node after enqueue on empty."""
    build_empty_queue.enqueue('hi!')
    assert build_empty_queue.head.next_node is None


def test_enqueue_non_empty_queue(build_queue_one_node):
    """Test head after enqueue on non empty."""
    build_queue_one_node.enqueue('pie')
    assert build_queue_one_node.head.val == 'cake'


def test_enqueue_non_empty_queue_next(build_queue_one_node):
    """Test head.next_node after enqueue on non empty."""
    build_queue_one_node.enqueue('pie')
    assert build_queue_one_node.head.next_node.val == 'pie'


def test_next_node_three_nodes(build_queue_three_nodes):
    """Test head.next_node after multiple enqueues."""
    q = build_queue_three_nodes
    assert q.head.next_node.val == 'peaches'
    assert q.head.next_node.next_node.val == 'bananas'


def test_peek_empty_queue(build_empty_queue):
    """Test peek method for empty queue."""
    assert build_empty_queue.peek() is None


def test_peek_one_node(build_queue_one_node):
    """Test peek method for one node queue."""
    assert build_queue_one_node.peek() == 'cake'


def test_peek_two_nodes(build_queue_two_nodes):
    """Test peek method for two node queue."""
    assert build_queue_two_nodes.peek() == 'blue'


def test_peek_against_head_two_nodes(build_queue_two_nodes):
    """Test peek method for one node queue."""
    assert build_queue_two_nodes.peek() == build_queue_two_nodes.head.val


def test_dequeue_empty_queue(build_empty_queue):
    """Test dequeue on empty queue raises error."""
    with pytest.raises(IndexError):
        build_empty_queue.dequeue()


def test_dequeue_once_three_nodes(build_queue_three_nodes):
    """Test head movement on dequeue method for one node using peek."""
    assert build_queue_three_nodes.dequeue() == 'apple'
    assert build_queue_three_nodes.peek() == 'peaches'


def test_dequeue_twice_three_nodes(build_queue_three_nodes):
    """Test next node and head after dequeue twice."""
    last_before_dequeue = build_queue_three_nodes.head.next_node.next_node
    build_queue_three_nodes.dequeue()
    build_queue_three_nodes.dequeue()
    assert last_before_dequeue.val == build_queue_three_nodes.head.val
    assert last_before_dequeue.next_node is None


def test_dequeue_all(build_queue_three_nodes):
    """Test dequeue all nodes."""
    build_queue_three_nodes.dequeue()
    build_queue_three_nodes.dequeue()
    build_queue_three_nodes.dequeue()
    assert len(build_queue_three_nodes) == 0
    assert build_queue_three_nodes.peek() is None


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
    """Test change in len after enqueue on empty."""
    q = build_empty_queue
    q.enqueue('hi!')
    assert len(q) == 1


def test_len_after_queue_on_three(build_queue_three_nodes):
    """Test change in len after enqueue on non empty."""
    q = build_queue_three_nodes
    q.enqueue('hi!')
    assert len(q) == 4


def test_len_after_queue_two_on_two(build_queue_two_nodes):
    """Test change in len after enqueue two on non empty."""
    q = build_queue_two_nodes
    q.enqueue('red')
    q.enqueue(4)
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
    """Test change in size after enqueue on empty."""
    q = build_empty_queue
    q.enqueue('hi!')
    assert q.size() == 1


def test_size_after_queue_on_three(build_queue_three_nodes):
    """Test change in size after enqueue on non empty."""
    q = build_queue_three_nodes
    q.enqueue('hi!')
    assert q.size() == 4


def test_size_after_queue_two_on_two(build_queue_two_nodes):
    """Test change in size after enqueue two on non empty."""
    q = build_queue_two_nodes
    q.enqueue('red')
    q.enqueue(4)
    assert q.size() == 4
