#!/bin/python3

from functools import total_ordering

n1, n2, n3 = input().strip().split(' ')
n1, n2, n3 = [int(n1), int(n2), int(n3)]
h1 = list(reversed([int(h1_temp) for h1_temp in input().strip().split(' ')]))
h2 = list(reversed([int(h2_temp) for h2_temp in input().strip().split(' ')]))
h3 = list(reversed([int(h3_temp) for h3_temp in input().strip().split(' ')]))


@total_ordering
class Stack(object):
    __slots__ = 'blocks'

    def __init__(self, blocks):
        self.blocks = blocks

    def __eq__(self, other):
        return self.height() == other.height()

    def __lt__(self, other):
        return self.height() < other.height()

    def height(self):
        return sum(self.blocks)




def solve(h1, h2, h3):
    stack1 = Stack(h1)
    stack2 = Stack(h2)
    stack3 = Stack(h3)

    while True:
        if stack1 == stack2 == stack3:
            print(stack1.height())
            break
        highest_stack = max(stack1, stack2, stack3)
        highest_stack.blocks.pop()

solve(h1, h2, h3)
