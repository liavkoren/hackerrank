'''
https://www.hackerrank.com/challenges/insertionsort1

insertion_item = last item in the array
for index in remaining items, decrementing:
    the comparison item is the item at the index
    if the comparison item is > the insertion item:
        copy the comparison item over one,
    otherwise:
        write the value of the insertion item into that index location
    print the array

'''


def insertion_sorter(ar, start_at):
    """ Start_at: the zero-based index of the item to sort-left from. """

    insert = ar[start_at]
    compare = ar[start_at - 1]
    index = start_at - 1
    while compare > insert:
        ar[index+1] = compare
        if index > 0:
            index -= 1
            compare = ar[index]
        else:
            ar[0] = insert
            return ar
    ar[index+1] = insert
    return ar


def insertionSort(ar):
    if len(ar) <= 1:
        print_items(ar)
        return
    index = 1
    while index <= len(ar) - 1:
        ar = insertion_sorter(ar, index)
        print_items(ar)
        index += 1


def print_items(ar):
    print ' '.join(str(num) for num in ar)
