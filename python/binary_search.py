class Avot:
    def __init__(self, name, sefer) -> None:
        self.name = name
        self.sefer = sefer

    def __str__(self) -> str:
        return F"name:{self.name}, sefer:{self.sefer}"


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

avot_list = []
avot_list.append( Avot("Avraham","Bereshit"))
avot_list.append( Avot("Jacob","Bereshit"))
avot_list.append( Avot("Moshe","Shmot"))
avot_list.append( Avot("Aharon","Shmot"))

for a in avot_list:
    print(a)
print("--------------")
avot_sorted = sorted(avot_list, key = lambda a: a.name)

for a in avot_sorted:
    print(a)

exit()

a = [ ("Aharon","Shmot"), ("Avraham","Bereshit"), ("Jacob","Bereshit"), ("Moshe","Shmot") ]
name = "Avraham"

t = binary_search(a, name)
if not t:
    print(F"{name} not found")
else:
    print(F"{t[0]} appears in Sefer {t[1]}")

