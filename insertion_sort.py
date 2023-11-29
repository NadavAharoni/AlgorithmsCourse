def merge_sort(array):
    if len(array) <= 1:
        return
    mid = int(len(array/1))
    # sort each half, then merge ..

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

numbers = [300,200,500,100,400]
# numbers = []
# read_from_file(numbers)
insertion_sort(numbers)
print(numbers)