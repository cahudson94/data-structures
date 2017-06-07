"""Python implementation of a graph that is unweighted and directed."""


class Graph(object):
    """."""

    def __init__(self):
        """Instantiate a graph with no nodes or edges."""
        self.nodes_list = []
        self.edges_list = []

    def nodes(self):
        """Return the nodes on the graph."""
        return self.nodes_list

    def edges(self):
        """Return the edges of the graph."""
        return self.edges_list

    def add_node(self, val):
        """Add a node to the graph with a value."""
        if val is None or type(val) is bool:
            raise ValueError('Please use a valid value.')
        if self.has_node(val):
            raise ValueError('{} is already in this graph.'.format(val))
        self.nodes_list.append(val)

    def has_node(self, val):
        """Check if a node is in the graph."""
        if val not in self.nodes_list:
            return False
        return True

    def add_edge(self, val1, val2):
        """
        Add an edge between two nodes in the graph.

        If the nodes are not in the graph add them and the edge.
        """
        if not self.has_node(val1):
            self.add_node(val1)
        if not self.has_node(val2):
            self.add_node(val2)
        if (val1, val2) not in self.edges_list:
            self.edges_list.append((val1, val2))

    def del_node(self, val):
        """Remove a node and any edges it is part of."""
        if not self.has_node(val):
            raise ValueError('This node does not exist.')
        self.nodes_list.remove(val)
        self.edges_list = list(filter(lambda x: val not in x, self.edges_list))

    def del_edge(self, val1, val2):
        """Remove an edge between two nodes."""
        if (val1, val2) not in self.edges_list:
            raise ValueError('This edge does not exist.')
        self.edges_list.remove((val1, val2))

    def neighbors(self, val):
        """Check for the edges from a node."""
        if val in self.nodes_list:
            neighbors = filter(lambda x: x[0] == val, self.edges_list)
            neighbors = list(map(lambda x: x[1], neighbors))
            return neighbors
        raise ValueError('That node is not part of this graph.')

    def adjacent(self, val1, val2):
        """Check if two nodes are connected via an edge."""
        for edge in self.edges_list:
            if val1 in edge and val2 in edge:
                return True
        return False
