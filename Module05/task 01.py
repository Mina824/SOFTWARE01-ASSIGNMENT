import random
dices = int(input("How many dices to roll ?"))
total = 0
for number in range(dices):
    rolls = random.randint(1, 6)
    total += rolls

