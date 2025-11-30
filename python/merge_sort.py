import random

def merge_sort(array, depth=0):
    if len(array) <= 1:
        return

    mid = int(len(array)/2)
    # sort each half, then merge
    array_a = array[:mid] # creates a copy
    array_b = array[mid:] # creates a copy

    if depth == 0:
        # print the sub arrays for learning purposes
        print(F"array_a={array_a}")
        print(F"array_b={array_b}")
        print()

    merge_sort(array_a, depth+1)
    merge_sort(array_b, depth+1)

    if depth == 0:
        # print the sub arrays for learning purposes
        print(F"array_a={array_a}")
        print(F"array_b={array_b}")
        print()

    merge(array_a, array_b, array)

def merge(array_a, array_b, array_dest):
    assert( len(array_dest) == len(array_a) + len(array_b) )
    i = j = k = 0
    while k < len(array_dest):
        if i >= len(array_a):
            array_dest[k] = array_b[j]
            j += 1
        elif j >= len(array_b):
            array_dest[k] = array_a[i]
            i += 1
        else:
            if array_a[i] <= array_b[j]:
                array_dest[k] = array_a[i]
                i += 1
            else:
                array_dest[k] = array_b[j]
                j += 1
        k += 1

# previous version of merge using list.pop
# which is less efficient
def merge_pop(array_a, array_b, array_dest):
    assert( len(array_dest) == len(array_a) + len(array_b) )
    # assume array_a and array_b
    for i in range(0,len(array_dest)):
        if len(array_b)==0:
            array_dest[i] = array_a.pop(0)
        elif len(array_a)==0:
            array_dest[i] = array_b.pop(0)
        else: # both arrays must have a non-zero length
            if array_a[0] <= array_b[0]:
                array_dest[i] = array_a.pop(0)
            else:
                array_dest[i] = array_b.pop(0)




# main
numbers = list(range(1,12))
random.shuffle(numbers)
print(F"numbers before sort:{numbers}")

merge_sort(numbers)
print(F"sorted:{numbers}")