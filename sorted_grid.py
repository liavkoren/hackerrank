#!/usr/bin/python

import fileinput


def data_stream():
    for line in fileinput.input():
        line = line.strip()
        yield line


def sortedGrid(grid):
    n = len(grid[0])
    for column in range(n):
        for row in range(n-1):
            if grid[row][column] > grid[row + 1][column]:
                return False

    return True


def process(data):
    test_cases = int(next(data))

    for _ in range(test_cases):
        size = int(next(data))
        grid = []
        while size:
            size -= 1
            row = next(data)
            line = list(row)
            line.sort()
            grid.append(line)

        is_sorted = sortedGrid(grid)
        if is_sorted:
            print 'YES'
        else:
            print 'NO'

stream = data_stream()
process(stream)
