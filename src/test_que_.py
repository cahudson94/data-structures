"""Test Queue data structure."""
from que_ import QueueStructure
import pytest


@pytest.fixture
def build_empty_queue():
    """Build empty queue."""
    return QueueStructure()


@pytest.fixture
def build_queue_one_node():
    """Build one-node queue."""
    q = QueueStructure()
    q.enqueue('cake')
    return q


@pytest.fixture
def build_queue_two_nodes():
    """Build one-node queue."""
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
    """Test doubly linked list instantiated."""
    assert build_empty_queue.head is None


def test_enqueue_empty_queue(build_empty_queue):
    """Test head after enqueue."""
    q = build_empty_queue
    q.enqueue('hi!')
    assert q.head.val == 'hi!'


def test_enqueue_empty_queue_next(build_empty_queue):
    """Test head.next_node after one enqueue."""
    q = build_empty_queue
    q.enqueue('hi!')
    assert q.head.next_node is None


def test_next_node_three_nodes(build_queue_three_nodes):
    """Test head.next_node after multiple enqueues."""
    q = build_queue_three_nodes
    assert q.head.next_node.val == 'peaches'
    assert q.head.next_node.next_node.val == 'bananas'


def test_peek_empty_queue(build_empty_queue):
    """Test peek method for one node."""
    peek = build_empty_queue.peek()
    assert peek is None


def test_peek_one_node(build_queue_one_node):
    """Test peek method for one node."""
    peek = build_queue_one_node.peek()
    assert peek.val == 'cake'


def test_peek_two_nodes(build_queue_two_nodes):
    """Test peek method for one node."""
    peek = build_queue_two_nodes.peek()
    assert peek.val == 'blue'


def test_head_two_nodes(build_queue_two_nodes):
    """Test peek method for one node."""
    peek = build_queue_two_nodes.peek()
    assert build_queue_two_nodes.head == peek


def test_dequeue_empty_queue(build_empty_queue):
    """Test queue."""
    with pytest.raises(IndexError):
        build_empty_queue.dequeue()


def test_dequeue_two_nodes(build_queue_two_nodes):
    """Test peek method for one node."""
    head_before_dequeue = build_queue_two_nodes.peek()
    next_before_dequeue = head_before_dequeue.next_node
    build_queue_two_nodes.dequeue()
    assert next_before_dequeue == build_queue_two_nodes.head


def test_dequeue_three_nodes(build_queue_three_nodes):
    """Test peek method for one node."""
    head_before_dequeue = build_queue_three_nodes.peek()
    next_before_dequeue = head_before_dequeue.next_node
    build_queue_three_nodes.dequeue()
    assert next_before_dequeue == build_queue_three_nodes.head


def test_len_empty_queue(build_empty_queue):
    """Test len of empty queue."""
    assert len(build_empty_queue) == 0


def test_len_one_node_queue(build_queue_one_node):
    """Test len of empty queue."""
    assert len(build_queue_one_node) == 1


def test_len_three_node_queue(build_queue_three_nodes):
    """Test len of empty queue."""
    assert len(build_queue_three_nodes) == 3


def test_len_after_queue(build_empty_queue):
    """Test head after enqueue."""
    q = build_empty_queue
    q.enqueue('hi!')
    assert len(q) == 1


def test_len_after_queue_three(build_queue_three_nodes):
    """Test head after enqueue."""
    q = build_queue_three_nodes
    q.enqueue('hi!')
    assert len(q) == 4
