'''
https://www.hackerrank.com/challenges/icecream-parlor

Given a target amount of money to spend, and an unsorted list of prices, find
the index of the two prices that sum to the target. Print the two indicies,
lowest then highest.

Note: this code may not handle the case where the price is the same for both
items correctly.
'''

from functools import total_ordering
import fileinput


@total_ordering
class Node(object):
    def __init__(self, index, value,):
        self.value = value
        self.index = index

    def __repr__(self):
        return 'Node(index=%s, value=%s)' % (self.index, self.value)

    def __lt__(self, other):
        try:
            return self.value < other.value
        except AttributeError:
            return self.value < other

    def __eq__(self, other):
        try:
            return self.value == other.value
        except AttributeError:
            return self.value == other


def binary_search(items, target):
    if not items:
        return

    middle_item_index = len(items)/2
    middle_item = items[middle_item_index]

    if middle_item < target:
        return binary_search(items[middle_item_index+1:], target)
    elif middle_item == target:
        return middle_item
    else:
        return binary_search(items[0:middle_item_index], target)


def process(items, budget):
    """ We are looking for two items that sum to our budget. """
    items.sort()
    for first_item in items:
        target_amount = budget - first_item.value
        second_item = binary_search(items, target_amount)
        if second_item:
            result = sorted([first_item.index + 1, second_item.index + 1])
            print '{0} {1}'.format(*result)
            return


def data_stream():
    for line in fileinput.input():
        line = line.strip().split(' ')
        yield map(int, line)

data_stream = data_stream()
number_of_trips = next(data_stream)[0]
for _ in range(number_of_trips):
    budget = next(data_stream)[0]
    _ = next(data_stream)  # number of ice-cream flavors
    items = next(data_stream)  # ice-cream prices
    items = [Node(index, value) for index, value in enumerate(items)]
    process(items, budget)
