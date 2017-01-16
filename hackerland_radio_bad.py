'''
https://www.hackerrank.com/challenges/hackerland-radio-transmitters

tests:
8 2
1 2 6 8 10 12 15 20

1 1:
1

- sort the town map.
- calculate the coverage of a station: coverage = 2 * range + 1

the first transmitter must be placed <= coverage + 1 units from the first house
we can then move coverage + 1 units forward, and place the next transmitter.
The next transmitter must be placed in the same way at the first house beyond
the coverage of the previous transmitter

Algorithm:
current transmitter count = 0
current zone covered by transmitters = first house
for each house in the town:
    if the next house - the coverage zone > the transmitter range, then the
    transmitter count is incremented, and the coverage zone is next house + range










           |              |        |                       |        |
  .  o  .  o  o  o  o  .  o  .  o  o  o  o  .  .  .  o  .  o  o  .  o
 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23


2, 4 --> 4
4, 6 --> 9
7, 9
9, 12 --> 12
12, 14
14, 18
18, 20 --> 20
20, 23 --> 23

transmitter range = k
transmiiter count = 0

first = the first house that is uncovered
next = the next house

is-uncovered-houses():
    # the last house is not yet in range of a transmitter
    if not self.transmitter:
        return True
    return self.transmitters[-1] + self.range < self.houses[-1]

while is-uncovered-houses():
    find the next transmitter site(first, next, transmitter-range):
        if the next house is further away than the transmitter range:
            return
        if the next house == the transmitter site:
            # we've reached the end of the houses
            return
        else:
            while the next-next house is <= (trans-range + first) away AND next is not at the end of the town:
                next = the next-next
            first = next  # first is now on the transmitter site
            next = next next  # next is now the house after the transmitter
            return

    add a transmitter
    if the next house == the transmitter site:
        # we've reached the end of the houses
        print(len(self.transmitters))
        return

    find the next uncovered house():
        if the next house is further away than the (first + transmitter range):
            first = next
            next = next next
            return
        else:
            while next-next <= transmitter-range + first:
                next = next-next
            first = next-next # first is now on the first uncovered house
            next = next next next  # next = self.advance_next().advance_next()
            return

    @property
    def next()
        return self.houses[self._next_pointer]

    @property
    def first():
        return self.houses[self._first_pointer]

    advance_next():
        if self._next_pointer <= len(houses):
            self._next_pointer += 1
        return self

    advance_first():
        if self._first_pointer <= len(houses):
            self._first_pointer += 1
        return self

    add_transmitter(location):
        append the location to the transmitter list














site = stack(house)
next_stack = stack(houses[1:])
transmitters = []

coverage_edge = last transmitter + transmitter range

while next:
    while




























'''






















class Solver(object):
    def __init__(self, transmitter_range, houses):
        self.site_pointer = 0
        self.next_pointer = 1 if len(houses) > 0 else 0
        self.transmitter_range = transmitter_range
        self.transmitters = []
        self.houses = sorted(houses)

    def solve(self):
        while self.has_uncovered_houses():
            self.find_next_site()
            self.add_transmitter()
            if self.next_pointer == self.site_pointer:
                print(len(self.transmiiters))
                return
            self.find_next_uncovered_house()

    def has_uncovered_houses(self):
        if not self.transmitters:
            return True
        return self.transmitters[-1] + self.transmitter_range < self.houses[-1]

    @property
    def site(self):
        return self.houses[self.site_pointer]

    @property
    def next(self):
        return self.houses[self.next_pointer]

    def advance_site(self):
        if self.site_pointer < len(self.houses):
            self.site_pointer += 1
        return self

    def advance_next(self):
        while self.next_pointer <= len(self.houses) - 1:
            self.next_pointer += 1
        return self

    def peek_next_next(self):
        if self._next_pointer + 2 < len()
        return self.houses[self.next_pointer + 2]

    def add_transmitter(self):
        self.transmitters.append(self.site)

    def find_next_site(self):
        if self.next > self.site + self.transmitter_range:
            # the next house is further away than the transmitter range, so we
            # need to put a transmitter here.
            return
        if self.next == self.site:
            # we've reached the end of town.
            return

        while self.next_pointer <= len(self.houses) - 1 and self.peek_next_next() <= (self.site + self.transmitter_range):
            self.advance_next()
            self.site_pointer = self.next_pointer
            self.adventure()

    def find_next_uncovered_house(self):
        if self.next > self.site + self.transmitter_range:
            self.site_pointer = self.next_pointer
            self.advance_next()
            return

        while self.next_pointer <= len(self.houses) - 1 and self.peek_next_next() <= (self.site + self.transmitter_range):
            self.advance_next()
        self.advance_next()
        self.site_pointer = self.next_pointer
        self.advance_next()


# import pdb; pdb.set_trace()
solver = Solver(2, [1, 3, 5])
solver.solve()






































