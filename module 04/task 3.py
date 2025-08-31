smallest = None
largest = None
while True:
    numbers = input("Enter a number (or press Enter to quit): ")
    if numbers == "":
        break
    numbers = float(numbers)

    if smallest is None or numbers < smallest:
        smallest = numbers
    if largest is None or numbers > largest:
        largest = numbers

if smallest is None and largest is None:
    print("You didn't enter a number.")

else:
    print("The smallest number is", smallest)
    print("The largest number is", largest)