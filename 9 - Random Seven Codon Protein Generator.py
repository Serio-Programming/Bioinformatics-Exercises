# Random Seven Codon Protein Generator
# This program combines codons and stop codons to produce strings of RNA
# Circa February 2023
# A program by Tyler Serio
# Python 3.9.6

import random

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
    "UGU":"C",	
    "UGC":"C",		
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

stopcodons = {
    "UAA":"Stop",	
    "UAG":"Stop",
    "UGA":"Stop",
    }

filename = "10 - sample.txt"
file = open(filename, "w")

producin = 1
while producin <= 100:
    string = ""
    choosin = 1
    while choosin <= 6:
        string = string + (random.choice(list(codons.keys())))
        choosin += 1
    string = string + (random.choice(list(stopcodons.keys())))
    print(string)
    file.write(f"PROTEIN {producin} \n")
    file.write(string + "\n")
    file.write("\n")
    producin += 1
file.close()
