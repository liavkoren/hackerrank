#!/bin/python
'''
https://www.hackerrank.com/challenges/equal-stacks
Implementation inspired by uplinksandy9 & sushant001 comments.

'''

n1, n2, n3 = input().strip().split(' ')
h1 = list(reversed([int(h1_temp) for h1_temp in input().strip().split(' ')]))
h2 = list(reversed([int(h2_temp) for h2_temp in input().strip().split(' ')]))
h3 = list(reversed([int(h3_temp) for h3_temp in input().strip().split(' ')]))


def sum_list(numbers):
    out = []
    for index, number in enumerate(numbers):
        if index == 0:
            out.append(number)
        else:
            out.append(numbers[index] + out[index-1])
    return out

stack_heights1 = set(sum_list(h1))
stack_heights2 = set(sum_list(h2))
stack_heights3 = set(sum_list(h3))

common_heights = stack_heights1.intersection(stack_heights2).intersection(stack_heights3)
try:
    print(max(common_heights))
except ValueError:
    print(0)
