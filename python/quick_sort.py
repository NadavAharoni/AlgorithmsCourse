import random
from partition import partition

def quickSort(arr, low, high):
    if low < high:
        # pi is the partition return index (Hoare partition)
        pi = partition(arr, low, high)

        # For Hoare partition, recurse on [low..pi] and [pi+1..high]
        quickSort(arr, low, pi)
        quickSort(arr, pi + 1, high)

def main():
    numbers = list(range(10))
    random.shuffle(numbers)
    print(F"numbers before quicksort={numbers}")
    quickSort(numbers,0,len(numbers)-1)
    print(F"numbers={numbers}")

if __name__ == "__main__":
    main()

