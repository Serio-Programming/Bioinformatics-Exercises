# Transcribing DNA into RNA Sequences
# This program converts DNA strings into RNA strings
# It replaces all the T nucleotides with U
# It will return the original string for each DNA sequence, and then the new RNA string
# Circa January 2023
# A program by Tyler Serio
# Python 3.9.6

filename = "2 - sample.fastq"
file = open(filename, "r")
seqline = 0
for line in file:
    seqline += 1
    if seqline == 2:
        print(line)
        line = line.replace("T", "U")
        print(line)
    if seqline >= 4:
        seqline = 0
