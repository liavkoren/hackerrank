"""
https://www.hackerrank.com/challenges/journey-to-the-moon

The first line contains two integers, N and , P separated by a single space. P
lines follow. Each line contains integers separated by a single space A and B such
that 0 <= A, B <= N - 1

and A and B are astronauts from the same country.

----

Algo build_graph(nnodes, edge_list):
    graph = Init Graph w. nnodes
    discovered = [False] * nnodes
    for each node in the graph:
        do DFS, and push the component size onto the graph's component_sizes list
    return graph

Algo count_pairs(graph):
    pair count = 0
    For every component_i in the graph:
        let size := number nodes in the commponent
        for every component_j in the graph: (j > i)
            pair count += size of component_i * size of component_j

alternatively:
    component_sizes = [size(component) for component in graph]
    total_component_count = sum(component_size[1:])
    pair_count = 0
    for index, component in component_sizes[-1]:
        pair_count += component*total_component_count
        total_component_count -= component_size[index+1]
    return pair_count

"""


class Graph:
    """ Adjacency-list graph. """
    def __init__(self, nnodes):
        self.nodes = {index: [] for index in range(nnodes)}
        self.nnodes = nnodes

    def add_edge(self, x, y):
        self.nodes[x].append(y)
        self.nodes[y].append(x)


def build_graph(raw_input):
    lines = [list(map(int, line.split())) for line in raw_input.splitlines()]
    nnodes, nedges = lines[0]
    graph = Graph(nnodes)
    for edge in lines[1:]:
        x, y = edge
        graph.add_edge(x, y)
    return graph


def get_component_sizes(graph):
    """ Given a graph, does DFS across it and returns a list of the graph's component sizes. """
    def recurse(node_index):
        """ Does DFS across a component. """
        nonlocal component_size
        if not discovered[node_index]:
            discovered[node_index] = True
            component_size += 1
            for edge in graph.nodes[node_index]:
                recurse(edge)

    sizes = []
    discovered = [False] * graph.nnodes
    for node in graph.nodes:
        component_size = 0
        recurse(node)
        if component_size > 0:
            sizes.append(component_size)
    return sizes


def count_pairs(graph):
    """ Returns the number of ways you can pick two nodes from the graph with both nodes being in different components. """
    component_sizes = get_component_sizes(graph)
    total_component_count = sum(component_sizes[1:])
    pair_count = 0
    for index, component_size in enumerate(component_sizes[:-1]):
        pair_count += component_size * total_component_count
        total_component_count -= component_sizes[index+1]
    return pair_count


test1 = """5 3
0 1
2 3
0 4
"""
graph1 = build_graph(test1)
assert count_pairs(graph1) == 6

test2 = """4 1
0 2"""
graph2 = build_graph(test2)
assert count_pairs(graph2) == 5

test3 = """12 10
2 3
3 4
5 6
6 7
7 8
5 7
9 10
10 11
11 9"""
graph3 = build_graph(test3)
assert count_pairs(graph3) == 54

