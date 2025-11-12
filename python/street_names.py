import sys
import csv

if len(sys.argv) < 2:
    print("Error: missing argument")
    print(F"Usage: python {sys.argv[0]} filename")
    exit(-1)

filename = sys.argv[1]
# print(filename)
street_name_frequency = {}
try:
    with open(filename, 'r', encoding="windows-1255", newline='') as csvfile:
        csv_reader = csv.reader(csvfile)

except FileNotFoundError:
    print(F"{filename} not found")


