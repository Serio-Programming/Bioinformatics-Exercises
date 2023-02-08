# Finding DNA Substrings
# This program finds the number of times a substring is repeated in a string of DNA
# And lists where the substrings occur in the string
# Circa February 2023
# A program by Tyler Serio
# Python 3.9.6

filename = "11 - sample.fastq"
file = open(filename, "r")
seqline = 0
for line in file:
    seqline += 1
    if seqline == 2:
        substr = line[0:4]
        print("DNA String:")
        print(line.strip("\n"))
        print("Substring:")
        print(substr)
        search = 0
        count = 0
        y = 0
        places = []
        nline = line
        while search == 0:
            x = nline.find(substr)
            if x == -1:
                break
            else:
                places.append(x + y)
                nline = nline[x + 1:]
                y = len(line) - len(nline)
            count += 1
        print(f"Number of occurrences of substring: {count}")
        print(f"Indexes where substrings occur: {places}")
        print("")
    if seqline == 4:
        seqline = 0
