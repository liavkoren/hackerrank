'''
https://www.hackerrank.com/challenges/bfsshortreach

Input:
2       : Number of test cases
4 2     : # nodes, # edges
1 2     : edge #1
1 3     : edge #2
1       : starting node

3 1     : # nodes, # edges
2 3     : edge #1
2       : starting node

"Given `q` queries in the form of a graph and some starting node, `s`, perform
each query by calculating the shortest distance from starting node `s` to all
the other nodes in the graph. Then print a single line of `n - 1` space-
separated integers listing node `s`'s shortest distance to each of the `n - 1`
other nodes (ordered sequentially by node number); if `s` is disconnected from a
node, print `-1` as the distance to that node."

node.increment_neighbors():
    If a neighbor's distance is -1, set the distance to self.distance + 1

Get node root node (`s`). Set root's distance to 0. Place root into queue.
While queue:
    Get the next node in the queue. Call node.increment_neighbors()
    Put the neighbors into the queue.
Finally:
    - get each node by index, EXCEPT node root, multiply distance by 6,
    add to output array, cast to string, concat with whitespace, print.
'''
from collections import deque
import fileinput


class Node(object):
    def __init__(self, index):
        self.index = index
        self.neighbors = []
        self.depth = -1

    def __repr__(self):
        return u'Node({self.index}, {self.depth}, {neighbors})'.format(self=self, neighbors=[node.index for node in self.neighbors])

    def increment_neighbors(self):
        for node in self.unvisited_neighbors:
            node.depth = self.depth + 1

    @property
    def unvisited_neighbors(self):
        return [node for node in self.neighbors if node.depth == -1]


def data_stream():
    for line in fileinput.input():
        line = line.strip().split(' ')
        yield map(int, line)


def build_graph(number_nodes, number_edges, stream):
    graph = {index+1: Node(index+1) for index in range(number_nodes)}
    for index in range(number_edges):
        index_a, index_b = next(stream)
        node_a = graph[index_a]
        node_b = graph[index_b]
        node_a.neighbors.append(node_b)
        node_b.neighbors.append(node_a)
    return graph


def search_graph(root_index, graph):
    """
    Given a root_index and a graph:
    Get the root by index
    Set the root's depth 0
    Queue = [root]
    while there's a queue:
        - get the next node
        - set neighbor's depth
        - add unvisited neighbors to queue.

    Finally:
    """
    root = graph[root_index]
    root.depth = 0
    queue = deque([root])

    while queue:
        node = queue.popleft()
        queue.extend(node.unvisited_neighbors)
        node.increment_neighbors()


def print_graph(root_index, graph):
    """
    - get each node by index, EXCEPT node root,
    - multiply distance by 6 if dist > -1,
    - add to output array, cast to string, concat with whitespace, print.
    """
    out = []
    for index in range(1, len(graph) + 1):
        if index == root_index:
            continue
        node = graph[index]
        if node.depth > -1:
            out.append(node.depth * 6)
        else:
            out.append(node.depth)
    print ' '.join(map(str, out))


def process():
    stream = data_stream()
    number_test_cases = next(stream)[0]
    for test in range(number_test_cases):
        number_nodes, number_edges = next(stream)
        graph = build_graph(number_nodes, number_edges, stream)
        root_index = next(stream)[0]
        search_graph(root_index, graph)
        print_graph(root_index, graph)

process()
