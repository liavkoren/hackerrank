"""
https://www.hackerrank.com/challenges/luck-balance


[(6, 3), (5, 1), (2, 1), (1, 1), (8, 1), (10, 0), (5, 0),]
"""
import fileinput


def data_stream():
    for line in fileinput.input():
        line = line.strip().split(' ')
        yield map(int, line)


def process(data):
    contests, important_count = next(data)
    score = 0
    important_contests = []
    for contest in data:
        value, is_important = contest
        if is_important == 1:
            important_contests.append(value)
        else:
            score += value
    important_contests.sort(reverse=True)
    score += sum(important_contests[0:important_count])
    score -= sum(important_contests[important_count:])
    print score

stream = data_stream()
process(stream)
