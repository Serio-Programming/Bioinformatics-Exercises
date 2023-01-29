# Counting of DNA Nucleotides
# This program counts the nucleotides of a DNA string
# It returns the count of A, C, G, and T in a sequence
# Circa January 2023
# A program by Tyler Serio
# Python 3.9.6

filename = "1 - sample.fastq"
file = open(filename, "r")
seqline = 0
for line in file:
    seqline += 1
    if seqline == 2:
        a = 0
        c = 0
        g = 0
        t = 0
        s = line
        s = list(s)
        while len(s) > 0:
            n = s.pop()
            if n == "A":
                a += 1
            elif n == "C":
                c += 1
            elif n == "G":
                g += 1
            else:
                t += 1
        print(str(a) + " " + str(c) + " " + str(g) + " " + str(t))
    if seqline >= 4:
        seqline = 0
