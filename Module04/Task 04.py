import random
number = random.randint(1, 10)

while True:
    guess = input("Guess a number between 1 and 10: ")
    guess = int(guess)

    if guess< number:
        print("Too low")
    elif guess> number:
        print("Too high")
    else:
        print("Correct")





