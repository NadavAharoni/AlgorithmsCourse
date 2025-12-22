def is_max_heap(arr, key=lambda x: x):
    """
    Check if the array is a valid max heap.
    Goes from the end backwards checking each parent with its children.
    """
    # Start from the last parent node and check backwards
    for i in range(len(arr) // 2 - 1, -1, -1):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        
        # Check left child
        if left_index < len(arr) and key(arr[i]) < key(arr[left_index]):
            return False
        
        # Check right child
        if right_index < len(arr) and key(arr[i]) < key(arr[right_index]):
            return False
    
    return True
