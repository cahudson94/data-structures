"""Python implementation of a graph that is unweighted and directed."""


class Graph(object):
    """Define attributes and methods of graph class."""

    def __init__(self):
        """Instantiate graph object."""
        self._graphdict = {}

    def nodes(self):
        """Return list of graph nodes."""
        return list(self._graphdict.keys())

    def edges(self):
        """Return list of graph edges."""
        edges = []
        for key in self.nodes():
            for item in self._graphdict[key]:
                edges.append((key, item))
        return edges

    def add_node(self, val):
        """Add a node to graph."""
        if type(val) not in [str, int, float]:
            raise ValueError('Please use a valid value.')
        if self.has_node(val):
            raise ValueError('{} is already in this graph.'.format(val))
        self._graphdict[val] = []

    def has_node(self, val):
        """Return boolean for node in graph membership."""
        return val in self._graphdict

    def add_edge(self, val1, val2):
        """Add an edge between to vals, add vals if not currently node."""
        if not self.has_node(val1):
            self.add_node(val1)
        if not self.has_node(val2):
            self.add_node(val2)
        if (val1, val2) not in self.edges():
            self._graphdict[val1].append(val2)

    def del_node(self, val):
        """Remove a node and edges that refer to it."""
        if not self.has_node(val):
            raise ValueError('This node is not in the graph.')
        del self._graphdict[val]
        for key in self.nodes():
            if val in self._graphdict[key]:
                self._graphdict[key].remove(val)

    def del_edge(self, val1, val2):
        """Remove an edge between two nodes."""
        if (val1, val2) not in self.edges():
            raise ValueError('This edge does not exist.')
        self._graphdict[val1].remove(val2)

    def neighbors(self, val):
        """Return list of neighbors for a given node."""
        if val not in self.nodes():
            raise ValueError('This node is not in the graph.')
        return self._graphdict[val]

    def adjacent(self, val1, val2):
        """Return bool of whether val1 is val2's neighbor."""
        if val1 not in self._graphdict or val2 not in self._graphdict:
            raise ValueError('One or both values are not in the graph.')
        if val2 in self._graphdict[val1]:
            return True
        else:
            raise AssertionError('There is no edge from the \
first value to the second.')

    def depth_first_traversal(self, val):
        """Return a path starting from val, traversing depth-first."""
        from stack import Stack
        if not self.has_node(val):
            raise ValueError('This node is not in the graph.')
        path = []
        to_visit = Stack()
        current_val = val
        while True:
            if current_val not in path:
                path.append(current_val)
                for neighb in self._graphdict[current_val][::-1]:
                    to_visit.push(neighb)
            if len(to_visit) == 0:
                break
            current_val = to_visit.pop()
        return path

    def breadth_first_traversal(self, val):
        """Return a path starting from val, traversing depth-first."""
        from que_ import QueueStructure
        if not self.has_node(val):
            raise ValueError('This node is not in the graph.')
        path = []
        current_val = val
        to_visit = QueueStructure()
        while True:
            if current_val not in path:
                path.append(current_val)
                for neighb in self._graphdict[current_val]:
                    to_visit.enqueue(neighb)
            if len(to_visit) == 0:
                break
            current_val = to_visit.dequeue()
        return path
