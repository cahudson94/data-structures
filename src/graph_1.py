
"""Python implementation of a graph that is unweighted and directed."""


class Graph(object):
    """."""

    def __init__(self):
        """."""
        self._graphdict = {}

    def nodes(self):
        """."""
        return list(self._graphdict.keys())

    def edges(self):
        """."""
        edges = []
        for key in self.nodes():
            for item in self._graphdict[key]:
                edges.append((key, item))
        return edges

    def add_node(self, val):
        """."""
        if type(val) not in [str, int, float]:
            raise ValueError('Please use a valid value.')
        if self.has_node(val):
            raise ValueError('{} is already in this graph.'.format(val))
        self._graphdict[val] = []

    def has_node(self, val):
        """."""
        return val in self._graphdict

    def add_edge(self, val1, val2):
        """."""
        if not self.has_node(val1):
            self.add_node(val1)
        if not self.has_node(val2):
            self.add_node(val2)
        if (val1, val2) not in self.edges():
            self._graphdict[val1].append(val2)

    def del_node(self, val):
        """."""
        if not self.has_node(val):
            raise ValueError('This node is not in the graph.')
        del self._graphdict[val]
        for key in self.nodes():
            if val in self._graphdict[key]:
                self._graphdict[key].remove(val)

    def del_edge(self, val1, val2):
        """."""
        if (val1, val2) not in self.edges():
            raise ValueError('This edge does not exist.')
        self._graphdict[val1].remove(val2)

    def neighbors(self, val):
        """."""
        if val not in self.nodes():
            raise ValueError('This node is not in the graph.')
        return self._graphdict[val]

    def adjacent(self, val1, val2):
        """."""
        return val2 in self._graphdict[val1] or val1 in self._graphdict[val2]
