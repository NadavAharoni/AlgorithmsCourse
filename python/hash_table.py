import hashlib

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

def main():
    print(djb2("college"))

if __name__ == "__main__":
    main()
