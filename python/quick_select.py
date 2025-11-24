import random
from partition import partition

# finds the kth value 
def kth(arr, l, r, k):
    print(f"=====\nin kth: l={l}, r={r}, k={k}, a={arr}")
    if k < 1 or k > r - l + 1:
        raise ValueError("k is out of bounds")

    index = partition(arr, l, r)
    print(f"a={arr}, index={index}")

    # if position is same as k
    if index - l == k - 1:
        return arr[index]

    # If position is more, recur left 
    if index - l > k - 1:
        return kth(arr, l, index - 1, k)

    # Else recur right 
    return kth(arr, index + 1, r, k - (index - l + 1))

def main():
    numbers = list(range(1,11))
    print(f"numbers: {numbers}")
    random.shuffle(numbers)
    print(f"shuffled numbers: {numbers}")
    p = kth(numbers,0,len(numbers)-1,7)
    print(p)
    print(f"numbers: {numbers}")

if __name__ == "__main__":
    main()
