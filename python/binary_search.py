def binary_search(arr, key):
    l = len(arr)

    start = 0
    end = l

    while end > start:
        mid = (start + end)//2
        print(F"start={start}, end={end}, mid={mid}")
        if key == arr[mid][0]:
            return arr[mid]

        if key < arr[mid][0]:
            print(F"{key} is before {arr[mid][0]}")
            end = mid

        else:
            print(F"{key} is after {arr[mid][0]}")
            start = mid + 1

    return None


a = [ ("Aharon","Shmot"), ("Avraham","Bereshit"), ("Jacob","Bereshit"), ("Moshe","Shmot") ]
name = "Avraham"

t = binary_search(a, name)
if not t:
    print(F"{name} not found")
else:
    print(F"{t[0]} appears in Sefer {t[1]}")

