def left(i):
    return (i + 1) * 2 - 1

def right(i):
    return (i + 1) * 2

def parent(i):
    if i <= 0:
        return None
    return (i - 1) // 2

def is_max_heap(arr, i=0, key=lambda x: x):
    n = len(arr)
    for j in range(i, n):
        l = left(j)
        r = right(j)
        if l < n and key(arr[j]) < key(arr[l]):
            return False
        if r < n and key(arr[j]) < key(arr[r]):
            return False
    return True

if __name__ == "__main__":
    print("Testing index helpers (0-based):")
    for i in range(8):
        print(f"i={i:2}  left={left(i):2}  right={right(i):2}  parent={parent(i)}")

    # Explicit numeric tests for left/right (0-based)
    assert left(0) == 1
    assert right(0) == 2
    assert left(1) == 3
    assert right(1) == 4
    assert left(2) == 5
    assert right(2) == 6
    assert left(3) == 7
    assert right(3) == 8
    assert left(4) == 9
    assert right(4) == 10
    assert left(5) == 11
    assert right(5) == 12
    assert left(6) == 13
    assert right(6) == 14

    assert parent(0) is None
    assert parent(1) == 0
    assert parent(2) == 0
    assert parent(3) == 1
    assert parent(4) == 1
    assert parent(5) == 2
    assert parent(6) == 2

    heap = [100, 50, 90, 20, 10, 40, 60]
    not_heap = [10, 50, 90, 20, 100]
    print("\nis_max_heap on `heap` (expected True):", is_max_heap(heap))
    print("is_max_heap on `not_heap` (expected False):", is_max_heap(not_heap))

