"""Python implementation of a graph that is unweighted and directed."""
from math import inf


class Graph(object):
    """Define attributes and methods of graph class."""

    def __init__(self):
        """Instantiate graph object."""
        self._graphdict = {}

    def nodes(self):
        """Return list of graph nodes."""
        return list(self._graphdict.keys())

    def edges(self):
        """Return dict of graph edges."""
        edges = {}
        for key in self.nodes():
            for item in self._graphdict[key]:
                edges[(key, item[0])] = item[1]
        return edges

    def add_node(self, val):
        """Add a node to graph."""
        if type(val) not in [str, int, float]:
            raise ValueError('Please use a valid value.')
        if self.has_node(val):
            raise KeyError('{} is already in this graph.'.format(val))
        self._graphdict[val] = []

    def has_node(self, val):
        """Return boolean for node in graph membership."""
        return val in self._graphdict

    def add_edge(self, val1, val2, weight):
        """Add an edge between to vals, add vals if not currently node."""
        if type(weight) not in [int, float]:
            raise ValueError('Weight must be int or float.')
        if not self.has_node(val1):
            self.add_node(val1)
        if not self.has_node(val2):
            self.add_node(val2)
        if (val1, val2, weight) not in self.edges():
            self._graphdict[val1].append((val2, weight))

    def del_node(self, val):
        """Remove a node and edges that refer to it."""
        if not self.has_node(val):
            raise KeyError('This node is not in the graph.')
        del self._graphdict[val]
        for key in self.nodes():
            print(key)
            for item in self._graphdict[key]:
                print(item)
                if val == item[0]:
                    self._graphdict[key].remove(item)

    def del_edge(self, val1, val2, weight):
        """Remove an edge between two nodes."""
        if (val1, val2, weight) not in self.edges():
            raise KeyError('This edge does not exist.')
        self._graphdict[val1].remove((val2, weight))

    def neighbors(self, val):
        """Return list of neighbors for a given node."""
        if val not in self.nodes():
            raise ValueError('This node is not in the graph.')
        return [item[0] for item in self._graphdict[val]]

    def adjacent(self, val1, val2):
        """Return bool of whether val1 is val2's neighbor or vice versa."""
        if val1 not in self._graphdict or val2 not in self._graphdict:
            raise KeyError('One or both values are not in the graph.')
        return val2 in self.neighbors(val1) or val1 in self.neighbors(val2)

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
                    to_visit.push(neighb[0])
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
                    to_visit.enqueue(neighb[0])
            if len(to_visit) == 0:
                break
            current_val = to_visit.dequeue()
        return path

    def b_f_shortest_path(self, start, end):
        """"Find the shortest path using the bellman ford algorithm."""
        iterations = len(self.edges) - 1
        iteration = 0
        unvisited = [node for node in self.nodes()]
        paths = dict([[node, inf] for node in self.nodes()])
        prev_paths = {}
        current_node = start
        paths[current_node] = 0
        edges = self.edges()
        path_total = 0
        while iteration < iterations or paths == prev_paths:
            for edge in edges:
                if edge[0] == current_node:
                    if path_total + edge[2] < paths[edge[1]]:
                        paths[edge[1]] = path_total + edge[2]
            current_index = unvisited[current_node]
            current_node = unvisited[current_index + 1]
            if current_node == start:
                iteration += 1
        return paths[end]

    def d_shortest_path(self, start, end):
        """Find the shortest path using Dijkstra's algorithm."""
        if start not in self.nodes() or end not in self.nodes():
            raise KeyError('Graph does not contain one or both nodes.')
        current_node = start  # set current node to start value
        visited = {}  # create empty set of visited nodes
        unvisited = dict([[node, inf] for node in self.nodes()])  # populate dictionary of node keys and infinite values for all nodes in graph
        unvisited[current_node] = 0  # overwrite the path weight for current node to 0
        edges = self.edges()  # save a list of graph edges
        while end not in visited or min(unvisited.values()) == inf:  # runs while end val isn't in visited or the min value of unvisited is infinite
            for node in unvisited:  # for every node that hasn't been visited
                if (current_node, node) in edges:  # if there's an edge between the current and an unvisited node
                    tentative_weight = unvisited[current_node] + edges[(current_node, node)]  # calculate the weight of the path to the current node plus the weight of the edge in question
                    if unvisited[node] > tentative_weight:  # if the stored weight is greater than the calculated weight
                        unvisited[node] = tentative_weight  # overwrite with the new weight
            visited[current_node] = min(unvisited.values())  # create a key of current node in visited with the lowest weight in unvisited
            del unvisited[current_node]  # delete the current node from unvisited
            if len(unvisited):  # if there are still entries in unvisited
                current_node = min(unvisited.keys(), key=unvisited.get)[0]  # change the current node to the lowest valued key in unvisited
            else:
                break  # break the while loop if unvisited is empty
        return visited[end]
