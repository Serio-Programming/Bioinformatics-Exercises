# Snip Snip
# This program reduces all DNA strings in a FASTQ file to an equal number of nucleotides
# Then saves the new strings to a new file
# Circa February 2023
# A program by Tyler Serio
# Python 3.9.6

filename = "12 - sample.fastq"
file = open(filename, "r")
outputname = "13 - sample.fastq"
outputfile = open(outputname, "w")
file.readline()
firstline = file.readline()
firstline = firstline.strip("\n")
cap = len(firstline)
file.seek(0)
seqline = 0
for line in file:
    seqline += 1
    if seqline == 4:
        seqline = 0
    if seqline == 2:
        if cap >= len(line.strip("\n")):
            cap = len(line.strip("\n"))

file.seek(0)
seqline = 0
for line in file:
    seqline += 1
    if seqline == 4:
        if cap <= len(line.strip("\n")):
            diff = len(line.strip("\n")) - cap
            line = list(line.strip("\n"))
            while diff > 0:
                line.pop()
                diff -= 1
            line = "".join(line)
            l4 = line + "\n"
        outputfile.write(l1)
        outputfile.write(l2)
        outputfile.write(l3)
        outputfile.write(l4)
        seqline = 0
    if seqline == 3:
        l3 = line      
    if seqline == 2:
        if cap <= len(line.strip("\n")):
            diff = len(line.strip("\n")) - cap
            line = list(line.strip("\n"))
            while diff > 0:
                line.pop()
                diff -= 1
            line = "".join(line)
            l2 = line + "\n"
    if seqline == 1:
        l1 = line

print("Done!")
file.close()
outputfile.close()
