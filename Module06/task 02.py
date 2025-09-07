import random

def dice_roll(sides):
    return random.randint(1, sides)

sides = int(input("Enter how many sides in dice:"))
while True:
    result = dice_roll(sides)
    print(f"side dice rolled:{result}")
    if result == sides:
        break


