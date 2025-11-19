import random_tuples

def insertion_sort(array, key = lambda x: x):
    # array[0] is already "sorted" so we start with array[1]
    next_item_index=1
    while next_item_index < len(array):
        item_to_insert = array[next_item_index]
        i = next_item_index-1
        while i >= 0 and key(array[i]) > key(item_to_insert):
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


a = random_tuples.create_random_tuples(6, 3, [str, str, int])
t0 = a[0]
t1 = (t0[0],"wwwww", 134)
a.append(t1)
for t in a:
    print(t)

key=lambda x: x[2] % 100

insertion_sort(a)
print(F"sorted:")
for t in a:
    print(t)

