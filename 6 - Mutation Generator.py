# Mutation Generator
# This program takes a DNA string and randomly mutates parts of it
# It then returns the original DNA string and its mutated counterpart
# Circa February 2023
# A program by Tyler Serio
# Python 3.9.6

import random

nucleotides = ("A", "T", "C", "G")
filename = "6 - sample.fastq"
file = open(filename, "r")
seqline = 0
for line in file:
    seqline += 1
    if seqline == 2:
        line = line.strip("\n")
        mutey = list(line)
        place = 0
        for x in mutey:
            mutation = random.randint(0, 3)
            if mutation == 3:
                nukey = random.randint(0, 3)
                mutey[place] = nucleotides[nukey]
            place += 1
        line2 = ""
        for x in mutey:
            line2 = line2 + str(x)
        print(line + " - Original DNA")
        print(line2 + " - Mutant DNA")
        print("")
    if seqline >= 4:
        seqline = 0
file.close()
