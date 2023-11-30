def merge_sort(array):
    if len(array) <= 1:
        return
    mid = int(len(array)/2)
    # sort each half, then merge
    array_a = array[:mid]
    merge_sort(array_a)
    array_b = array[mid:]
    merge_sort(array_b)
    print(F"array_a={array_a}")
    print(F"array_b={array_b}")
    # merge
    for i in range(0,len(array)):
        if len(array_b)==0:
            array[i] = array_a.pop(0)
        elif len(array_a)==0:
            array[i] = array_b.pop(0)
        else: # both arrays must have a non-zero length
            if array_a[0] <= array_b[0]:
                array[i] = array_a.pop(0)
            else:
                array[i] = array_b.pop(0)


def insertion_sort(array):
    # array[0] is already "sorted" so we start with array[1]
    next_item_index=1
    while next_item_index < len(array):
        item_to_insert = array[next_item_index]
        i = next_item_index-1
        while i >= 0 and array[i] > item_to_insert:
            array[i+1] = array[i]
            i -= 1
        # assign to array[i+1] because we must increment i
        # inside the loop
        array[i+1] = item_to_insert
        next_item_index += 1


def read_from_file(array):
    f = open("data.txt","r")

    for line in f:
        # the following line assignes into a tuple
        num_str = line.strip()
        array.append(int(num_str))

numbers = [999,300,200,500,800,400,900,100,700]
# numbers = []
# read_from_file(numbers)
# insertion_sort(numbers)
merge_sort(numbers)
print(F"sorted:{numbers}")