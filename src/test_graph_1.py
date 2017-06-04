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


def test_has_node_one_node(one_node_graph):
    """Test one-node graph has_node method."""
    assert one_node_graph.has_node('corn') is True
    assert one_node_graph.has_node([1, 2, 3]) is False


def test_has_node_two_nodes(two_node_no_edge_graph):
    """Test two-node graph has_node method."""
    assert two_node_no_edge_graph.has_node('beans') is True
    assert two_node_no_edge_graph.has_node('picante') is False


def test_has_node_five_nodes(five_node_with_five_edges_graph):
    """Test five-node graph has_node method."""
    assert five_node_with_five_edges_graph.has_node('picante') is False
    assert five_node_with_five_edges_graph.has_node(11.1) is False
    assert five_node_with_five_edges_graph.has_node(2) is True
    assert five_node_with_five_edges_graph.has_node({'pie': 'cherry', 'cake': 'chocolate'}) is True
    assert five_node_with_five_edges_graph.has_node(['squash', 11.1]) is True


def test_edges_empty_graph(empty_graph):
    """Test an empty graph for edges."""
    assert empty_graph.edges() == []


def test_edges_one_node_graph(one_node_graph):
    """Test an empty graph for edges."""
    assert one_node_graph.edges() == []


def test_edges_two_node_no_edge_graph(two_node_no_edge_graph):
    """Test an empty graph for edges."""
    assert two_node_no_edge_graph.edges() == []


def test_edges_two_node_edge(two_node_with_edge_graph):
    """Test an empty graph for edges."""
    assert two_node_with_edge_graph.edges() == [('corn', 'beans')]


def test_edges_three_node_edge(three_node_with_two_edges_graph):
    """Test an empty graph for edges."""
    assert three_node_with_two_edges_graph.edges() == [('corn', 2),(['squash', 11], 'corn')]


def test_edges_five_node_edge(five_node_with_five_edges_graph):
    """Test an empty graph for edges."""
    assert five_node_with_five_edges_graph.edges() == [(2, ['squash', 11.1]), ((4, 'mustard', 'ketchup'), 'corn'), (2, 'corn'), ('corn', 2), (['squash', 11.1], 'corn')]
