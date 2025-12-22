import random

def is_max_heap(arr, i=0, key=lambda x: x):
    """
    Check if the array is a valid max heap starting from index i.
    Verifies that each node from i onwards is not greater than its parent.
    """
    for idx in range(i + 1, len(arr)):
        parent_index = (idx - 1) // 2
        if parent_index >= i and key(arr[idx]) > key(arr[parent_index]):
            return False
    
    return True


def max_heapify(arr, i, heap_size, key=lambda x: x):
    """
    Move element at index i down to maintain max heap property.
    Assumes left and right subtrees are already max heaps.
    """
    largest = i
    left_index = 2 * i + 1
    right_index = 2 * i + 2
    
    # Find the largest among node, left child, and right child
    if left_index < heap_size and key(arr[left_index]) > key(arr[largest]):
        largest = left_index
    
    if right_index < heap_size and key(arr[right_index]) > key(arr[largest]):
        largest = right_index
    
    # If largest is not the current node, swap and heapify down
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest, heap_size, key)


def max_heapify_iterative(arr, i, heap_size, key=lambda x: x):
    """
    Iterative version of max_heapify: restores max-heap property by
    moving the element at index `i` down the heap using a loop.

    Parameters:
    - arr: list to operate on
    - i: index of the node to heapify down
    - heap_size: number of elements in the heap (elements at indices >= heap_size
      are considered sorted / outside the heap)
    - key: optional key function for comparison
    """
    current = i
    while True:
        largest = current
        left_index = 2 * current + 1
        right_index = 2 * current + 2

        if left_index < heap_size and key(arr[left_index]) > key(arr[largest]):
            largest = left_index

        if right_index < heap_size and key(arr[right_index]) > key(arr[largest]):
            largest = right_index

        if largest == current:
            break

        arr[current], arr[largest] = arr[largest], arr[current]
        current = largest


def build_max_heap(arr, key=lambda x: x):
    """
    Build a max heap from an unordered array.
    Calls max_heapify on all non-leaf nodes in reverse order.
    """
    heap_size = len(arr)
    # Start from the last parent node and work backwards
    for i in range(heap_size // 2 - 1, -1, -1):
        max_heapify(arr, i, heap_size, key)


def heap_sort(arr, key=lambda x: x):
    """
    In-place heap sort (ascending) using max-heap.

    Steps:
    1. Build a max heap using `build_max_heap`.
    2. Repeatedly swap the max element (index 0) with the last element
       of the heap and reduce heap size by one, then `max_heapify` the root.

    Supports an optional `key` function for custom comparisons.
    """
    n = len(arr)
    if n <= 1:
        return

    build_max_heap(arr, key=key)

    # Extract elements from heap one by one
    for end in range(n - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        # Heap size is now `end`; restore heap property at root
        max_heapify(arr, 0, end, key)


def main():
    numbers = list(range(1, 11))
    random.shuffle(numbers)
    print(f"original shuffled numbers: {numbers}")
    
    # Test is_max_heap
    print(f"\nis_max_heap before building: {is_max_heap(numbers)}")
    
    # Test build_max_heap
    build_max_heap(numbers)
    print(f"after building max heap: {numbers}")
    print(f"is_max_heap after building: {is_max_heap(numbers)}")
    
    # Test with custom key function
    words = ["apple", "banana", "cherry", "date", "fig"]
    random.shuffle(words)
    print(f"\noriginal shuffled words: {words}")
    build_max_heap(words, key=len)
    print(f"after building max heap (by length): {words}")
    print(f"is_max_heap after building: {is_max_heap(words, key=len)}")

    # Test heap_sort on numbers
    numbers2 = list(range(1, 11))
    random.shuffle(numbers2)
    print(f"\noriginal shuffled numbers for heap_sort: {numbers2}")
    heap_sort(numbers2)
    print(f"after heap_sort: {numbers2}")
    print(f"is sorted ascending: {numbers2 == sorted(numbers2)}")

    # Test heap_sort with custom key (sort strings by length ascending)
    words2 = ["apple", "banana", "cherry", "date", "fig"]
    random.shuffle(words2)
    print(f"\noriginal shuffled words for heap_sort: {words2}")
    heap_sort(words2, key=len)
    print(f"after heap_sort (by length): {words2}")
    is_sorted_by_len = all(len(words2[i]) <= len(words2[i+1]) for i in range(len(words2)-1))
    print(f"is sorted by length ascending: {is_sorted_by_len}")


if __name__ == "__main__":
    main()
