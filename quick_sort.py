def partition(array: list, first: int, last: int):
    print(F"partition: array: {array}")
    print(F"partition: first={first}, last={last}")
    pivot = array[first]
    i = first
    j = last
    while True:
        while array[i] < pivot:
            i+=1
        while array[j] > pivot:
            j-=1
        print(F"i={i}, j={j}")
        if j>i:
            # swap
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
            print(F"after swap: {array}")
        else:
            return j

def median(array: list, first: int, last: int):
    middle = int(len(array) / 2)
    print(F"median: middle={middle}")
    while True:
        last_less = partition(array, first, last)
        print(F"median: last_less={last_less}")
        if last_less == middle:
            return array[last_less]
    
        if last_less < middle:
            first = last_less+1
        else:
            last = last_less

        

def main():
    numbers = [500,999,300,200,800,400,900,100,700]
    j = median(numbers, 0, len(numbers)-1)

    print(numbers, j)

main()

