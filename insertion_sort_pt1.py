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


def insertionSort(ar):
    if len(ar) <= 1:
        return ar

    insert = ar[-1]
    compare = ar[-2]
    index = len(ar) - 2
    while compare > insert:
        ar[index+1] = compare
        if index > 0:
            index -= 1
            compare = ar[index]
            print ' '.join(str(num) for num in ar)
        else:
            print ' '.join(str(num) for num in ar)
            ar[0] = insert
            print ' '.join(str(num) for num in ar)
            return
    ar[index+1] = insert
    print ' '.join(str(num) for num in ar)


