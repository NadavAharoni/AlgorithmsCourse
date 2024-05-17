def partition(array: list, first: int, last: int) -> int:
    print(F"partition: array: {array}")
    print(F"partition: first={first}, last={last}")
    pivot = array[first]
    print(F"pivot={pivot}")
    i = first
    j = last
    while True:
        while array[i] < pivot:
            i+=1
        while array[j] > pivot:
            j-=1
        print(F"loops ended with: i={i}, j={j}")
        if j>i:
            # swap
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
            print(F"after swap: {array}")
            assert(array[i] <= pivot)
            assert(array[j] >= pivot)
            i+=1
            j-=1
        else:
            return j

def median(array: list, first: int, last: int):
    middle = int(len(array) / 2)
    print(F"median: middle={middle}")
    while True:
        last_less = partition(array, first, last)
        print(F"median: last_less={last_less}")
        if last_less == middle:
            return last_less
    
        if last_less < middle:
            first = last_less+1
        else:
            last = last_less


def main():
    # numbers = [500,999,300,200,800,500,500,500,400,900,100,700,500,300]
    # numbers = [200,300,400]
    numbers = [100,200,100,100,200,200,200,200,200,200,100]
    j = median(numbers, 0, len(numbers)-1)

    # j = partition(numbers, 0, len(numbers)-1)

    print(F"index={j} numbers[j]={numbers[j]}")
    print(numbers[0:j+1], numbers[j+1:])

main()

