"""Python implementation of a graph that is unweighted and directed."""


class Graph(object):
    """."""

    def __init__(self):
        """."""
        self.nodes_list = []
        self.edges_list = []

    def nodes(self):
        """."""
        return self.nodes_list

    def edges(self):
        """."""
        return self.edges_list

    def add_node(self, val):
        """."""
        if val is None or type(val) is bool:
            raise ValueError('Please use a valid value.')
        if self.has_node(val):
            raise ValueError('{} is already in this graph.'.format(val))
        self.nodes_list.append(val)

    def has_node(self, val):
        """."""
        if val not in self.nodes_list:
            return False
        return True

    def add_edge(self, val1, val2):
        """."""
        if not self.has_node(val1):
            self.add_node(val1)
        if not self.has_node(val2):
            self.add_node(val2)
        if (val1, val2) not in self.edges_list:
            self.edges_list.append((val1, val2))

    def del_node(self, val):
        """."""
        if not self.has_node(val):
            raise ValueError('This node is not in the graph.')
        self.nodes_list.remove(val)
        self.edges_list = list(filter(lambda x: val not in x, self.edges_list))

    def del_edge(self, val1, val2):
        """."""
        if (val1, val2) not in self.edges_list:
            raise ValueError('This edge does not exist.')
        self.edges_list.remove((val1, val2))

    def neighbors(self, val):
        """."""
        if val not in self.nodes_list:
            raise ValueError('This node is not in the graph.')
        neighbors = filter(lambda x: x[0] == val, self.edges_list)
        neighbors = list(map(lambda x: x[1], neighbors))
        return neighbors

    def adjacent(self, val1, val2):
        """."""
        for edge in self.edges_list:
            return val1 in edge and val2 in edge
