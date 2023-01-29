# DNA Strand Complements
# This program takes a DNA strand and produces its complement
# It prints the DNA strand and then its complement
# Circa January 2023
# A program by Tyler Serio
# Python 3.9.6

filename = "3 - sample.fastq"
file = open(filename, "r")
seqline = 0
for line in file:
    seqline += 1
    if seqline == 2:
        print(line)
        print(line[::-1])
    if seqline >= 4:
        seqline = 0
