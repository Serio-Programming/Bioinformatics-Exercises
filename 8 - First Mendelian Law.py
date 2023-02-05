# First Mendelian Law
# This program returns the probability of two randomly selected individuals producing offspring with a dominant allele
# Given a population with an equal number of homozygous dominant individuals, heterozygous individuals, and homozygous recessive individuals
# Circa February 2023
# A program by Tyler Serio
# Python 3.9.6

pop = 0
while pop < 10:
    pop += 1
    total = pop * 3
    dominant = pop / total
    dominant2 = (pop - 1) / (total - 1)
    hetero = pop / total
    hetero2 = (pop - 1) / (total - 1)
    recessive = pop / total
    recessive2 = (pop - 1) / (total - 1)

    # Successful combinations
    prob1 = dominant # Dominant + x   
    prob2 = hetero * ((pop / (total - 1))) # Hetero + Dominant
    prob3 = hetero * ((pop - 1) / (total - 1)) * .75 # Hetero + Hetero
    prob4 = hetero * (pop / (total - 1)) * .5 # Hetero + Recessive
    prob5 = recessive * (pop / (total - 1)) # Recessive + Dominant
    prob6 = recessive * (pop / (total - 1)) * .5 # Recessive + Hetero

    probability = round(prob1 + prob2 + prob3 + prob4 + prob5 + prob6, 5)
    probability = probability * 100
    print(f"SCENARIO {str(pop)}:")
    print("Homozygous dominant population: " + str(pop))
    print("Heterozygous population: " + str(pop))
    print("Homozygous recessive population: " + str(pop))
    print("Total population: " + str(total))
    print("Probability of producing offspring with a dominant allele: " + str(probability) + "%")
    print("")
