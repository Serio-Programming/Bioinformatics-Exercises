# Fibonacci's Bunnies
# Given a starting pair of rabbits, and assuming that three pairs of rabbits are born per litter,
# This program tells you the number of inbred rabbit pairs after a period of five months
# Circa January 2023
# A program by Tyler Serio
# Python 3.9.6

month = 1
pairs = 1
abunns = 0
jbunns = 0
bbunns = 1
limit = 5
litter = 3
print("FIBBONACCI'S BUNNIES")
while month < limit:
    print("Month " + str(month) + ":")
    print("Pairs of Adult Bunnies: " + str(abunns))
    print("Pairs of Juvenile Bunnies: " + str(jbunns))
    print("Pairs of Baby Bunnies: " + str(bbunns))
    print("")
    abunns = abunns + jbunns
    jbunns = bbunns
    bbunns = abunns * litter
    month += 1
print("Month " + str(month) + ":")
print("Pairs of Adult Bunnies: " + str(abunns))
print("Pairs of Juvenile Bunnies: " + str(jbunns))
print("Pairs of Baby Bunnies: " + str(bbunns))
pairs = abunns + jbunns + bbunns
print("Total Pairs of Bunnies: " + str(pairs))
