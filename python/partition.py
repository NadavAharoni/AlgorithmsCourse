import random

def partition(array: list, first: int, last: int) -> int:
    # print(f"partition: array: {array}, first={first}, last={last}")
    # pivot = array[(first + last) // 2]
    pivot = array[first]
    # print(f"pivot={pivot}")
    i = first - 1
    j = last + 1
    while True:
        i += 1
        while array[i] < pivot:
            i += 1
        j -= 1
        while array[j] > pivot:
            j -= 1
        # print(f"loops ended with: i={i}, j={j}")
        if i >= j:
            return j
        # swap
        array[i], array[j] = array[j], array[i]
        # print(f"after swap: {array}")


def main():
    numbers = list(range(1,11))
    print(f"numbers: {numbers}")
    random.shuffle(numbers)
    print(f"shuffled numbers: {numbers}")
    p = partition(numbers,0,len(numbers)-1)
    print(p)
    print(f"numbers: {numbers}")

    # j = partition(numbers, 0, len(numbers)-1)
    # print(F"index={j} numbers[j]={numbers[j]}")
    # print(numbers[0:j+1], numbers[j+1:])

if __name__ == "__main__":
    main()
