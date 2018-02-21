# Python implementation of https://ideone.com/Fml7Sm, to
# https://www.hackerrank.com/challenges/swap-nodes-algo/forum


MAXN = 1024
left = [0] * (MAXN + 1)
right = [0] * (MAXN + 1)
depth = [0] * (MAXN + 1)


def calc_depth(cur_node_index, cur_depth):
    depth[cur_node_index] = cur_depth
    if left[cur_node_index] > 0:
        calc_depth(left[cur_node_index], cur_depth + 1)
    if right[cur_node_index] > 0:
        calc_depth(right[cur_node_index], cur_depth + 1)


def in_order(tree_index):
    output = []

    def inner(index):
        if left[index] > 0:
            inner(left[index])
        output.append(index)
        if right[index] > 0:
            inner(right[index])
    inner(tree_index)
    print ' '.join(str(num) for num in output)


def clean_tuple(string_pair):
    return tuple([int(num) for num in string_pair.strip().split(' ')])


def main(data):
    data.seek(0)
    numb = int(data.readline().strip())
    for index in range(1, numb+1):
        pair = data.readline()
        left_val, right_val = clean_tuple(pair)
        left[index] = left_val
        right[index] = right_val

    calc_depth(1, 1)
    t = int(data.readline().strip())
    while t:
        t -= 1
        k = int(data.readline().strip())
        for index in range(1, numb+1):
            if depth[index] % k == 0:
                left[index], right[index] = right[index], left[index]
        in_order(1)


def get_data():
    base_dir = '/Users/liavkoren/dev/hackerrank/swap-nodes/{}'.format
    data_file = open(base_dir('input02.txt'), 'r')
    return data_file


