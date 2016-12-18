#!/bin/python

# Test-case:
h1 = [3, 1, 1, 1, 1]
h2 = [3, 1, 2]
h3 = [5, 1, 1, 1]


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
    max(common_heights)
except ValueError:
    print(0)
