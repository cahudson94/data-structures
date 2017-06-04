"""Test for first Graph data structure."""
import pytest
from graph_1 import Graph


@pytest.fixture
def empty_graph():
    """."""
    return Graph()


@pytest.fixture
def one_node_graph():
    """."""
    g = Graph()
    g.add_node('corn')
    return g


@pytest.fixture
def two_node_no_edge_graph():
    """."""
    g = Graph()
    g.add_node('corn')
    g.add_node('beans')
    return g


@pytest.fixture
def two_node_with_edge_graph():
    """."""
    g = Graph()
    g.add_node('corn')
    g.add_node('beans')
    g.add_edge('corn', 'beans')
    return g


@pytest.fixture
def three_node_with_two_edges_graph():
    """."""
    g = Graph()
    g.add_node('corn')
    g.add_node(2)
    import pdb; pdb.set_trace()
    g.add_node(['squash', 11])
    g.add_edge('corn', 2)
    g.add_edge(['squash', 11], 'corn')
    return g


@pytest.fixture
def five_node_with_five_edges_graph():
    """."""
    g = Graph()
    g.add_node('corn')
    g.add_node(2)
    g.add_node(['squash', 11.1])
    g.add_node({'pie': 'cherry', 'cake': 'chocolate'})
    g.add_node((4, 'mustard', 'ketchup'))
    g.add_edge(2, ['squash', 11.1])
    g.add_edge((4, 'mustard', 'ketchup'), 'corn')
    g.add_edge(2, 'corn')
    g.add_edge('corn', 2)
    g.add_edge(['squash', 11.1], 'corn')
    return g


def test_nodes_in_empty_graph(empty_graph):
    """."""
    assert empty_graph.nodes() == []


def test_nodes_in_one_node_graph(one_node_graph):
    """."""
    assert one_node_graph.nodes() == ['corn']


def test_nodes_in_two_node_graph(two_node_no_edge_graph):
    """."""
    assert two_node_no_edge_graph.nodes() == ['corn', 'beans']


def test_nodes_in_three_node_graph(three_node_with_two_edges_graph):
    """."""
    assert three_node_with_two_edges_graph.nodes() == ['corn', 2, ['squash', 11]]


def test_nodes_in_five_node_graph(five_node_with_five_edges_graph):
    """."""
    assert five_node_with_five_edges_graph.nodes() == ['corn', 2, ['squash',
                                                       11.1], {'pie': 'cherry',
                                                       'cake': 'chocolate'},
                                                       (4, 'mustard', 'ketchup')]
