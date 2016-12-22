'''
Poison plants
https://www.hackerrank.com/challenges/poisonous-plants

Input
6 5 8 4 7 10 9
Initially all plants are alive:

Plants = {(6,1), (5,2), (8,3), (4,4), (7,5), (10,6), (9,7)}

Plants[k] = (i,j) => jth plant has pesticide amount = i.
After the 1st day, 4 plants remain as plants 3, 5, and 6 die:

Plants = {(6,1), (5,2), (4,4), (9,7)}
After the 2nd day, 3 plants survive as plant 7 dies:

Plants = {(6,1), (5,2), (4,4)}
After the 3rd day, 3 plants survive and no more plants die.

Plants = {(6,1), (5,2), (4,4)}
After the 2nd day the plants stop dying.

---
6 5 8 4 7 10 9
'''


import fileinput


def process(data):
    ceil = data[0]
    floor = data[0]
    death_count = 0
    global_death_count = 0

    for index, number in enumerate(data[1:]):
        if number > floor:
            is_start_of_interval = death_count == 0
            if is_start_of_interval:
                death_count = 1

            if number > ceil:
                ceil = number
            else:
                death_count += 1
            global_death_count = max(global_death_count, death_count)
            print ('index: %s, death-count: %s' % (index + 1, global_death_count) )
        else:
            floor = number
            ceil = number
            death_count = 0
    return global_death_count


'''
4 7 10 9

'''

def data_stream():
    for line in fileinput.input():
        line = line.strip().split(' ')
        yield map(int, line)


assert process([6, 5, 8, 4, 7, 10, 9]) == 2
assert process([4, 10, 9, 8, 7, 6, 5]) == 6
assert process([4, 3, 2, 1, 10, 9, 8, 7, 6, 5]) == 6
assert process([4, 3, 2, 1, 10, 11, 15, 17, 9, 8, 7, 6, 5]) == 6
assert process([5, 4, 3, 2, 1]) == 0
assert process([1, 2, 3, 4, 5]) == 1

process([3, 7, 1, 2, 4, 8, 2, 7, 10])
