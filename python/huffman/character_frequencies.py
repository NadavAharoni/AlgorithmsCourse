import sys


def count_characters(filepath):
    """Read a text file and return a dictionary of character frequencies."""
    frequencies = {}
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            for char in line:
                frequencies[char] = frequencies.get(char, 0) + 1
    return frequencies


def write_frequencies(frequencies, output_path="frequencies.txt"):
    """Write character frequencies to a CSV-style output file."""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("char,count\n")
        for char, count in frequencies.items():
            # For non-printable characters, we use repr to get a string representation (like '\n' for newline).
            # Note: repr('\n') returns the string '\n' — including the surrounding single quotes
            # which are part of the repr output. The [1:-1] strips those quote characters, leaving just \n.
            display = char if char.isprintable() else repr(char)[1:-1]
            f.write(f"{display},{count}\n")


def main():
    if len(sys.argv) != 2:
        print("Usage: python character_frequencies.py <input_file>")
        sys.exit(1)

    input_path = sys.argv[1]
    frequencies = count_characters(input_path)
    write_frequencies(frequencies)
    print(f"Done! Frequencies written to frequencies.txt ({len(frequencies)} unique characters)")


if __name__ == "__main__":
    main()
