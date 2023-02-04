# Hamming Distance Calculator
# This program calculates the number of differences between two DNA strands of equal length
# Circa February 2023
# A program by Tyler Serio
# Python 3.9.6

filename = "7 - sample.txt"
file = open(filename, "r")
seqline = 0
tcount = 0
for line in file:
    seqline += 1
    if seqline == 2:
        tcount += 1
        seq1 = list(line.strip("\n"))
    if seqline == 3:
        seq2 = list(line.strip("\n"))
    if seqline == 4:
        place = 0
        count = 0
        for x in seq1:
            if x != seq2[place]:
                count += 1
            place += 1
        seqline = 0
        print("Hamming Distance for DNA Line " + str(tcount) + ": " + str(count))
