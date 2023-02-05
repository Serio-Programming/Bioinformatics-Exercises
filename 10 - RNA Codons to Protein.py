# RNA Codons to Protein
# This program takes a string of RNA, parses it for codons, and then produces its protein string
# Circa February 2023
# A program by Tyler Serio
# Python 3.9.6

codons = {
    "UUU":"F",	
    "UUC":"F",	
    "UUA":"L",	
    "UUG":"L",	
    "UCU":"S",	
    "UCC":"S",	
    "UCA":"S",	
    "UCG":"S",	
    "UAU":"Y",	
    "UAC":"Y",	
    "UAA":"Stop",	
    "UAG":"Stop",	
    "UGU":"C",	
    "UGC":"C",	
    "UGA":"Stop",	
    "UGG":"W",	
    "CUU":"L",	
    "CUC":"L",	
    "CUA":"L",	
    "CUG":"L",	
    "CCU":"P",	
    "CCC":"P",	
    "CCA":"P",	
    "CCG":"P",	
    "CAU":"H",	
    "CAC":"H",	
    "CAA":"Q",	
    "CAG":"Q",	
    "CGU":"R",	
    "CGC":"R",	
    "CGA":"R",	
    "CGG":"R",	
    "AUU":"I",	
    "AUC":"I",	
    "AUA":"I",	
    "AUG":"M",	
    "ACU":"T",	
    "ACC":"T",	
    "ACA":"T",	
    "ACG":"T",	
    "AAU":"N",	
    "AAC":"N",	
    "AAA":"K",	
    "AAG":"K",	
    "AGU":"S",	
    "AGC":"S",	
    "AGA":"R",	
    "AGG":"R",	
    "GUU":"V",
    "GUC":"V",
    "GUA":"V",
    "GUG":"V",
    "GCU":"A",
    "GCC":"A",
    "GCA":"A",
    "GCG":"A",
    "GAU":"D",
    "GAC":"D",
    "GAA":"E",
    "GAG":"E",
    "GGU":"G",
    "GGC":"G",
    "GGA":"G",
    "GGG":"G",
}

filename = "10 - sample.txt"
file = open(filename, "r")
pos = 0
for line in file:
    pos += 1
    if pos == 1:
        title = line
    if pos == 2:
        line = list(line)
        p = 0
        s = ""
        proteins = ""
        for x in line:
            p += 1
            s = s + x
            if p == 3:
                if codons[s] != "Stop":
                    proteins = proteins + codons[s]
                else:
                    proteins = proteins
                p = 0
                s = ""
    if pos == 3:
        print(title.strip("\n"))
        print(proteins)
        print("")
        pos = 0
file.close()

