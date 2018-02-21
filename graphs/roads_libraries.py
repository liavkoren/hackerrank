"""
https://www.hackerrank.com/challenges/torque-and-development

Build a representation of the graph.

If library cost is > road cost:
    return library cost * city count

def cost(road_count, library_cost, road_cost):
    return library_cost + road_count * road_count

for each vertex:
    - Do DFS, labeling each vertex with component number, and calculating the weight of the MST.
    - For each new component, inc the component count

total cost = 0
For each component:
    total_cost += library_cost + road_cost + MST weight.

return total cost

count_compnents(graph):
    for node in graph.nodes:
        node.discovered = False
    component_count = 0
    for node in graph.nodes:
        if not node.discovered:
            component_count += 1
        DFS(graph, node)
    return component_count


def cost(road_count, library_cost, road_cost):
    return library_cost + road_count * road_count

"""


class Graph:
    """ Adjacency-list graph. """
    def __init__(self, nnodes):
        self.nodes = {index: [] for index in range(nnodes)}
        self.nnodes = nnodes

    def add_edge(self, x, y):
        self.nodes[x].append(y)
        self.nodes[y].append(x)


def count_road_cities(graph):
    """
    Does DFS on a graph, returns the count of edges in the MST.

    Based on Skiena's implementation of edge-classification on undirected graphs.
    All edges are either tree-edges or back edges, we only care about tree edges
    here.
    """
    tree_edge_count = 0
    discovered = [False] * graph.nnodes
    component_count = 0

    def recurse(node_index):
        nonlocal tree_edge_count
        discovered[node_index] = True
        for edge in graph.nodes[node_index]:
            if not discovered[edge]:
                discovered[edge] = True
                tree_edge_count += 1
                recurse(edge)

    for node_index in graph.nodes:
        if not discovered[node_index]:
            component_count += 1
            recurse(node_index)
    return tree_edge_count, component_count


def cost(road_count, road_cost, library_cost):
    return library_cost + road_cost * road_count


# The actual code for hackerrank

q = int(input().strip())
for a0 in range(q):
    nnodes, nedges, library_cost, road_cost = input().strip().split(' ')
    nnodes, nedges, library_cost, road_cost = [int(nnodes,), int(nedges,), int(library_cost,), int(road_cost)]
    if library_cost < road_cost:
        print(f'{nnodes * library_cost}')
    else:
        graph = Graph(nnodes=nnodes)
        for a1 in range(nedges):
            city_1, city_2 = input().strip().split(' ')
            # One-indexing!!!
            graph.add_edge(int(city_1) - 1, int(city_2) - 1)
        roads, cities = count_road_cities(graph)
        print(roads * road_cost + cities * library_cost)


# -----
# Tests
# single component graph
test1 = Graph(nnodes=5)
test1.add_edge(0, 1)
test1.add_edge(0, 2)
test1.add_edge(1, 3)
test1.add_edge(1, 4)
test1.add_edge(4, 0)
assert count_road_cities(test1) == (4, 0)

# three compnent graph:
test2 = Graph(nnodes=12)
test2.add_edge(0, 1)
test2.add_edge(0, 2)
test2.add_edge(1, 3)
test2.add_edge(1, 4)
test2.add_edge(4, 0)
test2.add_edge(5, 6)
test2.add_edge(6, 7)
test2.add_edge(8, 9)
test2.add_edge(9, 10)
test2.add_edge(10, 11)
test2.add_edge(10, 8)
test2.add_edge(11, 9)
assert count_road_cities(test2) == (9, 0)


test1 = """3 3 2 1
1 2
3 1
2 3"""

test2 = """6 6 2 5
1 3
3 4
2 4
1 2
2 3
5 6"""


# For local testing
def solve(raw_input):
    lines = raw_input.splitlines()
    nnodes, nedges, library_cost, road_cost = lines[0].strip().split(' ')
    nnodes, nedges, library_cost, road_cost = [int(nnodes,), int(nedges,), int(library_cost,), int(road_cost)]
    if library_cost < road_cost:
        return nnodes * library_cost
    else:
        graph = Graph(nnodes=nnodes)
        for a1 in range(nedges):
            city_1, city_2 = lines[1+a1].strip().split(' ')
            # One-indexing!!!
            graph.add_edge(int(city_1) - 1, int(city_2) - 1)
        roads, cities = count_road_cities(graph)
        return roads * road_cost + cities * library_cost



test1 = """9 2 91 84
8 2
2 9"""
assert solve(test1) == 805


test2 = """5 9 92 23
2 1
5 3
5 1
3 4
3 1
5 4
4 1
5 2
4 2"""
assert solve(test2) == 184

test3 = """8 3 10 55
6 4
3 2
7 1"""
assert solve(test3) == 80
assert solve('1 0 5 3') == 5
assert solve('2 0 102 1') == 204


