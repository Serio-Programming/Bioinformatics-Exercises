# Profile and Consensus
# This programs analyzes DNA sequences in a FASTQ file
# Then builds a consensus DNA sequence by comparing their nucleotide content
# Circa February 2023
# A program by Tyler Serio
# Python 3.9.6

filename = "13 - sample.fastq"
file = open(filename, "r")
total = []
a = 0
c = 0
t = 0
g = 0
al = []
cl = []
gl = []
tl = []
pline = []
profile = []
alllines = []
seqline = 0

for line in file:
    seqline += 1
    if seqline == 2:
        line = line.strip()
        line = list(line)
        alllines.append(line)
    if seqline == 4:
        seqline = 0

z = -1
while z < len(alllines[0]):
    z += 1
    if z == len(alllines[0]):
        break
    for x in alllines:
        if x[z] == "A":
            a += 1
        if x[z] == "C":
            c += 1
        if x[z] == "G":
            g += 1
        if x[z] == "T":
            t += 1
    pline.append(a)
    pline.append(c)
    pline.append(g)
    pline.append(t)
    profile.append(list(pline))
    pline.clear()
    a = 0
    c = 0
    t = 0
    g = 0
    
for x in profile:
    al.append(x[0])
    cl.append(x[1])
    gl.append(x[2])
    tl.append(x[3])
    
print("Sequence Profile: ")
al2 = ", ".join(map(str, al))
print(f"A: {al2}")
print("")
cl2 = ", ".join(map(str, cl))
print(f"C: {cl2}")
print("")
gl2 = ", ".join(map(str, gl))
print(f"G: {gl2}")
print("")
tl2 = ", ".join(map(str, tl))
print(f"T: {tl2}")
print("")
print(f"Consensus: ")

consensus = []
step = -1
while step < len(al) - 1:
    step += 1
    ac = al[step]
    cc = cl[step]
    gc = gl[step]
    tc = tl[step]
    if ac > cc and ac > tc and ac > gc:
        consensus.append("A")
    if cc > ac and cc > tc and cc > gc:
        consensus.append("C")
    if gc > ac and gc > tc and gc > cc:
        consensus.append("G")
    if tc > ac and tc > cc and tc > gc:
        consensus.append("T")
        
consensus = "".join(consensus)
print(consensus)
        
