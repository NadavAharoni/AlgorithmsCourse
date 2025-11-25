import random
from partition import partition_hoare, partition_lomuto


def quickSort_hoare(arr, low, high):
    if low < high:
        # pi is the partition return index (Hoare partition)
        pi = partition_hoare(arr, low, high)

        # For Hoare partition, recurse on [low..pi] and [pi+1..high]
        quickSort_hoare(arr, low, pi)
        quickSort_hoare(arr, pi + 1, high)


def quickSort_lomuto(arr, low, high):
    if low < high:
        # pi is the partition return index (Lomuto partition)
        # Lomuto places the pivot at its final sorted position
        pi = partition_lomuto(arr, low, high)

        # Recurse on [low..pi-1] and [pi+1..high]
        quickSort_lomuto(arr, low, pi - 1)
        quickSort_lomuto(arr, pi + 1, high)

def main():
    numbers = list(range(1, 11))
    random.shuffle(numbers)
    print(f"original shuffled numbers: {numbers}")

    # Test Hoare-based quicksort
    nums_hoare = numbers.copy()
    print(f"\nnumbers before quickSort_hoare: {nums_hoare}")
    quickSort_hoare(nums_hoare, 0, len(nums_hoare) - 1)
    print(f"numbers after quickSort_hoare: {nums_hoare}")

    # Test Lomuto-based quicksort
    nums_lomuto = numbers.copy()
    print(f"\nnumbers before quickSort_lomuto: {nums_lomuto}")
    quickSort_lomuto(nums_lomuto, 0, len(nums_lomuto) - 1)
    print(f"numbers after quickSort_lomuto: {nums_lomuto}")

if __name__ == "__main__":
    main()

