import random_tuples
import itertools

def is_sorted(array, key=lambda x: x):
   return all(key(a) < key(b) for a, b in itertools.pairwise(array)) 

a = random_tuples.create_random_tuples(5, 3, [int, float, str])

print("Generated tuples:")
for item in a:
    print(item)

print("Sorted tuples:")
a_sorted = sorted(a, key=lambda x: (x[0]))
for item in a_sorted:
    print(item)

print("\nIs the original array sorted by first element?:", is_sorted(a, key=lambda x: x[0]))
print("Is the sorted array sorted by first element?:", is_sorted(a_sorted, key=lambda x: x[0]))
