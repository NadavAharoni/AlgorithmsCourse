def merge_sort(array):
    if len(array) <= 1:
        return
    mid = int(len(array)/2)
    # sort each half, then merge
    array_a = array[:mid] # creates a copy
    array_b = array[mid:] # creates a copy

    # print the sub arrays for learning purposes
    print(F"array_a={array_a}")
    print(F"array_b={array_b}")
    print()

    merge_sort(array_a)
    merge_sort(array_b)

    merge(array_a, array_b, array)

def merge(array_a, array_b, array_dest):
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
numbers = [999,300,200,500,800,400,900,100,700]
# numbers = []
# read_from_file(numbers)
# insertion_sort(numbers)
merge_sort(numbers)
print(F"sorted:{numbers}")