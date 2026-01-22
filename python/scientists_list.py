scientists = [
    ("Einstein", "Albert", 1905, "Theory of Relativity"),
    ("Newton", "Isaac", 1687, "Laws of Motion and Universal Gravitation"),
    ("Curie", "Marie", 1898, "Radioactivity"),
    ("Darwin", "Charles", 1859, "Theory of Evolution"),
    ("Tesla", "Nikola", 1887, "Alternating Current"),
    ("Galilei", "Galileo", 1610, "Telescopic Observations of Jupiter"),
    ("Lovelace", "Ada", 1843, "First Computer Algorithm"),
    ("Hawking", "Stephen", 1974, "Hawking Radiation"),
    ("Bohr", "Niels", 1913, "Bohr Model of the Atom"),
    ("Faraday", "Michael", 1831, "Electromagnetic Induction"),
    ("Maxwell", "James Clerk", 1865, "Equations of Electromagnetism"),
    ("Franklin", "Rosalind", 1952, "DNA Double Helix Structure"),
    ("Mendel", "Gregor", 1866, "Laws of Inheritance"),
    ("Feynman", "Richard", 1948, "Quantum Electrodynamics"),
    ("Mendeleev", "Dmitri", 1869, "Periodic Table of Elements"),
    ("Planck", "Max", 1900, "Quantum Theory"),
    ("Pasteur", "Louis", 1864, "Germ Theory of Disease"),
    ("Fermi", "Enrico", 1942, "Nuclear Chain Reaction"),
    ("McClintock", "Barbara", 1951, "Genetic Transposition"),
    ("Sagan", "Carl", 1975, "Cosmic Evolution"),
]

# print( f"type(scientists)={type(scientists)}" )
# print( f"type(scientists[0])={type(scientists[0])}" )

# an example of a "key" function that can be 
# passed to the function "sorted"
def get_year(s):
    return s[2]

# test the "get_year" function:
# s0 = scientists[0]
# print( get_year(s0) )

def main():
    sorted_scientists = sorted(scientists, key=get_year)
    for s in sorted_scientists:
        print(s)

if __name__ == "__main__":
    main()
