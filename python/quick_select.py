import random
from partition import partition_hoare, partition_lomuto


# finds the kth value using Hoare partition semantics
def kth_hoare(arr, l, r, k):
    if k < 1 or k > r - l + 1:
        raise ValueError("k is out of bounds")
    
    if l == r:
        return arr[l]
    
    index = partition_hoare(arr, l, r)

    # For Hoare: left partition is l..index (inclusive)
    count_left = index - l + 1

    if count_left == k:
        return max(arr[l:index+1])
    if k <= count_left:
        return kth_hoare(arr, l, index, k)
    return kth_hoare(arr, index + 1, r, k - count_left)


# finds the kth value using Lomuto partition semantics
def kth_lomuto(arr, l, r, k):
    if k < 1 or k > r - l + 1:
        raise ValueError("k is out of bounds")
    
    if l == r:
        return arr[l]
    
    index = partition_lomuto(arr, l, r)

    # For Lomuto: arr[index] is at its final position
    pos = index - l + 1
    if pos == k:
        return arr[index]
    if k < pos:
        return kth_lomuto(arr, l, index - 1, k)
    return kth_lomuto(arr, index + 1, r, k - pos)


def main():
    numbers = list(range(1, 11))
    print(f"original numbers: {numbers}")
    random.shuffle(numbers)
    print(f"shuffled numbers: {numbers}")
    k = 7

    # test Hoare-based quickselect (works with Hoare partition semantics)
    nums_hoare = numbers.copy()
    p1 = kth_hoare(nums_hoare, 0, len(nums_hoare) - 1, k)
    print(f"\nkth_hoare -> the {k}th number is {p1}")
    print(f"array after kth_hoare: {nums_hoare}")

    # test Lomuto-based quickselect (pivot placed at final position)
    nums_lomuto = numbers.copy()
    p2 = kth_lomuto(nums_lomuto, 0, len(nums_lomuto) - 1, k)
    print(f"\nkth_lomuto -> the {k}th number is {p2}")
    print(f"array after kth_lomuto: {nums_lomuto}")


if __name__ == "__main__":
    main()
