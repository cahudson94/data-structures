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


@pytest.fixture
def five_node_simple_nodes_five_edges_graph():
    """."""
    g = Graph()
    g.add_node('corn')
    g.add_node(2)
    g.add_node(3)
    g.add_node('meep')
    g.add_node(10)
    g.add_edge(2, 3)
    g.add_edge(3, 2)
    g.add_edge(2, 'corn')
    g.add_edge('meep', 10)
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


def test_add_node_no_val(one_node_graph):
    """Test adding node with no value raises ValueError."""
    with pytest.raises(ValueError):
        one_node_graph.add_node(None)


def test_add_node_bool(one_node_graph):
    """Test adding node with bool raises ValueError."""
    with pytest.raises(ValueError):
        one_node_graph.add_node(True)


def test_add_node_dupe(two_node_no_edge_graph):
    """Add two nodes to graph."""
    with pytest.raises(ValueError):
        two_node_no_edge_graph.add_node('corn')


def test_add_node_two_times(two_node_no_edge_graph):
    """Add two nodes to graph."""
    two_node_no_edge_graph.add_node('greetings')
    two_node_no_edge_graph.add_node('welcome back')
    assert two_node_no_edge_graph.has_node('greetings')
    assert two_node_no_edge_graph.has_node('welcome back')
    assert two_node_no_edge_graph.nodes() == ['corn', 'beans', 'greetings', 'welcome back']


def test_add_node_once(two_node_no_edge_graph):
    """Add one node to graph."""
    two_node_no_edge_graph.add_node('why')
    assert two_node_no_edge_graph.has_node('why')
    assert two_node_no_edge_graph.nodes() == ['corn', 'beans', 'why']


def test_add_edge_new_nodes(three_node_with_two_edges_graph):
    """Test adding edge with two new nodes."""
    three_node_with_two_edges_graph.add_edge('beans', 'tomato')
    assert three_node_with_two_edges_graph.edges() == [('corn', 2), (['squash', 11], 'corn'), ('beans', 'tomato')]


def test_add_edge_one_new_node(five_node_simple_nodes_five_edges_graph):
    """Test adding edge to one new node, one existing node."""
    five_node_simple_nodes_five_edges_graph.add_edge('hi', 3)
    assert five_node_simple_nodes_five_edges_graph.edges() == [(2, 3), (3, 2), (2, 'corn'), ('meep', 10), ('hi', 3)]


def test_add_edge_existing_nodes(five_node_simple_nodes_five_edges_graph):
    """Test adding edge to two existing nodes."""
    five_node_simple_nodes_five_edges_graph.add_edge(3, 'meep')
    assert five_node_simple_nodes_five_edges_graph.edges() == [(2, 3), (3, 2), (2, 'corn'), ('meep', 10), (3, 'meep')]


def test_delete_node_empty_graph_error(empty_graph):
    """Delete node on empty graph."""
    with pytest.raises(ValueError):
        empty_graph.del_node('delete')


def test_delete_node_graph_error(five_node_with_five_edges_graph):
    """Delete node on populated graph."""
    with pytest.raises(ValueError):
        five_node_with_five_edges_graph.del_node('delete')


def test_delete_node_graph(five_node_with_five_edges_graph):
    """Delete node on populated graph."""
    five_node_with_five_edges_graph.del_node(2)
    assert 2 not in five_node_with_five_edges_graph.nodes()
    assert five_node_with_five_edges_graph.edges() == [((4, 'mustard', 'ketchup'), 'corn'), (['squash', 11.1], 'corn')]


def test_delete_edge_empty_graph_error(empty_graph):
    """Delete node on empty graph."""
    with pytest.raises(ValueError):
        empty_graph.del_edge(1, 2)


def test_delete_edge_graph_error(five_node_with_five_edges_graph):
    """Delete node on empty graph."""
    with pytest.raises(ValueError):
        five_node_with_five_edges_graph.del_edge(1, 2)


def test_delete_edge_graph(five_node_simple_nodes_five_edges_graph):
    """Delete node on empty graph."""
    assert (2, 'corn') in five_node_simple_nodes_five_edges_graph.edges()
    five_node_simple_nodes_five_edges_graph.del_edge(2, 'corn')
    assert (2, 'corn') not in five_node_simple_nodes_five_edges_graph.edges()
