# Hackerrank

#!/bin/python

import sys


n, m = raw_input().strip().split(' ')
n, m = [int(n), int(m)]

competitor_list = []
topic_i = 0
for topic_i in xrange(n):
    topic_t = str(raw_input().strip())
    competitor_list.append(topic_t)


def score_list(competitor_list):
    max_topics_known = 0
    max_topics_known_team_count = 0
    for index, competitor_a in enumerate(competitor_list):
        for competitor_b in competitor_list[index:]:
            topics_known = bin_to_score(bin_combine(competitor_a, competitor_b))
            if topics_known > max_topics_known:
                max_topics_known = topics_known
                max_topics_known_team_count = 1
            elif topics_known == max_topics_known:
                max_topics_known_team_count += 1
    print(max_topics_known)
    # print(bin_to_score(max_topics_known))
    print(max_topics_known_team_count)


def bin_to_score(bin_string):
    return bin_string.count('1')


def bin_combine(a, b):
    a_bin = '0b%s' % a
    a_ten = int(a_bin, 2)

    b_bin = '0b%s' % b
    b_ten = int(b_bin, 2)
    return bin(a_ten | b_ten)

score_list(competitor_list)

'''
The first line contains two integers, and , separated by a single space, where
represents the number of people, and represents the number of topics. lines
follow. Each line contains a binary string of length . If the th line's th
character is , then the th person knows the th topic; otherwise, he doesn't know
the topic.

Okay..
- O(n^2)
- For each competitor, OR them together with every subsequent competitor. If:
    - the total is higher than the previous max_topics_know:
        Then set the max_topics_known to the new value, and set max_know_team_count to zero.
    - elif the total is equal to the max_topics know:
        Then increment max_topics_team_count + 1
return max_topics_known, max_topics_team_count
test = [10101, 11100, 11010, 00101]
'''


# --------------

import fileinput
import math


def has_squares(num_pair):
    low, high = num_pair
    sq_root_low = math.sqrt(low)
    sq_root_high = math.sqrt(high)
    return sorted([math.ceil(sq_root_low), math.floor(sq_root_high)]) == [math.ceil(sq_root_low), math.floor(sq_root_high)]


def is_square(num):
    return math.sqrt(num).is_integer()


def count_squares(num_pair):
    low, high = num_pair
    if low < 0 and high < 0:
        return 0
    low = max(0, low)
    if has_squares((low, high)):
        sq_root_low = math.ceil(math.sqrt(low))
        sq_root_high = math.floor(math.sqrt(high))
        return int(sq_root_high + 1 - sq_root_low)
    else:
        return 0


def process(test_cases):
    tests = [test.strip().split(' ') for test in test_cases]
    tests = tests[1:]
    tests = [[int(num) for num in test] for test in tests]
    for test in tests:
        print count_squares(test)


def get_raw_input(online=True):
    if online:
        return [line for line in fileinput.input()]
    else:
        return ['2', '3 9\n', '17 24', '-10 100', '-10 10', '0 0', '-100 -10', '-10 1000000000']

raw_input = get_raw_input(online=False)
process(raw_input)






# Custom PDF
# ----------

from string import ascii_lowercase

h = map(int, raw_input().strip().split(' '))
# h = map(int, h.strip().split(' '))

word = raw_input().strip()
height_map = dict(zip(ascii_lowercase, h))


def word_area(word):
    letter_heights = [height_map[letter] for letter in word]
    word_height = max(letter_heights)
    print word_height * len(word)

word_area(word)

# Kangaroo
# https://www.hackerrank.com/challenges/kangaroo

#!/bin/python

x1, v1, x2, v2 = raw_input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]

'''
x1 + v1*t = x2 + v2*t
x1 + v1*t - v2*t = x2
t(v1 - v2) = x2 - x1
t = (x2 - x1) / (v1 - v2)
'''

numerator = x2 - x1
denominator = v1 - v2
if denominator == 0:
    if numerator == 0:
        print 'YES'
    else:
        print 'NO'
elif numerator / denominator > 0:
    print 'YES'
else:
    print 'NO'


# ================================================

# Tree traversals
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

nodes = {value: Node(value) for value in range(1, 7)}
nodes[5].left = nodes[1]
nodes[5].right = nodes[4]
nodes[3].left = nodes[5]
nodes[3].right = nodes[2]
nodes[2].left = nodes[6]

def preOrder(node):
    def inner(node):
        if not node:
            return
        stack = [node]
        history = []
        while stack:
            node = stack.pop()
            history.append(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return history
    traversal = inner(node)
    print ' '.join(str(num) for num in traversal)

nodes = {value: Node(value) for value in range(1, 7)}
'''
PostOrder traversal:
While there are unexplored nodes:
    Push the current node onto the stack.
    If the current node has a left branch, push the left branch onto the stack.
    If the current node has a right branch, push the right branch onto the stack.
    else if the current node has no branches, or the node has been explored, pop it off the stack and add it to the history.
'''


def postOrder(node):
    def inner(node):
        if not node:
            return
        stack = [node]
        history = []
        while stack:
            if node.left:
                stack.append(node.left)
                node = node.left
                continue
            if node.right:
                stack.append(node.right)
                node = node.right
                continue
            else:



    traversal = inner(node)
    print ' '.join(str(num) for num in traversal)


def postOrder(node):
    def inner(node):
        if not node:
            return
        stack = []
        history = []
        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            if not node.right and not node.left:
                history.append(node.data)
        return history
    traversal = inner(node)
    print ' '.join(str(num) for num in traversal)


# Inorder
nodes = {value: Node(value) for value in range(1, 7)}
nodes[3].left = nodes[5]
nodes[3].right = nodes[2]
nodes[5].left = nodes[1]
nodes[5].right = nodes[4]
nodes[2].left = nodes[6]


"""
- While node:
if node.left & new:
    push node onto stack
    node = node.left
elif node.right & new:
    push node
    node = node.right
else:
    hist.append(node)
    node = stack.pop()

stack   history     node    temp
[]      []          3
[3]                 5
[3 5]               1
[3]     [1]         5
[3 5]   [1]         4
[]



    Check if the current node is empty / null
    Traverse the left subtree by recursively calling the in-order function.
    Display the data part of the root (or current node).
    Traverse the right subtree by recursively calling the in-order function.

"""


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
    print ' '.join(str(num) for num in history if num)
InOrder(nodes[3])


'''
TREE DEPTH
set global_depth counter to 0
Check if the current node is empty / null:
    return depth counter
Traverse the left subtree by recursively calling the depth-counter function, and inc local_depth.

Display the data part of the root (or current node):
    global_depth = max(global_depth, local_depth)

Traverse the right subtree by recursively calling the depth-counter function, and inc local_depth.
'''


class Solution:
    def insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def getHeight(self, root):
        self.global_depth = 0

        def inner(node, local_depth):
            if node is None:
                return
            if node.left:
                inner(node.left, local_depth + 1)
            self.global_depth = max(local_depth, self.global_depth)
            if node.right:
                inner(node.right, local_depth + 1)
        inner(root, 0)
        return self.global_depth

Solution().getHeight(nodes[3])


'''
https://www.hackerrank.com/challenges/swap-nodes-algo

Sample input #00
3
2 3
-1 -1
-1 -1
2
1
1

Sample output
3 1 2
2 1 3

Sample Input #01

5
2 3
-1 4
-1 5
-1 -1
-1 -1
1
2

Sample Output #01

4 2 1 5 3

Sample Input #02

11
2 3
4 -1
5 -1
6 -1
7 8
-1 9
-1 -1
10 11
-1 -1
-1 -1
-1 -1
2
2
4

Sample Output #02

2 9 6 4 1 3 7 5 11 8 10
2 6 9 4 1 3 7 5 10 8 11
'''
def clean_file_input(input):
    output = []
    for line in input:
        output.append(tuple(int(item) for item in line.strip().split(' ')))
    return output


import fileinput

def get_input():
    output = []
    for line in fileinput.input():
        output.append(tuple(int(item) for item in line.strip().split(' ')))
    return output



input = get_input()

test1 = [(3,), (2, 3), (-1, -1), (-1, -1), (2,), (1,), (1,)]
test2 = [(17,), (2, 3), (4, 5), (6, -1), (-1, 7), (8, 9), (10, 11), (12, 13), (-1, 14), (-1, -1), (15, -1), (16, 17), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (2,), (2,), (3,)]
test3 = [(11,), (2, 3), (4, -1), (5, -1), (6, -1), (7, 8), (-1, 9), (-1, -1), (10, 11), (-1, -1), (-1, -1), (-1, -1), (2,), (2,), (4,)]

'''
test3 = [(11,),

     (2, 3),  #1
  (4, -1), (5, -1), #2, 3
(6, -1),       (7, 8), #4, 5
(-1, 9), (-1, -1), (10, 11), #6, 7, 8
(-1, -1), (-1, -1), (-1, -1),
(2,), (2,), (4,)]
'''
from collections import deque


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


def solver():
    tree = build_tree(test_case)
    swap_nodes(tree, test_case)






# ---------------
# https://www.hackerrank.com/challenges/is-binary-search-tree


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
    return history


def check_binary_search_tree_(root):
    traversal = in_order(root)
    is_ordered = sorted(traversal) == traversal
    is_strictly_increasing = len(set(traversal)) == len(traversal)
    return is_ordered and is_strictly_increasing
