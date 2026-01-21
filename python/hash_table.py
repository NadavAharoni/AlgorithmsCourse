import hashlib
import scientists_list

def list_hashlib_algorithms():
    for a in hashlib.algorithms_available:
        print(a)


def djb2(s: str) -> int:
    hash_value = 5381

    """
    Implementation of the djb2 hash algorithm.
    It is fast and provides a good distribution for general use cases.
    """
    for char in s:
        # (hash << 5) + hash is equivalent to hash * 32 + hash = hash * 33
        # In C, this is faster than a standard multiplication
        hash_value = ((hash_value << 5) + hash_value) + ord(char)
        
        # Simulate C-style 32-bit "falling off" behavior
        # Without this, hash_value will grow indefinitely in Python
        hash_value &= 0xFFFFFFFF
        
    return hash_value


class HashTable:
    def __init__(self):
        self.table = [None] * 16
        self.count = 0

    def insert(self, key, value):
        table_size = len(self.table)
        h1 = djb2(key)
        h = h1 % (table_size)
        print(f"key={key}, h={h}, h1={h1}")
        if self.table[h] is None:
            self.table[h] = (key, value)
            return
        # else
        print(f"collision: hash for {key} and {self.table[h][0]} are the same")
        return
        j = i
        j = (i+1) % table_size
        while self.table[j] is not None and j!=i:
            j = (j+1) % table_size
        if j==i:
            print("table is full")
            return
        print(f"{key} inserted at {j}")
        self.table[j] = (key, value)

        # self.find_slot(h)

    def search(self, key):
        table_size = len(self.table)
        h = djb2(key)
        i = h % (table_size-1)
        if self.table[i] is None:
            return None
        
        j = i
        while True:
            if self.table[j] is None:
                return None
            if self.table[j][0] == key:
                return self.table[j][1]
            j = (j+1) % table_size
            if j==i:
                return None
        return None

    def find_slot(self, target_hash):
        """
        Simulates Python's dict probing logic.
        table_size must be a power of 2.
        current_indices is the 'Indices Array' (the sparse table).
        """
        table_size = len(self.table)
        mask = table_size - 1
        i = target_hash & mask
        perturb = target_hash
        
        # Python uses unsigned integers in C; 
        # We use abs() or mask for Python simulation
        if perturb < 0:
            perturb = abs(perturb)

        print(f"Starting at index: {i}")

        while self.table[i] is not None:  # While slot is occupied
            # The "Twist": 5*i + 1 + perturb
            # The '>> 5' ensures high bits of the hash eventually affect the index
            print(f"Collision at {i}. Perturb is {perturb}")
            
            i = (5 * i + 1 + perturb) & mask
            perturb >>= 5  # Perturb eventually becomes 0
            
            print(f"Next probe: {i}")
            
            # In a real dict, we'd check if the key matches here
            # If we've probed enough and found nothing, the loop naturally continues
        
        return i # The first empty slot found


def main():
    # print(djb2("college"))
    
    hash_table = HashTable()

    for scientist in scientists_list.scientists[0:7]:
        print(f"==============")
        hash_table.insert(scientist[0], scientist)

    s = hash_table.search("Tesla")
    print(s)
    s = hash_table.search("Uman")
    print(s)

    # hash_table.insert("college")
    # hash_table.insert("hello")

if __name__ == "__main__":
    main()
