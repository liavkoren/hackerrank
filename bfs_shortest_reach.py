'''
https://www.hackerrank.com/challenges/bfsshortreach

2       : Number of test cases
4 2     : # nodes, # edges
1 2     : edge #1
1 3     : edge #2
1       : starting node

3 1     : # nodes, # edges
2 3     : edge #1
2       : starting node
'''
import fileinput


class Node(object):
    def __init__(self, index):
        self.index = index
        self.neighbors = []
        self.depth = -1

    def __repr__(self):
        return u'Node({self.index}, {self.depth}, {neighbors})'.format(self=self, neighbors=[node.index for node in self.neighbors])


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


def process():
    stream = data_stream()
    number_test_cases = next(stream)[0]
    for test in range(number_test_cases):
        number_nodes, number_edges = next(stream)
        print 'Test case #%d' % (test + 1)
        print(build_graph(number_nodes, number_edges, stream))
        root = next(stream)
        print 'root node is: %d' % root[0]
process()
