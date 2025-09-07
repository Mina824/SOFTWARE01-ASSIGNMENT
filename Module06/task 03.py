def convert_to_liters(galloons):
    return galloons * 3.79
while True:
    galloons = float(input("Enter how many galloons:"))
    liters = convert_to_liters(galloons)
    print(f"The galloons are {liters} liters")
    if galloons < 0:
        print("Program quited")
        break
