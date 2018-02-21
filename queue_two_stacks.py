"""
https://www.hackerrank.com/challenges/queue-using-two-stacks

In this challenge, you must first implement a queue using two stacks. Then process queries, where each query is one of the following types:

    1 x: Enqueuee element into the end of the queue.
    2: Dequeue the element at the front of the queue.
    3: Print the element at the front of the queue.

Sample input:
10
1 42
2
1 14
3
1 28
3
1 60
1 78
2
2

Sample output:
14
14
"""
import fileinput


def data_stream():
    for line in fileinput.input():
        line = line.strip().split(' ')
        yield map(int, line)


class Queue(object):
    def __init__(self):
        self.newest_on_top = []
        self.oldest_on_top = []

    def shift_stacks(self):
        self.oldest_on_top = list(reversed(self.newest_on_top))
        self.newest_on_top = []

    def enqueue(self, number):
        self.newest_on_top.append(number)

    def dequeue(self):
        if not self.oldest_on_top:
            self.shift_stacks()
        return self.oldest_on_top.pop()

    def peak(self):
        if not self.oldest_on_top:
            self.shift_stacks()
        print(self.oldest_on_top[-1])


def process():
    queue = Queue()
    stream = data_stream()
    next(stream)
    for query in stream:
        if query[0] == 1:
            queue.enqueue(query[1])
        elif query[0] == 2:
            queue.dequeue()
        elif query[0] == 3:
            queue.peak()
        else:
            raise Exception()

process()


# Tests
q = Queue()
q.enqueue(1)
print('expect 1')
q.peak()
q.enqueue(2)
q.enqueue(3)
print('expect 1')
q.peak()
assert q.dequeue() == 1
assert q.dequeue() == 2
q.enqueue(10)
print('expect 3')
q.peak()
assert q.dequeue() == 3
assert q.dequeue() == 10
