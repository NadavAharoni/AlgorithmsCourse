import sys
import heapq


def read_frequencies(filepath):
    """
    Read a frequencies file in the format produced by character_frequencies.py.
    Each line is: char,count
    Non-printable characters are stored as escape sequences (e.g. \\n, \\t).
    Returns a dict mapping the actual character to its integer count.
    """
    frequencies = {}
    with open(filepath, "r", encoding="utf-8") as f:
        header = f.readline()  # skip "char,count" header
        for line in f:
            # Remove the trailing newline from the line itself,
            # then split on the LAST comma to handle the comma character as a key.
            line = line.rstrip("\n")
            last_comma = line.rfind(",")
            char_repr = line[:last_comma]
            count = int(line[last_comma + 1:])

            # Unescape: convert escape sequences like \\n back to the real character.
            # encode().decode('unicode_escape') handles \n, \t, \r, etc.
            actual_char = char_repr.encode("utf-8").decode("unicode_escape")
            frequencies[actual_char] = count

    return frequencies


class HuffmanNode:
    """A node in the Huffman tree."""

    def __init__(self, char, freq, left=None, right=None):
        self.char = char        # None for internal nodes
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        # heapq requires a comparison; break ties by char representation
        if self.freq == other.freq:
            return repr(self.char) < repr(other.char)
        return self.freq < other.freq


def build_huffman_tree(frequencies):
    """Build a Huffman tree from a frequency dict and return the root node."""
    heap = [HuffmanNode(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(char=None, freq=left.freq + right.freq,
                             left=left, right=right)
        heapq.heappush(heap, merged)

    return heap[0] if heap else None


def generate_codes(node, prefix="", codes=None):
    """Recursively traverse the Huffman tree and collect the binary code for each character."""
    if codes is None:
        codes = {}

    if node is None:
        return codes

    if node.char is not None:
        # Leaf node — this is an actual character.
        # Edge case: single unique character gets code "0".
        codes[node.char] = prefix if prefix else "0"
    else:
        generate_codes(node.left,  prefix + "0", codes)
        generate_codes(node.right, prefix + "1", codes)

    return codes


def write_codes(codes, output_path="huffman.txt"):
    """
    Write Huffman codes to a file in the format:
        char:code
    Non-printable characters are written as escape sequences (same convention
    as frequencies.txt), so the two files are consistent.
    """
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("char:code\n")
        for char, code in codes.items():
            char_to_print = char if char.isprintable() else repr(char)[1:-1]
            f.write(f"{char_to_print}:{code}\n")


def main():
    if len(sys.argv) != 2:
        print("Usage: python huffman_code.py <frequencies_file>")
        sys.exit(1)

    frequencies_path = sys.argv[1]
    frequencies = read_frequencies(frequencies_path)

    if not frequencies:
        print("Error: frequencies file is empty.")
        sys.exit(1)

    root = build_huffman_tree(frequencies)
    codes = generate_codes(root)
    write_codes(codes)

    print(f"Done! Huffman codes written to huffman.txt ({len(codes)} characters)")


if __name__ == "__main__":
    main()
