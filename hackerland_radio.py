# https://www.hackerrank.com/challenges/hackerland-radio-transmitters
import fileinput
import sys

sys.setrecursionlimit(10000)


def solve(houses, transmitter_range):
    houses.sort(reverse=True)
    if len(houses) == 0:
        return 0

    if len(houses) == 1:
        return 1

    first_house = site = houses[-1]
    # Find the site for the transmitter
    try:
        while houses[-1] <= first_house + transmitter_range:
            site = houses.pop()
    except IndexError:
        # We've run out of houses
        return 1

    # move us to the first house outside the transmitter's range:
    try:
        while houses[-1] <= site + transmitter_range:
            houses.pop()
        else:
            # If there's no houses within range of the transmitter on the right,
            # we need to advance to the next house:
            if site == houses[-1]:
                houses.pop()
    except IndexError:
        # out of houses
        return 1

    return 1 + solve(houses, transmitter_range)


def data_stream():
    for line in fileinput.input():
        line = line.strip().split(' ')
        yield map(int, line)


stream = data_stream()
n, transmitter_range = next(stream)
houses = next(stream)
print(solve(houses, transmitter_range))

test1 = [7, 2, 4, 6, 5, 9, 12, 11]
assert solve(test1, 2) == 3

test2 = range(1, 6)
assert solve(test2, 2) == 1

test3 = range(1, 7)
assert solve(test3, 2) == 2
