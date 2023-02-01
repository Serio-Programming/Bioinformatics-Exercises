# Guanine and Cytosine Content
# This program calculates what percentage of a DNA string is Guanine and Cytosine
# This program will return the ID of the string and its GC percentage
# Circa February 2023
# A program by Tyler Serio
# Python 3.9.6

filename = "5 - sample.fastq"
file = open(filename, "r")
seqline = 0
for line in file:
    seqline += 1
    if seqline == 1:
        name = line.strip("\n")
    if seqline == 2:      
        line = line.split()
        for x in line:
            gc = x.count("G") + x.count("C")
            total = gc / len(x)
            total = total * 100
            print(name)
            print(str(total) + "%")
            print("")
    if seqline >= 4:
        seqline = 0
file.close()
