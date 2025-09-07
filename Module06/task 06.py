from math import pi
def unit_price(diameter_cm, price_euros):
    radius = diameter_cm / 200
    area = pi * radius * radius
    return price_euros / area

def main_program():
    diameter1 = float(input("Diameter of first pizza in cm:"))
    price1 = float(input("Price of first pizza in euros:"))
    diameter2 = float(input("Diameter of second pizza in cm:"))
    price2 = float(input("Price of second pizza in euros:"))

    unit_price1 = unit_price(diameter1, price1)
    unit_price2 = unit_price(diameter2, price2)

    print(f"The unit price of pizza 1:", unit_price1)
    print(f"The unit price of pizza 2:", unit_price2)
    if unit_price1 < unit_price2:
        print("First pizza is better for value of money ")
    elif unit_price1 > unit_price2:
        print("Second pizza is better for value of money ")
    else:
        print("Both are in same value ")

main_program()



