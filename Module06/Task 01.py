import random

def dice_roll():
    return random.randint(1, 6)

while True:
    result = dice_roll()
    print(f"The rolled is: {result}")
    if result == 6:
        break



