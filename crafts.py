#Thomas Kidd
#28/09/2017
#make a random dice rolling game

import random

die1 = random.randint(1, 6)
die2 = random.randrange(6) + 1

total = die1 + die2

print("You rolled a", die1, "and a", die2, "for a total of", total)


