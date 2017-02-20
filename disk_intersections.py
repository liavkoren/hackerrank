"""
https://codility.com/programmers/lessons/6-sorting/number_of_disc_intersections/
"""


class Interval(object):
    def __init__(self, center, radius):
        self.left = center - radius
        self.right = center + radius

    def __repr__(self):
        return u'<Interval: [{self.left}, {self.right}]>'.format(self=self)

    def __equal__(self, other):
        return self.left == other.left and self.right == other.right

    def __lte__(self, other):
        return self.right <= other.left

    def __lt__(self, other):
        return self.right < other.left

    def __gte__(self, other):
        return self.left >= other.right

    def __gt__(self, other):
        return self.left > other.right

    def __ne__(self, other):
        return not self == other

    def overlaps(self, other):
        return not self.disjoint(other)

    def disjoint(self, other):
        return other.left > self.right or other.right < self.left

intervals = [Interval(center, radius) for center, radius in enumerate([1, 5, 2, 1, 4, 0, ])]
sort_left = sorted(intervals, key=lambda interval: interval.left)

'''
frozenset({Interval: [2, 4], Interval: [-4, 6]}),
frozenset({Interval: [0, 4], Interval: [0, 8]}),
frozenset({Interval: [-4, 6], Interval: [0, 4]}),
frozenset({Interval: [-4, 6], Interval: [5, 5]}),
frozenset({Interval: [-1, 1], Interval: [0, 4]}),
frozenset({Interval: [-4, 6], Interval: [0, 8]}),
frozenset({Interval: [2, 4], Interval: [0, 4]}),
frozenset({Interval: [-1, 1], Interval: [0, 8]}),
frozenset({Interval: [-4, 6], Interval: [-1, 1]}),
frozenset({Interval: [2, 4], Interval: [0, 8]}),
frozenset({Interval: [5, 5], Interval: [0, 8]})
'''
