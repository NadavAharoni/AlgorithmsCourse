import sys
import csv

print(sys.argv)

if len(sys.argv) < 2:
    print("Error: missing argument")
    print(F"Usage: python {sys.argv[0]} filename")
    exit(-1)

filename = sys.argv[1]
# print(filename)
# street_name_frequency = {}
street_list = []
try:
    # csvfile = open(filename, 'r', encoding="windows-1255", newline='')
    with open(filename, 'r', encoding="windows-1255", newline='') as file:
        r = csv.DictReader(file)
        for street in r:
            street_list.append(street)
        
except FileNotFoundError:
    print(F"{filename} not found")

print( len(street_list) )
for s in street_list[0:4]:
    print(s["street_name"], s["city_name"], s["street_code"])

print("===========")

def get_street_name(d):
    return d["street_name"]

# def get_city_of_street(d):
#     return d["city_name"]

streets_sorted = sorted(street_list, key=get_street_name)
for s in streets_sorted[-4:-1]:
    print(s["street_name"], s["city_name"], s["street_code"])

print("===========")
streets_sorted_by_city = sorted(street_list, key=lambda d: (d["city_name"], d["street_name"]) )
for s in streets_sorted_by_city[20000:20020]:
    print(s["street_name"], s["city_name"], s["street_code"])

