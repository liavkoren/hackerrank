'''
https://www.hackerrank.com/challenges/sparse-arrays
4
aba
baba
aba
xzxb
3
aba
xzxb
ab

'''
import fileinput


def data_stream():
    for line in fileinput.input():
        line = line.strip()
        try:
            yield int(line)
        except ValueError:
            yield line


def process():
    stream = data_stream()
    input_lines = next(stream)
    input_lines = [next(stream) for _ in range(input_lines)]
    data = {}
    for line in input_lines:
        data[line] = data.get(line, 0) + 1
    next(stream)
    for query in stream:
        print(data.get(query, 0))

process()
