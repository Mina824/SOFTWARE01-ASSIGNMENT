number = int(input("enter number:"))
if number < 2:
    print(f"{number} is not a prime number.")
else:
    for i in range(2, number//2 + 1):
        if number % i == 0:
            print(f"{number} is not a prime number.")
            break
    else:
        print(f"{number} is a prime number.")

