# Claude Code Prompt — Character Frequencies Exercise

## Background

The exercise is part of a lesson on character frequencies and text processing.
Students are asked to download the raw text of a Wikipedia article using the
`?action=raw` URL parameter (e.g. `https://he.wikipedia.org/wiki/ירושלים?action=raw`),
save it, and run the program against it.

## The Exercise

Write a Python program called `character_frequencies.py` that:

- Accepts a text file path as a command-line argument
- Reads the file and counts the frequency of **every character**
  (including spaces, punctuation, commas, newlines, etc.)
- Writes the results to a file called `frequencies.txt`

### Output format of `frequencies.txt`:

```
char,count
א,280
ב,89
 ,300
,,100
```

The last two lines in the example are for a space character and a comma character.
All characters must be included — spaces, punctuation, everything.
The file should use `utf-8` encoding so Hebrew characters appear correctly.

## What's Already Done

We have a working solution:

```python
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
            f.write(f"{char},{count}\n")


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
```

## What I'd Like to Do Next

> Replace this line with your next goal — e.g. sort the output by frequency,
> accept a Wikipedia URL directly, add a histogram, integrate with a Huffman encoder, etc.
