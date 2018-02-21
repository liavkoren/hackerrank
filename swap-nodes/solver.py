from collections import deque
import fileinput


class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.depth = None

    def __repr__(self):
        return 'Node({self.data}, left={self.left}, right={self.right} (@ {self.depth}))'.format(self=self)

    def __str__(self):
        return str(self.data)


def clean_input(file_iterable):
    output = []
    for line in file_iterable:
        output.append(tuple(int(item) for item in line.strip().split(' ')))
    return output

test1 = [(3,), (2, 3), (-1, -1), (-1, -1), (2,), (1,), (1,)]
test2 = [(17,), (2, 3), (4, 5), (6, -1), (-1, 7), (8, 9), (10, 11), (12, 13), (-1, 14), (-1, -1), (15, -1), (16, 17), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (2,), (2,), (3,)]
test3 = [(11,), (2, 3), (4, -1), (5, -1), (6, -1), (7, 8), (-1, 9), (-1, -1), (10, 11), (-1, -1), (-1, -1), (-1, -1), (2,), (2,), (4,)]


def clean_node_pair(pair):
    left, right = pair
    if left == -1:
        left = None
    if right == -1:
        right = None
    return (left, right)


def build_tree(test_case):
    number_nodes = test_case[0][0]
    nodes = test_case[1:number_nodes+1]
    assert len(nodes[-1]) == 2
    nodes = deque([clean_node_pair(pair) for pair in nodes])
    root = Node(1)
    root.depth = 1

    # build the tree using bread-first search
    visitor_queue = deque([root])
    while visitor_queue:
        current_node = visitor_queue.popleft()
        if not current_node.data:
            continue

        current_pair = nodes.popleft()
        left, right = current_pair
        current_node.left = Node(left)
        current_node.right = Node(right)
        inc_node_depth(current_node)
        visitor_queue.extend([current_node.left, current_node.right])
    return root


def inc_node_depth(node):
    try:
        if node.left.data:
            node.left.depth = node.depth + 1
    except AttributeError:
        pass
    try:
        if node.right.data:
            node.right.depth = node.depth + 1
    except AttributeError:
        pass


tree = build_tree(test2)


def swap_nodes(tree, test_case, file_path=None):
    '''
    Perform breadth-first search thru the tree, tagging each node
    with its depth. For each index in the swap-indicies,  If the depth is a
    multiple of the index, the swap each sub-tree for every node at that level.
    After completing all swaps for that index, print in_order traversal.
    '''
    number_nodes = test_case[0][0]
    number_swaps = test_case[number_nodes+1]
    assert len(number_swaps) == 1
    number_swaps = number_swaps[0]
    swap_indicies = test_case[number_nodes+2:]
    for swap_index in swap_indicies:
        swap_index = swap_index[0]
        visitor_queue = deque([tree])
        while visitor_queue:
            current = visitor_queue.popleft()
            if current.data is None:
                continue
            if current.depth % swap_index == 0:
                current.left, current.right = current.right, current.left
            visitor_queue.extend([current.left, current.right])
        output = in_order(tree)
        if file_path:
            with open(file_path, 'a') as file:
                file.write(output)
                file.write('\n')


def in_order(root):
    history = []

    def inner(root):
        if not root:
            return
        if root.left:
            inner(root.left)
        history.append(root.data)
        if root.right:
            inner(root.right)
    inner(root)
    output = ' '.join(str(num) for num in history if num)
    print output
    return output


def solver(test_case, file_path=None):
    tree = build_tree(test_case)
    swap_nodes(tree, test_case, file_path=file_path)

if __name__ == '__main__':
    # file_input = fileinput.input()
    base_dir = '/Users/liavkoren/dev/hackerrank/swap-nodes/%s'
    with open(base_dir % 'input10.txt')  as file_input:
        cleaned_input = clean_input(file_input)
        solver(cleaned_input, file_path='actual_output10.txt')
