import random

def partition_hoare(array: list, first: int, last: int) -> int:
    # Hoare partition scheme
    pivot = array[first]
    i = first - 1
    j = last + 1
    while True:
        i += 1
        while array[i] < pivot:
            i += 1
        j -= 1
        while array[j] > pivot:
            j -= 1
        if i >= j:
            return j
        array[i], array[j] = array[j], array[i]


def partition_lomuto(array: list, first: int, last: int) -> int:
    # Lomuto partition scheme (places pivot at its final position)
    pivot = array[last]
    i = first
    for j in range(first, last):
        if array[j] <= pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[i], array[last] = array[last], array[i]
    return i


def main():
    numbers = list(range(1, 11))
    print(f"original numbers: {numbers}")
    random.shuffle(numbers)
    print(f"shuffled numbers: {numbers}\n")

    # Test Hoare partition
    nums_hoare = numbers.copy()
    p_hoare = partition_hoare(nums_hoare, 0, len(nums_hoare) - 1)
    print(f"After partition_hoare:")
    print(f"  pivot location is {p_hoare}")
    print(f"  numbers: {nums_hoare}")

    # note: this is Hoare's partition scheme
    # therefore, numbers[p] is not necessarily the pivot value
    # p is the index where left partition ends
    # so the correct slicing is numbers[0:p+1] and numbers[p+1:]
    left_partition = nums_hoare[:p_hoare+1]
    right_partition = nums_hoare[p_hoare+1:]
    print(f"  left partition: {left_partition}, right partition: {right_partition}")
    print(f"  max of left partition: {max(left_partition)}, min of right partition: {min(right_partition)}")

    # Test Lomuto partition
    nums_lomuto = numbers.copy()
    p_lomuto = partition_lomuto(nums_lomuto, 0, len(nums_lomuto) - 1)
    print(f"\nAfter partition_lomuto:")
    print(f"  pivot location is {p_lomuto}")
    print(f"  pivot value is {nums_lomuto[p_lomuto]}")
    print(f"  numbers: {nums_lomuto}")

    # note: Lomuto places the pivot at its final sorted position
    # all elements before p_lomuto are <= pivot
    # all elements after p_lomuto are > pivot
    left_partition = nums_lomuto[:p_lomuto]
    pivot_value = nums_lomuto[p_lomuto]
    right_partition = nums_lomuto[p_lomuto+1:]
    print(f"  left partition: {left_partition}, pivot: {pivot_value}, right partition: {right_partition}")
    max_left = max(left_partition) if left_partition else 'N/A'
    min_right = min(right_partition) if right_partition else 'N/A'
    print(f"  max of left partition: {max_left}, pivot: {pivot_value}, min of right partition: {min_right}")

if __name__ == "__main__":
    main()
