def insertion_sort(array):
    # array[0] is already "sorted" so we start with array[1]
    next_item_index=1
    while next_item_index < len(array):
        item_to_insert = array[next_item_index]
        i = next_item_index-1
        while i >= 0 and array[i] > item_to_insert:
            array[i+1] = array[i]
            i -= 1
        # assign to array[i+1] because we decrement i
        # inside the loop
        array[i+1] = item_to_insert
        next_item_index += 1


def read_from_file(array):
    f = open("data.txt","r")

    for line in f:
        num_str = line.strip()
        array.append(int(num_str))

numbers = [999,300,200,500,800,400,900,100,700]
# numbers = []
# read_from_file(numbers)
# insertion_sort(numbers)
insertion_sort(numbers)
print(F"sorted:{numbers}")

